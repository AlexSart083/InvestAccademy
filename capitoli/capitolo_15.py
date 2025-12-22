"""
Capitolo 15: Psicologia dell'investitore e bias comportamentali
InvestAccademy - Corso di Finanza Personale
"""

import streamlit as st
import pandas as pd

# Metadata
CAPITOLO_NUM = 15
TITOLO = "Psicologia dell'investitore e bias comportamentali"

OBIETTIVI = [
    "Comprendere perché la psicologia conta più della tecnica",
    "Riconoscere i principali bias comportamentali",
    "Capire come emozioni e decisioni finanziarie sono collegate",
    "Applicare strategie pratiche per ridurre gli errori comportamentali",
    "Costruire un processo di investimento più razionale e disciplinato"
]

QUIZ = [
    {
        "id": 1,
        "domanda": "Cos'è l'avversione alle perdite?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "La tendenza a soffrire più per una perdita che a gioire per un guadagno equivalente",
            "La paura di investire",
            "L'incapacità di guadagnare",
            "Un tipo di investimento"
        ],
        "risposta_corretta": "La tendenza a soffrire più per una perdita che a gioire per un guadagno equivalente",
        "spiegazione": "L'avversione alle perdite è un bias per cui le perdite pesano psicologicamente circa il doppio dei guadagni equivalenti."
    },
    {
        "id": 2,
        "domanda": "Perché l'overconfidence (eccesso di fiducia) è pericolosa negli investimenti?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Porta a prendere rischi eccessivi e a fare trading troppo frequente",
            "Fa guadagnare di più",
            "Non è pericolosa",
            "Aiuta a investire meglio"
        ],
        "risposta_corretta": "Porta a prendere rischi eccessivi e a fare trading troppo frequente",
        "spiegazione": "L'eccesso di fiducia porta a sovrastimare le proprie capacità, generando trading eccessivo e sottovalutazione dei rischi."
    },
    {
        "id": 3,
        "domanda": "In che modo l'automazione aiuta l'investitore?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Riduce l'intervento emotivo e mantiene la disciplina",
            "Fa guadagnare di più",
            "Elimina tutti i rischi",
            "Non aiuta"
        ],
        "risposta_corretta": "Riduce l'intervento emotivo e mantiene la disciplina",
        "spiegazione": "L'automazione (PAC, ribilanciamenti automatici) elimina le decisioni emotive e mantiene coerenza con il piano."
    },
    {
        "id": 4,
        "domanda": "Il bias di conferma porta a cercare solo informazioni che confermano le proprie idee.",
        "tipo": "vero_falso",
        "risposta_corretta": True,
        "spiegazione": "Il bias di conferma ci porta a ignorare informazioni contrarie alle nostre convinzioni, riducendo la capacità di valutazione obiettiva."
    },
    {
        "id": 5,
        "domanda": "Seguire il comportamento della massa (herd behavior) riduce il rischio.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "L'effetto gregge porta spesso a comprare sui massimi e vendere sui minimi, aumentando le perdite invece di ridurle."
    }
]


def valuta_comportamento(risposte: dict) -> dict:
    """Valuta il profilo comportamentale dell'investitore"""
    
    punteggio = sum(risposte.values())
    
    if punteggio <= 6:
        profilo = "Alto rischio emotivo"
        descrizione = "Tendi a prendere decisioni guidate dalle emozioni. L'automazione è essenziale per te."
        raccomandazioni = [
            "Automatizza completamente investimenti e ribilanciamenti",
            "Riduci drasticamente il monitoraggio del portafoglio",
            "Scrivi regole precise e seguile meccanicamente",
            "Considera un consulente che faccia da filtro emotivo"
        ]
        colore = "🔴"
    elif punteggio <= 12:
        profilo = "Rischio emotivo moderato"
        descrizione = "Hai una buona consapevolezza ma sei ancora influenzabile dalle emozioni."
        raccomandazioni = [
            "Usa l'automazione per le decisioni principali",
            "Controlla il portafoglio non più di una volta al trimestre",
            "Mantieni un diario delle decisioni di investimento",
            "Stabilisci regole chiare per situazioni di stress"
        ]
        colore = "🟡"
    else:
        profilo = "Buona disciplina emotiva"
        descrizione = "Hai sviluppato una buona capacità di gestire le emozioni negli investimenti."
        raccomandazioni = [
            "Mantieni comunque automazione per coerenza",
            "Monitora periodicamente i tuoi bias residui",
            "Continua a seguire regole prestabilite",
            "Non sottovalutare mai il potere delle emozioni"
        ]
        colore = "🟢"
    
    return {
        "punteggio": punteggio,
        "profilo": profilo,
        "descrizione": descrizione,
        "raccomandazioni": raccomandazioni,
        "colore": colore
    }


