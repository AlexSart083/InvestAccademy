"""
Capitolo 9: Rendimento, rischio e diversificazione
InvestAccademy - Corso di Finanza Personale
"""

import streamlit as st
import pandas as pd
import numpy as np

# Metadata
CAPITOLO_NUM = 9
TITOLO = "Rendimento, rischio e diversificazione"

OBIETTIVI = [
    "Comprendere le diverse tipologie di rendimento",
    "Misurare il rischio in modo pratico",
    "Capire perché la diversificazione riduce il rischio",
    "Distinguere tra rischio sistematico e specifico",
    "Costruire i primi principi di un portafoglio equilibrato"
]

# Quiz
QUIZ = [
    {
        "id": 1,
        "domanda": "Qual è la differenza tra rischio specifico e sistematico?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Il rischio specifico riguarda il singolo investimento, quello sistematico il mercato",
            "Il rischio specifico riguarda il mercato, quello sistematico il singolo investimento",
            "Sono la stessa cosa",
            "Non c'è differenza pratica"
        ],
        "risposta_corretta": "Il rischio specifico riguarda il singolo investimento, quello sistematico il mercato",
        "spiegazione": "Il rischio specifico può essere ridotto con la diversificazione, mentre il rischio sistematico riguarda l'intero mercato."
    },
    {
        "id": 2,
        "domanda": "La diversificazione elimina completamente il rischio di investimento.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "La diversificazione riduce il rischio specifico ma non elimina il rischio sistematico di mercato."
    },
    {
        "id": 3,
        "domanda": "Cosa significa correlazione tra due investimenti?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Quanto si muovono insieme",
            "Il loro rendimento totale",
            "Il loro rischio individuale",
            "La loro liquidità"
        ],
        "risposta_corretta": "Quanto si muovono insieme",
        "spiegazione": "La correlazione misura quanto due investimenti tendono a muoversi nella stessa direzione o in direzioni opposte."
    },
    {
        "id": 4,
        "domanda": "Se un investimento rende il 7% e l'inflazione è al 2%, qual è il rendimento reale approssimato?",
        "tipo": "numero",
        "risposta_corretta": 5,
        "spiegazione": "Rendimento reale ≈ 7% - 2% = 5%"
    },
    {
        "id": 5,
        "domanda": "Dieci azioni dello stesso settore offrono vera diversificazione.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "Falso. La diversificazione efficace richiede asset class, settori e aree geografiche diverse."
    }
]


def calcola_rendimento_reale(nominale: float, inflazione: float) -> float:
    """Calcola il rendimento reale approssimato"""
    return nominale - inflazione


def calcola_rendimento_reale_esatto(nominale: float, inflazione: float) -> float:
    """Calcola il rendimento reale con formula esatta"""
    return ((1 + nominale / 100) / (1 + inflazione / 100) - 1) * 100


def simula_correlazione(corr: float, volatilita_a: float, volatilita_b: float, periodi: int = 100) -> dict:
    """Simula due asset con correlazione specifica"""
    np.random.seed(42)
    
    # Genera rendimenti correlati
    mean = [0, 0]
    cov = [[volatilita_a**2, corr * volatilita_a * volatilita_b],
           [corr * volatilita_a * volatilita_b, volatilita_b**2]]
    
    rendimenti = np.random.multivariate_normal(mean, cov, periodi)
    
    asset_a = 100 * np.exp(np.cumsum(rendimenti[:, 0] / 100))
    asset_b = 100 * np.exp(np.cumsum(rendimenti[:, 1] / 100))
    portafoglio = (asset_a + asset_b) / 2
    
    return {
        "asset_a": asset_a,
        "asset_b": asset_b,
        "portafoglio": portafoglio,
        "vol_a": np.std(rendimenti[:, 0]),
        "vol_b": np.std(rendimenti[:, 1]),
        "vol_portafoglio": np.std((rendimenti[:, 0] + rendimenti[:, 1]) / 2)
    }


