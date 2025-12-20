"""
Capitolo 5: Scelta del conto e struttura dei conti personali
InvestAccademy - Corso di Finanza Personale
"""

import streamlit as st
import pandas as pd

# Metadata
CAPITOLO_NUM = 5
TITOLO = "Scelta del conto e struttura dei conti personali"

OBIETTIVI = [
    "Definire criteri pratici per scegliere un conto bancario",
    "Progettare una struttura di conti personale coerente con i tuoi obiettivi",
    "Separare correttamente liquidità, risparmi e investimenti",
    "Ridurre errori comportamentali attraverso una migliore organizzazione dei conti",
    "Valutare sicurezza e costi operativi in modo sistematico"
]

# Quiz
QUIZ = [
    {
        "id": 1,
        "domanda": "Perché è utile separare il fondo emergenze dal conto operativo?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Per ottenere rendimenti più alti",
            "Per evitare di spendere i risparmi e controllare meglio la liquidità",
            "Per pagare meno tasse",
            "Non è necessario separarli"
        ],
        "risposta_corretta": "Per evitare di spendere i risparmi e controllare meglio la liquidità",
        "spiegazione": "La separazione fisica dei conti riduce il rischio di spendere risorse destinate ad altri obiettivi."
    },
    {
        "id": 2,
        "domanda": "Qual è il principale vantaggio di una struttura multi-conto?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Complicare la gestione finanziaria",
            "Separare il denaro in base alla funzione e ridurre errori comportamentali",
            "Ottenere più carte di credito",
            "Aumentare i costi bancari"
        ],
        "risposta_corretta": "Separare il denaro in base alla funzione e ridurre errori comportamentali",
        "spiegazione": "Una struttura multi-conto funziona come un sistema di contenitori: ogni euro ha uno scopo preciso."
    },
    {
        "id": 3,
        "domanda": "Il conto operativo dovrebbe contenere:",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Tutti i tuoi risparmi",
            "Il fondo emergenze",
            "Solo il saldo minimo necessario per coprire le spese del mese",
            "Gli investimenti"
        ],
        "risposta_corretta": "Solo il saldo minimo necessario per coprire le spese del mese",
        "spiegazione": "Il conto operativo serve per le spese quotidiane, non per accumulare denaro."
    },
    {
        "id": 4,
        "domanda": "Un conto perfetto esiste ed è uguale per tutti.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "Non esiste un conto perfetto universale: esiste quello più adatto al tuo utilizzo reale."
    },
    {
        "id": 5,
        "domanda": "L'automazione dei trasferimenti tra conti aiuta a mantenere la disciplina finanziaria.",
        "tipo": "vero_falso",
        "risposta_corretta": True,
        "spiegazione": "Automatizzare i trasferimenti riduce l'attrito decisionale e rende il risparmio una conseguenza automatica."
    }
]


def calcola_costi_annui(canone_mensile: float, commissioni_bonifici: float, num_bonifici: int, 
                         costo_prelievi: float, num_prelievi: int) -> dict:
    """Calcola i costi totali annui di un conto"""
    
    costo_canone = canone_mensile * 12
    costo_bonifici_tot = commissioni_bonifici * num_bonifici
    costo_prelievi_tot = costo_prelievi * num_prelievi
    
    totale = costo_canone + costo_bonifici_tot + costo_prelievi_tot
    
    return {
        "canone": costo_canone,
        "bonifici": costo_bonifici_tot,
        "prelievi": costo_prelievi_tot,
        "totale": totale
    }


