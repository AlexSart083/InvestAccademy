"""
Capitolo 11: Strumenti di investimento: ETF, fondi e azioni
InvestAccademy - Corso di Finanza Personale
"""

import streamlit as st
import pandas as pd

# Metadata
CAPITOLO_NUM = 11
TITOLO = "Strumenti di investimento: ETF, fondi e azioni"

OBIETTIVI = [
    "Comprendere le principali differenze tra ETF, fondi comuni e azioni",
    "Valutare costi, vantaggi e limiti di ciascuno strumento",
    "Capire quando uno strumento è più adatto di un altro",
    "Evitare errori comuni nella scelta degli strumenti",
    "Collegare strumenti, asset allocation e strategia"
]

# Quiz
QUIZ = [
    {
        "id": 1,
        "domanda": "Qual è la differenza principale tra ETF e fondi comuni?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Gestione passiva vs attiva e costi inferiori",
            "Gli ETF sono più rischiosi",
            "I fondi sono sempre migliori",
            "Non c'è differenza"
        ],
        "risposta_corretta": "Gestione passiva vs attiva e costi inferiori",
        "spiegazione": "Gli ETF hanno generalmente gestione passiva e costi significativamente inferiori rispetto ai fondi comuni a gestione attiva."
    },
    {
        "id": 2,
        "domanda": "Perché i costi sono così importanti negli investimenti?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Non sono importanti",
            "Riducono il rendimento composto nel tempo",
            "Solo per importi elevati",
            "Si recuperano con rendimenti alti"
        ],
        "risposta_corretta": "Riducono il rendimento composto nel tempo",
        "spiegazione": "I costi erodono il rendimento composto anno dopo anno, con un impatto significativo sul capitale finale."
    },
    {
        "id": 3,
        "domanda": "Le azioni singole sono adatte a tutti gli investitori.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "Le azioni singole richiedono competenze specifiche, tempo per l'analisi e alta tolleranza al rischio."
    },
    {
        "id": 4,
        "domanda": "Un ETF permette di ottenere:",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Diversificazione istantanea",
            "Rendimenti garantiti",
            "Nessun rischio",
            "Rendimenti sempre superiori"
        ],
        "risposta_corretta": "Diversificazione istantanea",
        "spiegazione": "Un ETF su indice offre diversificazione immediata su molti titoli con un singolo acquisto."
    },
    {
        "id": 5,
        "domanda": "Sovrapporre strumenti simili migliora la diversificazione.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "Sovrapporre strumenti simili non aumenta la diversificazione, ma aumenta complessità e costi."
    }
]


def calcola_impatto_costi(capitale: float, anni: int, rendimento: float, costo_perc: float) -> dict:
    """Calcola l'impatto dei costi sul capitale finale"""
    
    rendimento_lordo = rendimento / 100
    costo = costo_perc / 100
    rendimento_netto = rendimento_lordo - costo
    
    capitale_lordo = capitale * ((1 + rendimento_lordo) ** anni)
    capitale_netto = capitale * ((1 + rendimento_netto) ** anni)
    
    differenza = capitale_lordo - capitale_netto
    
    return {
        "capitale_lordo": capitale_lordo,
        "capitale_netto": capitale_netto,
        "differenza_costi": differenza,
        "perc_riduzione": (differenza / capitale_lordo * 100) if capitale_lordo > 0 else 0
    }


def confronta_strumenti(capitale: float, anni: int) -> dict:
    """Confronta diversi strumenti con costi tipici"""
    
    rendimento_base = 6.0  # Rendimento lordo ipotetico
    
    strumenti = {
        "ETF": {"costo": 0.2, "tipo": "Passivo"},
        "Fondo Attivo": {"costo": 2.0, "tipo": "Attivo"},
        "Azione Singola": {"costo": 0.1, "tipo": "Diretto"}
    }
    
    risultati = {}
    
    for nome, dati in strumenti.items():
        calc = calcola_impatto_costi(capitale, anni, rendimento_base, dati["costo"])
        risultati[nome] = {
            "costo_annuo": dati["costo"],
            "tipo": dati["tipo"],
            "capitale_finale": calc["capitale_netto"],
            "costi_totali": calc["differenza_costi"]
        }
    
    return risultati