def render_contenuto():
    """Renderizza il contenuto teorico"""
    
    st.markdown("""
    ## Cos'è il rendimento
    
    Il rendimento rappresenta il guadagno (o la perdita) di un investimento nel tempo.
    
    Può derivare da:
    - **Reddito**: dividendi, cedole, interessi
    - **Variazione di prezzo**: aumento o diminuzione del valore dell'attivo
    
    **Rendimento totale = reddito + variazione di prezzo**
    """)
    
    st.markdown("---")
    
    st.markdown("## Rendimento nominale e reale")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### Rendimento Nominale")
            st.markdown("""
            Rendimento espresso in termini monetari, senza considerare l'inflazione.
            
            **Esempio:**
            - Investimento iniziale: €10.000
            - Valore finale: €10.500
            - Rendimento nominale: 5%
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### Rendimento Reale")
            st.markdown("""
            Rendimento al netto dell'inflazione, che misura l'effettivo aumento del potere d'acquisto.
            
            **Formula approssimata:**
            """)
            st.latex(r"\text{Rend. reale} \approx \text{Rend. nominale} - \text{Inflazione}")
    
    st.info("""
    💡 **Ciò che conta davvero è il potere d'acquisto finale.**
    
    Se un investimento rende il 5% ma l'inflazione è al 3%, il rendimento reale è circa 2%.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Cos'è il rischio
    
    Il rischio è la possibilità che il rendimento effettivo sia diverso da quello atteso.
    
    In pratica si manifesta come **volatilità**, cioè oscillazioni del valore nel tempo.
    
    > Il rischio non è solo perdita permanente: è anche incertezza nel breve periodo.
    """)
    
    st.markdown("---")
    
    st.markdown("## Tipologie di rischio")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 🎯 Rischio Specifico")
            st.markdown("""
            Rischio legato a un singolo emittente o investimento.
            
            **Esempi:**
            - Fallimento di un'azienda
            - Problemi gestionali
            - Scandali o eventi isolati
            
            **Importante:** Questo rischio può essere **ridotto con la diversificazione**.
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### 🌍 Rischio Sistematico")
            st.markdown("""
            Rischio legato al mercato nel suo complesso.
            
            **Esempi:**
            - Recessioni
            - Crisi finanziarie
            - Shock macroeconomici
            
            **Importante:** Non può essere eliminato, solo **gestito**.
            """)
    
    st.warning("""
    ⚠️ **Concetto chiave:**
    
    La diversificazione riduce il rischio specifico ma non elimina quello sistematico.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Il principio della diversificazione
    
    La diversificazione consiste nel distribuire il capitale tra più investimenti non perfettamente correlati.
    
    ### Obiettivi:
    - Ridurre il rischio complessivo
    - Stabilizzare il percorso dei rendimenti
    - Migliorare il rapporto rischio/rendimento
    
    > La diversificazione è l'unico "pasto gratis" in finanza.
    """)
    
    st.markdown("---")
    
    st.markdown("## Diversificare non significa moltiplicare")
    
    st.markdown("""
    Avere molti investimenti simili **non è vera diversificazione**.
    
    ### Diversificazione efficace avviene tra:
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("### 📊")
        st.markdown("**Asset class diverse**")
        st.caption("Azioni, obbligazioni, liquidità")
    
    with col2:
        st.markdown("### 🏭")
        st.markdown("**Settori**")
        st.caption("Tecnologia, sanità, energia, ecc.")
    
    with col3:
        st.markdown("### 🌎")
        st.markdown("**Aree geografiche**")
        st.caption("USA, Europa, Asia, emergenti")
    
    with col4:
        st.markdown("### 🔧")
        st.markdown("**Strumenti**")
        st.caption("Singoli titoli, ETF, fondi")
    
    st.error("""
    ❌ **Dieci azioni dello stesso settore non sono più sicure di una.**
    """)
    
    st.markdown("---")
    
    st.markdown("## Correlazione: il concetto chiave")
    
    st.markdown("""
    La **correlazione** misura quanto due investimenti si muovono insieme.
    
    | Correlazione | Significato | Effetto sulla diversificazione |
    |--------------|-------------|-------------------------------|
    | +1 | Si muovono perfettamente insieme | Nessun beneficio |
    | 0 | Movimenti indipendenti | Buona diversificazione |
    | -1 | Si muovono in direzioni opposte | Massima diversificazione |
    
    **Diversificare significa combinare strumenti con correlazione bassa o negativa.**
    """)
    
    st.markdown("---")
    
    st.markdown("## Esempio pratico: l'effetto della diversificazione")
    
    with st.container(border=True):
        st.markdown("### Scenario A: Un singolo investimento")
        st.markdown("""
        - 100% azioni di una singola azienda
        - Rischio specifico molto elevato
        - Vulnerabile a eventi aziendali
        """)
    
    with st.container(border=True):
        st.markdown("### Scenario B: Portafoglio diversificato")
        st.markdown("""
        - 60% azioni globali (diversificate)
        - 35% obbligazioni
        - 5% liquidità
        
        **Risultato:** Oscillazioni più contenute pur mantenendo potenziale di crescita.
        """)


def render_calcolatore():
    """Renderizza i calcolatori"""
    
    st.markdown("## 🧮 Calcolatori")
    
    calc_type = st.radio(
        "Seleziona calcolatore:",
        ["Rendimento Reale", "Effetto Correlazione", "Simulatore Diversificazione"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if calc_type == "Rendimento Reale":
        render_calc_rendimento()
    elif calc_type == "Effetto Correlazione":
        render_calc_correlazione()
    else:
        render_calc_diversificazione()


def render_calc_rendimento():
    """Calcolatore rendimento reale"""
    
    st.markdown("### Calcolo Rendimento Reale")
    
    st.markdown("""
    Scopri quanto vale davvero il tuo rendimento al netto dell'inflazione.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        nominale = st.slider(
            "📈 Rendimento nominale (%)",
            min_value=0.0,
            max_value=15.0,
            value=6.0,
            step=0.5,
            key="cap9_nominale"
        )
        
        inflazione = st.slider(
            "📉 Inflazione (%)",
            min_value=0.0,
            max_value=10.0,
            value=2.5,
            step=0.5,
            key="cap9_inflazione"
        )
        
        capitale = st.number_input(
            "💰 Capitale investito (€)",
            min_value=1000.0,
            value=10000.0,
            step=1000.0,
            key="cap9_capitale"
        )
        
        anni = st.slider(
            "📅 Orizzonte (anni)",
            min_value=1,
            max_value=30,
            value=10,
            key="cap9_anni"
        )
    
    with col2:
        reale_approssimato = calcola_rendimento_reale(nominale, inflazione)
        reale_esatto = calcola_rendimento_reale_esatto(nominale, inflazione)
        
        st.markdown("### Risultati")
        
        col_nom, col_real = st.columns(2)
        
        with col_nom:
            st.metric("Rendimento nominale", f"{nominale:.1f}%")
        
        with col_real:
            st.metric("Rendimento reale", f"{reale_approssimato:.1f}%")
        
        # Calcolo montanti
        montante_nominale = capitale * ((1 + nominale / 100) ** anni)
        montante_reale = capitale * ((1 + reale_approssimato / 100) ** anni)
        perdita_inflazione = montante_nominale - montante_reale
        
        st.markdown("---")
        st.markdown(f"#### Dopo {anni} anni")
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Capitale nominale", f"€{montante_nominale:,.2f}")
        with c2:
            st.metric("Potere d'acquisto reale", f"€{montante_reale:,.2f}")
        
        if reale_approssimato > 0:
            st.success(f"✅ Guadagno reale positivo in {anni} anni")
        elif reale_approssimato == 0:
            st.warning(f"⚠️ Rendimento nullo: mantieni il potere d'acquisto")
        else:
            st.error(f"❌ Perdita di potere d'acquisto")
        
        st.info(f"💸 Perdita per inflazione: €{perdita_inflazione:,.2f}")
    
    st.markdown("---")
    st.markdown("#### 📊 Evoluzione nel tempo")
    
    # Grafico evoluzione
    anni_range = list(range(anni + 1))
    nominali = [capitale * ((1 + nominale / 100) ** a) for a in anni_range]
    reali = [capitale * ((1 + reale_approssimato / 100) ** a) for a in anni_range]
    
    df_evoluzione = pd.DataFrame({
        "Anno": anni_range,
        "Valore Nominale": nominali,
        "Potere d'Acquisto Reale": reali
    })
    
    st.line_chart(df_evoluzione.set_index("Anno"))


def render_calc_correlazione():
    """Calcolatore effetto correlazione"""
    
    st.markdown("### Effetto della Correlazione sulla Diversificazione")
    
    st.markdown("""
    Visualizza come la correlazione tra due asset influisce sul rischio del portafoglio.
    """)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        correlazione = st.slider(
            "🔗 Correlazione",
            min_value=-1.0,
            max_value=1.0,
            value=0.3,
            step=0.1,
            key="cap9_corr",
            help="Da -1 (opposte) a +1 (identiche)"
        )
        
        vol_a = st.slider(
            "📊 Volatilità Asset A",
            min_value=5.0,
            max_value=30.0,
            value=15.0,
            step=1.0,
            key="cap9_vol_a"
        )
        
        vol_b = st.slider(
            "📊 Volatilità Asset B",
            min_value=5.0,
            max_value=30.0,
            value=15.0,
            step=1.0,
            key="cap9_vol_b"
        )
        
        periodi = st.slider(
            "Periodi di simulazione",
            min_value=50,
            max_value=200,
            value=100,
            step=10,
            key="cap9_periodi"
        )
    
    with col2:
        simulazione = simula_correlazione(correlazione, vol_a, vol_b, periodi)
        
        st.markdown("### Risultati Simulazione")
        
        # Metriche
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Volatilità Asset A", f"{simulazione['vol_a']:.1f}%")
        with c2:
            st.metric("Volatilità Asset B", f"{simulazione['vol_b']:.1f}%")
        with c3:
            riduzione = ((simulazione['vol_a'] + simulazione['vol_b']) / 2 - simulazione['vol_portafoglio'])
            st.metric(
                "Volatilità Portafoglio 50/50", 
                f"{simulazione['vol_portafoglio']:.1f}%",
                f"-{riduzione:.1f}%"
            )
        
        # Interpretazione
        if correlazione < -0.5:
            st.success("🟢 Correlazione negativa: forte beneficio di diversificazione")
        elif correlazione < 0.3:
            st.info("🔵 Bassa correlazione: buona diversificazione")
        elif correlazione < 0.7:
            st.warning("🟡 Correlazione moderata: beneficio limitato")
        else:
            st.error("🔴 Alta correlazione: scarsa diversificazione")
        
        # Grafico
        st.markdown("#### 📈 Andamento simulato")
        
        df_sim = pd.DataFrame({
            "Periodo": range(len(simulazione['asset_a'])),
            "Asset A": simulazione['asset_a'],
            "Asset B": simulazione['asset_b'],
            "Portafoglio 50/50": simulazione['portafoglio']
        })
        
        st.line_chart(df_sim.set_index("Periodo"))


def render_calc_diversificazione():
    """Simulatore diversificazione"""
    
    st.markdown("### Simulatore: Concentrazione vs Diversificazione")
    
    st.markdown("""
    Confronta l'effetto di un portafoglio concentrato con uno diversificato.
    """)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        capitale = st.number_input(
            "💰 Capitale totale (€)",
            min_value=1000.0,
            value=10000.0,
            step=1000.0,
            key="cap9_div_cap"
        )
        
        num_titoli = st.slider(
            "📊 Numero di titoli nel portafoglio",
            min_value=1,
            max_value=20,
            value=10,
            key="cap9_num_titoli"
        )
        
        prob_fallimento = st.slider(
            "⚠️ Probabilità fallimento singolo titolo (%)",
            min_value=1.0,
            max_value=20.0,
            value=5.0,
            step=1.0,
            key="cap9_prob_fall"
        )
    
    with col2:
        capitale_per_titolo = capitale / num_titoli
        
        # Calcolo rischio
        prob_almeno_un_fallimento = 1 - (1 - prob_fallimento / 100) ** num_titoli
        perdita_attesa_singolo = capitale * (prob_fallimento / 100)
        perdita_attesa_diversificato = capitale_per_titolo * (prob_fallimento / 100)
        
        st.markdown("### Analisi del Rischio")
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown("#### 🎯 Portafoglio Concentrato")
            st.markdown(f"**1 titolo** da €{capitale:,.2f}")
            st.metric("Perdita attesa", f"€{perdita_attesa_singolo:,.2f}")
            st.metric("Prob. perdita totale", f"{prob_fallimento:.1f}%")
        
        with c2:
            st.markdown(f"#### 🌐 Portafoglio Diversificato")
            st.markdown(f"**{num_titoli} titoli** da €{capitale_per_titolo:,.2f} ciascuno")
            st.metric("Perdita attesa per fallimento", f"€{perdita_attesa_diversificato:,.2f}")
            st.metric("Prob. almeno un fallimento", f"{prob_almeno_un_fallimento * 100:.1f}%")
        
        riduzione_rischio = ((perdita_attesa_singolo - perdita_attesa_diversificato) / perdita_attesa_singolo) * 100
        
        st.success(f"✅ Riduzione del rischio specifico: {riduzione_rischio:.1f}%")
        
        st.info("""
        💡 **Osservazione:**
        
        Con la diversificazione:
        - La perdita massima su singolo titolo si riduce
        - Il rischio si distribuisce
        - Il portafoglio diventa più resiliente
        
        **Importante:** Questo riduce solo il rischio specifico, non quello sistematico!
        """)


def render_quiz():
    """Renderizza il quiz di verifica"""
    
    st.markdown("## 📝 Quiz di verifica")
    
    if "cap9_risposte" not in st.session_state:
        st.session_state.cap9_risposte = {}
    if "cap9_verificato" not in st.session_state:
        st.session_state.cap9_verificato = False
    
    for i, q in enumerate(QUIZ):
        with st.container(border=True):
            st.markdown(f"**Domanda {i+1}:** {q['domanda']}")
            
            if q["tipo"] == "vero_falso":
                risposta = st.radio(
                    "Seleziona:",
                    ["Vero", "Falso"],
                    key=f"cap9_q{q['id']}",
                    horizontal=True
                )
                st.session_state.cap9_risposte[q['id']] = risposta == "Vero"
                
            elif q["tipo"] == "scelta_multipla":
                risposta = st.radio(
                    "Seleziona:",
                    q["opzioni"],
                    key=f"cap9_q{q['id']}"
                )
                st.session_state.cap9_risposte[q['id']] = risposta
                
            elif q["tipo"] == "numero":
                risposta = st.number_input(
                    "Inserisci il valore:",
                    key=f"cap9_q{q['id']}",
                    step=0.5
                )
                st.session_state.cap9_risposte[q['id']] = risposta
            
            if st.session_state.cap9_verificato:
                user_ans = st.session_state.cap9_risposte.get(q['id'])
                if q["tipo"] == "numero":
                    corretto = abs(user_ans - q["risposta_corretta"]) < 1
                else:
                    corretto = user_ans == q["risposta_corretta"]
                
                if corretto:
                    st.success(f"✅ Corretto! {q['spiegazione']}")
                else:
                    st.error(f"❌ Sbagliato. Risposta corretta: {q['risposta_corretta']}")
                    st.info(q['spiegazione'])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Verifica risposte", type="primary", use_container_width=True, key="cap9_verifica"):
            st.session_state.cap9_verificato = True
            st.rerun()
    with col2:
        if st.button("🔄 Ricomincia", use_container_width=True, key="cap9_reset"):
            st.session_state.cap9_verificato = False
            st.session_state.cap9_risposte = {}
            st.rerun()


def render_takeaways():
    """Renderizza i punti chiave"""
    
    st.markdown("## 💡 Punti chiave")
    
    takeaways = [
        "Il rendimento totale deriva sia dal reddito che dalla variazione di prezzo",
        "Ciò che conta è il rendimento reale (al netto dell'inflazione), non quello nominale",
        "Il rischio si manifesta come volatilità, cioè oscillazioni del valore nel tempo",
        "Esistono due tipi di rischio: specifico (riducibile) e sistematico (non eliminabile)",
        "La diversificazione riduce il rischio specifico ma non elimina quello sistematico",
        "La correlazione misura quanto due investimenti si muovono insieme",
        "Diversificare significa combinare strumenti con correlazione bassa o negativa",
        "Dieci azioni dello stesso settore non offrono vera diversificazione"
    ]
    
    for t in takeaways:
        st.markdown(f"- {t}")
    
    st.markdown("---")
    
    # Esercizio pratico
    with st.expander("📝 Esercizio guidato: Analizza la diversificazione"):
        st.markdown("""
        **Scenario pratico:**
        
        Immagina di avere due investimenti:
        1. **Asset A:** Azioni tecnologiche USA
        2. **Asset B:** Obbligazioni governative
        
        **Domande di riflessione:**
        
        1. Come reagirebbero questi due asset a:
           - Un aumento dei tassi di interesse?
           - Una recessione economica?
           - Un periodo di forte crescita?
        
        2. Quale correlazione ti aspetteresti tra questi due asset?
           - Alta positiva
           - Bassa
           - Negativa
        
        3. Perché combinare questi due asset riduce il rischio complessivo?
        
        ---
        
        **Risposte suggerite:**
        
        1. **Aumento tassi:** Azioni giù, obbligazioni giù (ma meno)
           **Recessione:** Azioni giù, obbligazioni su (bene rifugio)
           **Crescita:** Azioni su, obbligazioni stabili
        
        2. Correlazione **bassa o leggermente negativa** - si muovono spesso in direzioni diverse
        
        3. Quando uno scende, l'altro tende a rimanere stabile o salire, stabilizzando il portafoglio
        
        💡 *Questo è il principio base della diversificazione efficace!*
        """)


def render():
    """Funzione principale per renderizzare il capitolo"""
    
    st.title(f"📖 Capitolo {CAPITOLO_NUM}")
    st.header(TITOLO)
    
    with st.expander("🎯 Obiettivi di apprendimento", expanded=False):
        for obj in OBIETTIVI:
            st.markdown(f"- {obj}")
    
    st.markdown("---")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📚 Contenuto", 
        "🧮 Calcolatori", 
        "📝 Quiz",
        "💡 Takeaways"
    ])
    
    with tab1:
        render_contenuto()
    
    with tab2:
        render_calcolatore()
    
    with tab3:
        render_quiz()
    
    with tab4:
        render_takeaways()
