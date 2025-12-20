"""
Capitolo 3: Risparmio e obiettivi finanziari
InvestAccademy - Corso di Finanza Personale
"""

import streamlit as st
import pandas as pd

# Metadata
CAPITOLO_NUM = 3
TITOLO = "Risparmio e obiettivi finanziari"

OBIETTIVI = [
    "Definire obiettivi finanziari in modo chiaro e misurabile",
    "Utilizzare il metodo SMART per trasformare desideri in piani concreti",
    "Costruire un piano di risparmio sostenibile nel tempo",
    "Comprendere il ruolo e la dimensione corretta del fondo emergenze",
    "Applicare tecniche pratiche per aumentare la capacità di risparmio"
]

# Quiz
QUIZ = [
    {
        "id": 1,
        "domanda": "Cosa significa la 'S' nell'acronimo SMART?",
        "tipo": "scelta_multipla",
        "opzioni": ["Semplice", "Specifico", "Sicuro", "Sostenibile"],
        "risposta_corretta": "Specifico",
        "spiegazione": "SMART = Specifico, Misurabile, Raggiungibile (Affordable), Rilevante, Temporizzato."
    },
    {
        "id": 2,
        "domanda": "Qual è la funzione principale del fondo emergenze?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Generare rendimenti elevati",
            "Coprire spese impreviste senza indebitarsi",
            "Investire in azioni",
            "Pagare le vacanze"
        ],
        "risposta_corretta": "Coprire spese impreviste senza indebitarsi",
        "spiegazione": "Il fondo emergenze serve a coprire spese impreviste senza dover vendere investimenti o indebitarsi."
    },
    {
        "id": 3,
        "domanda": "Se le spese essenziali sono €900/mese, quanto dovrebbe essere un fondo emergenze di 6 mesi?",
        "tipo": "numero",
        "risposta_corretta": 5400,
        "spiegazione": "€900 × 6 mesi = €5.400"
    },
    {
        "id": 4,
        "domanda": "Il risparmio automatico riduce la tentazione di spendere.",
        "tipo": "vero_falso",
        "risposta_corretta": True,
        "spiegazione": "L'automazione riduce l'attrito decisionale e rende il risparmio una conseguenza, non una scelta quotidiana."
    },
    {
        "id": 5,
        "domanda": "È sempre meglio investire subito piuttosto che creare un fondo emergenze.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "No: senza fondo emergenze si rischia di liquidare investimenti in momenti sfavorevoli."
    }
]


def calcola_risparmio_periodico(obiettivo: float, mesi: int) -> float:
    """Calcola il risparmio mensile necessario"""
    if mesi <= 0:
        return 0
    return obiettivo / mesi


def calcola_tempo_obiettivo(obiettivo: float, risparmio_mensile: float) -> int:
    """Calcola i mesi necessari per raggiungere l'obiettivo"""
    if risparmio_mensile <= 0:
        return 0
    return int(obiettivo / risparmio_mensile)


def calcola_fondo_emergenze(spese_mensili: float, mesi: int) -> float:
    """Calcola l'importo del fondo emergenze"""
    return spese_mensili * mesi


def piano_risparmio(obiettivo: float, risparmio_mensile: float) -> list:
    """Genera il piano di accumulo mese per mese"""
    piano = []
    accumulato = 0
    mese = 0
    while accumulato < obiettivo:
        mese += 1
        accumulato += risparmio_mensile
        piano.append({
            "mese": mese,
            "versamento": risparmio_mensile,
            "accumulato": min(accumulato, obiettivo),
            "percentuale": min((accumulato / obiettivo) * 100, 100)
        })
        if mese > 360:  # Limite di 30 anni
            break
    return piano


