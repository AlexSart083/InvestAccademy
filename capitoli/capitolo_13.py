"""
Capitolo 13: Ribilanciamento del portafoglio
InvestAccademy - Corso di Finanza Personale
"""

import streamlit as st
import pandas as pd

# Metadata
CAPITOLO_NUM = 13
TITOLO = "Ribilanciamento del portafoglio"

OBIETTIVI = [
    "Comprendere cos'è il ribilanciamento del portafoglio",
    "Capire perché è una pratica fondamentale nel lungo periodo",
    "Conoscere le principali strategie di ribilanciamento",
    "Valutare quando e come intervenire",
    "Evitare errori comuni legati al market timing"
]

QUIZ = [
    {
        "id": 1,
        "domanda": "Cos'è il ribilanciamento del portafoglio?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Riportare il portafoglio all'asset allocation originale",
            "Vendere tutto e ricomprare",
            "Aumentare le azioni",
            "Cambiare strategia"
        ],
        "risposta_corretta": "Riportare il portafoglio all'asset allocation originale",
        "spiegazione": "Il ribilanciamento consiste nel riportare il portafoglio alla sua asset allocation target dopo che le variazioni di mercato l'hanno modificata."
    },
    {
        "id": 2,
        "domanda": "Perché vendere ciò che è cresciuto di più può ridurre il rischio?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Perché evita che una singola asset class domini il rischio",
            "Perché è sempre meglio vendere",
            "Per pagare meno tasse",
            "Non riduce il rischio"
        ],
        "risposta_corretta": "Perché evita che una singola asset class domini il rischio",
        "spiegazione": "Se non ribilanci, l'asset class più volatile (solitamente azioni) può diventare una percentuale eccessiva del portafoglio, aumentando il rischio."
    },
    {
        "id": 3,
        "domanda": "Il ribilanciamento serve a battere il mercato.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "Il ribilanciamento non serve a battere il mercato ma a mantenere il profilo di rischio coerente con gli obiettivi."
    },
    {
        "id": 4,
        "domanda": "Quando è meglio ribilanciare?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Ogni giorno",
            "Secondo regole prestabilite (annuale o per soglia)",
            "Solo quando il mercato scende",
            "Mai"
        ],
        "risposta_corretta": "Secondo regole prestabilite (annuale o per soglia)",
        "spiegazione": "Il ribilanciamento deve seguire regole chiare definite in anticipo, non decisioni emotive."
    },
    {
        "id": 5,
        "domanda": "Ribilanciare troppo spesso aumenta i costi senza benefici significativi.",
        "tipo": "vero_falso",
        "risposta_corretta": True,
        "spiegazione": "Ribilanciare troppo frequentemente genera costi di transazione e tasse senza migliorare significativamente i risultati."
    }
]


def calcola_ribilanciamento(portafoglio_attuale: dict, target: dict) -> dict:
    """Calcola le operazioni necessarie per il ribilanciamento"""
    
    valore_totale = sum(portafoglio_attuale.values())
    
    scostamenti = {}
    operazioni = {}
    
    for asset, valore_attuale in portafoglio_attuale.items():
        perc_attuale = (valore_attuale / valore_totale * 100) if valore_totale > 0 else 0
        perc_target = target.get(asset, 0)
        
        scostamento = perc_attuale - perc_target
        valore_target = valore_totale * (perc_target / 100)
        operazione = valore_target - valore_attuale
        
        scostamenti[asset] = {
            "valore_attuale": valore_attuale,
            "perc_attuale": perc_attuale,
            "perc_target": perc_target,
            "scostamento": scostamento,
            "valore_target": valore_target,
            "operazione": operazione
        }
        
        operazioni[asset] = operazione
    
    return {
        "scostamenti": scostamenti,
        "operazioni": operazioni,
        "valore_totale": valore_totale,
        "necessario": any(abs(s["scostamento"]) > 5 for s in scostamenti.values())
    }


def simula_drift(azioni_iniz: float, obblig_iniz: float, anni: int, 
                 rend_azioni: float, rend_obblig: float) -> list:
    """Simula il drift del portafoglio senza ribilanciamento"""
    
    evoluzione = []
    azioni = azioni_iniz
    obblig = obblig_iniz
    
    for anno in range(anni + 1):
        totale = azioni + obblig
        perc_azioni = (azioni / totale * 100) if totale > 0 else 0
        perc_obblig = (obblig / totale * 100) if totale > 0 else 0
        
        evoluzione.append({
            "anno": anno,
            "azioni": azioni,
            "obbligazioni": obblig,
            "totale": totale,
            "perc_azioni": perc_azioni,
            "perc_obbligazioni": perc_obblig
        })
        
        if anno < anni:
            azioni = azioni * (1 + rend_azioni / 100)
            obblig = obblig * (1 + rend_obblig / 100)
    
    return evoluzione


