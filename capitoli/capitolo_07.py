"""
Capitolo 7: Credito e punteggio creditizio
InvestAccademy - Corso di Finanza Personale
"""

import streamlit as st
import pandas as pd

# Metadata
CAPITOLO_NUM = 7
TITOLO = "Credito e punteggio creditizio"

OBIETTIVI = [
    "Comprendere cos'è il punteggio creditizio e perché è importante",
    "Conoscere i principali fattori che lo determinano",
    "Calcolare e interpretare l'utilizzo del credito",
    "Applicare azioni concrete per migliorare il profilo creditizio",
    "Evitare errori comuni che peggiorano il punteggio nel tempo"
]

# Quiz
QUIZ = [
    {
        "id": 1,
        "domanda": "Il punteggio creditizio influisce sul tasso di interesse che paghi per un prestito.",
        "tipo": "vero_falso",
        "risposta_corretta": True,
        "spiegazione": "Un buon punteggio creditizio permette di ottenere tassi di interesse più bassi, risparmiando denaro nel tempo."
    },
    {
        "id": 2,
        "domanda": "Qual è il fattore più importante per il punteggio creditizio?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Storico dei pagamenti",
            "Numero di carte di credito",
            "Reddito annuo",
            "Età"
        ],
        "risposta_corretta": "Storico dei pagamenti",
        "spiegazione": "Pagare in tempo è il fattore più importante. Ritardi nei pagamenti danneggiano significativamente il punteggio."
    },
    {
        "id": 3,
        "domanda": "Quale percentuale di utilizzo del credito è considerata ottimale?",
        "tipo": "scelta_multipla",
        "opzioni": ["Sotto il 10%", "Sotto il 30%", "Sotto il 60%", "Sotto il 90%"],
        "risposta_corretta": "Sotto il 30%",
        "spiegazione": "Mantenere l'utilizzo del credito sotto il 30% è considerato positivo per il punteggio creditizio."
    },
    {
        "id": 4,
        "domanda": "Se hai una carta con limite €5.000 e saldo medio €3.000, qual è il tuo utilizzo del credito?",
        "tipo": "numero",
        "risposta_corretta": 60,
        "spiegazione": "3.000 / 5.000 = 0,60 = 60%"
    },
    {
        "id": 5,
        "domanda": "Chiudere una carta di credito migliora sempre il punteggio creditizio.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "Falso. Chiudere una carta può ridurre il limite totale, aumentare l'utilizzo percentuale e accorciare la storia creditizia."
    }
]


def calcola_utilizzo_credito(saldo: float, limite: float) -> float:
    """Calcola la percentuale di utilizzo del credito"""
    if limite <= 0:
        return 0
    return (saldo / limite) * 100


def valuta_utilizzo(utilizzo: float) -> dict:
    """Valuta il livello di utilizzo del credito"""
    if utilizzo < 30:
        return {
            "livello": "Ottimale",
            "colore": "🟢",
            "descrizione": "Eccellente! Stai usando meno del 30% del credito disponibile.",
            "impatto": "Positivo sul punteggio creditizio"
        }
    elif utilizzo < 50:
        return {
            "livello": "Attenzione",
            "colore": "🟡",
            "descrizione": "Utilizzo moderato. Considera di ridurre il saldo.",
            "impatto": "Impatto neutro o lievemente negativo"
        }
    elif utilizzo < 70:
        return {
            "livello": "Alto",
            "colore": "🟠",
            "descrizione": "Utilizzo elevato. Riduci il saldo quando possibile.",
            "impatto": "Impatto negativo sul punteggio"
        }
    else:
        return {
            "livello": "Critico",
            "colore": "🔴",
            "descrizione": "Utilizzo molto elevato. Priorità: ridurre i saldi.",
            "impatto": "Forte impatto negativo sul punteggio"
        }


def simula_riduzione_saldo(saldo_attuale: float, limite: float, riduzione: float) -> dict:
    """Simula l'effetto della riduzione del saldo"""
    nuovo_saldo = max(0, saldo_attuale - riduzione)
    utilizzo_attuale = calcola_utilizzo_credito(saldo_attuale, limite)
    utilizzo_nuovo = calcola_utilizzo_credito(nuovo_saldo, limite)
    
    return {
        "saldo_attuale": saldo_attuale,
        "saldo_nuovo": nuovo_saldo,
        "utilizzo_attuale": utilizzo_attuale,
        "utilizzo_nuovo": utilizzo_nuovo,
        "miglioramento": utilizzo_attuale - utilizzo_nuovo
    }


