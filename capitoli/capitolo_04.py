"""
Capitolo 4: Il fondo di emergenza
InvestAccademy - Corso di Finanza Personale
"""

import streamlit as st
import pandas as pd

# Metadata
CAPITOLO_NUM = 4
TITOLO = "Il fondo di emergenza"

OBIETTIVI = [
    "Comprendere cos'è un fondo di emergenza",
    "Capire perché è una priorità assoluta",
    "Stimare l'importo corretto in base alla propria situazione",
    "Sapere dove collocarlo e come utilizzarlo",
    "Evitare gli errori più comuni nella gestione del fondo"
]

# Quiz
QUIZ = [
    {
        "id": 1,
        "domanda": "Il fondo di emergenza ha come obiettivo principale generare rendimento.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "Il fondo di emergenza non è un investimento. Il suo scopo principale è la stabilità, non il rendimento."
    },
    {
        "id": 2,
        "domanda": "Per un reddito stabile, quanti mesi di spese dovrebbe coprire il fondo emergenze?",
        "tipo": "scelta_multipla",
        "opzioni": ["1 mese", "3-6 mesi", "12-24 mesi", "Non serve"],
        "risposta_corretta": "3-6 mesi",
        "spiegazione": "Per situazioni stabili si consigliano 3-6 mesi di spese. Per redditi variabili o incerti, anche di più."
    },
    {
        "id": 3,
        "domanda": "Il fondo emergenze deve essere facilmente accessibile.",
        "tipo": "vero_falso",
        "risposta_corretta": True,
        "spiegazione": "Il fondo deve essere facilmente accessibile, separato dal conto operativo e protetto da rischi di mercato."
    },
    {
        "id": 4,
        "domanda": "È corretto usare il fondo emergenze per una vacanza pianificata.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "Il fondo va usato solo per eventi imprevisti, necessari e non rimandabili. Non per spese pianificate."
    },
    {
        "id": 5,
        "domanda": "Se le spese mensili sono €1.500 e vuoi 4 mesi di copertura, quanto deve essere il fondo?",
        "tipo": "numero",
        "risposta_corretta": 6000,
        "spiegazione": "€1.500 × 4 mesi = €6.000"
    }
]


def calcola_fondo_emergenze(spese_mensili: float, mesi: int) -> float:
    """Calcola l'importo del fondo emergenze"""
    return spese_mensili * mesi


def tempo_costruzione(obiettivo: float, risparmio_mensile: float) -> int:
    """Calcola i mesi necessari per costruire il fondo"""
    if risparmio_mensile <= 0:
        return 0
    return int(obiettivo / risparmio_mensile) + (1 if obiettivo % risparmio_mensile > 0 else 0)


def piano_costruzione(obiettivo: float, risparmio_mensile: float) -> list:
    """Genera il piano di costruzione del fondo"""
    piano = []
    accumulato = 0
    mese = 0
    while accumulato < obiettivo and mese < 120:
        mese += 1
        accumulato = min(accumulato + risparmio_mensile, obiettivo)
        piano.append({
            "mese": mese,
            "versamento": risparmio_mensile if accumulato < obiettivo else obiettivo - (accumulato - risparmio_mensile),
            "accumulato": accumulato,
            "copertura_mesi": accumulato / (obiettivo / 6) if obiettivo > 0 else 0  # Assumendo 6 mesi target
        })
    return piano


