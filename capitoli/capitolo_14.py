"""
Capitolo 14: Fiscalità degli investimenti
InvestAccademy - Corso di Finanza Personale
"""

import streamlit as st
import pandas as pd

# Metadata
CAPITOLO_NUM = 14
TITOLO = "Fiscalità degli investimenti"

OBIETTIVI = [
    "Comprendere perché la fiscalità è parte integrante della strategia",
    "Conoscere le principali tipologie di imposte sugli investimenti",
    "Capire la differenza tra tassazione su redditi e capital gain",
    "Valutare l'impatto delle imposte sul rendimento netto",
    "Evitare errori che riducono i risultati nel lungo periodo"
]

QUIZ = [
    {
        "id": 1,
        "domanda": "Perché il rendimento netto è più importante di quello lordo?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Perché è ciò che rimane all'investitore dopo le tasse",
            "Perché è più alto",
            "Perché non include i costi",
            "Non è più importante"
        ],
        "risposta_corretta": "Perché è ciò che rimane all'investitore dopo le tasse",
        "spiegazione": "Il rendimento netto, al netto di costi e tasse, è quello che effettivamente aumenta il tuo patrimonio."
    },
    {
        "id": 2,
        "domanda": "Qual è il vantaggio del differimento fiscale?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Non si pagano mai le tasse",
            "L'interesse composto lavora su una base più ampia più a lungo",
            "Si pagano meno tasse",
            "Non ci sono vantaggi"
        ],
        "risposta_corretta": "L'interesse composto lavora su una base più ampia più a lungo",
        "spiegazione": "Differire la tassazione permette al capitale di crescere senza essere eroso annualmente dalle imposte."
    },
    {
        "id": 3,
        "domanda": "La tassazione avviene sempre ogni anno.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "Dipende dal tipo di reddito: i capital gain sono tassati solo alla vendita, mentre dividendi e cedole sono tassati quando percepiti."
    },
    {
        "id": 4,
        "domanda": "Fare trading frequente aumenta l'impatto fiscale.",
        "tipo": "vero_falso",
        "risposta_corretta": True,
        "spiegazione": "Ogni vendita in guadagno genera tassazione immediata, riducendo il capitale disponibile per l'interesse composto."
    },
    {
        "id": 5,
        "domanda": "Cosa si intende per regime amministrato?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "L'intermediario calcola e versa le imposte per conto dell'investitore",
            "L'investitore deve calcolare tutto da solo",
            "Non si pagano tasse",
            "Si pagano tasse più alte"
        ],
        "risposta_corretta": "L'intermediario calcola e versa le imposte per conto dell'investitore",
        "spiegazione": "Nel regime amministrato, l'intermediario si occupa di calcolare e versare le imposte, semplificando la gestione."
    }
]


def calcola_impatto_tasse(capitale: float, rendimento: float, anni: int, 
                          tassazione_annua: float, tassazione_differita: float) -> dict:
    """Confronta tassazione annua vs differita"""
    
    # Tassazione annua
    rend_netto_annuo = rendimento * (1 - tassazione_annua / 100)
    capitale_tass_annua = capitale * ((1 + rend_netto_annuo / 100) ** anni)
    
    # Tassazione differita
    capitale_lordo = capitale * ((1 + rendimento / 100) ** anni)
    guadagno = capitale_lordo - capitale
    tasse_finali = guadagno * (tassazione_differita / 100)
    capitale_tass_diff = capitale_lordo - tasse_finali
    
    # Differenza
    vantaggio_differimento = capitale_tass_diff - capitale_tass_annua
    
    return {
        "capitale_tass_annua": capitale_tass_annua,
        "capitale_tass_differita": capitale_tass_diff,
        "vantaggio_differimento": vantaggio_differimento,
        "tasse_annua_totali": capitale_tass_annua - capitale - (capitale * ((1 + rendimento / 100) ** anni) - capitale_tass_annua),
        "tasse_differita_totali": tasse_finali
    }


def calcola_rendimento_netto(rendimento_lordo: float, tassazione: float, costi: float) -> float:
    """Calcola il rendimento netto dopo tasse e costi"""
    return rendimento_lordo - tassazione - costi