def render_contenuto():
    """Renderizza il contenuto teorico"""
    
    st.markdown("""
    ## Perché la psicologia è centrale negli investimenti
    
    Molti investitori falliscono **non per mancanza di conoscenze tecniche**, 
    ma per **errori comportamentali ripetuti**.
    
    Le decisioni finanziarie vengono spesso prese sotto l'influenza di emozioni come:
    - Paura
    - Avidità
    - Eccesso di fiducia
    - Panico
    
    > Nel lungo periodo, il **comportamento** dell'investitore incide più della scelta degli strumenti.
    """)
    
    st.markdown("---")
    
    st.markdown("## Emozioni e mercati")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 📈 Fasi di Rialzo")
            st.markdown("""
            **Emozione dominante:** Euforia
            
            **Comportamenti tipici:**
            - Eccesso di ottimismo
            - Sottovalutazione del rischio
            - FOMO (Fear Of Missing Out)
            - Acquisti sui massimi
            
            **Risultato:** Comprare caro
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### 📉 Fasi di Ribasso")
            st.markdown("""
            **Emozione dominante:** Paura
            
            **Comportamenti tipici:**
            - Panico
            - Pessimismo eccessivo
            - Vendite impulsive
            - Abbandono del piano
            
            **Risultato:** Vendere a basso costo
            """)
    
    st.error("""
    ❌ **Il ciclo emotivo distruttivo:**
    
    Comprare alto (euforia) → Vendere basso (panico) → Ripetere
    
    Esattamente l'opposto di ciò che una strategia razionale suggerirebbe.
    """)
    
    st.markdown("---")
    
    st.markdown("## I principali bias comportamentali")
    
    # Avversione alle perdite
    with st.container(border=True):
        st.markdown("### 1️⃣ Avversione alle Perdite")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            Le perdite fanno psicologicamente **più male** dei guadagni equivalenti.
            
            **Effetti tipici:**
            - Mantenere investimenti in perdita troppo a lungo ("non voglio realizzare la perdita")
            - Vendere troppo presto quelli in guadagno ("blocco il profitto")
            - Paralisi decisionale
            
            **Risultato:** Portafoglio pieno di perdenti, pochi vincitori
            """)
        
        with col2:
            st.metric("Impatto psicologico", "2:1")
            st.caption("Una perdita di €100 pesa come un guadagno di €200")
    
    # Overconfidence
    with st.container(border=True):
        st.markdown("### 2️⃣ Overconfidence (Eccesso di Fiducia)")
        
        st.markdown("""
        Porta a **sovrastimare le proprie capacità** di previsione e controllo.
        
        **Conseguenze:**
        - Trading eccessivo ("so quando comprare e vendere")
        - Sottovalutazione del rischio
        - Performance inferiori alla media
        - Costi elevati
        
        **Verità scomoda:** La maggior parte degli investitori professionali non batte il mercato. 
        Perché un investitore individuale dovrebbe riuscirci?
        """)
    
    # Bias di conferma
    with st.container(border=True):
        st.markdown("### 3️⃣ Bias di Conferma")
        
        st.markdown("""
        Si tende a **cercare informazioni che confermano** le proprie idee e a **ignorare quelle contrarie**.
        
        **Effetti:**
        - Visione parziale della realtà
        - Mancata valutazione dei rischi
        - Decisioni basate su dati incompleti
        
        **Esempio:** Sei convinto che un'azione salirà? Leggerai solo notizie positive su di essa.
        """)
    
    # Herd behavior
    with st.container(border=True):
        st.markdown("### 4️⃣ Herd Behavior (Effetto Gregge)")
        
        st.markdown("""
        **Seguire ciò che fanno gli altri** dà una sensazione di sicurezza.
        
        Nei mercati porta a:
        - Bolle speculative ("tutti comprano, lo faccio anch'io")
        - Decisioni prese troppo tardi
        - Perdite collettive
        
        **Famosa citazione:** "Sii avido quando gli altri sono timorosi, e timoroso quando gli altri sono avidi" 
        *(Warren Buffett)*
        """)
    
    # Recency bias
    with st.container(border=True):
        st.markdown("### 5️⃣ Recency Bias")
        
        st.markdown("""
        Si dà troppo peso agli **eventi recenti** rispetto alla storia di lungo periodo.
        
        **Esempio:**
        - Mercato sale per 2 anni → "salirà sempre"
        - Mercato scende per 3 mesi → "non risalirà mai"
        
        **Realtà:** I mercati sono ciclici, il breve termine non predice il lungo termine.
        """)
    
    st.markdown("---")
    
    st.markdown("## Il ruolo delle notizie e dei media")
    
    st.warning("""
    ⚠️ **Le notizie finanziarie sono spesso:**
    - Focalizzate sul breve termine
    - Emotivamente cariche
    - Progettate per catturare attenzione (non per informare razionalmente)
    
    Consumare informazioni finanziarie in modo continuo può:
    - Aumentare l'ansia
    - Generare decisioni impulsive
    - Danneggiare i risultati di lungo periodo
    """)
    
    st.markdown("---")
    
    st.markdown("## Strategie pratiche per ridurre i bias")
    
    strategie = [
        ("✅ Definire regole scritte", "Scrivi il tuo piano prima, non durante la volatilità"),
        ("✅ Automatizzare investimenti e ribilanciamenti", "Elimina le decisioni emotive quotidiane"),
        ("✅ Ridurre la frequenza di controllo", "Non guardare il portafoglio ogni giorno"),
        ("✅ Concentrarsi sugli obiettivi, non sui movimenti", "Il tuo obiettivo è tra 20 anni, non domani"),
        ("✅ Accettare la volatilità come parte del processo", "Oscillazioni = normalità, non emergenza"),
        ("✅ Tenere un diario delle decisioni", "Rileggilo nei momenti di stress"),
        ("✅ Avere un consulente o mentore", "Un filtro esterno riduce l'emotività")
    ]
    
    for strategia, descrizione in strategie:
        with st.container(border=True):
            st.markdown(f"**{strategia}**")
            st.caption(descrizione)
    
    st.success("""
    ✅ **Principio fondamentale:**
    
    La **disciplina** batte l'intelligenza quando si investe.
    
    Non devi essere il più intelligente, devi essere il più disciplinato.
    """)
    
    st.markdown("---")
    
    st.markdown("## Esempio pratico")
    
    with st.container(border=True):
        st.markdown("### Due investitori affrontano un ribasso del 25%")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Investitore A - Emotivo**")
            st.markdown("""
            1. Vede il ribasso del 25%
            2. Va in panico
            3. Vende tutto "per limitare le perdite"
            4. Il mercato recupera
            5. Rientra quando i prezzi sono più alti
            
            **Risultato:** Perdita permanente
            """)
        
        with col2:
            st.markdown("**Investitore B - Disciplinato**")
            st.markdown("""
            1. Vede il ribasso del 25%
            2. Controlla il piano
            3. Continua il PAC (compra più a buon mercato)
            4. Il mercato recupera
            5. Beneficia del rimbalzo
            
            **Risultato:** Guadagno nel lungo periodo
            """)
        
        st.info("""
        💡 **La differenza?**
        
        Non l'intelligenza, non la conoscenza tecnica.
        
        La **disciplina** e il **processo** prestabilito.
        """)