def render_contenuto():
    """Renderizza il contenuto teorico"""
    
    st.markdown("""
    ## Perché il punteggio creditizio conta
    
    Il punteggio creditizio misura la probabilità che una persona rimborsi correttamente i propri debiti. 
    Banche e intermediari lo utilizzano per decidere:
    
    - Se concedere credito
    - A quali condizioni
    - A quale tasso di interesse
    
    > Un buon punteggio non serve solo a ottenere prestiti, ma a **pagare meno per il credito** 
    > nel corso della vita finanziaria.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## I principali fattori del punteggio creditizio
    
    Sebbene i modelli varino da paese a paese, i fattori chiave sono simili:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 1️⃣ Storico dei pagamenti")
            st.markdown("""
            **Il fattore più importante.**
            
            - Pagare sempre in tempo
            - Ritardi > 30 giorni danneggiano molto
            - L'impatto diminuisce col tempo
            """)
        
        with st.container(border=True):
            st.markdown("### 2️⃣ Utilizzo del credito")
            st.markdown("""
            Percentuale di credito utilizzato rispetto al limite disponibile.
            
            **Regola pratica:**
            - < 30%: Positivo
            - 30-50%: Attenzione
            - > 50%: Rischio penalizzazione
            """)
        
        with st.container(border=True):
            st.markdown("### 3️⃣ Durata della storia creditizia")
            st.markdown("""
            Rapporti più lunghi e stabili sono generalmente premiati.
            
            Per questo chiudere vecchie carte può essere controproducente.
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### 4️⃣ Tipologia di credito")
            st.markdown("""
            Mix equilibrato tra:
            - Carte di credito
            - Prestiti personali
            - Mutui
            
            Diversità moderata è vista positivamente.
            """)
        
        with st.container(border=True):
            st.markdown("### 5️⃣ Nuove richieste di credito")
            st.markdown("""
            Troppe richieste ravvicinate possono essere penalizzanti.
            
            **Suggerimento:** evita richieste multiple in breve tempo.
            """)
    
    st.markdown("---")
    
    st.markdown("""
    ## L'utilizzo del credito: un fattore chiave
    
    L'utilizzo del credito è uno degli indicatori più rilevanti e controllabili.
    """)
    
    st.latex(r"\text{Utilizzo} = \frac{\text{Saldo utilizzato}}{\text{Limite totale}} \times 100")
    
    st.markdown("""
    ### Esempio pratico
    
    Hai una carta di credito con:
    - Limite: €5.000
    - Saldo medio: €3.000
    
    **Utilizzo:** 3.000 / 5.000 = 60%
    
    Riducendo il saldo a €1.000:
    - **Nuovo utilizzo:** 1.000 / 5.000 = 20%
    
    Il profilo creditizio migliora senza aprire nuovi conti.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Come migliorare il punteggio creditizio
    
    Azioni concrete ed efficaci:
    """)
    
    azioni = [
        ("✅ Paga sempre in tempo", "L'azione singola più importante"),
        ("✅ Mantieni basso l'utilizzo delle carte", "Idealmente sotto il 30%"),
        ("✅ Evita aperture e chiusure frequenti", "Stabilità è premiata"),
        ("✅ Controlla periodicamente il report", "Verifica errori o anomalie"),
        ("✅ Correggi eventuali errori segnalati", "Puoi contestare informazioni errate"),
        ("✅ Non richiedere troppo credito insieme", "Dilaziona le richieste nel tempo")
    ]
    
    for azione, descrizione in azioni:
        with st.container(border=True):
            st.markdown(f"**{azione}**")
            st.caption(descrizione)
    
    st.info("💡 Il miglioramento è graduale: la costanza conta più degli interventi drastici.")
    
    st.markdown("---")
    
    st.markdown("""
    ## Chiusura delle carte: attenzione agli effetti collaterali
    
    Chiudere una carta con saldo zero **non è sempre una buona idea**.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ⚠️ Possibili effetti negativi:")
        st.markdown("""
        - Riduzione del limite totale disponibile
        - Aumento dell'utilizzo percentuale
        - Accorciamento della storia creditizia
        - Riduzione del mix di credito
        """)
    
    with col2:
        st.markdown("### ✅ Quando ha senso chiudere:")
        st.markdown("""
        - Canone annuo elevato non giustificato
        - Difficoltà nel controllo della spesa
        - Carte duplicate senza valore aggiunto
        - Dopo aver aperto alternative migliori
        """)
    
    st.warning("Prima di chiudere una linea di credito, valuta l'impatto complessivo sul tuo profilo.")


def render_calcolatore():
    """Renderizza i calcolatori"""
    
    st.markdown("## 🧮 Calcolatori")
    
    calc_type = st.radio(
        "Seleziona calcolatore:",
        ["Utilizzo del credito", "Simulatore riduzione saldo", "Analisi multi-carta"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if calc_type == "Utilizzo del credito":
        render_calc_utilizzo()
    elif calc_type == "Simulatore riduzione saldo":
        render_calc_simulatore()
    else:
        render_calc_multicarta()


def render_calc_utilizzo():
    """Calcolatore utilizzo del credito"""
    
    st.markdown("### Calcola il Tuo Utilizzo del Credito")
    
    col1, col2 = st.columns(2)
    
    with col1:
        saldo = st.number_input(
            "💳 Saldo utilizzato (€)",
            min_value=0.0,
            value=2000.0,
            step=100.0,
            key="cap7_saldo"
        )
        
        limite = st.number_input(
            "📊 Limite totale (€)",
            min_value=100.0,
            value=5000.0,
            step=100.0,
            key="cap7_limite"
        )
    
    with col2:
        utilizzo = calcola_utilizzo_credito(saldo, limite)
        valutazione = valuta_utilizzo(utilizzo)
        
        st.markdown("### Risultato")
        
        st.metric(
            "Utilizzo del credito",
            f"{utilizzo:.1f}%",
            f"{valutazione['livello']}"
        )
        
        st.markdown(f"{valutazione['colore']} **{valutazione['descrizione']}**")
        st.caption(f"**Impatto:** {valutazione['impatto']}")
        
        # Progress bar visuale
        st.progress(min(utilizzo / 100, 1.0))
        
        # Soglie visuali
        st.markdown("#### Soglie di riferimento")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.caption("🟢 < 30% Ottimale")
        with col_b:
            st.caption("🟡 30-50% Attenzione")
        with col_c:
            st.caption("🔴 > 50% Alto rischio")
    
    st.markdown("---")
    
    # Suggerimenti personalizzati
    if utilizzo < 30:
        st.success("✅ Continua così! Il tuo utilizzo è nella fascia ottimale.")
    elif utilizzo < 50:
        riduzione_target = saldo - (limite * 0.30)
        st.warning(f"⚠️ Per raggiungere il 30%, dovresti ridurre il saldo di €{riduzione_target:.2f}")
    else:
        riduzione_target = saldo - (limite * 0.30)
        st.error(f"🔴 Priorità: ridurre il saldo di almeno €{riduzione_target:.2f} per scendere sotto il 30%")


def render_calc_simulatore():
    """Simulatore riduzione saldo"""
    
    st.markdown("### Simula l'Effetto della Riduzione del Saldo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        saldo_attuale = st.number_input(
            "💳 Saldo attuale (€)",
            min_value=0.0,
            value=3000.0,
            step=100.0,
            key="cap7_sim_saldo"
        )
        
        limite = st.number_input(
            "📊 Limite carta (€)",
            min_value=100.0,
            value=5000.0,
            step=100.0,
            key="cap7_sim_limite"
        )
        
        riduzione = st.slider(
            "💰 Quanto potresti ridurre il saldo? (€)",
            min_value=0.0,
            max_value=float(saldo_attuale),
            value=min(1000.0, saldo_attuale),
            step=100.0,
            key="cap7_sim_riduzione"
        )
    
    with col2:
        simulazione = simula_riduzione_saldo(saldo_attuale, limite, riduzione)
        
        st.markdown("### Confronto")
        
        col_prima, col_dopo = st.columns(2)
        
        with col_prima:
            st.markdown("#### 📍 Prima")
            st.metric("Saldo", f"€{simulazione['saldo_attuale']:,.2f}")
            st.metric("Utilizzo", f"{simulazione['utilizzo_attuale']:.1f}%")
        
        with col_dopo:
            st.markdown("#### ✨ Dopo")
            st.metric("Saldo", f"€{simulazione['saldo_nuovo']:,.2f}")
            st.metric(
                "Utilizzo", 
                f"{simulazione['utilizzo_nuovo']:.1f}%",
                delta=f"-{simulazione['miglioramento']:.1f}%"
            )
        
        # Valutazioni
        val_prima = valuta_utilizzo(simulazione['utilizzo_attuale'])
        val_dopo = valuta_utilizzo(simulazione['utilizzo_nuovo'])
        
        st.markdown("---")
        st.markdown("#### 📊 Impatto sul profilo creditizio")
        
        st.markdown(f"**Prima:** {val_prima['colore']} {val_prima['livello']}")
        st.markdown(f"**Dopo:** {val_dopo['colore']} {val_dopo['livello']}")
        
        if simulazione['miglioramento'] > 10:
            st.success(f"✅ Miglioramento significativo: -{simulazione['miglioramento']:.1f}%")
        elif simulazione['miglioramento'] > 0:
            st.info(f"📊 Miglioramento moderato: -{simulazione['miglioramento']:.1f}%")


def render_calc_multicarta():
    """Analizzatore utilizzo multi-carta"""
    
    st.markdown("### Analisi Utilizzo Multi-Carta")
    
    st.markdown("""
    Calcola l'utilizzo complessivo considerando tutte le tue carte di credito.
    """)
    
    # Inizializza session state per le carte
    if "cap7_carte" not in st.session_state:
        st.session_state.cap7_carte = [
            {"nome": "Carta 1", "saldo": 1500, "limite": 3000},
            {"nome": "Carta 2", "saldo": 800, "limite": 2000}
        ]
    
    st.markdown("#### 💳 Le tue carte")
    
    for i, carta in enumerate(st.session_state.cap7_carte):
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
        
        with col1:
            carta['nome'] = st.text_input(
                f"Nome carta {i+1}", 
                value=carta['nome'], 
                key=f"cap7_mc_nome_{i}"
            )
        with col2:
            carta['saldo'] = st.number_input(
                f"Saldo", 
                value=float(carta['saldo']), 
                min_value=0.0, 
                step=100.0, 
                key=f"cap7_mc_saldo_{i}"
            )
        with col3:
            carta['limite'] = st.number_input(
                f"Limite", 
                value=float(carta['limite']), 
                min_value=100.0, 
                step=100.0, 
                key=f"cap7_mc_limite_{i}"
            )
        with col4:
            utilizzo_carta = calcola_utilizzo_credito(carta['saldo'], carta['limite'])
            val = valuta_utilizzo(utilizzo_carta)
            st.caption(f"{val['colore']} {utilizzo_carta:.1f}%")
    
    st.markdown("---")
    
    # Calcoli aggregati
    saldo_totale = sum(c['saldo'] for c in st.session_state.cap7_carte)
    limite_totale = sum(c['limite'] for c in st.session_state.cap7_carte)
    utilizzo_totale = calcola_utilizzo_credito(saldo_totale, limite_totale)
    valutazione_totale = valuta_utilizzo(utilizzo_totale)
    
    st.markdown("### 📊 Analisi Complessiva")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Saldo totale", f"€{saldo_totale:,.2f}")
    with col2:
        st.metric("Limite totale", f"€{limite_totale:,.2f}")
    with col3:
        st.metric(
            "Utilizzo complessivo", 
            f"{utilizzo_totale:.1f}%",
            valutazione_totale['livello']
        )
    
    st.markdown(f"**Valutazione:** {valutazione_totale['colore']} {valutazione_totale['descrizione']}")
    
    # Grafico distribuzione
    st.markdown("#### 📈 Distribuzione per carta")
    
    df_carte = pd.DataFrame({
        "Carta": [c['nome'] for c in st.session_state.cap7_carte],
        "Utilizzo %": [calcola_utilizzo_credito(c['saldo'], c['limite']) for c in st.session_state.cap7_carte],
        "Saldo": [c['saldo'] for c in st.session_state.cap7_carte]
    })
    
    st.dataframe(df_carte, use_container_width=True, hide_index=True)
    
    # Suggerimento strategico
    if utilizzo_totale > 50:
        carta_prioritaria = max(st.session_state.cap7_carte, key=lambda x: calcola_utilizzo_credito(x['saldo'], x['limite']))
        st.warning(f"💡 Suggerimento: concentrati prima sulla riduzione di '{carta_prioritaria['nome']}'")


def render_quiz():
    """Renderizza il quiz di verifica"""
    
    st.markdown("## 📝 Quiz di verifica")
    
    if "cap7_risposte" not in st.session_state:
        st.session_state.cap7_risposte = {}
    if "cap7_verificato" not in st.session_state:
        st.session_state.cap7_verificato = False
    
    for i, q in enumerate(QUIZ):
        with st.container(border=True):
            st.markdown(f"**Domanda {i+1}:** {q['domanda']}")
            
            if q["tipo"] == "vero_falso":
                risposta = st.radio(
                    "Seleziona:",
                    ["Vero", "Falso"],
                    key=f"cap7_q{q['id']}",
                    horizontal=True
                )
                st.session_state.cap7_risposte[q['id']] = risposta == "Vero"
                
            elif q["tipo"] == "scelta_multipla":
                risposta = st.radio(
                    "Seleziona:",
                    q["opzioni"],
                    key=f"cap7_q{q['id']}"
                )
                st.session_state.cap7_risposte[q['id']] = risposta
                
            elif q["tipo"] == "numero":
                risposta = st.number_input(
                    "Inserisci il valore:",
                    key=f"cap7_q{q['id']}",
                    step=1.0
                )
                st.session_state.cap7_risposte[q['id']] = risposta
            
            if st.session_state.cap7_verificato:
                user_ans = st.session_state.cap7_risposte.get(q['id'])
                if q["tipo"] == "numero":
                    corretto = abs(user_ans - q["risposta_corretta"]) < 5
                else:
                    corretto = user_ans == q["risposta_corretta"]
                
                if corretto:
                    st.success(f"✅ Corretto! {q['spiegazione']}")
                else:
                    st.error(f"❌ Sbagliato. Risposta corretta: {q['risposta_corretta']}")
                    st.info(q['spiegazione'])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Verifica risposte", type="primary", use_container_width=True, key="cap7_verifica"):
            st.session_state.cap7_verificato = True
            st.rerun()
    with col2:
        if st.button("🔄 Ricomincia", use_container_width=True, key="cap7_reset"):
            st.session_state.cap7_verificato = False
            st.session_state.cap7_risposte = {}
            st.rerun()


def render_takeaways():
    """Renderizza i punti chiave"""
    
    st.markdown("## 💡 Punti chiave")
    
    takeaways = [
        "Il punteggio creditizio influisce direttamente sui tassi di interesse che paghi",
        "Lo storico dei pagamenti è il fattore più importante: paga sempre in tempo",
        "Mantieni l'utilizzo del credito sotto il 30% per un profilo ottimale",
        "Chiudere carte può essere controproducente: valuta sempre l'impatto complessivo",
        "Il miglioramento del punteggio è graduale: la costanza è fondamentale",
        "Controlla periodicamente il tuo report di credito per individuare errori"
    ]
    
    for t in takeaways:
        st.markdown(f"- {t}")
    
    st.markdown("---")
    
    # Esercizio pratico
    with st.expander("📝 Piano d'azione: Migliora il tuo punteggio"):
        st.markdown("""
        **Compila questo piano di miglioramento:**
        
        1. **Pagamenti**
           - Configuro promemoria automatici: ☐
           - Attivo addebito diretto dove possibile: ☐
        
        2. **Utilizzo del credito**
           - Utilizzo attuale: _____%
           - Obiettivo: _____% (sotto il 30%)
           - Azione: ridurre saldo di €_____ al mese
        
        3. **Storia creditizia**
           - Carte più vecchie che mantengo: _____________
           - Carte da valutare per chiusura: _____________
        
        4. **Monitoraggio**
           - Controllo report di credito ogni _____ mesi
           - Verifico utilizzo carte ogni _____ mese/i
        
        ---
        
        💡 *Rivedi questo piano tra 3 mesi e misura i progressi.*
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