def simula_trading_vs_hold(capitale: float, rendimento_annuo: float, anni: int,
                           operazioni_anno: int, tassa_capital_gain: float) -> dict:
    """Confronta trading frequente vs buy and hold"""
    
    # Buy and Hold
    capitale_finale_hold = capitale * ((1 + rendimento_annuo / 100) ** anni)
    guadagno_hold = capitale_finale_hold - capitale
    tasse_hold = guadagno_hold * (tassa_capital_gain / 100)
    netto_hold = capitale_finale_hold - tasse_hold
    
    # Trading frequente
    capitale_trading = capitale
    tasse_cumulate = 0
    
    rend_per_operazione = rendimento_annuo / operazioni_anno
    
    for anno in range(anni):
        for _ in range(operazioni_anno):
            guadagno_op = capitale_trading * (rend_per_operazione / 100)
            tassa_op = guadagno_op * (tassa_capital_gain / 100)
            capitale_trading = capitale_trading + guadagno_op - tassa_op
            tasse_cumulate += tassa_op
    
    netto_trading = capitale_trading
    
    return {
        "netto_hold": netto_hold,
        "tasse_hold": tasse_hold,
        "netto_trading": netto_trading,
        "tasse_trading": tasse_cumulate,
        "differenza": netto_hold - netto_trading
    }