def render_calcolatore():
    """Renderizza i calcolatori"""
    
    st.markdown("## 🧮 Test e Strumenti")
    
    calc_type = st.radio(
        "Seleziona:",
        ["Test Profilo Comportamentale", "Diario Decisioni"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if calc_type == "Test Profilo Comportamentale":
        render_test_comportamentale()
    else:
        render_diario()


def render_test_comportamentale():
    """Test per valutare il profilo comportamentale"""
    
    st.markdown("### Test: Valuta il Tuo Profilo Comportamentale")
    
    st.markdown("""
    Rispondi onestamente a queste domande per identificare le tue tendenze emotive negli investimenti.
    """)
    
    risposte = {}
    
    domande = [
        {
            "id": 1,
            "testo": "Il tuo portafoglio perde il 20% in un mese. Cosa fai?",
            "opzioni": {
                "Vendo tutto immediatamente": 1,
                "Vendo metà per sicurezza": 2,
                "Mantengo e basta": 3,
                "Mantengo e valuto se comprare di più": 4
            }
        },
        {
            "id": 2,
            "testo": "Con quale frequenza controlli il valore del tuo portafoglio?",
            "opzioni": {
                "Più volte al giorno": 1,
                "Una volta al giorno": 2,
                "Una volta a settimana": 3,
                "Una volta al mese o meno": 4
            }
        },
        {
            "id": 3,
            "testo": "Un amico ti racconta di aver guadagnato il 50% con un investimento. Tu:",
            "opzioni": {
                "Investi subito nello stesso modo": 1,
                "Ti informi velocemente e investi": 2,
                "Fai ricerca approfondita prima": 3,
                "Ignori e continui il tuo piano": 4
            }
        },
        {
            "id": 4,
            "testo": "Durante un forte ribasso dei mercati, tu:",
            "opzioni": {
                "Non dormi la notte e pensi di vendere": 1,
                "Sei preoccupato ma resisti": 2,
                "Sei calmo, è parte del processo": 3,
                "Sei contento, compri a sconto": 4
            }
        },
        {
            "id": 5,
            "testo": "Hai venduto un'azione e subito dopo il prezzo sale del 30%. Tu:",
            "opzioni": {
                "Ti penti molto e cambi strategia": 1,
                "Sei un po' dispiaciuto": 2,
                "Accetti che è normale": 3,
                "Non ti interessa, seguivi il piano": 4
            }
        }
    ]
    
    for domanda in domande:
        with st.container(border=True):
            st.markdown(f"**Domanda {domanda['id']}:** {domanda['testo']}")
            
            risposta = st.radio(
                "Seleziona:",
                list(domanda['opzioni'].keys()),
                key=f"cap15_comportamento_{domanda['id']}"
            )
            
            risposte[domanda['id']] = domanda['opzioni'][risposta]
    
    if st.button("📊 Valuta Profilo", type="primary", use_container_width=True):
        risultato = valuta_comportamento(risposte)
        
        st.markdown("---")
        st.markdown("### 🎯 Il Tuo Profilo")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.metric("Punteggio", risultato['punteggio'])
            st.markdown(f"## {risultato['colore']} {risultato['profilo']}")
        
        with col2:
            st.markdown(f"**{risultato['descrizione']}**")
            
            st.markdown("#### 💡 Raccomandazioni")
            for racc in risultato['raccomandazioni']:
                st.markdown(f"- {racc}")
        
        if risultato['punteggio'] <= 6:
            st.error("""
            ⚠️ **Attenzione:** Sei molto vulnerabile alle emozioni negli investimenti.
            
            L'automazione e le regole rigide sono **essenziali** per te. Senza, rischi di 
            danneggiare seriamente i tuoi risultati.
            """)
        elif risultato['punteggio'] <= 12:
            st.warning("""
            📊 **Buon punto di partenza:** Hai consapevolezza ma margini di miglioramento.
            
            Continua a lavorare sulla disciplina e usa l'automazione come supporto.
            """)
        else:
            st.success("""
            ✅ **Ottimo controllo emotivo:** Hai sviluppato buona disciplina.
            
            Mantieni la guardia alta: le emozioni possono sempre sorprenderti nei momenti estremi.
            """)


def render_diario():
    """Template per diario delle decisioni"""
    
    st.markdown("### 📔 Diario delle Decisioni di Investimento")
    
    st.markdown("""
    Tenere un diario delle decisioni ti aiuta a:
    - Identificare pattern comportamentali
    - Riflettere prima di agire
    - Imparare dagli errori
    - Mantenere coerenza nel tempo
    """)
    
    st.markdown("---")
    
    with st.expander("📝 Template Decisione", expanded=True):
        data = st.date_input("Data decisione")
        
        tipo_decisione = st.selectbox(
            "Tipo di decisione",
            ["Acquisto", "Vendita", "Ribilanciamento", "Modifica piano", "Altro"]
        )
        
        descrizione = st.text_area(
            "Descrizione della decisione",
            placeholder="Es: Ho venduto il 50% delle azioni perché..."
        )
        
        stato_emotivo = st.select_slider(
            "Il mio stato emotivo",
            options=["Panico", "Paura", "Preoccupazione", "Neutrale", "Fiducioso", "Euforico"]
        )
        
        motivazione = st.text_area(
            "Motivazione razionale",
            placeholder="Perché questa decisione è coerente con il mio piano?"
        )
        
        coerenza_piano = st.radio(
            "Questa decisione è coerente con il mio piano?",
            ["Sì", "No", "Non sono sicuro"],
            horizontal=True
        )
        
        if st.button("💾 Salva nel diario"):
            st.success("✅ Decisione registrata!")
            
            st.info("""
            💡 **Suggerimento:**
            
            Rileggi questo diario tra 3-6 mesi. Ti aiuterà a capire quali decisioni 
            erano razionali e quali emotive.
            """)
    
    st.markdown("---")
    
    with st.expander("🔍 Domande di riflessione (da compilare periodicamente)"):
        st.markdown("""
        **Ogni 3 mesi, rispondi:**
        
        1. Quante decisioni ho preso guidato dalle emozioni?
        2. Quante volte ho deviato dal piano originale?
        3. Le mie decisioni emotive hanno migliorato o peggiorato i risultati?
        4. Cosa posso automatizzare per ridurre l'intervento emotivo?
        5. Quali trigger emotivi devo riconoscere e gestire meglio?
        
        ---
        
        **Analisi annuale:**
        
        1. Confronta i risultati con il piano originale
        2. Identifica le decisioni che hanno funzionato
        3. Identifica gli errori ripetuti
        4. Aggiorna le regole per l'anno prossimo
        """)


def render_quiz():
    """Renderizza il quiz di verifica"""
    
    st.markdown("## 📝 Quiz di verifica")
    
    if "cap15_risposte" not in st.session_state:
        st.session_state.cap15_risposte = {}
    if "cap15_verificato" not in st.session_state:
        st.session_state.cap15_verificato = False
    
    for i, q in enumerate(QUIZ):
        with st.container(border=True):
            st.markdown(f"**Domanda {i+1}:** {q['domanda']}")
            
            if q["tipo"] == "vero_falso":
                risposta = st.radio(
                    "Seleziona:",
                    ["Vero", "Falso"],
                    key=f"cap15_q{q['id']}",
                    horizontal=True
                )
                st.session_state.cap15_risposte[q['id']] = risposta == "Vero"
                
            elif q["tipo"] == "scelta_multipla":
                risposta = st.radio(
                    "Seleziona:",
                    q["opzioni"],
                    key=f"cap15_q{q['id']}"
                )
                st.session_state.cap15_risposte[q['id']] = risposta
            
            if st.session_state.cap15_verificato:
                user_ans = st.session_state.cap15_risposte.get(q['id'])
                corretto = user_ans == q["risposta_corretta"]
                
                if corretto:
                    st.success(f"✅ Corretto! {q['spiegazione']}")
                else:
                    st.error(f"❌ Sbagliato. Risposta corretta: {q['risposta_corretta']}")
                    st.info(q['spiegazione'])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Verifica risposte", type="primary", use_container_width=True, key="cap15_verifica"):
            st.session_state.cap15_verificato = True
            st.rerun()
    with col2:
        if st.button("🔄 Ricomincia", use_container_width=True, key="cap15_reset"):
            st.session_state.cap15_verificato = False
            st.session_state.cap15_risposte = {}
            st.rerun()


def render_takeaways():
    """Renderizza i punti chiave"""
    
    st.markdown("## 💡 Punti chiave")
    
    takeaways = [
        "Il comportamento dell'investitore incide più della scelta degli strumenti",
        "Le emozioni (paura, avidità) portano a comprare alto e vendere basso",
        "L'avversione alle perdite ci porta a tenere i perdenti e vendere i vincitori",
        "L'overconfidence genera trading eccessivo e sottovalutazione del rischio",
        "Il bias di conferma riduce la capacità di valutazione obiettiva",
        "L'effetto gregge porta a decisioni collettive dannose",
        "L'automazione e le regole scritte riducono l'intervento emotivo",
        "La disciplina batte l'intelligenza negli investimenti di lungo periodo"
    ]
    
    for t in takeaways:
        st.markdown(f"- {t}")
    
    st.markdown("---")
    
    with st.expander("📝 Esercizio: Crea le tue regole comportamentali"):
        st.markdown("""
        **Definisci le tue regole per resistere alle emozioni:**
        
        ### 🔴 In caso di forte ribasso (>20%)
        
        **Mi impegno a:**
        1. _____________________________________________
        2. _____________________________________________
        3. _____________________________________________
        
        **NON farò:**
        1. _____________________________________________
        2. _____________________________________________
        
        ---
        
        ### 🟢 In caso di forte rialzo (>30%)
        
        **Mi impegno a:**
        1. _____________________________________________
        2. _____________________________________________
        3. _____________________________________________
        
        **NON farò:**
        1. _____________________________________________
        2. _____________________________________________
        
        ---
        
        ### 📊 Regole generali
        
        - Controllerò il portafoglio: ☐ Mensile ☐ Trimestrale ☐ Semestrale
        - Ribilancerò: ☐ Annuale ☐ Per soglia (___%)
        - In caso di dubbio: ☐ Non fare nulla ☐ Consultare ________
        - Non modificherò il piano se: _____________
        - Modificherò il piano solo se: _____________
        
        ---
        
        ### ✍️ Commitment
        
        "Riconosco che le emozioni sono il nemico principale dei miei risultati finanziari.
        Mi impegno a seguire queste regole anche quando sarà difficile,
        specialmente nei momenti di massima volatilità emotiva."
        
        Firma: _____________ Data: _____________
        
        ---
        
        💡 **Conserva queste regole e rileggile nei momenti di stress del mercato.**
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
        "🧮 Test", 
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
