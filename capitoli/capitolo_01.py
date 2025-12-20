"""
Capitolo 1: Introduzione alla finanza personale
InvestAccademy - Corso di Finanza Personale
"""

import streamlit as st

# Metadata
CAPITOLO_NUM = 1
TITOLO = "Introduzione alla finanza personale"

OBIETTIVI = [
    "Definire correttamente la finanza personale e i suoi ambiti principali",
    "Comprendere l'importanza del controllo del cash flow",
    "Impostare priorità finanziarie solide e realistiche",
    "Applicare un metodo pratico per analizzare la tua situazione finanziaria mensile"
]

# Quiz
QUIZ = [
    {
        "id": 1,
        "domanda": "La finanza personale riguarda solo gli investimenti.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "La finanza personale riguarda l'insieme delle decisioni su reddito, spesa, risparmio, investimento e protezione."
    },
    {
        "id": 2,
        "domanda": "Il cash flow è la differenza tra entrate e uscite.",
        "tipo": "vero_falso",
        "risposta_corretta": True,
        "spiegazione": "Corretto. Il cash flow misura esattamente questo: quanto entra meno quanto esce."
    },
    {
        "id": 3,
        "domanda": "Qual è generalmente la priorità prima di investire?",
        "tipo": "scelta_multipla",
        "opzioni": ["Azioni speculative", "Fondo emergenze", "Criptovalute", "Trading ad alta frequenza"],
        "risposta_corretta": "Fondo emergenze",
        "spiegazione": "Il fondo emergenze viene prima degli investimenti per evitare di dover disinvestire in momenti sfavorevoli."
    },
    {
        "id": 4,
        "domanda": "Se il reddito netto è €3.000, le spese fisse €1.500 e le spese variabili €900, quanto resta per il risparmio?",
        "tipo": "numero",
        "risposta_corretta": 600,
        "spiegazione": "€3.000 - €1.500 - €900 = €600"
    }
]


def calcola_cash_flow(reddito: float, spese_fisse: float, spese_variabili: float) -> dict:
    """Calcola e analizza il cash flow mensile"""
    risparmio = reddito - spese_fisse - spese_variabili
    
    if reddito > 0:
        perc_fisse = (spese_fisse / reddito) * 100
        perc_variabili = (spese_variabili / reddito) * 100
        perc_risparmio = (risparmio / reddito) * 100
    else:
        perc_fisse = perc_variabili = perc_risparmio = 0
    
    if perc_risparmio >= 20:
        valutazione = ("🟢", "Ottimo! Stai risparmiando più del 20%")
    elif perc_risparmio >= 10:
        valutazione = ("🟡", "Buono. Margine di risparmio nella norma")
    elif perc_risparmio > 0:
        valutazione = ("🟠", "Attenzione. Margine di risparmio ridotto")
    else:
        valutazione = ("🔴", "Critico. Spese superiori alle entrate")
    
    return {
        "risparmio": risparmio,
        "perc_fisse": perc_fisse,
        "perc_variabili": perc_variabili,
        "perc_risparmio": perc_risparmio,
        "valutazione": valutazione
    }