def render_contenuto():
    """Renderizza il contenuto teorico"""
    
    st.markdown("""
    ## Perché la struttura dei conti è importante
    
    Molte difficoltà finanziarie non derivano da mancanza di reddito, ma da **confusione operativa**. 
    Tenere tutto su un unico conto rende più facile spendere risorse destinate ad altri obiettivi 
    e più difficile misurare i progressi.
    
    > Una struttura di conti ben progettata funziona come un **sistema di contenitori**: 
    > ogni euro ha uno scopo preciso.
    
    Questo riduce gli errori, migliora l'autocontrollo e rende automatiche molte decisioni finanziarie.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Criteri pratici per scegliere un conto
    
    Quando valuti un conto bancario, considera sempre l'**insieme dei fattori**, non un singolo elemento.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 📋 Criteri principali")
            st.markdown("""
            - **Canoni e commissioni**: costo annuo totale
            - **Operatività**: bonifici, carte, prelievi
            - **Servizi digitali**: app, notifiche, gestione online
            - **Limiti e vincoli**: prelievi gratuiti, soglie, tempi
            - **Remunerazione**: tassi realistici, non promozionali
            - **Sicurezza**: garanzia depositi, autenticazione forte
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### 💡 Regola d'oro")
            st.markdown("""
            Un conto perfetto non esiste.
            
            Esiste quello **più adatto al tuo utilizzo reale**.
            
            Non farti abbagliare da un singolo vantaggio 
            (es. canone zero) se poi paghi molto per 
            operazioni che usi frequentemente.
            """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Il concetto di struttura multi-conto
    
    Una struttura multi-conto separa il denaro **in base alla funzione**, non alla provenienza.
    """)
    
    st.markdown("""
    ### Le quattro funzioni principali:
    
    1. **Spese quotidiane** - il flusso operativo
    2. **Risparmi di sicurezza** - il fondo emergenze
    3. **Obiettivi a breve e medio termine** - vacanze, acquisti pianificati
    4. **Investimenti** - il capitale destinato ai mercati
    
    Separare queste funzioni riduce il rischio di usare risparmi o investimenti per spese impulsive.
    """)
    
    st.markdown("---")
    
    st.markdown("## I quattro conti fondamentali")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 1️⃣ Conto Operativo")
            st.markdown("""
            È il conto della **vita quotidiana**.
            
            **Funzioni:**
            - Accredito del reddito
            - Pagamento spese correnti
            - Domiciliazioni e carte
            
            **Regola:** mantieni solo il saldo minimo 
            necessario per coprire le spese del mese.
            """)
        
        with st.container(border=True):
            st.markdown("### 2️⃣ Conto Risparmi / Fondo Emergenze")
            st.markdown("""
            È il conto della **sicurezza**.
            
            **Funzioni:**
            - Fondo emergenze
            - Risparmi a breve termine
            
            **Caratteristiche:**
            - Basso rischio
            - Facile accesso
            - Separato dal conto operativo
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### 3️⃣ Conto Obiettivi")
            st.markdown("""
            Serve per **obiettivi specifici**.
            
            **Esempi:**
            - Vacanze
            - Acquisti programmati
            - Spese previste ma non mensili
            
            Separare questi fondi riduce la sensazione 
            di "avere più soldi" di quanti siano 
            realmente disponibili.
            """)
        
        with st.container(border=True):
            st.markdown("### 4️⃣ Conto Investimenti")
            st.markdown("""
            È il **ponte verso il broker**.
            
            **Funzioni:**
            - Trasferimenti verso il conto titoli
            - Gestione liquidità per investimenti
            
            **Regola:** mantieni saldo basso e 
            trasferimenti programmati.
            """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Esempio pratico: struttura consigliata
    
    **Scenario:** Marco ha reddito stabile e una famiglia.
    """)
    
    example_data = {
        "Conto": ["Conto A - Operativo", "Conto B - Risparmi", "Conto C - Obiettivi", "Conto D - Investimenti"],
        "Scopo": [
            "Stipendio e spese correnti",
            "Fondo emergenze (3-6 mesi)",
            "Vacanze e spese pianificate",
            "Collegato al broker"
        ],
        "Movimento mensile": [
            "Tutto il flusso quotidiano",
            "Trasferimento automatico €300",
            "Trasferimento automatico €200",
            "Versamento programmato €150"
        ]
    }
    
    df_example = pd.DataFrame(example_data)
    st.dataframe(df_example, use_container_width=True, hide_index=True)
    
    st.info("""
    💡 **Flusso ottimale:**
    - Stipendio → Conto A
    - Trasferimento automatico → Conto B e C
    - Versamento programmato → Conto D
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Regole pratiche di gestione
    
    ✅ **Automatizza i trasferimenti** - riduci l'attrito decisionale
    
    ✅ **Evita di usare il conto investimenti per spese** - mantieni separazione netta
    
    ✅ **Controlla periodicamente costi nascosti** - canoni, commissioni, bolli
    
    ✅ **Mantieni semplicità** - meglio pochi conti ben gestiti che molti confusi
    
    ❌ **Non moltiplicare i conti senza motivo** - ogni conto ha un costo di gestione mentale
    """)


def render_calcolatore():
    """Renderizza i calcolatori"""
    
    st.markdown("## 🧮 Calcolatori")
    
    calc_type = st.radio(
        "Seleziona calcolatore:",
        ["Confronto Costi Conti", "Progetta la tua struttura"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if calc_type == "Confronto Costi Conti":
        render_calc_costi()
    else:
        render_calc_struttura()


def render_calc_costi():
    """Calcolatore confronto costi conti"""
    
    st.markdown("### Confronto Costi Annui tra Conti")
    
    st.markdown("Confronta i costi totali di due conti bancari per decidere quale conviene.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🏦 Conto A")
        
        canone_a = st.number_input(
            "Canone mensile (€)",
            min_value=0.0,
            value=5.0,
            step=0.5,
            key="cap5_canone_a"
        )
        
        comm_bonif_a = st.number_input(
            "Commissione bonifico (€)",
            min_value=0.0,
            value=1.0,
            step=0.1,
            key="cap5_bonif_a"
        )
        
        num_bonif = st.number_input(
            "Bonifici al mese",
            min_value=0,
            value=4,
            step=1,
            key="cap5_num_bonif"
        )
        
        comm_prel_a = st.number_input(
            "Costo prelievo ATM esterno (€)",
            min_value=0.0,
            value=2.0,
            step=0.5,
            key="cap5_prel_a"
        )
        
        num_prel = st.number_input(
            "Prelievi esterni al mese",
            min_value=0,
            value=2,
            step=1,
            key="cap5_num_prel"
        )
        
        costi_a = calcola_costi_annui(canone_a, comm_bonif_a, num_bonif * 12, comm_prel_a, num_prel * 12)
        
        st.markdown("#### Costi annui Conto A")
        st.metric("Totale anno", f"€{costi_a['totale']:.2f}")
        
        with st.expander("Dettaglio"):
            st.write(f"Canone: €{costi_a['canone']:.2f}")
            st.write(f"Bonifici: €{costi_a['bonifici']:.2f}")
            st.write(f"Prelievi: €{costi_a['prelievi']:.2f}")
    
    with col2:
        st.markdown("#### 🏦 Conto B")
        
        canone_b = st.number_input(
            "Canone mensile (€)",
            min_value=0.0,
            value=0.0,
            step=0.5,
            key="cap5_canone_b"
        )
        
        comm_bonif_b = st.number_input(
            "Commissione bonifico (€)",
            min_value=0.0,
            value=2.5,
            step=0.1,
            key="cap5_bonif_b"
        )
        
        st.write(f"Bonifici al mese: {num_bonif}")
        
        comm_prel_b = st.number_input(
            "Costo prelievo ATM esterno (€)",
            min_value=0.0,
            value=3.0,
            step=0.5,
            key="cap5_prel_b"
        )
        
        st.write(f"Prelievi esterni al mese: {num_prel}")
        
        costi_b = calcola_costi_annui(canone_b, comm_bonif_b, num_bonif * 12, comm_prel_b, num_prel * 12)
        
        st.markdown("#### Costi annui Conto B")
        st.metric("Totale anno", f"€{costi_b['totale']:.2f}")
        
        with st.expander("Dettaglio"):
            st.write(f"Canone: €{costi_b['canone']:.2f}")
            st.write(f"Bonifici: €{costi_b['bonifici']:.2f}")
            st.write(f"Prelievi: €{costi_b['prelievi']:.2f}")
    
    st.markdown("---")
    
    st.markdown("### 📊 Confronto")
    
    differenza = abs(costi_a['totale'] - costi_b['totale'])
    
    if costi_a['totale'] < costi_b['totale']:
        st.success(f"✅ Il Conto A costa €{differenza:.2f} in meno all'anno")
    elif costi_b['totale'] < costi_a['totale']:
        st.success(f"✅ Il Conto B costa €{differenza:.2f} in meno all'anno")
    else:
        st.info("⚖️ I due conti hanno lo stesso costo annuo")
    
    # Grafico comparativo
    chart_data = pd.DataFrame({
        "Voce": ["Canone", "Bonifici", "Prelievi"],
        "Conto A": [costi_a['canone'], costi_a['bonifici'], costi_a['prelievi']],
        "Conto B": [costi_b['canone'], costi_b['bonifici'], costi_b['prelievi']]
    })
    
    st.markdown("#### Distribuzione costi")
    st.bar_chart(chart_data.set_index("Voce"))


def render_calc_struttura():
    """Designer struttura conti personale"""
    
    st.markdown("### Progetta la Tua Struttura di Conti")
    
    st.markdown("""
    Usa questo strumento per definire la tua struttura ideale di conti e i movimenti automatici.
    """)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        reddito = st.number_input(
            "💰 Reddito netto mensile (€)",
            min_value=0.0,
            value=2400.0,
            step=100.0,
            key="cap5_redd_strutt"
        )
        
        st.markdown("#### 📤 Destinazioni mensili")
        
        perc_emergenze = st.slider(
            "% Fondo emergenze",
            min_value=0,
            max_value=50,
            value=10,
            step=5,
            key="cap5_perc_emerg"
        )
        
        perc_obiettivi = st.slider(
            "% Obiettivi",
            min_value=0,
            max_value=50,
            value=10,
            step=5,
            key="cap5_perc_obiett"
        )
        
        perc_investimenti = st.slider(
            "% Investimenti",
            min_value=0,
            max_value=50,
            value=5,
            step=5,
            key="cap5_perc_invest"
        )
    
    with col2:
        import_emergenze = reddito * (perc_emergenze / 100)
        import_obiettivi = reddito * (perc_obiettivi / 100)
        import_investimenti = reddito * (perc_investimenti / 100)
        import_operativo = reddito - import_emergenze - import_obiettivi - import_investimenti
        
        st.markdown("### 🔄 Piano di trasferimenti automatici")
        
        struttura_data = {
            "Conto": ["Operativo", "Fondo Emergenze", "Obiettivi", "Investimenti"],
            "Destinazione (€)": [
                f"{import_operativo:,.2f}",
                f"{import_emergenze:,.2f}",
                f"{import_obiettivi:,.2f}",
                f"{import_investimenti:,.2f}"
            ],
            "Percentuale": [
                f"{(import_operativo/reddito*100):.1f}%",
                f"{perc_emergenze}%",
                f"{perc_obiettivi}%",
                f"{perc_investimenti}%"
            ],
            "Quando": [
                "Immediato (accredito stipendio)",
                "Giorno 1 del mese",
                "Giorno 1 del mese",
                "Giorno 5 del mese"
            ]
        }
        
        df_struttura = pd.DataFrame(struttura_data)
        st.dataframe(df_struttura, use_container_width=True, hide_index=True)
        
        st.markdown("### 📊 Distribuzione visiva")
        
        chart_data = pd.DataFrame({
            "Importo": [import_operativo, import_emergenze, import_obiettivi, import_investimenti],
        }, index=["Operativo", "Emergenze", "Obiettivi", "Investimenti"])
        
        st.bar_chart(chart_data)
        
        # Verifica
        totale_allocato = import_emergenze + import_obiettivi + import_investimenti
        perc_risparmiata = (totale_allocato / reddito * 100) if reddito > 0 else 0
        
        if perc_risparmiata >= 20:
            st.success(f"✅ Ottimo! Stai allocando il {perc_risparmiata:.1f}% del reddito")
        elif perc_risparmiata >= 10:
            st.info(f"📊 Buon inizio: {perc_risparmiata:.1f}% allocato")
        else:
            st.warning(f"⚠️ Solo {perc_risparmiata:.1f}% allocato. Prova ad aumentare.")


def render_quiz():
    """Renderizza il quiz di verifica"""
    
    st.markdown("## 📝 Quiz di verifica")
    
    if "cap5_risposte" not in st.session_state:
        st.session_state.cap5_risposte = {}
    if "cap5_verificato" not in st.session_state:
        st.session_state.cap5_verificato = False
    
    for i, q in enumerate(QUIZ):
        with st.container(border=True):
            st.markdown(f"**Domanda {i+1}:** {q['domanda']}")
            
            if q["tipo"] == "vero_falso":
                risposta = st.radio(
                    "Seleziona:",
                    ["Vero", "Falso"],
                    key=f"cap5_q{q['id']}",
                    horizontal=True
                )
                st.session_state.cap5_risposte[q['id']] = risposta == "Vero"
                
            elif q["tipo"] == "scelta_multipla":
                risposta = st.radio(
                    "Seleziona:",
                    q["opzioni"],
                    key=f"cap5_q{q['id']}"
                )
                st.session_state.cap5_risposte[q['id']] = risposta
            
            if st.session_state.cap5_verificato:
                user_ans = st.session_state.cap5_risposte.get(q['id'])
                corretto = user_ans == q["risposta_corretta"]
                
                if corretto:
                    st.success(f"✅ Corretto! {q['spiegazione']}")
                else:
                    st.error(f"❌ Sbagliato. Risposta corretta: {q['risposta_corretta']}")
                    st.info(q['spiegazione'])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Verifica risposte", type="primary", use_container_width=True, key="cap5_verifica"):
            st.session_state.cap5_verificato = True
            st.rerun()
    with col2:
        if st.button("🔄 Ricomincia", use_container_width=True, key="cap5_reset"):
            st.session_state.cap5_verificato = False
            st.session_state.cap5_risposte = {}
            st.rerun()


def render_takeaways():
    """Renderizza i punti chiave"""
    
    st.markdown("## 💡 Punti chiave")
    
    takeaways = [
        "Una struttura di conti ben progettata funziona come un sistema di contenitori",
        "Non esiste un conto perfetto: esiste quello più adatto al tuo utilizzo reale",
        "Separa il denaro in base alla funzione, non alla provenienza",
        "Il conto operativo deve contenere solo il minimo per le spese mensili",
        "Automatizza i trasferimenti tra conti per ridurre l'attrito decisionale",
        "Controlla sempre i costi totali annui, non solo il canone"
    ]
    
    for t in takeaways:
        st.markdown(f"- {t}")
    
    st.markdown("---")
    
    # Esercizio pratico
    with st.expander("📝 Esercizio pratico: Disegna la tua struttura"):
        st.markdown("""
        Compila questa tabella per definire la tua struttura ideale:
        
        | Conto | Scopo | Saldo target | Regola automatica |
        |-------|-------|--------------|-------------------|
        | Conto 1 | | | |
        | Conto 2 | | | |
        | Conto 3 | | | |
        | Conto 4 | | | |
        
        **Domande guida:**
        
        1. Dove arriva il tuo stipendio?
        2. Dove tieni il fondo emergenze?
        3. Come separi le spese quotidiane dai risparmi?
        4. Quali trasferimenti puoi automatizzare?
        
        ---
        
        💡 *Ricorda: meglio pochi conti ben gestiti che molti confusi.*
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