def render_contenuto():
    """Renderizza il contenuto teorico"""
    
    st.markdown("""
    ## Il ruolo del risparmio nella finanza personale
    
    Il risparmio è il **ponte tra il controllo del cash flow e gli investimenti**. 
    Senza risparmio non esiste investimento; senza obiettivi il risparmio perde motivazione.
    
    > Risparmiare non significa privarsi di tutto, ma rinviare una parte dei consumi presenti 
    > per ottenere maggiore sicurezza e libertà futura.
    
    La chiave non è l'importo iniziale, ma la **regolarità**.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Obiettivi finanziari: perché sono fondamentali
    
    Gli obiettivi finanziari danno una **direzione al denaro**. Senza obiettivi chiari, 
    il risparmio tende a essere irregolare e facilmente sacrificabile.
    
    Un buon obiettivo risponde a cinque domande:
    - **Quanto?** L'importo target
    - **Entro quando?** La scadenza
    - **Per cosa?** Lo scopo specifico
    - **Perché è importante?** La motivazione
    - **È realistico?** La fattibilità
    """)
    
    st.markdown("---")
    
    st.markdown("## Il metodo SMART")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 🎯 Un obiettivo SMART è:")
            st.markdown("""
            - **S**pecifico: chiaramente definito
            - **M**isurabile: quantificabile in euro
            - **A**ffordable (Raggiungibile): coerente con reddito e spese
            - **R**ilevante: significativo per la tua vita
            - **T**emporizzato: con una scadenza precisa
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### ❌ vs ✅")
            st.markdown("""
            ❌ *"Voglio risparmiare"*
            
            Non è un obiettivo SMART.
            
            ✅ *"Accumulare €6.000 in 24 mesi per un fondo emergenze"*
            
            Questo è un obiettivo SMART!
            """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Costruire un piano di risparmio
    
    Una volta definito l'obiettivo, il passo successivo è tradurlo in un **importo periodico**.
    """)
    
    st.latex(r"\text{Risparmio periodico} = \frac{\text{Obiettivo}}{\text{Numero di periodi}}")
    
    st.info("""
    💡 **Se l'importo non è sostenibile, puoi:**
    - Estendere l'orizzonte temporale
    - Ridurre l'obiettivo
    - Intervenire su entrate o spese
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Tecniche pratiche per aumentare il risparmio
    
    | Tecnica | Descrizione |
    |---------|-------------|
    | **Regola 50/30/20** | 50% bisogni, 30% desideri, 20% risparmio/debito |
    | **Risparmio automatico** | Trasferimenti programmati appena arriva il reddito |
    | **Revisione spese ricorrenti** | Abbonamenti, servizi inutilizzati |
    | **Aumenti progressivi** | Ogni aumento di reddito genera più risparmio |
    
    > L'automazione riduce l'attrito decisionale e rende il risparmio una conseguenza, 
    > non una scelta quotidiana.
    """)