def render_contenuto():
    """Renderizza il contenuto teorico"""
    
    st.markdown("""
    ## Perché la fiscalità conta
    
    Negli investimenti **non conta quanto rendi, ma quanto tieni**.
    
    Due portafogli con lo stesso rendimento lordo possono produrre risultati molto diversi a causa di:
    - Tassazione
    - Frequenza delle operazioni
    - Tipologia di strumenti utilizzati
    
    > Ignorare la fiscalità significa sovrastimare il rendimento reale e prendere decisioni inefficienti.
    """)
    
    st.markdown("---")
    
    st.markdown("## Le principali imposte sugli investimenti")
    
    st.markdown("""
    In generale, la tassazione sugli investimenti può riguardare:
    - **Redditi di capitale:** interessi, cedole, dividendi
    - **Redditi diversi (capital gain):** plusvalenze da vendita
    
    *Le aliquote variano in base alla normativa del paese di residenza fiscale.*
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 💰 Redditi di Capitale")
            st.markdown("""
            Tassati **quando vengono percepiti**.
            
            **Esempi:**
            - Interessi su obbligazioni
            - Cedole
            - Dividendi
            
            **Caratteristiche:**
            - Tassazione immediata
            - Riduzione dell'interesse composto
            - Minore flessibilità fiscale
            
            *In Italia: generalmente 26%*
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### 📈 Capital Gain")
            st.markdown("""
            Tassato **solo al momento della vendita**.
            
            **Vantaggi:**
            - Tassazione differita
            - Capitale cresce più a lungo
            - Interesse composto su base più ampia
            - Maggiore controllo timing
            
            *In Italia: 26% su plusvalenze*
            
            ⚠️ Compensazione con minusvalenze possibile
            """)
    
    st.success("""
    ✅ **Il differimento fiscale è una forma di rendimento implicito.**
    
    Posticipare le tasse permette al capitale di crescere esponenzialmente più a lungo.
    """)
    
    st.markdown("---")
    
    st.markdown("## L'impatto delle imposte sul rendimento")
    
    with st.container(border=True):
        st.markdown("### Esempio Pratico")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Investimento:**")
            st.markdown("- Capitale: €10.000")
            st.markdown("- Rendimento lordo: 6% annuo")
            st.markdown("- Periodo: 20 anni")
        
        with col2:
            st.markdown("**Risultati:**")
            
            # Tassazione annua (es. dividendi)
            cap_tass_annua = 10000 * ((1 + 0.06 * 0.74) ** 20)  # 26% tasse
            
            # Tassazione differita (es. capital gain)
            cap_lordo = 10000 * ((1.06) ** 20)
            guadagno = cap_lordo - 10000
            tasse = guadagno * 0.26
            cap_tass_diff = cap_lordo - tasse
            
            st.metric("Con tassazione annua", f"€{cap_tass_annua:,.0f}")
            st.metric("Con tassazione differita", f"€{cap_tass_diff:,.0f}")
            st.metric("Vantaggio differimento", f"€{cap_tass_diff - cap_tass_annua:,.0f}")
    
    st.markdown("---")
    
    st.markdown("## Efficienza fiscale degli strumenti")
    
    st.markdown("""
    Non tutti gli strumenti sono fiscalmente equivalenti.
    """)
    
    df_confronto = pd.DataFrame({
        "Strumento": ["ETF ad accumulazione", "ETF a distribuzione", "Fondo attivo", "Azioni singole"],
        "Tassazione dividendi": ["Differita", "Immediata", "Immediata", "Immediata"],
        "Controllo timing": ["Alto", "Medio", "Basso", "Alto"],
        "Efficienza fiscale": ["Alta", "Media", "Bassa", "Media-Alta"]
    })
    
    st.dataframe(df_confronto, use_container_width=True, hide_index=True)
    
    st.info("""
    💡 **Regola pratica:**
    - **ETF ad accumulazione:** massima efficienza fiscale (differimento totale)
    - **ETF a distribuzione:** tassazione annua su dividendi
    - **Trading frequente:** peggiora significativamente l'efficienza
    """)
    
    st.markdown("---")
    
    st.markdown("## Compensazione delle minusvalenze")
    
    st.markdown("""
    In molti sistemi fiscali (incluso quello italiano) è possibile:
    - **Compensare plusvalenze con minusvalenze**
    - Ridurre l'imposta complessiva
    - Riportare le minusvalenze per anni successivi
    
    **Esempio:**
    - Plusvalenza: +€5.000
    - Minusvalenza: -€2.000
    - Base imponibile: €3.000
    - Tasse: €3.000 × 26% = €780 (invece di €1.300)
    """)
    
    st.warning("⚠️ Ignorare le minusvalenze significa pagare più imposte del necessario.")
    
    st.markdown("---")
    
    st.markdown("## Regime amministrato vs dichiarativo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 🏦 Regime Amministrato")
            st.markdown("""
            L'intermediario:
            - Calcola le imposte
            - Le versa direttamente
            - Gestisce compensazioni
            
            **Vantaggi:**
            - Semplicità
            - Nessun adempimento
            - Compensazioni automatiche
            
            **Più comune per investitori individuali**
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### 📋 Regime Dichiarativo")
            st.markdown("""
            L'investitore:
            - Dichiara tutto autonomamente
            - Calcola le imposte
            - Gestisce compensazioni
            
            **Svantaggio:**
            - Complessità amministrativa
            - Rischio errori
            
            **Utile per broker esteri**
            """)
    
    st.markdown("---")
    
    st.markdown("## Errori comuni")
    
    errori = [
        ("❌ Concentrarsi solo sul rendimento lordo", "Guardare sempre il netto dopo tasse e costi"),
        ("❌ Fare trading frequente senza considerare le tasse", "Ogni operazione in utile genera tassazione immediata"),
        ("❌ Vendere inutilmente strumenti in utile", "Cristallizzare le plusvalenze anticipa la tassazione"),
        ("❌ Non conoscere il proprio regime fiscale", "Impossibile ottimizzare senza conoscere le regole"),
        ("❌ Ignorare le minusvalenze", "Compensarle riduce il carico fiscale complessivo")
    ]
    
    for errore, spiegazione in errori:
        with st.container(border=True):
            st.markdown(f"**{errore}**")
            st.caption(spiegazione)
    
    st.success("""
    ✅ **Principio guida:**
    
    Una strategia fiscalmente inefficiente può annullare buone scelte di investimento.
    Considera sempre tasse e costi insieme.
    """)


def render_calcolatore():
    """Renderizza i calcolatori"""
    
    st.markdown("## 🧮 Calcolatori")
    
    calc_type = st.radio(
        "Seleziona calcolatore:",
        ["Impatto Tassazione", "Trading vs Buy & Hold", "Rendimento Netto"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if calc_type == "Impatto Tassazione":
        render_calc_tassazione()
    elif calc_type == "Trading vs Buy & Hold":
        render_calc_trading()
    else:
        render_calc_netto()


def render_calc_tassazione():
    """Calcolatore impatto tassazione annua vs differita"""
    
    st.markdown("### Confronto Tassazione Annua vs Differita")
    
    col1, col2 = st.columns(2)
    
    with col1:
        capitale = st.number_input(
            "💰 Capitale iniziale (€)",
            min_value=1000.0,
            value=10000.0,
            step=1000.0,
            key="cap14_capitale"
        )
        
        rendimento = st.slider(
            "📊 Rendimento lordo annuo (%)",
            min_value=1.0,
            max_value=12.0,
            value=6.0,
            step=0.5,
            key="cap14_rendimento"
        )
        
        anni = st.slider(
            "📅 Orizzonte temporale (anni)",
            min_value=1,
            max_value=30,
            value=20,
            key="cap14_anni"
        )
        
        tass_annua = st.slider(
            "💸 Tassazione annua (%)",
            min_value=0.0,
            max_value=50.0,
            value=26.0,
            step=1.0,
            key="cap14_tass_annua"
        )
        
        tass_diff = st.slider(
            "💸 Tassazione differita (%)",
            min_value=0.0,
            max_value=50.0,
            value=26.0,
            step=1.0,
            key="cap14_tass_diff"
        )
    
    with col2:
        risultato = calcola_impatto_tasse(capitale, rendimento, anni, tass_annua, tass_diff)
        
        st.markdown("### Risultati")
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.metric(
                "Con tassazione annua",
                f"€{risultato['capitale_tass_annua']:,.0f}"
            )
        
        with c2:
            st.metric(
                "Con tassazione differita",
                f"€{risultato['capitale_tass_differita']:,.0f}",
                f"+€{risultato['vantaggio_differimento']:,.0f}"
            )
        
        st.markdown("---")
        
        perc_vantaggio = (risultato['vantaggio_differimento'] / risultato['capitale_tass_annua']) * 100
        
        if risultato['vantaggio_differimento'] > 0:
            st.success(f"""
            ✅ **Vantaggio del differimento: €{risultato['vantaggio_differimento']:,.0f}**
            
            Questo rappresenta un {perc_vantaggio:.1f}% in più grazie al differimento fiscale.
            """)
        
        st.info(f"""
        💡 **Dettaglio tasse pagate:**
        - Tassazione annua: genera imposte ogni anno
        - Tassazione differita: unica imposta finale di €{risultato['tasse_differita_totali']:,.0f}
        
        Il differimento permette all'interesse composto di lavorare su una base più ampia.
        """)


def render_calc_trading():
    """Calcolatore trading frequente vs buy and hold"""
    
    st.markdown("### Trading Frequente vs Buy & Hold")
    
    st.markdown("""
    Questa simulazione mostra l'impatto fiscale del trading frequente rispetto 
    alla strategia buy and hold.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        capitale = st.number_input(
            "💰 Capitale iniziale (€)",
            min_value=1000.0,
            value=10000.0,
            step=1000.0,
            key="cap14_trade_cap"
        )
        
        rendimento = st.slider(
            "📊 Rendimento annuo (%)",
            min_value=1.0,
            max_value=15.0,
            value=8.0,
            step=0.5,
            key="cap14_trade_rend"
        )
        
        anni = st.slider(
            "📅 Anni",
            min_value=1,
            max_value=20,
            value=10,
            key="cap14_trade_anni"
        )
        
        operazioni = st.slider(
            "🔄 Operazioni di compravendita all'anno",
            min_value=1,
            max_value=50,
            value=12,
            key="cap14_trade_op"
        )
        
        tassa = st.slider(
            "💸 Tassazione capital gain (%)",
            min_value=0.0,
            max_value=40.0,
            value=26.0,
            step=1.0,
            key="cap14_trade_tassa"
        )
    
    with col2:
        risultato = simula_trading_vs_hold(capitale, rendimento, anni, operazioni, tassa)
        
        st.markdown("### Confronto Risultati")
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown("**🎯 Buy & Hold**")
            st.metric("Capitale finale", f"€{risultato['netto_hold']:,.0f}")
            st.metric("Tasse pagate", f"€{risultato['tasse_hold']:,.0f}")
        
        with c2:
            st.markdown(f"**🔄 Trading ({operazioni}/anno)**")
            st.metric("Capitale finale", f"€{risultato['netto_trading']:,.0f}")
            st.metric("Tasse pagate", f"€{risultato['tasse_trading']:,.0f}")
        
        st.markdown("---")
        
        if risultato['differenza'] > 0:
            perc_diff = (risultato['differenza'] / risultato['netto_trading']) * 100
            st.error(f"""
            ❌ **Costo del trading frequente: €{risultato['differenza']:,.0f}**
            
            Hai perso il {perc_diff:.1f}% del capitale finale a causa delle tasse generate 
            dalle operazioni frequenti.
            """)
        
        tasse_extra = risultato['tasse_trading'] - risultato['tasse_hold']
        
        st.warning(f"""
        ⚠️ **Tasse extra pagate con il trading:** €{tasse_extra:,.0f}
        
        Ogni operazione in utile cristallizza una plusvalenza tassabile, riducendo il capitale 
        disponibile per l'interesse composto.
        """)


def render_calc_netto():
    """Calcolatore rendimento netto"""
    
    st.markdown("### Calcola il Tuo Rendimento Netto")
    
    st.markdown("""
    Inserisci rendimento lordo, tasse e costi per vedere il rendimento effettivo.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        rend_lordo = st.slider(
            "📈 Rendimento lordo (%)",
            min_value=0.0,
            max_value=15.0,
            value=7.0,
            step=0.5,
            key="cap14_netto_lordo"
        )
        
        tassazione = st.slider(
            "💸 Tassazione (%)",
            min_value=0.0,
            max_value=50.0,
            value=1.82,
            step=0.1,
            help="Tassazione media annua (es. 26% su 7% = 1.82%)",
            key="cap14_netto_tassa"
        )
        
        costi = st.slider(
            "💰 Costi totali (%)",
            min_value=0.0,
            max_value=3.0,
            value=0.3,
            step=0.05,
            help="Somma di TER, commissioni, spread, ecc.",
            key="cap14_netto_costi"
        )
        
        capitale_init = st.number_input(
            "💵 Capitale iniziale (€)",
            min_value=1000.0,
            value=10000.0,
            step=1000.0,
            key="cap14_netto_cap"
        )
        
        anni_calc = st.slider(
            "📅 Anni",
            min_value=1,
            max_value=30,
            value=20,
            key="cap14_netto_anni"
        )
    
    with col2:
        rend_netto = calcola_rendimento_netto(rend_lordo, tassazione, costi)
        
        st.markdown("### Analisi Rendimento")
        
        st.metric("Rendimento lordo", f"{rend_lordo:.2f}%")
        st.metric("- Tassazione", f"-{tassazione:.2f}%", delta_color="inverse")
        st.metric("- Costi", f"-{costi:.2f}%", delta_color="inverse")
        st.metric("= Rendimento netto", f"{rend_netto:.2f}%", delta_color="off")
        
        st.markdown("---")
        
        # Calcolo capitali finali
        cap_lordo = capitale_init * ((1 + rend_lordo / 100) ** anni_calc)
        cap_netto = capitale_init * ((1 + rend_netto / 100) ** anni_calc)
        perdita = cap_lordo - cap_netto
        
        st.markdown(f"### Impatto su {anni_calc} anni")
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.metric("Capitale con rend. lordo", f"€{cap_lordo:,.0f}")
        
        with c2:
            st.metric("Capitale con rend. netto", f"€{cap_netto:,.0f}")
        
        perc_perdita = (perdita / cap_lordo) * 100
        
        st.error(f"""
        💸 **Costo di tasse e costi:** €{perdita:,.0f}
        
        Hai perso il {perc_perdita:.1f}% del capitale potenziale.
        """)
        
        st.info("""
        💡 **Conclusione:**
        
        Ogni punto percentuale di costi o tasse riduce significativamente 
        il capitale finale grazie all'effetto composto.
        """)


def render_quiz():
    """Renderizza il quiz di verifica"""
    
    st.markdown("## 📝 Quiz di verifica")
    
    if "cap14_risposte" not in st.session_state:
        st.session_state.cap14_risposte = {}
    if "cap14_verificato" not in st.session_state:
        st.session_state.cap14_verificato = False
    
    for i, q in enumerate(QUIZ):
        with st.container(border=True):
            st.markdown(f"**Domanda {i+1}:** {q['domanda']}")
            
            if q["tipo"] == "vero_falso":
                risposta = st.radio(
                    "Seleziona:",
                    ["Vero", "Falso"],
                    key=f"cap14_q{q['id']}",
                    horizontal=True
                )
                st.session_state.cap14_risposte[q['id']] = risposta == "Vero"
                
            elif q["tipo"] == "scelta_multipla":
                risposta = st.radio(
                    "Seleziona:",
                    q["opzioni"],
                    key=f"cap14_q{q['id']}"
                )
                st.session_state.cap14_risposte[q['id']] = risposta
            
            if st.session_state.cap14_verificato:
                user_ans = st.session_state.cap14_risposte.get(q['id'])
                corretto = user_ans == q["risposta_corretta"]
                
                if corretto:
                    st.success(f"✅ Corretto! {q['spiegazione']}")
                else:
                    st.error(f"❌ Sbagliato. Risposta corretta: {q['risposta_corretta']}")
                    st.info(q['spiegazione'])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Verifica risposte", type="primary", use_container_width=True, key="cap14_verifica"):
            st.session_state.cap14_verificato = True
            st.rerun()
    with col2:
        if st.button("🔄 Ricomincia", use_container_width=True, key="cap14_reset"):
            st.session_state.cap14_verificato = False
            st.session_state.cap14_risposte = {}
            st.rerun()


def render_takeaways():
    """Renderizza i punti chiave"""
    
    st.markdown("## 💡 Punti chiave")
    
    takeaways = [
        "Non conta quanto rendi, ma quanto tieni dopo tasse e costi",
        "Il differimento fiscale è una forma di rendimento implicito",
        "ETF ad accumulazione offrono massima efficienza fiscale",
        "Trading frequente aumenta drasticamente l'impatto fiscale",
        "La compensazione delle minusvalenze riduce il carico fiscale",
        "Il regime amministrato semplifica la gestione per investitori individuali",
        "Una strategia fiscalmente inefficiente può annullare buone scelte di investimento"
    ]
    
    for t in takeaways:
        st.markdown(f"- {t}")
    
    st.markdown("---")
    
    with st.expander("📝 Esercizio: Analizza la tua situazione fiscale"):
        st.markdown("""
        **Valuta l'efficienza fiscale del tuo portafoglio:**
        
        1. **Identifica la tassazione**
           - Regime: ☐ Amministrato ☐ Dichiarativo
           - Aliquota capital gain: _____%
           - Aliquota redditi capitale: _____%
        
        2. **Analizza i tuoi strumenti**
           
           | Strumento | % Portafoglio | Tipo tassazione | Efficienza |
           |-----------|---------------|-----------------|------------|
           | | | | |
           | | | | |
           | | | | |
        
        3. **Calcola l'impatto**
           - Rendimento lordo atteso: _____%
           - Tassazione media annua: _____%
           - Costi totali: _____%
           - **Rendimento netto:** _____%
        
        4. **Identifica ottimizzazioni**
           - [ ] Preferire ETF ad accumulazione
           - [ ] Ridurre frequenza operazioni
           - [ ] Compensare minusvalenze
           - [ ] Verificare regime fiscale ottimale
        
        5. **Commitment**
           "Mi impegno a considerare l'impatto fiscale in ogni decisione di investimento 
           e a privilegiare strategie fiscalmente efficienti."
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