def render_contenuto():
    """Renderizza il contenuto teorico"""
    
    st.markdown("""
    ## Perché la scelta dello strumento conta
    
    Una volta definita l'asset allocation, la domanda successiva è: **con quali strumenti implementarla?**
    
    La scelta dello strumento incide su:
    - Costi
    - Semplicità di gestione
    - Rischio operativo
    - Risultati nel lungo periodo
    
    Strumenti diversi possono replicare la stessa allocazione con esiti molto differenti.
    """)
    
    st.markdown("---")
    
    st.markdown("## I tre principali strumenti di investimento")
    
    # Azioni
    with st.container(border=True):
        st.markdown("### 📊 Azioni")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            Le azioni rappresentano una quota di proprietà di una singola azienda.
            
            **Vantaggi:**
            - Potenziale di rendimento elevato
            - Partecipazione diretta alla crescita dell'impresa
            - Trasparenza e controllo
            
            **Svantaggi:**
            - Rischio specifico elevato
            - Necessità di analisi e monitoraggio costante
            - Elevata volatilità nel breve termine
            - Richiede tempo e competenze
            """)
        
        with col2:
            st.metric("Costi tipici", "Bassi", help="Commissioni di negoziazione")
            st.metric("Diversificazione", "Bassa", delta_color="off")
            st.metric("Complessità", "Alta", delta_color="off")
    
    # Fondi comuni
    with st.container(border=True):
        st.markdown("### 🏦 Fondi Comuni di Investimento")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            I fondi comuni raccolgono capitali di più investitori e li gestiscono 
            tramite un gestore professionale.
            
            **Caratteristiche:**
            - Gestione attiva
            - Diversificazione interna
            - Delega completa della gestione
            
            **Pro:**
            - Accesso a mercati complessi
            - Gestione professionale
            
            **Contro:**
            - Costi di gestione spesso elevati (1-2%+ annuo)
            - Performance spesso inferiori agli indici nel lungo periodo
            - Minore trasparenza
            """)
        
        with col2:
            st.metric("Costi tipici", "1-2%+ annuo", delta_color="inverse")
            st.metric("Diversificazione", "Alta", delta_color="off")
            st.metric("Complessità", "Media", delta_color="off")
    
    # ETF
    with st.container(border=True):
        st.markdown("### 📈 ETF (Exchange Traded Fund)")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            Gli ETF sono fondi quotati che replicano passivamente un indice.
            
            **Caratteristiche principali:**
            - Gestione passiva
            - Costi molto contenuti (0,1-0,5% annuo)
            - Elevata diversificazione
            - Negoziazione in tempo reale
            - Alta trasparenza
            
            Gli ETF permettono di implementare un'asset allocation in modo 
            **semplice, efficiente e disciplinato**.
            """)
        
        with col2:
            st.metric("Costi tipici", "0,1-0,5% annuo", delta_color="normal")
            st.metric("Diversificazione", "Alta", delta_color="off")
            st.metric("Complessità", "Bassa", delta_color="off")
    
    st.markdown("---")
    
    st.markdown("## Confronto Sintetico")
    
    df_confronto = pd.DataFrame({
        "Strumento": ["Azioni", "Fondi", "ETF"],
        "Costi": ["Bassi", "Alti", "Molto bassi"],
        "Diversificazione": ["Bassa", "Media/Alta", "Alta"],
        "Complessità": ["Alta", "Media", "Bassa"],
        "Controllo": ["Alto", "Basso", "Medio"]
    })
    
    st.dataframe(df_confronto, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    st.markdown("## L'impatto dei costi nel lungo periodo")
    
    st.markdown("""
    I costi sono uno dei pochi fattori **certi** negli investimenti.
    
    Anche una differenza apparentemente piccola ha un impatto enorme nel lungo periodo 
    grazie all'effetto composto.
    """)
    
    with st.container(border=True):
        st.markdown("### 💡 Esempio pratico")
        st.markdown("""
        **Investimento:** €10.000 per 30 anni  
        **Rendimento lordo:** 6% annuo
        
        | Costi annui | Capitale finale | Differenza |
        |------------|----------------|------------|
        | 0,2% | €53.000 | Riferimento |
        | 1,0% | €43.000 | -€10.000 |
        | 2,0% | €32.000 | -€21.000 |
        
        **La differenza è dovuta solo ai costi.**
        """)
    
    st.warning("""
    ⚠️ **Un costo dell'1,5% in più può ridurre il capitale finale del 30-40% su orizzonti lunghi.**
    """)
    
    st.markdown("---")
    
    st.markdown("## Quando scegliere uno strumento rispetto a un altro")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### ETF")
        st.markdown("""
        **Per:**
        - La maggior parte degli investitori individuali
        - Chi cerca semplicità
        - Chi vuole costi bassi
        - Piani di lungo periodo
        """)
    
    with col2:
        st.markdown("### Fondi")
        st.markdown("""
        **Solo se:**
        - Il valore aggiunto giustifica i costi
        - Mercati molto specializzati
        - Strategie complesse
        - Dopo attenta valutazione
        """)
    
    with col3:
        st.markdown("### Azioni")
        st.markdown("""
        **Per:**
        - Parte limitata del portafoglio
        - Chi ha competenze specifiche
        - Strategie mirate
        - Alta tolleranza al rischio
        """)
    
    st.info("""
    💡 **Regola pratica:**
    
    Per la maggior parte degli investitori, un portafoglio di ETF diversificati 
    rappresenta la soluzione più efficiente.
    """)
    
    st.markdown("---")
    
    st.markdown("## Errori comuni nella scelta degli strumenti")
    
    errori = [
        ("❌ Sovrapporre strumenti simili", "Usare 5 ETF azionari globali invece di 1 aumenta complessità senza benefici"),
        ("❌ Ignorare i costi", "Non considerare l'impatto composto dei costi nel tempo"),
        ("❌ Cambiare strumenti frequentemente", "Il turnover genera costi e tasse"),
        ("❌ Investire in ciò che non si comprende", "Strumenti complessi aumentano il rischio di errori"),
        ("❌ Privilegiare strumenti alla moda", "Inseguire le mode porta spesso a comprare al momento sbagliato")
    ]
    
    for errore, spiegazione in errori:
        with st.container(border=True):
            st.markdown(f"**{errore}**")
            st.caption(spiegazione)
    
    st.success("""
    ✅ **Principio guida:**
    
    Lo strumento deve servire la strategia, non il contrario.
    La semplicità è spesso un vantaggio competitivo.
    """)


def render_calcolatore():
    """Renderizza i calcolatori"""
    
    st.markdown("## 🧮 Calcolatori")
    
    calc_type = st.radio(
        "Seleziona calcolatore:",
        ["Impatto Costi", "Confronto Strumenti", "Analisi Portafoglio"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if calc_type == "Impatto Costi":
        render_calc_costi()
    elif calc_type == "Confronto Strumenti":
        render_calc_confronto()
    else:
        render_calc_analisi()


def render_calc_costi():
    """Calcolatore impatto costi"""
    
    st.markdown("### Calcola l'Impatto dei Costi nel Tempo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        capitale = st.number_input(
            "💰 Capitale iniziale (€)",
            min_value=1000.0,
            value=10000.0,
            step=1000.0,
            key="cap11_capitale"
        )
        
        anni = st.slider(
            "📅 Orizzonte temporale (anni)",
            min_value=5,
            max_value=40,
            value=30,
            key="cap11_anni"
        )
        
        rendimento = st.slider(
            "📊 Rendimento lordo annuo (%)",
            min_value=0.0,
            max_value=15.0,
            value=6.0,
            step=0.5,
            key="cap11_rend"
        )
        
        costo = st.slider(
            "💸 Costi annui (%)",
            min_value=0.0,
            max_value=3.0,
            value=0.5,
            step=0.1,
            key="cap11_costo"
        )
    
    with col2:
        risultato = calcola_impatto_costi(capitale, anni, rendimento, costo)
        
        st.markdown("### Risultati")
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.metric("Capitale senza costi", f"€{risultato['capitale_lordo']:,.0f}")
        
        with c2:
            st.metric(
                "Capitale con costi",
                f"€{risultato['capitale_netto']:,.0f}",
                f"-€{risultato['differenza_costi']:,.0f}",
                delta_color="inverse"
            )
        
        st.markdown("---")
        
        st.metric(
            "Riduzione per costi",
            f"{risultato['perc_riduzione']:.1f}%",
            f"-€{risultato['differenza_costi']:,.0f}",
            delta_color="inverse"
        )
        
        if risultato['perc_riduzione'] > 30:
            st.error("🔴 Impatto dei costi molto elevato!")
        elif risultato['perc_riduzione'] > 15:
            st.warning("⚠️ Impatto dei costi significativo")
        else:
            st.success("✅ Impatto dei costi contenuto")
    
    st.markdown("---")
    st.info(f"""
    💡 **Interpretazione:**
    
    Con costi del {costo}% annuo, perdi il {risultato['perc_riduzione']:.1f}% 
    del capitale che avresti potuto accumulare in {anni} anni.
    
    Questo equivale a **€{risultato['differenza_costi']:,.0f}** che vanno ai gestori 
    invece che rimanere nel tuo portafoglio.
    """)


def render_calc_confronto():
    """Confronto tra strumenti"""
    
    st.markdown("### Confronto Costi: ETF vs Fondo vs Azione")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        capitale = st.number_input(
            "💰 Capitale iniziale (€)",
            min_value=1000.0,
            value=10000.0,
            step=1000.0,
            key="cap11_conf_cap"
        )
        
        anni = st.slider(
            "📅 Orizzonte (anni)",
            min_value=5,
            max_value=40,
            value=20,
            key="cap11_conf_anni"
        )
    
    with col2:
        risultati = confronta_strumenti(capitale, anni)
        
        st.markdown("### Risultati Confronto")
        
        df_risultati = pd.DataFrame({
            "Strumento": list(risultati.keys()),
            "Tipo": [r['tipo'] for r in risultati.values()],
            "Costo Annuo": [f"{r['costo_annuo']}%" for r in risultati.values()],
            "Capitale Finale": [f"€{r['capitale_finale']:,.0f}" for r in risultati.values()],
            "Costi Totali": [f"€{r['costi_totali']:,.0f}" for r in risultati.values()]
        })
        
        st.dataframe(df_risultati, use_container_width=True, hide_index=True)
        
        # Grafico
        st.markdown("#### 📊 Confronto Visivo")
        
        chart_data = pd.DataFrame({
            "Capitale Finale": [r['capitale_finale'] for r in risultati.values()]
        }, index=list(risultati.keys()))
        
        st.bar_chart(chart_data)
    
    # Analisi
    etf_capitale = risultati["ETF"]["capitale_finale"]
    fondo_capitale = risultati["Fondo Attivo"]["capitale_finale"]
    differenza = etf_capitale - fondo_capitale
    
    st.markdown("---")
    st.warning(f"""
    ⚠️ **Differenza ETF vs Fondo Attivo:**
    
    L'ETF genera **€{differenza:,.0f} in più** rispetto al fondo attivo 
    a causa dei minori costi.
    
    Questo rappresenta il {((differenza / fondo_capitale) * 100):.1f}% del capitale 
    che avresti con il fondo.
    """)


def render_calc_analisi():
    """Analisi portafoglio attuale"""
    
    st.markdown("### Analizza i Costi del Tuo Portafoglio")
    
    st.markdown("""
    Inserisci gli strumenti che possiedi per analizzare i costi complessivi.
    """)
    
    # Session state per strumenti
    if "cap11_strumenti" not in st.session_state:
        st.session_state.cap11_strumenti = [
            {"nome": "ETF Azionario Globale", "valore": 6000, "costo": 0.2},
            {"nome": "ETF Obbligazionario", "valore": 3000, "costo": 0.15},
            {"nome": "Fondo Attivo", "valore": 1000, "costo": 2.0}
        ]
    
    for i, strumento in enumerate(st.session_state.cap11_strumenti):
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            strumento['nome'] = st.text_input(
                f"Strumento {i+1}",
                value=strumento['nome'],
                key=f"cap11_str_nome_{i}"
            )
        with col2:
            strumento['valore'] = st.number_input(
                "Valore (€)",
                value=float(strumento['valore']),
                min_value=0.0,
                step=100.0,
                key=f"cap11_str_val_{i}"
            )
        with col3:
            strumento['costo'] = st.number_input(
                "Costo %",
                value=float(strumento['costo']),
                min_value=0.0,
                max_value=5.0,
                step=0.05,
                key=f"cap11_str_cost_{i}"
            )
    
    # Calcoli
    valore_totale = sum(s['valore'] for s in st.session_state.cap11_strumenti)
    
    if valore_totale > 0:
        # Costo medio ponderato
        costo_ponderato = sum(s['valore'] * s['costo'] for s in st.session_state.cap11_strumenti) / valore_totale
        costo_annuo_euro = valore_totale * (costo_ponderato / 100)
        
        st.markdown("---")
        st.markdown("### 📊 Analisi Complessiva")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Valore Totale", f"€{valore_totale:,.0f}")
        with col2:
            st.metric("Costo Medio Ponderato", f"{costo_ponderato:.2f}%")
        with col3:
            st.metric("Costo Annuo", f"€{costo_annuo_euro:,.0f}")
        
        # Breakdown per strumento
        st.markdown("#### Dettaglio per Strumento")
        
        df_breakdown = pd.DataFrame({
            "Strumento": [s['nome'] for s in st.session_state.cap11_strumenti],
            "Valore": [f"€{s['valore']:,.0f}" for s in st.session_state.cap11_strumenti],
            "Peso": [f"{(s['valore']/valore_totale*100):.1f}%" for s in st.session_state.cap11_strumenti],
            "Costo %": [f"{s['costo']:.2f}%" for s in st.session_state.cap11_strumenti],
            "Costo € annuo": [f"€{s['valore'] * s['costo'] / 100:,.0f}" for s in st.session_state.cap11_strumenti]
        })
        
        st.dataframe(df_breakdown, use_container_width=True, hide_index=True)
        
        # Valutazione
        if costo_ponderato < 0.5:
            st.success("✅ Costi molto bassi! Portafoglio efficiente.")
        elif costo_ponderato < 1.0:
            st.info("📊 Costi nella norma per un portafoglio misto.")
        else:
            st.warning(f"⚠️ Costi elevati. Valuta alternative più economiche.")
            st.caption(f"Risparmiando l'1% annuo su €{valore_totale:,.0f}, dopo 20 anni avresti circa €{valore_totale * 0.22:,.0f} in più.")


def render_quiz():
    """Renderizza il quiz di verifica"""
    
    st.markdown("## 📝 Quiz di verifica")
    
    if "cap11_risposte" not in st.session_state:
        st.session_state.cap11_risposte = {}
    if "cap11_verificato" not in st.session_state:
        st.session_state.cap11_verificato = False
    
    for i, q in enumerate(QUIZ):
        with st.container(border=True):
            st.markdown(f"**Domanda {i+1}:** {q['domanda']}")
            
            if q["tipo"] == "vero_falso":
                risposta = st.radio(
                    "Seleziona:",
                    ["Vero", "Falso"],
                    key=f"cap11_q{q['id']}",
                    horizontal=True
                )
                st.session_state.cap11_risposte[q['id']] = risposta == "Vero"
                
            elif q["tipo"] == "scelta_multipla":
                risposta = st.radio(
                    "Seleziona:",
                    q["opzioni"],
                    key=f"cap11_q{q['id']}"
                )
                st.session_state.cap11_risposte[q['id']] = risposta
            
            if st.session_state.cap11_verificato:
                user_ans = st.session_state.cap11_risposte.get(q['id'])
                corretto = user_ans == q["risposta_corretta"]
                
                if corretto:
                    st.success(f"✅ Corretto! {q['spiegazione']}")
                else:
                    st.error(f"❌ Sbagliato. Risposta corretta: {q['risposta_corretta']}")
                    st.info(q['spiegazione'])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Verifica risposte", type="primary", use_container_width=True, key="cap11_verifica"):
            st.session_state.cap11_verificato = True
            st.rerun()
    with col2:
        if st.button("🔄 Ricomincia", use_container_width=True, key="cap11_reset"):
            st.session_state.cap11_verificato = False
            st.session_state.cap11_risposte = {}
            st.rerun()


def render_takeaways():
    """Renderizza i punti chiave"""
    
    st.markdown("## 💡 Punti chiave")
    
    takeaways = [
        "La scelta dello strumento impatta significativamente sui risultati di lungo periodo",
        "I costi sono uno dei pochi fattori certi: anche piccole differenze hanno grandi effetti composti",
        "Gli ETF offrono diversificazione, bassi costi e semplicità per la maggioranza degli investitori",
        "I fondi attivi raramente giustificano i costi aggiuntivi nel lungo periodo",
        "Le azioni singole richiedono competenze, tempo e alta tolleranza al rischio",
        "Lo strumento deve servire la strategia, non il contrario",
        "La semplicità è spesso un vantaggio competitivo negli investimenti"
    ]
    
    for t in takeaways:
        st.markdown(f"- {t}")
    
    st.markdown("---")
    
    # Esercizio pratico
    with st.expander("📝 Esercizio: Semplifica il tuo portafoglio"):
        st.markdown("""
        **Analizza il tuo portafoglio attuale:**
        
        1. **Elenca tutti gli strumenti che possiedi**
           
           | Strumento | Valore | Costo annuo % |
           |-----------|--------|---------------|
           | | | |
           | | | |
        
        2. **Calcola il costo medio ponderato**
           
           Somma: (Valore1 × Costo1) + (Valore2 × Costo2) + ...  
           Dividi per: Valore totale
        
        3. **Identifica le sovrapposizioni**
           
           - Hai più ETF che fanno la stessa cosa?
           - Hai fondi con costi elevati che potresti sostituire?
        
        4. **Definisci un piano di semplificazione**
           
           - Cosa puoi eliminare?
           - Cosa puoi consolidare?
           - Quale struttura target vuoi raggiungere?
        
        ---
        
        💡 **Obiettivo:** Portafoglio con 3-5 strumenti massimo, costo medio < 0,5%
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