def render_contenuto():
    """Renderizza il contenuto teorico"""
    
    st.markdown("""
    ## Cos'è il ribilanciamento
    
    Il ribilanciamento consiste nel **riportare il portafoglio alla sua asset allocation originale** 
    dopo che le variazioni di mercato hanno modificato i pesi degli attivi.
    
    Nel tempo, infatti, alcune asset class crescono più velocemente di altre, alterando il profilo 
    di rischio iniziale.
    
    > Ribilanciare significa **controllare il rischio**, non prevedere il mercato.
    """)
    
    st.markdown("---")
    
    st.markdown("## Perché il ribilanciamento è importante")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### ❌ Senza ribilanciamento")
            st.markdown("""
            Il portafoglio tende a:
            - Diventare più rischioso dopo lunghi rialzi azionari
            - Allontanarsi dagli obiettivi iniziali
            - Esporti a decisioni emotive
            
            **Esempio:**
            Target 60/40 → Dopo 5 anni diventa 75/25
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### ✅ Con ribilanciamento")
            st.markdown("""
            Il portafoglio:
            - Mantiene il profilo di rischio coerente
            - Implementa automaticamente "vendi alto, compra basso"
            - Riduce l'intervento emotivo
            
            **Disciplina sistematica**
            """)
    
    st.info("""
    💡 **Dal punto di vista psicologico**, il ribilanciamento è controintuitivo:
    - Si vende ciò che "sta andando bene"
    - Si compra ciò che "sembra andare male"
    
    Proprio per questo è una delle pratiche più efficaci nel ridurre errori comportamentali.
    """)
    
    st.markdown("---")
    
    st.markdown("## Strategie di ribilanciamento")
    
    tab1, tab2 = st.tabs(["Ribilanciamento Temporale", "Ribilanciamento per Soglia"])
    
    with tab1:
        st.markdown("### 📅 Ribilanciamento Temporale")
        st.markdown("""
        Si effettua a **intervalli regolari** prestabiliti.
        
        **Frequenze comuni:**
        - Annuale (più comune)
        - Semestrale
        - Trimestrale
        
        **Vantaggi:**
        - Semplice da applicare
        - Facile da automatizzare
        - Prevedibile
        
        **Per la maggior parte degli investitori individuali, il ribilanciamento annuale è sufficiente.**
        """)
    
    with tab2:
        st.markdown("### 🎯 Ribilanciamento per Soglia")
        st.markdown("""
        Si interviene quando il peso di un'asset class supera una **certa deviazione** rispetto al target.
        
        **Esempio:**
        - Allocazione azioni target: 60%
        - Soglia: ±5%
        - Si ribilancia se le azioni scendono sotto il 55% o salgono sopra il 65%
        
        **Vantaggi:**
        - Più reattivo ai movimenti significativi
        - Utile con portafogli grandi
        
        **Svantaggi:**
        - Richiede monitoraggio più frequente
        - Più complesso da gestire
        """)
    
    st.success("""
    ✅ **Quale strategia scegliere?**
    
    - **Annuale:** Semplice, efficace per la maggioranza
    - **Per soglia:** Se hai portafoglio grande o vuoi maggiore controllo
    
    L'importante è la **coerenza**, non la frequenza.
    """)
    
    st.markdown("---")
    
    st.markdown("## Esempio pratico")
    
    with st.container(border=True):
        st.markdown("### Portafoglio che si sbilancia")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Inizio anno:**")
            st.markdown("- Azioni: €60.000 (60%)")
            st.markdown("- Obbligazioni: €40.000 (40%)")
            st.markdown("- **Totale: €100.000**")
        
        with col2:
            st.markdown("**Fine anno:**")
            st.markdown("- Azioni: €72.000 (+20%)")
            st.markdown("- Obbligazioni: €42.000 (+5%)")
            st.markdown("- **Totale: €114.000**")
        
        st.markdown("---")
        
        st.markdown("**Nuova allocazione senza ribilanciamento:**")
        st.markdown("- Azioni: 63% (target era 60%)")
        st.markdown("- Obbligazioni: 37% (target era 40%)")
        
        st.markdown("---")
        
        st.markdown("**Operazioni per tornare al 60/40:**")
        target_azioni = 114000 * 0.60
        target_obblig = 114000 * 0.40
        
        st.markdown(f"- Vendere azioni: €{72000 - target_azioni:,.0f}")
        st.markdown(f"- Acquistare obbligazioni: €{target_obblig - 42000:,.0f}")
    
    st.markdown("---")
    
    st.markdown("## Ribilanciamento con nuovi versamenti")
    
    st.markdown("""
    Un metodo **efficiente** per ridurre costi e tasse è ribilanciare usando:
    - Nuovi contributi
    - PAC in corso
    - Reinvestimento dividendi
    
    Versando più capitale nelle asset class **sottopesate** si può correggere l'allocazione 
    senza vendere.
    """)
    
    st.markdown("---")
    
    st.markdown("## Costi e tassazione")
    
    st.warning("""
    ⚠️ **Prima di ribilanciare considera:**
    - Commissioni di transazione
    - Impatto fiscale delle vendite (capital gain)
    - Dimensione dello scostamento
    
    Ribilanciare troppo spesso può essere controproducente.
    """)
    
    st.markdown("---")
    
    st.markdown("## Errori comuni")
    
    errori = [
        ("❌ Ribilanciare emotivamente", "Seguire le emozioni invece delle regole prestabilite"),
        ("❌ Inseguire le performance recenti", "Modificare l'asset allocation perché un settore ha reso di più"),
        ("❌ Confondere ribilanciamento con market timing", "Non stai cercando di prevedere il mercato"),
        ("❌ Non considerare costi e tasse", "Può annullare i benefici del ribilanciamento"),
        ("❌ Ribilanciare troppo frequentemente", "Genera costi senza benefici significativi")
    ]
    
    for errore, spiegazione in errori:
        with st.container(border=True):
            st.markdown(f"**{errore}**")
            st.caption(spiegazione)
    
    st.success("""
    ✅ **Principio guida:**
    
    Il ribilanciamento è una **regola**, non un'opinione.
    Decidi oggi, esegui meccanicamente domani.
    """)


def render_calcolatore():
    """Renderizza i calcolatori"""
    
    st.markdown("## 🧮 Calcolatori")
    
    calc_type = st.radio(
        "Seleziona calcolatore:",
        ["Calcola Ribilanciamento", "Simula Drift Portafoglio"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if calc_type == "Calcola Ribilanciamento":
        render_calc_ribilanciamento()
    else:
        render_calc_drift()


def render_calc_ribilanciamento():
    """Calcolatore ribilanciamento necessario"""
    
    st.markdown("### Calcola il Ribilanciamento Necessario")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📊 Portafoglio Attuale")
        
        azioni_att = st.number_input(
            "Valore Azioni (€)",
            min_value=0.0,
            value=63000.0,
            step=1000.0,
            key="cap13_azioni_att"
        )
        
        obblig_att = st.number_input(
            "Valore Obbligazioni (€)",
            min_value=0.0,
            value=37000.0,
            step=1000.0,
            key="cap13_obblig_att"
        )
        
        liquid_att = st.number_input(
            "Valore Liquidità (€)",
            min_value=0.0,
            value=0.0,
            step=100.0,
            key="cap13_liquid_att"
        )
        
        st.markdown("---")
        
        st.markdown("#### 🎯 Target")
        
        target_azioni = st.slider(
            "Target Azioni (%)",
            min_value=0,
            max_value=100,
            value=60,
            key="cap13_target_az"
        )
        
        target_obblig = st.slider(
            "Target Obbligazioni (%)",
            min_value=0,
            max_value=100 - target_azioni,
            value=35,
            key="cap13_target_ob"
        )
        
        target_liquid = 100 - target_azioni - target_obblig
        
        st.metric("Target Liquidità", f"{target_liquid}%")
    
    with col2:
        portafoglio_attuale = {
            "Azioni": azioni_att,
            "Obbligazioni": obblig_att,
            "Liquidità": liquid_att
        }
        
        target = {
            "Azioni": target_azioni,
            "Obbligazioni": target_obblig,
            "Liquidità": target_liquid
        }
        
        risultato = calcola_ribilanciamento(portafoglio_attuale, target)
        
        st.markdown("### Analisi")
        
        # Tabella situazione attuale vs target
        df_analisi = pd.DataFrame({
            "Asset": list(risultato["scostamenti"].keys()),
            "Valore": [f"€{s['valore_attuale']:,.0f}" for s in risultato["scostamenti"].values()],
            "% Attuale": [f"{s['perc_attuale']:.1f}%" for s in risultato["scostamenti"].values()],
            "% Target": [f"{s['perc_target']:.1f}%" for s in risultato["scostamenti"].values()],
            "Scostamento": [f"{s['scostamento']:+.1f}%" for s in risultato["scostamenti"].values()]
        })
        
        st.dataframe(df_analisi, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Verifica se necessario
        if risultato["necessario"]:
            st.warning("⚠️ Ribilanciamento consigliato (scostamento > 5%)")
            
            st.markdown("#### 🔄 Operazioni Necessarie")
            
            for asset, operazione in risultato["operazioni"].items():
                if abs(operazione) > 100:  # Solo se significativo
                    if operazione > 0:
                        st.success(f"✅ **{asset}:** Acquistare €{operazione:,.0f}")
                    else:
                        st.error(f"📤 **{asset}:** Vendere €{abs(operazione):,.0f}")
        else:
            st.success("✅ Portafoglio in linea con il target (scostamento < 5%)")
        
        # Grafico
        st.markdown("#### 📊 Visualizzazione")
        
        chart_data = pd.DataFrame({
            "Attuale": [s['perc_attuale'] for s in risultato["scostamenti"].values()],
            "Target": [s['perc_target'] for s in risultato["scostamenti"].values()]
        }, index=list(risultato["scostamenti"].keys()))
        
        st.bar_chart(chart_data)


def render_calc_drift():
    """Simulatore drift del portafoglio"""
    
    st.markdown("### Simula il Drift del Portafoglio")
    
    st.markdown("""
    Questa simulazione mostra come il portafoglio si sbilancia nel tempo 
    senza ribilanciamento.
    """)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        azioni_iniz = st.number_input(
            "Azioni iniziali (€)",
            min_value=1000.0,
            value=60000.0,
            step=1000.0,
            key="cap13_drift_az"
        )
        
        obblig_iniz = st.number_input(
            "Obbligazioni iniziali (€)",
            min_value=1000.0,
            value=40000.0,
            step=1000.0,
            key="cap13_drift_ob"
        )
        
        anni = st.slider(
            "Anni di simulazione",
            min_value=1,
            max_value=30,
            value=10,
            key="cap13_drift_anni"
        )
        
        rend_azioni = st.slider(
            "Rendimento azioni (%)",
            min_value=0.0,
            max_value=15.0,
            value=8.0,
            step=0.5,
            key="cap13_drift_rend_az"
        )
        
        rend_obblig = st.slider(
            "Rendimento obbligazioni (%)",
            min_value=0.0,
            max_value=10.0,
            value=3.5,
            step=0.5,
            key="cap13_drift_rend_ob"
        )
    
    with col2:
        evoluzione = simula_drift(azioni_iniz, obblig_iniz, anni, rend_azioni, rend_obblig)
        
        perc_azioni_iniz = azioni_iniz / (azioni_iniz + obblig_iniz) * 100
        perc_azioni_fine = evoluzione[-1]["perc_azioni"]
        drift = perc_azioni_fine - perc_azioni_iniz
        
        st.markdown("### Risultato Simulazione")
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.metric("Allocazione iniziale azioni", f"{perc_azioni_iniz:.1f}%")
            st.metric("Valore iniziale", f"€{azioni_iniz + obblig_iniz:,.0f}")
        
        with c2:
            st.metric(
                "Allocazione finale azioni",
                f"{perc_azioni_fine:.1f}%",
                f"{drift:+.1f}%"
            )
            st.metric("Valore finale", f"€{evoluzione[-1]['totale']:,.0f}")
        
        if abs(drift) > 10:
            st.warning(f"⚠️ Drift significativo: {drift:+.1f}%")
        elif abs(drift) > 5:
            st.info(f"📊 Drift moderato: {drift:+.1f}%")
        else:
            st.success(f"✅ Drift contenuto: {drift:+.1f}%")
    
    st.markdown("---")
    st.markdown("### 📈 Evoluzione nel Tempo")
    
    df_evoluzione = pd.DataFrame(evoluzione)
    
    chart_data = pd.DataFrame({
        "Anno": df_evoluzione['anno'],
        "% Azioni": df_evoluzione['perc_azioni'],
        "% Obbligazioni": df_evoluzione['perc_obbligazioni']
    })
    
    st.line_chart(chart_data.set_index("Anno"))
    
    st.info("""
    💡 **Interpretazione:**
    
    Senza ribilanciamento, l'asset class con rendimento maggiore (di solito azioni) 
    tende a dominare il portafoglio, aumentando il rischio oltre il livello desiderato.
    
    Il ribilanciamento periodico mantiene l'allocazione in linea con gli obiettivi.
    """)


def render_quiz():
    """Renderizza il quiz di verifica"""
    
    st.markdown("## 📝 Quiz di verifica")
    
    if "cap13_risposte" not in st.session_state:
        st.session_state.cap13_risposte = {}
    if "cap13_verificato" not in st.session_state:
        st.session_state.cap13_verificato = False
    
    for i, q in enumerate(QUIZ):
        with st.container(border=True):
            st.markdown(f"**Domanda {i+1}:** {q['domanda']}")
            
            if q["tipo"] == "vero_falso":
                risposta = st.radio(
                    "Seleziona:",
                    ["Vero", "Falso"],
                    key=f"cap13_q{q['id']}",
                    horizontal=True
                )
                st.session_state.cap13_risposte[q['id']] = risposta == "Vero"
                
            elif q["tipo"] == "scelta_multipla":
                risposta = st.radio(
                    "Seleziona:",
                    q["opzioni"],
                    key=f"cap13_q{q['id']}"
                )
                st.session_state.cap13_risposte[q['id']] = risposta
            
            if st.session_state.cap13_verificato:
                user_ans = st.session_state.cap13_risposte.get(q['id'])
                corretto = user_ans == q["risposta_corretta"]
                
                if corretto:
                    st.success(f"✅ Corretto! {q['spiegazione']}")
                else:
                    st.error(f"❌ Sbagliato. Risposta corretta: {q['risposta_corretta']}")
                    st.info(q['spiegazione'])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Verifica risposte", type="primary", use_container_width=True, key="cap13_verifica"):
            st.session_state.cap13_verificato = True
            st.rerun()
    with col2:
        if st.button("🔄 Ricomincia", use_container_width=True, key="cap13_reset"):
            st.session_state.cap13_verificato = False
            st.session_state.cap13_risposte = {}
            st.rerun()


def render_takeaways():
    """Renderizza i punti chiave"""
    
    st.markdown("## 💡 Punti chiave")
    
    takeaways = [
        "Il ribilanciamento mantiene il portafoglio in linea con l'asset allocation target",
        "Senza ribilanciamento, il portafoglio diventa più rischioso dopo lunghi rialzi",
        "Il ribilanciamento implementa automaticamente 'vendi alto, compra basso'",
        "Due strategie principali: temporale (annuale) o per soglia (±5%)",
        "Per la maggioranza degli investitori, il ribilanciamento annuale è sufficiente",
        "Usare nuovi versamenti per ribilanciare riduce costi e tasse",
        "Il ribilanciamento è una regola, non un'opinione: decidi oggi, esegui meccanicamente"
    ]
    
    for t in takeaways:
        st.markdown(f"- {t}")
    
    st.markdown("---")
    
    with st.expander("📝 Esercizio: Definisci le tue regole di ribilanciamento"):
        st.markdown("""
        **Crea il tuo piano di ribilanciamento:**
        
        1. **Asset allocation target**
           - Azioni: _____% 
           - Obbligazioni: _____%
           - Liquidità: _____%
        
        2. **Strategia di ribilanciamento**
           - ☐ Temporale (ogni _____ mesi)
           - ☐ Per soglia (quando scostamento > ____%)
        
        3. **Data prossimo ribilanciamento**
           - Data: _____________
        
        4. **Regole comportamentali**
           - Ribilancerò anche se il mercato: _____________
           - Non modificherò la strategia anche se: _____________
           - Considererò costi e tasse prima di: _____________
        
        5. **Commitment**
           "Mi impegno a seguire queste regole per almeno _____ anni, 
           modificandole solo se cambiano i miei obiettivi, non per movimenti di mercato."
           
           Firma: _____________ Data: _____________
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