def render_contenuto():
    """Renderizza il contenuto teorico del capitolo"""
    
    st.markdown("""
    ## Cos'è la finanza personale
    
    La finanza personale riguarda l'insieme delle decisioni che ciascuno di noi prende 
    in merito a **reddito, spesa, risparmio, investimento e protezione**. Non è una disciplina 
    teorica riservata agli esperti, ma una competenza pratica che influisce quotidianamente 
    sulla qualità della nostra vita.
    
    > Gestire bene la finanza personale non vuol dire "fare trading" o cercare rendimenti 
    > elevati, ma costruire **stabilità, flessibilità e libertà di scelta** nel tempo.
    """)
    
    st.markdown("---")
    st.markdown("## I tre pilastri della finanza personale")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 1️⃣ Cash Flow")
            st.markdown("""
            Il cash flow è la **differenza tra entrate e uscite** mensili.
            
            È il vero motore di tutte le decisioni finanziarie.
            
            **Regola:** Prima controlli il flusso di cassa, poi prendi decisioni.
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### 2️⃣ Priorità")
            st.markdown("""
            L'ordine consigliato:
            1. Spese essenziali
            2. Fondo emergenze
            3. Rimborso debiti
            4. Risparmio obiettivi
            5. Investimenti
            """)
    
    with col3:
        with st.container(border=True):
            st.markdown("### 3️⃣ Sostenibilità")
            st.markdown("""
            Le buone decisioni finanziarie sono quelle **ripetibili nel tempo**.
            
            Un piano sostenibile produce risultati migliori grazie alla **costanza**.
            """)


def render_calcolatore():
    """Renderizza il calcolatore di cash flow"""
    
    st.markdown("## 🧮 Calcolatore Cash Flow")
    st.markdown("Inserisci i tuoi dati per analizzare il tuo flusso di cassa mensile.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        reddito = st.number_input(
            "💰 Reddito netto mensile (€)",
            min_value=0.0,
            value=2400.0,
            step=100.0,
            key="cap1_reddito"
        )
        spese_fisse = st.number_input(
            "🏠 Spese fisse (€)",
            min_value=0.0,
            value=1200.0,
            step=50.0,
            help="Affitto, mutuo, utenze, assicurazioni...",
            key="cap1_fisse"
        )
        spese_variabili = st.number_input(
            "🛒 Spese variabili (€)",
            min_value=0.0,
            value=700.0,
            step=50.0,
            help="Cibo, trasporti, tempo libero...",
            key="cap1_variabili"
        )
    
    with col2:
        if reddito > 0:
            risultato = calcola_cash_flow(reddito, spese_fisse, spese_variabili)
            
            st.markdown("### Risultato")
            
            # Metriche
            st.metric(
                "Risparmio disponibile",
                f"€{risultato['risparmio']:,.2f}",
                f"{risultato['perc_risparmio']:.1f}% del reddito"
            )
            
            st.markdown(f"**Valutazione:** {risultato['valutazione'][0]} {risultato['valutazione'][1]}")
            
            # Grafico distribuzione
            st.markdown("#### Distribuzione")
            
            import pandas as pd
            data = {
                "Categoria": ["Spese fisse", "Spese variabili", "Risparmio"],
                "Importo": [spese_fisse, spese_variabili, max(0, risultato['risparmio'])],
                "Percentuale": [
                    risultato['perc_fisse'],
                    risultato['perc_variabili'],
                    max(0, risultato['perc_risparmio'])
                ]
            }
            
            # Visualizza con barre orizzontali
            for cat, imp, perc in zip(data["Categoria"], data["Importo"], data["Percentuale"]):
                col_a, col_b = st.columns([3, 1])
                with col_a:
                    st.progress(min(perc / 100, 1.0))
                with col_b:
                    st.caption(f"{cat}: {perc:.1f}%")


def render_quiz():
    """Renderizza il quiz di verifica"""
    
    st.markdown("## 📝 Quiz di verifica")
    
    # Inizializza stato quiz
    if "cap1_risposte" not in st.session_state:
        st.session_state.cap1_risposte = {}
    if "cap1_verificato" not in st.session_state:
        st.session_state.cap1_verificato = False
    
    for i, q in enumerate(QUIZ):
        with st.container(border=True):
            st.markdown(f"**Domanda {i+1}:** {q['domanda']}")
            
            if q["tipo"] == "vero_falso":
                risposta = st.radio(
                    "Seleziona:",
                    ["Vero", "Falso"],
                    key=f"cap1_q{q['id']}",
                    horizontal=True
                )
                st.session_state.cap1_risposte[q['id']] = risposta == "Vero"
                
            elif q["tipo"] == "scelta_multipla":
                risposta = st.radio(
                    "Seleziona:",
                    q["opzioni"],
                    key=f"cap1_q{q['id']}"
                )
                st.session_state.cap1_risposte[q['id']] = risposta
                
            elif q["tipo"] == "numero":
                risposta = st.number_input(
                    "Inserisci il valore:",
                    key=f"cap1_q{q['id']}",
                    step=1.0
                )
                st.session_state.cap1_risposte[q['id']] = risposta
            
            # Mostra feedback se verificato
            if st.session_state.cap1_verificato:
                user_ans = st.session_state.cap1_risposte.get(q['id'])
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
        if st.button("✅ Verifica risposte", type="primary", use_container_width=True):
            st.session_state.cap1_verificato = True
            st.rerun()
    with col2:
        if st.button("🔄 Ricomincia", use_container_width=True):
            st.session_state.cap1_verificato = False
            st.session_state.cap1_risposte = {}
            st.rerun()


def render_takeaways():
    """Renderizza i punti chiave"""
    
    st.markdown("## 💡 Punti chiave")
    
    takeaways = [
        "La finanza personale è una competenza pratica che influisce sulla qualità della vita",
        "Il cash flow è il punto di partenza: prima misura, poi decidi",
        "Rispetta l'ordine delle priorità finanziarie",
        "Un piano sostenibile batte sempre un piano perfetto ma irrealistico",
        "Senza misurazione non esiste miglioramento"
    ]
    
    for t in takeaways:
        st.markdown(f"- {t}")


def render():
    """Funzione principale per renderizzare il capitolo"""
    
    st.title(f"📖 Capitolo {CAPITOLO_NUM}")
    st.header(TITOLO)
    
    # Obiettivi
    with st.expander("🎯 Obiettivi di apprendimento", expanded=False):
        for obj in OBIETTIVI:
            st.markdown(f"- {obj}")
    
    st.markdown("---")
    
    # Tabs per navigazione interna
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