def render_contenuto():
    """Renderizza il contenuto teorico"""
    
    st.markdown("""
    ## Cos'è il fondo di emergenza
    
    Il fondo di emergenza è una **riserva di denaro destinata a far fronte a eventi imprevisti**.
    
    Serve a coprire spese inattese **senza dover ricorrere a debiti o disinvestimenti forzati**.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### ✅ È")
            st.markdown("""
            - Una riserva di sicurezza
            - Denaro facilmente accessibile
            - Protezione dalla volatilità della vita
            - La base della stabilità finanziaria
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### ❌ Non è")
            st.markdown("""
            - Un investimento
            - Un fondo per le vacanze
            - Denaro da far "lavorare"
            - Qualcosa di opzionale
            """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Perché il fondo di emergenza è fondamentale
    
    Gli imprevisti fanno parte della vita:
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("### 💼")
        st.markdown("Perdita o riduzione del reddito")
    
    with col2:
        st.markdown("### 🏥")
        st.markdown("Spese mediche impreviste")
    
    with col3:
        st.markdown("### 🔧")
        st.markdown("Riparazioni urgenti")
    
    with col4:
        st.markdown("### 👨‍👩‍👧")
        st.markdown("Eventi familiari inattesi")
    
    st.warning("""
    ⚠️ **Senza un fondo di emergenza, ogni imprevisto diventa una crisi finanziaria.**
    
    Con un fondo adeguato, l'impatto emotivo ed economico si riduce drasticamente.
    """)
    
    st.markdown("""
    ### Il fondo di emergenza protegge:
    - 💰 Il bilancio personale
    - 🧘 La serenità mentale
    - 📈 Il piano di investimento di lungo periodo
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Quanto dovrebbe essere grande
    
    Non esiste una cifra universale. La dimensione dipende da **fattori personali**:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 🟢 Situazioni stabili")
            st.markdown("""
            **3 mesi di spese**
            
            - Reddito fisso e sicuro
            - Nessuna persona a carico
            - Altre risorse disponibili
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### 🟠 Situazioni variabili")
            st.markdown("""
            **6+ mesi di spese**
            
            - Reddito variabile o incerto
            - Persone a carico
            - Unica fonte di reddito familiare
            """)
    
    st.info("""
    💡 **L'obiettivo:** poter mantenere il proprio tenore di vita per un periodo sufficiente 
    a gestire l'emergenza.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Come costruirlo nel tempo
    
    Il fondo di emergenza **non si crea in un giorno**. È più efficace costruirlo gradualmente:
    
    1. 📊 Accantonando una quota fissa ogni mese
    2. 🎁 Destinando entrate straordinarie (bonus, rimborsi)
    3. ⚙️ Automatizzando il processo
    
    > La priorità è la **costanza**, non la velocità.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Dove tenere il fondo di emergenza
    
    Il fondo deve essere:
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🔓 Accessibile")
        st.markdown("Disponibile in pochi giorni")
    
    with col2:
        st.markdown("### 📦 Separato")
        st.markdown("Distinto dal conto operativo")
    
    with col3:
        st.markdown("### 🛡️ Sicuro")
        st.markdown("Protetto da rischi di mercato")
    
    st.markdown("""
    **Strumenti comuni:**
    - Conti di risparmio
    - Conti deposito (non vincolati o con svincolo rapido)
    - Strumenti a bassissimo rischio e alta liquidità
    
    > Il rendimento è **secondario** rispetto alla disponibilità immediata.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Quando utilizzare il fondo
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### ✅ Usalo per:")
            st.markdown("""
            - Eventi **imprevisti**
            - Spese **necessarie**
            - Situazioni **non rimandabili**
            
            *Esempio: riparazione auto necessaria per lavorare*
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### ❌ Non usarlo per:")
            st.markdown("""
            - Spese pianificate
            - Acquisti impulsivi
            - Investimenti
            
            *Esempio: nuova TV in offerta*
            """)
    
    st.success("""
    ✅ **Regola d'oro:** Usarlo correttamente evita di trasformare un imprevisto 
    in un problema strutturale.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Errori comuni da evitare
    """)
    
    errori = [
        ("❌ Considerarlo un investimento", "Il fondo emergenze non deve generare rendimento, deve essere disponibile"),
        ("❌ Tenerlo in strumenti rischiosi", "No azioni, no crypto, no strumenti volatili"),
        ("❌ Utilizzarlo per spese non urgenti", "Resisti alla tentazione di 'prenderlo in prestito'"),
        ("❌ Non ricostruirlo dopo l'uso", "Dopo un prelievo, torna a versare appena possibile")
    ]
    
    for errore, spiegazione in errori:
        with st.container(border=True):
            st.markdown(f"**{errore}**")
            st.caption(spiegazione)
    
    st.warning("""
    ⚠️ Il fondo di emergenza è una **priorità continua**, non una fase temporanea.
    """)


def render_calcolatore():
    """Renderizza il calcolatore del fondo emergenze"""
    
    st.markdown("## 🧮 Calcolatore Fondo Emergenze")
    
    calc_type = st.radio(
        "Seleziona:",
        ["Calcola il tuo fondo", "Simula scenario emergenza"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if calc_type == "Calcola il tuo fondo":
        render_calc_fondo()
    else:
        render_calc_scenario()


def render_calc_fondo():
    """Calcolatore dimensionamento fondo"""
    
    st.markdown("### Quanto dovrebbe essere il tuo fondo emergenze?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📊 Le tue spese essenziali mensili")
        
        affitto = st.number_input("🏠 Affitto/Mutuo (€)", min_value=0.0, value=700.0, step=50.0, key="cap4_affitto")
        utenze = st.number_input("💡 Utenze (€)", min_value=0.0, value=150.0, step=10.0, key="cap4_utenze")
        cibo = st.number_input("🛒 Alimentari (€)", min_value=0.0, value=300.0, step=25.0, key="cap4_cibo")
        trasporti = st.number_input("🚗 Trasporti (€)", min_value=0.0, value=100.0, step=25.0, key="cap4_trasporti")
        altro = st.number_input("📋 Altre spese essenziali (€)", min_value=0.0, value=150.0, step=25.0, key="cap4_altro")
        
        spese_totali = affitto + utenze + cibo + trasporti + altro
        
        st.metric("Totale spese essenziali", f"€{spese_totali:,.2f}/mese")
    
    with col2:
        st.markdown("#### 🎯 Il tuo profilo")
        
        tipo_reddito = st.selectbox(
            "Tipo di reddito",
            ["Dipendente tempo indeterminato", "Dipendente tempo determinato", "Libero professionista", "Imprenditore", "Reddito misto"],
            key="cap4_tipo_reddito"
        )
        
        persone = st.number_input("Persone a carico", min_value=0, max_value=10, value=0, key="cap4_persone")
        
        altre_entrate = st.checkbox("Altre fonti di reddito in famiglia", key="cap4_altre_entrate")
        
        # Calcolo mesi consigliati
        mesi_base = {
            "Dipendente tempo indeterminato": 3,
            "Dipendente tempo determinato": 4,
            "Libero professionista": 6,
            "Imprenditore": 6,
            "Reddito misto": 4
        }
        
        mesi = mesi_base[tipo_reddito]
        mesi += persone  # +1 mese per ogni persona a carico
        if not altre_entrate:
            mesi += 1  # +1 mese se unica fonte di reddito
        
        mesi = min(mesi, 12)  # Max 12 mesi
        
        fondo_minimo = calcola_fondo_emergenze(spese_totali, 3)
        fondo_consigliato = calcola_fondo_emergenze(spese_totali, mesi)
        fondo_prudente = calcola_fondo_emergenze(spese_totali, min(mesi + 2, 12))
        
        st.markdown("#### 💰 Fondo emergenze consigliato")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Minimo", f"€{fondo_minimo:,.0f}", "3 mesi")
        with c2:
            st.metric("Consigliato", f"€{fondo_consigliato:,.0f}", f"{mesi} mesi", delta_color="off")
        with c3:
            st.metric("Prudente", f"€{fondo_prudente:,.0f}", f"{min(mesi+2, 12)} mesi")
        
        st.info(f"💡 Per il tuo profilo, consigliamo **{mesi} mesi** di spese essenziali.")
    
    st.markdown("---")
    
    st.markdown("### 🏗️ Piano di costruzione")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fondo_attuale = st.number_input(
            "Quanto hai già accantonato? (€)",
            min_value=0.0,
            value=0.0,
            step=100.0,
            key="cap4_fondo_attuale"
        )
        
        risparmio_mensile = st.number_input(
            "Quanto puoi accantonare al mese? (€)",
            min_value=0.0,
            value=200.0,
            step=25.0,
            key="cap4_risparmio"
        )
    
    with col2:
        mancante = max(0, fondo_consigliato - fondo_attuale)
        
        if mancante > 0 and risparmio_mensile > 0:
            mesi_necessari = tempo_costruzione(mancante, risparmio_mensile)
            anni = mesi_necessari // 12
            mesi_resto = mesi_necessari % 12
            
            st.metric("Da accumulare", f"€{mancante:,.0f}")
            
            if anni > 0:
                st.success(f"⏱️ Raggiungerai l'obiettivo in **{anni} anni e {mesi_resto} mesi**")
            else:
                st.success(f"⏱️ Raggiungerai l'obiettivo in **{mesi_necessari} mesi**")
            
            # Progress bar
            progresso = (fondo_attuale / fondo_consigliato) * 100 if fondo_consigliato > 0 else 0
            st.progress(min(progresso / 100, 1.0))
            st.caption(f"Progresso: {progresso:.1f}%")
        elif mancante <= 0:
            st.success("🎉 Hai già raggiunto l'obiettivo!")
            st.balloons()
        else:
            st.warning("Inserisci un importo di risparmio mensile per vedere il piano")


def render_calc_scenario():
    """Simulatore scenario di emergenza"""
    
    st.markdown("### Simula uno scenario di emergenza")
    
    st.markdown("""
    Questo simulatore ti aiuta a capire come il fondo emergenze 
    ti proteggerebbe in diverse situazioni.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        spese_mensili = st.number_input(
            "💸 Spese mensili essenziali (€)",
            min_value=100.0,
            value=1500.0,
            step=100.0,
            key="cap4_sim_spese"
        )
        
        fondo_disponibile = st.number_input(
            "💰 Fondo emergenze disponibile (€)",
            min_value=0.0,
            value=4500.0,
            step=500.0,
            key="cap4_sim_fondo"
        )
        
        scenario = st.selectbox(
            "🎭 Seleziona scenario",
            [
                "Perdita lavoro (0 reddito)",
                "Riduzione reddito 50%",
                "Spesa imprevista €2.000",
                "Spesa imprevista €5.000",
                "Combinazione: riduzione reddito + spesa imprevista"
            ],
            key="cap4_scenario"
        )
    
    with col2:
        st.markdown("#### 📊 Risultato simulazione")
        
        if scenario == "Perdita lavoro (0 reddito)":
            mesi_copertura = fondo_disponibile / spese_mensili if spese_mensili > 0 else 0
            st.metric("Mesi di autonomia", f"{mesi_copertura:.1f}")
            
            if mesi_copertura >= 6:
                st.success("✅ Hai tempo sufficiente per trovare una nuova occupazione")
            elif mesi_copertura >= 3:
                st.warning("⚠️ Tempo limitato. Inizia subito la ricerca attiva")
            else:
                st.error("🔴 Situazione critica. Considera di aumentare il fondo")
                
        elif scenario == "Riduzione reddito 50%":
            gap_mensile = spese_mensili * 0.5
            mesi_copertura = fondo_disponibile / gap_mensile if gap_mensile > 0 else 0
            st.metric("Mesi di copertura gap", f"{mesi_copertura:.1f}")
            st.info(f"Gap mensile da coprire: €{gap_mensile:,.0f}")
            
        elif scenario == "Spesa imprevista €2.000":
            residuo = fondo_disponibile - 2000
            mesi_residui = residuo / spese_mensili if spese_mensili > 0 else 0
            st.metric("Fondo residuo", f"€{max(0, residuo):,.0f}")
            st.metric("Mesi di copertura residui", f"{max(0, mesi_residui):.1f}")
            
            if residuo > 0:
                st.success("✅ Spesa coperta, fondo ancora attivo")
            else:
                st.error("🔴 Fondo insufficiente per questa emergenza")
                
        elif scenario == "Spesa imprevista €5.000":
            residuo = fondo_disponibile - 5000
            mesi_residui = residuo / spese_mensili if spese_mensili > 0 else 0
            st.metric("Fondo residuo", f"€{max(0, residuo):,.0f}")
            
            if residuo > 0:
                st.warning(f"⚠️ Spesa coperta ma fondo ridotto a {mesi_residui:.1f} mesi")
            else:
                deficit = abs(residuo)
                st.error(f"🔴 Deficit di €{deficit:,.0f}. Servirebbe indebitarsi")
                
        else:  # Combinazione
            spesa_extra = 3000
            gap_mensile = spese_mensili * 0.3
            fondo_dopo_spesa = fondo_disponibile - spesa_extra
            
            if fondo_dopo_spesa > 0:
                mesi_copertura = fondo_dopo_spesa / gap_mensile if gap_mensile > 0 else 0
                st.metric("Dopo spesa imprevista €3.000", f"€{fondo_dopo_spesa:,.0f}")
                st.metric("Mesi copertura gap 30%", f"{mesi_copertura:.1f}")
            else:
                st.error("🔴 Fondo già esaurito dalla spesa imprevista")
        
        # Raccomandazione
        st.markdown("---")
        st.markdown("#### 💡 Raccomandazione")
        
        mesi_attuali = fondo_disponibile / spese_mensili if spese_mensili > 0 else 0
        if mesi_attuali < 3:
            st.error("Priorità assoluta: porta il fondo ad almeno 3 mesi di spese")
        elif mesi_attuali < 6:
            st.warning("Buon inizio! Continua fino a 6 mesi per maggiore sicurezza")
        else:
            st.success("Ottimo livello di protezione! Mantienilo e ricostruiscilo dopo ogni uso")


def render_quiz():
    """Renderizza il quiz di verifica"""
    
    st.markdown("## 📝 Quiz di verifica")
    
    if "cap4_risposte" not in st.session_state:
        st.session_state.cap4_risposte = {}
    if "cap4_verificato" not in st.session_state:
        st.session_state.cap4_verificato = False
    
    for i, q in enumerate(QUIZ):
        with st.container(border=True):
            st.markdown(f"**Domanda {i+1}:** {q['domanda']}")
            
            if q["tipo"] == "vero_falso":
                risposta = st.radio(
                    "Seleziona:",
                    ["Vero", "Falso"],
                    key=f"cap4_q{q['id']}",
                    horizontal=True
                )
                st.session_state.cap4_risposte[q['id']] = risposta == "Vero"
                
            elif q["tipo"] == "scelta_multipla":
                risposta = st.radio(
                    "Seleziona:",
                    q["opzioni"],
                    key=f"cap4_q{q['id']}"
                )
                st.session_state.cap4_risposte[q['id']] = risposta
                
            elif q["tipo"] == "numero":
                risposta = st.number_input(
                    "Inserisci il valore:",
                    key=f"cap4_q{q['id']}",
                    step=100.0
                )
                st.session_state.cap4_risposte[q['id']] = risposta
            
            if st.session_state.cap4_verificato:
                user_ans = st.session_state.cap4_risposte.get(q['id'])
                if q["tipo"] == "numero":
                    corretto = abs(user_ans - q["risposta_corretta"]) < 10
                else:
                    corretto = user_ans == q["risposta_corretta"]
                
                if corretto:
                    st.success(f"✅ Corretto! {q['spiegazione']}")
                else:
                    st.error(f"❌ Sbagliato. Risposta corretta: {q['risposta_corretta']}")
                    st.info(q['spiegazione'])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Verifica risposte", type="primary", use_container_width=True, key="cap4_verifica"):
            st.session_state.cap4_verificato = True
            st.rerun()
    with col2:
        if st.button("🔄 Ricomincia", use_container_width=True, key="cap4_reset"):
            st.session_state.cap4_verificato = False
            st.session_state.cap4_risposte = {}
            st.rerun()


def render_takeaways():
    """Renderizza i punti chiave"""
    
    st.markdown("## 💡 Punti chiave")
    
    takeaways = [
        "Il fondo emergenze è una riserva di sicurezza, non un investimento",
        "Obiettivo: 3-6 mesi di spese essenziali (di più per redditi variabili)",
        "Deve essere facilmente accessibile, separato e a basso rischio",
        "Usalo solo per eventi imprevisti, necessari e non rimandabili",
        "Ricostruiscilo sempre dopo ogni utilizzo",
        "Il fondo emergenze protegge anche il piano di investimento di lungo periodo"
    ]
    
    for t in takeaways:
        st.markdown(f"- {t}")
    
    st.markdown("---")
    
    # Esercizio pratico
    with st.expander("📝 Esercizio pratico"):
        st.markdown("""
        **Costruisci il tuo piano personale:**
        
        1. **Calcola** le tue spese mensili essenziali
           - Affitto/mutuo: _____€
           - Utenze: _____€
           - Alimentari: _____€
           - Trasporti: _____€
           - Altro essenziale: _____€
           - **Totale: _____€**
        
        2. **Moltiplica** per il numero di mesi adeguato alla tua situazione
           - Reddito stabile: × 3-4 mesi
           - Reddito variabile: × 6+ mesi
           - **Obiettivo fondo: _____€**
        
        3. **Definisci** una quota mensile da destinare al fondo
           - Risparmio mensile: _____€
           - Tempo necessario: _____ mesi
        
        4. **Separa** il fondo dal resto del denaro
           - Conto dedicato: ________________
        
        ---
        
        💡 *Il tempo necessario è parte del piano, non un fallimento.*
        """)
    
    # Checklist finale
    with st.expander("✅ Checklist del fondo emergenze"):
        st.markdown("""
        Usa questa checklist per verificare il tuo fondo:
        
        - [ ] Ho calcolato le mie spese essenziali mensili
        - [ ] Ho definito l'obiettivo in base al mio profilo
        - [ ] Il fondo è su un conto separato
        - [ ] È facilmente accessibile (max 2-3 giorni)
        - [ ] Non è esposto a rischi di mercato
        - [ ] Ho un piano per ricostruirlo dopo ogni uso
        - [ ] So distinguere tra emergenza vera e spesa rinviabile
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
        "🧮 Calcolatore", 
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