def render_calcolatore():
    """Renderizza i calcolatori"""
    
    st.markdown("## 🧮 Calcolatori")
    
    calc_type = st.radio(
        "Seleziona calcolatore:",
        ["Piano di Risparmio", "Fondo Emergenze", "Regola 50/30/20"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if calc_type == "Piano di Risparmio":
        render_calc_piano()
    elif calc_type == "Fondo Emergenze":
        render_calc_fondo()
    else:
        render_calc_503020()


def render_calc_piano():
    """Calcolatore piano di risparmio SMART"""
    
    st.markdown("### Piano di Risparmio SMART")
    
    col1, col2 = st.columns(2)
    
    with col1:
        nome_obiettivo = st.text_input(
            "🎯 Nome obiettivo",
            value="Vacanza",
            key="cap3_nome_ob"
        )
        obiettivo = st.number_input(
            "💰 Importo obiettivo (€)",
            min_value=100.0,
            value=3600.0,
            step=100.0,
            key="cap3_obiettivo"
        )
        
        modalita = st.radio(
            "Modalità di calcolo:",
            ["Calcola risparmio mensile", "Calcola tempo necessario"],
            key="cap3_modalita"
        )
        
        if modalita == "Calcola risparmio mensile":
            mesi = st.slider(
                "📅 Mesi disponibili",
                min_value=1,
                max_value=120,
                value=12,
                key="cap3_mesi"
            )
            risparmio = calcola_risparmio_periodico(obiettivo, mesi)
        else:
            risparmio = st.number_input(
                "💵 Risparmio mensile disponibile (€)",
                min_value=10.0,
                value=300.0,
                step=10.0,
                key="cap3_risparmio"
            )
            mesi = calcola_tempo_obiettivo(obiettivo, risparmio)
    
    with col2:
        st.markdown("### Risultato")
        
        if modalita == "Calcola risparmio mensile":
            st.metric(
                f"Risparmio mensile per '{nome_obiettivo}'",
                f"€{risparmio:,.2f}"
            )
            anni = mesi // 12
            mesi_resto = mesi % 12
            tempo_str = f"{anni} anni e {mesi_resto} mesi" if anni > 0 else f"{mesi} mesi"
            st.info(f"⏱️ Tempo: {tempo_str}")
        else:
            anni = mesi // 12
            mesi_resto = mesi % 12
            if anni > 0:
                st.metric(
                    f"Tempo per '{nome_obiettivo}'",
                    f"{anni} anni e {mesi_resto} mesi"
                )
            else:
                st.metric(
                    f"Tempo per '{nome_obiettivo}'",
                    f"{mesi} mesi"
                )
            st.info(f"💵 Risparmio mensile: €{risparmio:,.2f}")
        
        # Verifica SMART
        st.markdown("#### ✅ Checklist SMART")
        st.markdown(f"- **Specifico:** {nome_obiettivo}")
        st.markdown(f"- **Misurabile:** €{obiettivo:,.2f}")
        st.markdown(f"- **Temporizzato:** {mesi} mesi")
        
        # Grafico evoluzione
        if mesi > 0 and mesi <= 120:
            piano = piano_risparmio(obiettivo, risparmio)
            df = pd.DataFrame(piano)
            st.markdown("#### 📈 Evoluzione accumulo")
            st.line_chart(df.set_index("mese")["accumulato"])


def render_calc_fondo():
    """Calcolatore fondo emergenze"""
    
    st.markdown("### Dimensionamento Fondo Emergenze")
    
    col1, col2 = st.columns(2)
    
    with col1:
        spese_mensili = st.number_input(
            "💸 Spese essenziali mensili (€)",
            min_value=100.0,
            value=1200.0,
            step=100.0,
            help="Affitto, utenze, cibo, trasporti essenziali",
            key="cap3_spese_ess"
        )
        
        stabilita = st.select_slider(
            "📊 Stabilità del reddito",
            options=["Molto instabile", "Instabile", "Medio", "Stabile", "Molto stabile"],
            value="Medio",
            key="cap3_stabilita"
        )
        
        persone_carico = st.number_input(
            "👨‍👩‍👧 Persone a carico",
            min_value=0,
            max_value=10,
            value=0,
            key="cap3_persone"
        )
        
        # Calcolo mesi consigliati
        mesi_base = {"Molto instabile": 9, "Instabile": 6, "Medio": 5, "Stabile": 4, "Molto stabile": 3}
        mesi_consigliati = mesi_base[stabilita] + persone_carico
        
        mesi_fondo = st.slider(
            "📅 Mesi di copertura",
            min_value=1,
            max_value=12,
            value=min(mesi_consigliati, 12),
            key="cap3_mesi_fondo"
        )
    
    with col2:
        fondo_target = calcola_fondo_emergenze(spese_mensili, mesi_fondo)
        
        st.markdown("### Risultato")
        
        st.metric(
            "Fondo emergenze target",
            f"€{fondo_target:,.2f}",
            f"{mesi_fondo} mesi di spese"
        )
        
        st.info(f"💡 **Consigliato per il tuo profilo:** {mesi_consigliati} mesi (€{spese_mensili * mesi_consigliati:,.2f})")
        
        # Piano di costruzione
        st.markdown("#### 🏗️ Piano di costruzione")
        
        risparmio_fondo = st.number_input(
            "Quanto puoi accantonare al mese? (€)",
            min_value=10.0,
            value=200.0,
            step=10.0,
            key="cap3_risparmio_fondo"
        )
        
        mesi_necessari = calcola_tempo_obiettivo(fondo_target, risparmio_fondo)
        anni = mesi_necessari // 12
        mesi_resto = mesi_necessari % 12
        
        if anni > 0:
            st.success(f"⏱️ Raggiungerai l'obiettivo in **{anni} anni e {mesi_resto} mesi**")
        else:
            st.success(f"⏱️ Raggiungerai l'obiettivo in **{mesi_necessari} mesi**")


def render_calc_503020():
    """Calcolatore regola 50/30/20"""
    
    st.markdown("### Regola 50/30/20")
    
    st.markdown("""
    La regola 50/30/20 è una linea guida semplice per allocare il reddito:
    - **50%** per i bisogni essenziali
    - **30%** per i desideri
    - **20%** per risparmio e rimborso debiti
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        reddito = st.number_input(
            "💰 Reddito netto mensile (€)",
            min_value=100.0,
            value=2400.0,
            step=100.0,
            key="cap3_reddito_503020"
        )
    
    with col2:
        bisogni = reddito * 0.50
        desideri = reddito * 0.30
        risparmio = reddito * 0.20
        
        st.markdown("### Allocazione consigliata")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("🏠 Bisogni (50%)", f"€{bisogni:,.2f}")
        with c2:
            st.metric("🎯 Desideri (30%)", f"€{desideri:,.2f}")
        with c3:
            st.metric("💰 Risparmio (20%)", f"€{risparmio:,.2f}")
    
    st.markdown("---")
    
    st.markdown("#### Confronta con la tua situazione attuale")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        bisogni_reali = st.number_input(
            "Bisogni attuali (€)",
            min_value=0.0,
            value=1200.0,
            step=50.0,
            key="cap3_bisogni_reali"
        )
    
    with col2:
        desideri_reali = st.number_input(
            "Desideri attuali (€)",
            min_value=0.0,
            value=800.0,
            step=50.0,
            key="cap3_desideri_reali"
        )
    
    with col3:
        risparmio_reale = reddito - bisogni_reali - desideri_reali
        st.metric(
            "Risparmio risultante",
            f"€{risparmio_reale:,.2f}",
            f"{(risparmio_reale/reddito*100):.1f}% del reddito" if reddito > 0 else ""
        )
    
    # Feedback
    if reddito > 0:
        perc_risparmio = (risparmio_reale / reddito) * 100
        if perc_risparmio >= 20:
            st.success("✅ Ottimo! Stai rispettando o superando la regola del 20%")
        elif perc_risparmio >= 10:
            st.warning(f"⚠️ Sei al {perc_risparmio:.1f}%. Prova ad avvicinarti al 20%")
        elif perc_risparmio > 0:
            st.error(f"🔴 Solo {perc_risparmio:.1f}% di risparmio. Rivedi le spese")
        else:
            st.error("🔴 Attenzione: spese superiori alle entrate!")


def render_quiz():
    """Renderizza il quiz di verifica"""
    
    st.markdown("## 📝 Quiz di verifica")
    
    if "cap3_risposte" not in st.session_state:
        st.session_state.cap3_risposte = {}
    if "cap3_verificato" not in st.session_state:
        st.session_state.cap3_verificato = False
    
    for i, q in enumerate(QUIZ):
        with st.container(border=True):
            st.markdown(f"**Domanda {i+1}:** {q['domanda']}")
            
            if q["tipo"] == "vero_falso":
                risposta = st.radio(
                    "Seleziona:",
                    ["Vero", "Falso"],
                    key=f"cap3_q{q['id']}",
                    horizontal=True
                )
                st.session_state.cap3_risposte[q['id']] = risposta == "Vero"
                
            elif q["tipo"] == "scelta_multipla":
                risposta = st.radio(
                    "Seleziona:",
                    q["opzioni"],
                    key=f"cap3_q{q['id']}"
                )
                st.session_state.cap3_risposte[q['id']] = risposta
                
            elif q["tipo"] == "numero":
                risposta = st.number_input(
                    "Inserisci il valore:",
                    key=f"cap3_q{q['id']}",
                    step=100.0
                )
                st.session_state.cap3_risposte[q['id']] = risposta
            
            if st.session_state.cap3_verificato:
                user_ans = st.session_state.cap3_risposte.get(q['id'])
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
        if st.button("✅ Verifica risposte", type="primary", use_container_width=True, key="cap3_verifica"):
            st.session_state.cap3_verificato = True
            st.rerun()
    with col2:
        if st.button("🔄 Ricomincia", use_container_width=True, key="cap3_reset"):
            st.session_state.cap3_verificato = False
            st.session_state.cap3_risposte = {}
            st.rerun()


def render_takeaways():
    """Renderizza i punti chiave"""
    
    st.markdown("## 💡 Punti chiave")
    
    takeaways = [
        "Il risparmio è il ponte tra cash flow e investimenti",
        "Obiettivi SMART trasformano desideri vaghi in piani concreti",
        "Risparmio periodico = Obiettivo ÷ Numero di periodi",
        "Il fondo emergenze (3-6 mesi di spese) viene prima degli investimenti",
        "L'automazione del risparmio riduce l'attrito decisionale",
        "La regola 50/30/20 è una guida semplice per allocare il reddito"
    ]
    
    for t in takeaways:
        st.markdown(f"- {t}")
    
    st.markdown("---")
    
    # Esercizio guidato
    with st.expander("📝 Esercizio guidato"):
        st.markdown("""
        **Scenario:** Vuoi accumulare €4.800 in 24 mesi.
        
        **Calcolo:**
        """)
        
        st.latex(r"\text{Risparmio mensile} = \frac{4.800}{24} = €200")
        
        st.markdown("""
        **Domanda:** Se oggi risparmi €120, dove puoi trovare gli €80 mancanti?
        
        **Possibili soluzioni:**
        - Ridurre spese variabili (abbonamenti, uscite)
        - Aumentare le entrate (lavoro extra, vendita oggetti inutilizzati)
        - Estendere l'orizzonte temporale a 40 mesi (€120/mese)
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
