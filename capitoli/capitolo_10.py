"""
Capitolo 10: Asset allocation e costruzione del portafoglio
InvestAccademy - Corso di Finanza Personale
"""

import streamlit as st
import pandas as pd

# Metadata
CAPITOLO_NUM = 10
TITOLO = "Asset allocation e costruzione del portafoglio"

OBIETTIVI = [
    "Comprendere cos'è l'asset allocation e perché è fondamentale",
    "Distinguere tra asset allocation strategica e tattica",
    "Collegare asset allocation, profilo di rischio e orizzonte temporale",
    "Costruire una struttura di portafoglio coerente",
    "Evitare errori comuni nella composizione degli investimenti"
]

# Quiz
QUIZ = [
    {
        "id": 1,
        "domanda": "Cos'è l'asset allocation?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "La distribuzione del capitale tra diverse classi di attivi",
            "La scelta dei singoli titoli in portafoglio",
            "Il momento giusto per entrare sul mercato",
            "La strategia di trading"
        ],
        "risposta_corretta": "La distribuzione del capitale tra diverse classi di attivi",
        "spiegazione": "L'asset allocation è la distribuzione strategica del capitale tra azioni, obbligazioni, oro e altri asset."
    },
    {
        "id": 2,
        "domanda": "Qual è la differenza tra asset allocation strategica e tattica?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "La strategica è di lungo periodo, la tattica è temporanea",
            "La strategica costa di più",
            "La tattica è più sicura",
            "Non c'è differenza"
        ],
        "risposta_corretta": "La strategica è di lungo periodo, la tattica è temporanea",
        "spiegazione": "L'asset allocation strategica è la struttura di base del portafoglio, mentre quella tattica prevede aggiustamenti temporanei."
    },
    {
        "id": 3,
        "domanda": "L'asset allocation spiega la maggior parte dei risultati di un portafoglio nel lungo periodo.",
        "tipo": "vero_falso",
        "risposta_corretta": True,
        "spiegazione": "Numerosi studi dimostrano che l'asset allocation è più importante della scelta dei singoli titoli."
    },
    {
        "id": 4,
        "domanda": "Un portafoglio con 80% azioni è adatto a:",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Orizzonte 5 anni con alta tolleranza",
            "Orizzonte superiore a 10 anni con alta tolleranza",
            "Qualsiasi orizzonte se si accetta volatilità",
            "Solo investitori professionali"
        ],
        "risposta_corretta": "Orizzonte superiore a 10 anni con alta tolleranza",
        "spiegazione": "Un'allocazione così aggressiva richiede orizzonte temporale superiore a 10 anni E alta tolleranza al rischio. L'orizzonte lungo permette di attraversare i cicli di mercato."
    },
    {
        "id": 5,
        "domanda": "La liquidità dovrebbe far parte del portafoglio di lungo termine.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "Falso. La liquidità serve per fondo emergenze e breve termine, non per il portafoglio investito."
    }
]


def calcola_profilo_rischio(domande_risposte: dict) -> dict:
    """Calcola il profilo di rischio basato sulle risposte"""
    punteggio = sum(domande_risposte.values())
    
    if punteggio <= 10:
        profilo = "Prudente"
        descrizione = "Preferisci stabilità e hai bassa tolleranza alle oscillazioni"
        allocazione = {"Azioni": 30, "Obbligazioni": 60, "Oro": 10}
        colore = "🟢"
    elif punteggio <= 17:
        profilo = "Bilanciato"
        descrizione = "Cerchi equilibrio tra crescita e stabilità"
        allocazione = {"Azioni": 60, "Obbligazioni": 35, "Oro": 5}
        colore = "🔵"
    else:
        profilo = "Dinamico"
        descrizione = "Punti alla crescita di lungo periodo e accetti volatilità"
        allocazione = {"Azioni": 80, "Obbligazioni": 15, "Oro": 5}
        colore = "🔴"
    
    return {
        "punteggio": punteggio,
        "profilo": profilo,
        "descrizione": descrizione,
        "allocazione": allocazione,
        "colore": colore
    }


def simula_portafoglio(azioni_perc: float, obblig_perc: float, oro_perc: float, 
                       capitale: float, anni: int) -> dict:
    """Simula l'andamento di un portafoglio con diversa asset allocation"""
    
    # Rendimenti storici medi approssimativi
    rend_azioni = 8.0
    rend_obblig = 3.5
    rend_oro = 2.5  # Rendimento storico reale dell'oro
    
    # Volatilità storica approssimativa
    vol_azioni = 18.0
    vol_obblig = 6.0
    vol_oro = 15.0
    
    # Calcolo rendimento e volatilità del portafoglio
    rendimento_portafoglio = (
        azioni_perc / 100 * rend_azioni +
        obblig_perc / 100 * rend_obblig +
        oro_perc / 100 * rend_oro
    )
    
    # Approssimazione semplificata della volatilità del portafoglio
    vol_portafoglio = (
        azioni_perc / 100 * vol_azioni +
        obblig_perc / 100 * vol_obblig +
        oro_perc / 100 * vol_oro
    )
    
    # Calcolo montante atteso
    montante = capitale * ((1 + rendimento_portafoglio / 100) ** anni)
    
    # Scenario pessimistico (rendimento - volatilità)
    rend_pessimistico = rendimento_portafoglio - vol_portafoglio
    montante_pessimistico = capitale * ((1 + rend_pessimistico / 100) ** anni)
    
    # Scenario ottimistico (rendimento + volatilità)
    rend_ottimistico = rendimento_portafoglio + vol_portafoglio
    montante_ottimistico = capitale * ((1 + rend_ottimistico / 100) ** anni)
    
    return {
        "rendimento_atteso": rendimento_portafoglio,
        "volatilita": vol_portafoglio,
        "montante_atteso": montante,
        "montante_pessimistico": montante_pessimistico,
        "montante_ottimistico": montante_ottimistico
    }


def render_contenuto():
    """Renderizza il contenuto teorico"""
    
    st.markdown("""
    ## Cos'è l'asset allocation
    
    L'asset allocation è la **distribuzione del capitale tra diverse classi di attivi** 
    (azioni, obbligazioni, oro, ecc.).
    
    > Numerosi studi dimostrano che l'asset allocation spiega la **maggior parte dei risultati** 
    > di un portafoglio nel lungo periodo, molto più della scelta dei singoli titoli.
    
    In altre parole: **non conta tanto cosa compri, ma come distribuisci il capitale**.
    """)
    
    st.markdown("---")
    
    st.markdown("## Perché l'asset allocation è così importante")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ✅ Una buona asset allocation:")
        st.markdown("""
        - Allinea il portafoglio ai tuoi obiettivi
        - Riduce il rischio di decisioni emotive
        - Rende i risultati più prevedibili
        - Aumenta la probabilità di successo
        """)
    
    with col2:
        st.markdown("### ❌ Un'allocazione sbagliata:")
        st.markdown("""
        - Espone a rischi eccessivi
        - Può essere tecnicamente valida ma psicologicamente ingestibile
        - Porta ad abbandonare il piano
        - Riduce i risultati di lungo periodo
        """)
    
    st.warning("""
    ⚠️ **Concetto chiave:**
    
    Un portafoglio sbilanciato può essere tecnicamente valido ma psicologicamente ingestibile.
    """)
    
    st.markdown("---")
    
    st.markdown("## I tre elementi che determinano l'asset allocation")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container(border=True):
            st.markdown("### ⏱️ Orizzonte Temporale")
            st.markdown("""
            Più è lungo, maggiore può essere l'esposizione al rischio.
            
            **Esempi:**
            - < 3 anni: prudente
            - 5-10 anni: bilanciato
            - 10+ anni: dinamico
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### 💪 Capacità di Rischio")
            st.markdown("""
            Dipende da:
            - Reddito
            - Stabilità lavorativa
            - Patrimonio esistente
            - Altre fonti di entrata
            """)
    
    with col3:
        with st.container(border=True):
            st.markdown("### 🧠 Tolleranza al Rischio")
            st.markdown("""
            Reazione emotiva alle perdite temporanee.
            
            **Domanda chiave:**
            Come reagiresti a una perdita del 20%?
            """)
    
    st.info("""
    💡 **Il portafoglio deve essere sostenibile sia finanziariamente che emotivamente.**
    """)
    
    st.markdown("---")
    
    st.markdown("## L'importanza dell'orizzonte temporale")
    
    st.markdown("""
    L'orizzonte temporale è probabilmente il fattore più importante nell'asset allocation, 
    più della tolleranza al rischio stessa.
    
    **Perché il tempo riduce il rischio:**
    - Permette di attraversare cicli di mercato completi
    - Consente all'interesse composto di lavorare
    - Aumenta drasticamente la probabilità di rendimenti positivi
    - Riduce l'impatto di decisioni emotive
    """)
    
    with st.container(border=True):
        st.markdown("### 📊 Probabilità storiche: il potere del tempo")
        
        st.markdown("""
        Le statistiche storiche (mercati sviluppati, 1926-2023) mostrano come 
        **l'orizzonte temporale trasformi il rischio**:
        
        **Portafoglio Bilanciato (60/40):**
        - A 1 anno: ~70% probabilità rendimento positivo
        - A 5 anni: ~88% probabilità rendimento positivo
        - A 10 anni: ~97% probabilità rendimento positivo
        - A 20 anni: ~100% probabilità rendimento positivo
        
        **Questo spiega perché:**
        - Orizzonti brevi (<7 anni) = Allocazioni conservative necessarie
        - Orizzonti medi (10 anni) = Spazio per portafogli bilanciati
        - Orizzonti lunghi (>10 anni) = Possibilità di allocazioni più aggressive
        """)
    
    st.success("""
    ✅ **Regola pratica:**
    
    Non guardare alla tua "tolleranza al rischio" emotiva, ma al tuo **orizzonte temporale reale**. 
    Un orizzonte lungo ti permette di accettare più volatilità perché le probabilità 
    di successo aumentano drasticamente.
    """)
    
    st.markdown("---")
    
    st.markdown("## Asset allocation strategica vs tattica")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 🎯 Asset Allocation Strategica")
            st.markdown("""
            Struttura di base del portafoglio, definita con visione di lungo periodo 
            in base a obiettivi, orizzonte e tolleranza al rischio.
            
            **Caratteristiche:**
            - Cambia raramente (solo se cambiano obiettivi o situazione personale)
            - Riflette i tuoi obiettivi principali
            - È la base della strategia di investimento
            - Indipendente dai movimenti di mercato
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### ⚡ Asset Allocation Tattica")
            st.markdown("""
            Aggiustamenti temporanei rispetto alla struttura strategica.
            
            **Caratteristiche:**
            - Orizzonte breve/medio
            - Basata su valutazioni macro
            - Maggiore complessità
            - Non adatta a tutti
            
            **Per la maggior parte degli investitori individuali, 
            l'approccio strategico è sufficiente.**
            """)
    
    st.markdown("---")
    
    st.markdown("## Esempi di asset allocation")
    
    tab1, tab2, tab3 = st.tabs(["Prudente", "Bilanciato", "Dinamico"])
    
    with tab1:
        st.markdown("### 🟢 Profilo Prudente (30/60/10)")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            **Allocazione:**
            - 30% Azioni
            - 60% Obbligazioni
            - 10% Oro
            
            **Adatto a:**
            - Orizzonte **minimo 7 anni**
            - Bassa tolleranza al rischio
            - Priorità alla stabilità
            - Chi non può permettersi volatilità elevata
            """)
        
        with col2:
            st.markdown("""
            **Caratteristiche:**
            - Volatilità contenuta (~8-10% annua)
            - Rendimento atteso moderato
            - Massima protezione del capitale
            - Drawdown massimi storici ~15-20%
            
            **Rendimento storico medio:** ~4-5% annuo
            """)
        
        st.markdown("---")
        st.markdown("#### 📊 Probabilità storiche di rendimenti positivi")
        
        stats_prudente = pd.DataFrame({
            "Orizzonte": ["5 anni", "10 anni", "20 anni"],
            "Prob. rendimento positivo": ["~85%", "~95%", "~99%"],
            "Range rendimenti tipici": ["2-7%", "3-6%", "3.5-5.5%"]
        })
        
        st.dataframe(stats_prudente, use_container_width=True, hide_index=True)
        
        st.info("""
        💡 Questo portafoglio ha storicamente generato rendimenti positivi in circa il 95% 
        dei periodi di 10 anni, rendendolo adatto a chi privilegia la stabilità.
        """)
    
    with tab2:
        st.markdown("### 🔵 Profilo Bilanciato (60/35/5)")
        st.caption("Equilibrio Rischio/Rendimento per investitori a lungo termine")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            **Allocazione:**
            - 60% Azioni
            - 35% Obbligazioni
            - 5% Oro
            
            **Adatto a:**
            - Orizzonte **minimo 10 anni**
            - Tolleranza media al rischio
            - Equilibrio crescita/stabilità
            - Piani pensione, risparmi per figli
            """)
        
        with col2:
            st.markdown("""
            **Caratteristiche:**
            - Volatilità moderata (~12-14% annua)
            - Rendimento atteso equilibrato
            - Buon bilanciamento rischio/rendimento
            - Drawdown massimi storici ~25-30%
            
            **Rendimento storico medio:** ~6-7% annuo
            """)
        
        st.markdown("---")
        st.markdown("#### 📊 Probabilità storiche di rendimenti positivi")
        
        stats_bilanciato = pd.DataFrame({
            "Orizzonte": ["5 anni", "10 anni", "20 anni"],
            "Prob. rendimento positivo": ["~88%", "~97%", "~100%"],
            "Range rendimenti tipici": ["3-10%", "4-9%", "5-8%"]
        })
        
        st.dataframe(stats_bilanciato, use_container_width=True, hide_index=True)
        
        st.success("""
        ✅ Questo portafoglio rappresenta un ottimo compromesso per chi investe a lungo termine:
        elevata probabilità di rendimenti positivi (~97% a 10 anni) con volatilità gestibile.
        Ideale per piani pensionistici e accumuli multi-decennali.
        """)
    
    with tab3:
        st.markdown("### 🔴 Profilo Dinamico (80/15/5)")
        st.caption("Massima crescita per orizzonti molto lunghi")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            **Allocazione:**
            - 80% Azioni
            - 15% Obbligazioni
            - 5% Oro
            
            **Adatto a:**
            - Orizzonte **superiore a 10 anni**
            - Alta tolleranza al rischio
            - Focus sulla crescita massima
            - Capitale completamente non necessario nel medio termine
            """)
        
        with col2:
            st.markdown("""
            **Caratteristiche:**
            - Volatilità elevata (~15-18% annua)
            - Rendimento atteso alto
            - Oscillazioni significative di breve termine
            - Drawdown massimi storici ~35-40%
            
            **Rendimento storico medio:** ~7-8% annuo
            """)
        
        st.markdown("---")
        st.markdown("#### 📊 Probabilità storiche di rendimenti positivi")
        
        stats_dinamico = pd.DataFrame({
            "Orizzonte": ["5 anni", "10 anni", "20 anni"],
            "Prob. rendimento positivo": ["~85%", "~95%", "~100%"],
            "Range rendimenti tipici": ["1-13%", "4-11%", "6-9%"]
        })
        
        st.dataframe(stats_dinamico, use_container_width=True, hide_index=True)
        
        st.warning("""
        ⚠️ **Attenzione:** Questo portafoglio richiede disciplina ferrea. 
        La volatilità elevata significa che periodi di perdite del 20-30% sono possibili 
        e normali. Solo per chi può davvero permettersi di NON toccare il capitale per 10+ anni 
        e ha la forza emotiva di attraversare ribassi significativi.
        """)
    
    st.info("""
    💡 **Importante:** Non esiste un'allocazione "migliore" in assoluto. 
    Esiste quella più adatta a te, ai tuoi obiettivi e alla tua situazione.
    """)
    
    st.markdown("---")
    
    st.markdown("## Il ruolo dell'oro nel portafoglio")
    
    st.markdown("""
    L'oro non genera reddito (come dividendi o cedole) ma ha caratteristiche uniche 
    come asset di diversificazione nel lungo periodo.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ✅ Funzioni principali")
        st.markdown("""
        - **Protezione dall'inflazione** di lungo periodo
        - **Decorrelazione** con azioni e obbligazioni
        - **Riserva di valore** in scenari di stress sistemico
        - **Diversificazione geografica** e valutaria implicita
        """)
    
    with col2:
        st.markdown("### ⚠️ Limiti da considerare")
        st.markdown("""
        - Non genera flussi di cassa
        - Volatilità significativa nel breve termine
        - Rendimento reale storicamente modesto
        - Può rimanere stagnante per lunghi periodi
        """)
    
    st.success("""
    ✅ **Utilizzo ottimale:**
    
    L'oro funziona bene come componente stabile del **5-10%** del portafoglio, 
    per ridurre la correlazione complessiva e fornire protezione in scenari estremi.
    """)
    
    st.markdown("---")
    
    st.markdown("## La liquidità: dove deve stare")
    
    with st.container(border=True):
        st.markdown("### ⚠️ IMPORTANTE: La liquidità NON fa parte del portafoglio di investimento")
        
        st.markdown("""
        La liquidità (conti correnti, conti deposito) serve per esigenze completamente diverse 
        dal portafoglio investito.
        
        **La liquidità serve per:**
        - 💰 Fondo emergenze (3-6 mesi di spese)
        - 📅 Spese programmate a breve termine (< 3 anni)
        - 🔧 Buffer operativo per imprevisti
        
        **Regola pratica:** La liquidità va tenuta **separata** dal portafoglio investito. 
        Non ha senso "allocare" liquidità in un portafoglio di lungo termine perché:
        - Erode valore reale nel tempo a causa dell'inflazione
        - Non contribuisce alla crescita patrimoniale
        - Ha funzioni operative, non di investimento
        """)
    
    st.error("""
    ❌ **Errore comune:**
    
    Includere il 5-10% di "liquidità" nel portafoglio investito è inefficiente. 
    Meglio aumentare leggermente l'oro o le obbligazioni brevi se si cerca stabilità.
    """)
    
    st.markdown("---")
    
    st.markdown("## Errori comuni nell'asset allocation")
    
    errori = [
        ("❌ Copiare portafogli altrui", "Non tiene conto di obiettivi e tolleranza personali"),
        ("❌ Sovrastimare la propria tolleranza", "Porta a vendere in panico durante i ribassi"),
        ("❌ Cambiare strategia nelle fasi negative", "Cristallizza le perdite e impedisce il recupero"),
        ("❌ Concentrarsi sui singoli strumenti", "Perdere di vista la visione d'insieme"),
        ("❌ Ignorare l'orizzonte temporale", "Allocazione troppo aggressiva o troppo conservativa"),
        ("❌ Non ribilanciare mai", "Il portafoglio si sbilancia nel tempo"),
        ("❌ Includere liquidità nel portafoglio", "La liquidità non è un asset di investimento")
    ]
    
    for errore, spiegazione in errori:
        with st.container(border=True):
            st.markdown(f"**{errore}**")
            st.caption(spiegazione)
    
    st.success("""
    ✅ **Regola d'oro:**
    
    La coerenza è più importante dell'ottimizzazione estrema.
    """)


def render_calcolatore():
    """Renderizza i calcolatori"""
    
    st.markdown("## 🧮 Calcolatori")
    
    calc_type = st.radio(
        "Seleziona calcolatore:",
        ["Profilo di Rischio", "Simulatore Asset Allocation", "Analizzatore Portafoglio"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if calc_type == "Profilo di Rischio":
        render_calc_profilo()
    elif calc_type == "Simulatore Asset Allocation":
        render_calc_simulatore()
    else:
        render_calc_analizzatore()


def render_calc_profilo():
    """Calcolatore profilo di rischio"""
    
    st.markdown("### Scopri il Tuo Profilo di Rischio")
    
    st.markdown("""
    Rispondi a queste domande per identificare il tuo profilo di investitore.
    """)
    
    domande = {}
    
    with st.container(border=True):
        st.markdown("**1. Qual è il tuo orizzonte temporale?**")
        domande['orizzonte'] = st.radio(
            "",
            ["Meno di 3 anni (1 pt)", "3-5 anni (3 pt)", "5-10 anni (5 pt)", "Oltre 10 anni (7 pt)"],
            key="cap10_orizzonte",
            label_visibility="collapsed"
        )
    
    with st.container(border=True):
        st.markdown("**2. Come reagiresti a una perdita del 20% in un anno?**")
        domande['reazione'] = st.radio(
            "",
            ["Venderei tutto (1 pt)", "Sarei molto preoccupato (3 pt)", 
             "Manterrei la posizione (5 pt)", "Comprerei di più (7 pt)"],
            key="cap10_reazione",
            label_visibility="collapsed"
        )
    
    with st.container(border=True):
        st.markdown("**3. Qual è la tua priorità principale?**")
        domande['priorita'] = st.radio(
            "",
            ["Preservare il capitale (1 pt)", "Reddito stabile (3 pt)", 
             "Crescita moderata (5 pt)", "Massima crescita (7 pt)"],
            key="cap10_priorita",
            label_visibility="collapsed"
        )
    
    with st.container(border=True):
        st.markdown("**4. Quanto è stabile il tuo reddito?**")
        domande['stabilita'] = st.radio(
            "",
            ["Molto instabile (1 pt)", "Variabile (3 pt)", 
             "Abbastanza stabile (5 pt)", "Molto stabile (7 pt)"],
            key="cap10_stabilita",
            label_visibility="collapsed"
        )
    
    # Estrai punteggi
    punteggi = {}
    for key, risposta in domande.items():
        punteggio = int(risposta.split('(')[1].split(' ')[0])
        punteggi[key] = punteggio
    
    if st.button("📊 Calcola Profilo", type="primary", use_container_width=True):
        risultato = calcola_profilo_rischio(punteggi)
        
        st.markdown("---")
        st.markdown("### 🎯 Il Tuo Profilo")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.metric("Punteggio", risultato['punteggio'])
            st.markdown(f"## {risultato['colore']} {risultato['profilo']}")
            st.caption(risultato['descrizione'])
        
        with col2:
            st.markdown("#### Asset Allocation Consigliata")
            
            df_alloc = pd.DataFrame({
                "Asset Class": list(risultato['allocazione'].keys()),
                "Percentuale": list(risultato['allocazione'].values())
            })
            
            st.dataframe(df_alloc, use_container_width=True, hide_index=True)
            
            # Grafico
            st.bar_chart(df_alloc.set_index("Asset Class"))
        
        st.info("""
        💡 **Ricorda:** Questo è solo un punto di partenza. 
        Considera anche altri fattori personali e consulta un professionista se necessario.
        
        **Importante:** La liquidità per emergenze va tenuta SEPARATA da questo portafoglio.
        """)


def render_calc_simulatore():
    """Simulatore asset allocation"""
    
    st.markdown("### Simulatore: Impatto dell'Asset Allocation")
    
    st.markdown("""
    Visualizza come diverse allocazioni influenzano rendimento atteso e volatilità.
    """)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        capitale = st.number_input(
            "💰 Capitale iniziale (€)",
            min_value=1000.0,
            value=10000.0,
            step=1000.0,
            key="cap10_sim_cap"
        )
        
        anni = st.slider(
            "📅 Orizzonte (anni)",
            min_value=1,
            max_value=30,
            value=15,
            key="cap10_sim_anni"
        )
        
        st.markdown("#### Composizione Portafoglio")
        
        azioni = st.slider(
            "📊 Azioni (%)",
            min_value=0,
            max_value=100,
            value=60,
            key="cap10_sim_azioni"
        )
        
        obbligazioni = st.slider(
            "📈 Obbligazioni (%)",
            min_value=0,
            max_value=100 - azioni,
            value=min(35, 100 - azioni),
            key="cap10_sim_obblig"
        )
        
        oro = 100 - azioni - obbligazioni
        
        st.metric("Oro (%)", oro)
    
    with col2:
        simulazione = simula_portafoglio(azioni, obbligazioni, oro, capitale, anni)
        
        st.markdown("### Risultati Simulazione")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.metric("Rendimento atteso", f"{simulazione['rendimento_atteso']:.2f}%")
            st.metric("Volatilità", f"{simulazione['volatilita']:.2f}%")
        
        with col_b:
            st.metric("Capitale atteso", f"€{simulazione['montante_atteso']:,.0f}")
            guadagno = simulazione['montante_atteso'] - capitale
            st.metric("Guadagno atteso", f"€{guadagno:,.0f}")
        
        st.markdown("---")
        st.markdown("#### 📊 Range di Risultati Possibili")
        
        col_pess, col_att, col_ott = st.columns(3)
        
        with col_pess:
            st.metric(
                "Scenario Pessimistico",
                f"€{simulazione['montante_pessimistico']:,.0f}",
                delta_color="off"
            )
        
        with col_att:
            st.metric(
                "Scenario Atteso",
                f"€{simulazione['montante_atteso']:,.0f}",
                delta_color="off"
            )
        
        with col_ott:
            st.metric(
                "Scenario Ottimistico",
                f"€{simulazione['montante_ottimistico']:,.0f}",
                delta_color="off"
            )
        
        # Interpretazione
        st.markdown("---")
        
        if azioni >= 70:
            st.warning("""
            ⚠️ **Portafoglio aggressivo (Dinamico)**: alta esposizione azionaria. 
            
            Richiede:
            - Orizzonte temporale **superiore a 10 anni**
            - Alta tolleranza al rischio
            - Capacità di sopportare drawdown del 30-40%
            """)
        elif azioni >= 50:
            st.success("""
            ✅ **Portafoglio bilanciato**: buon compromesso tra crescita e stabilità.
            
            Adatto per:
            - Orizzonte temporale **minimo 10 anni**
            - Tolleranza media al rischio
            - Piani pensione e accumuli di lungo termine
            """)
        elif azioni >= 25:
            st.info("""
            🔵 **Portafoglio conservativo (Prudente)**: priorità alla stabilità. 
            
            Caratteristiche:
            - Orizzonte temporale **minimo 7 anni**
            - Bassa tolleranza al rischio
            - Volatilità contenuta
            """)
        else:
            st.error("""
            🔴 **Portafoglio troppo conservativo**: rischio di non battere l'inflazione nel lungo periodo.
            
            Considera di aumentare leggermente la componente azionaria se l'orizzonte è superiore a 7 anni.
            """)


def render_calc_analizzatore():
    """Analizzatore portafoglio esistente"""
    
    st.markdown("### Analizza il Tuo Portafoglio Attuale")
    
    st.markdown("""
    Inserisci la composizione del tuo portafoglio per analizzarne il profilo di rischio.
    """)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Composizione Attuale")
        
        capitale_totale = st.number_input(
            "💰 Capitale totale (€)",
            min_value=100.0,
            value=10000.0,
            step=1000.0,
            key="cap10_anal_cap"
        )
        
        azioni_val = st.number_input(
            "📊 Azioni (€)",
            min_value=0.0,
            value=6000.0,
            step=100.0,
            key="cap10_anal_azioni"
        )
        
        obbligazioni_val = st.number_input(
            "📈 Obbligazioni (€)",
            min_value=0.0,
            value=3500.0,
            step=100.0,
            key="cap10_anal_obblig"
        )
        
        oro_val = st.number_input(
            "🟡 Oro (€)",
            min_value=0.0,
            value=500.0,
            step=100.0,
            key="cap10_anal_oro"
        )
        
        totale_inserito = azioni_val + obbligazioni_val + oro_val
    
    with col2:
        if abs(totale_inserito - capitale_totale) > 1:
            st.error(f"⚠️ Somma degli asset (€{totale_inserito:,.2f}) diversa dal capitale totale (€{capitale_totale:,.2f})")
        else:
            st.markdown("### Analisi Portafoglio")
            
            # Calcolo percentuali
            azioni_perc = (azioni_val / capitale_totale * 100) if capitale_totale > 0 else 0
            obblig_perc = (obbligazioni_val / capitale_totale * 100) if capitale_totale > 0 else 0
            oro_perc = (oro_val / capitale_totale * 100) if capitale_totale > 0 else 0
            
            # Tabella allocazione
            df_current = pd.DataFrame({
                "Asset Class": ["Azioni", "Obbligazioni", "Oro"],
                "Valore (€)": [azioni_val, obbligazioni_val, oro_val],
                "Percentuale": [f"{azioni_perc:.1f}%", f"{obblig_perc:.1f}%", f"{oro_perc:.1f}%"]
            })
            
            st.dataframe(df_current, use_container_width=True, hide_index=True)
            
            # Grafico
            chart_data = pd.DataFrame({
                "Valore": [azioni_val, obbligazioni_val, oro_val]
            }, index=["Azioni", "Obbligazioni", "Oro"])
            
            st.bar_chart(chart_data)
            
            # Classificazione profilo
            st.markdown("---")
            st.markdown("#### 🎯 Classificazione")
            
            if azioni_perc >= 70:
                st.error("""
                🔴 **Profilo Dinamico/Aggressivo**
                
                - Alta esposizione azionaria (≥70%)
                - Volatilità elevata (~15-18% annua)
                - Orizzonte richiesto: **superiore a 10 anni**
                - Drawdown attesi: 30-40%
                - Probabilità rendimento positivo a 10 anni: ~95%
                """)
            elif azioni_perc >= 50:
                st.info("""
                🔵 **Profilo Bilanciato**
                
                - Equilibrio rischio/rendimento
                - Volatilità moderata (~12-14% annua)
                - Orizzonte richiesto: **minimo 10 anni**
                - Drawdown attesi: 25-30%
                - Probabilità rendimento positivo a 10 anni: ~97%
                """)
            else:
                st.success("""
                🟢 **Profilo Prudente/Conservativo**
                
                - Priorità alla stabilità
                - Volatilità contenuta (~8-10% annua)
                - Orizzonte richiesto: **minimo 7 anni**
                - Drawdown attesi: 15-20%
                - Probabilità rendimento positivo a 10 anni: ~95%
                """)
            
            # Confronto con allocazioni standard
            st.markdown("---")
            st.markdown("#### 📊 Confronto con Profili Standard")
            
            df_confronto = pd.DataFrame({
                "Profilo": ["Tuo Portafoglio", "Prudente", "Bilanciato", "Dinamico"],
                "Azioni": [f"{azioni_perc:.0f}%", "30%", "60%", "80%"],
                "Obbligazioni": [f"{obblig_perc:.0f}%", "60%", "35%", "15%"],
                "Oro": [f"{oro_perc:.0f}%", "10%", "5%", "5%"]
            })
            
            st.dataframe(df_confronto, use_container_width=True, hide_index=True)


def render_quiz():
    """Renderizza il quiz di verifica"""
    
    st.markdown("## 📝 Quiz di verifica")
    
    if "cap10_risposte" not in st.session_state:
        st.session_state.cap10_risposte = {}
    if "cap10_verificato" not in st.session_state:
        st.session_state.cap10_verificato = False
    
    for i, q in enumerate(QUIZ):
        with st.container(border=True):
            st.markdown(f"**Domanda {i+1}:** {q['domanda']}")
            
            if q["tipo"] == "vero_falso":
                risposta = st.radio(
                    "Seleziona:",
                    ["Vero", "Falso"],
                    key=f"cap10_q{q['id']}",
                    horizontal=True
                )
                st.session_state.cap10_risposte[q['id']] = risposta == "Vero"
                
            elif q["tipo"] == "scelta_multipla":
                risposta = st.radio(
                    "Seleziona:",
                    q["opzioni"],
                    key=f"cap10_q{q['id']}"
                )
                st.session_state.cap10_risposte[q['id']] = risposta
            
            if st.session_state.cap10_verificato:
                user_ans = st.session_state.cap10_risposte.get(q['id'])
                corretto = user_ans == q["risposta_corretta"]
                
                if corretto:
                    st.success(f"✅ Corretto! {q['spiegazione']}")
                else:
                    st.error(f"❌ Sbagliato. Risposta corretta: {q['risposta_corretta']}")
                    st.info(q['spiegazione'])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Verifica risposte", type="primary", use_container_width=True, key="cap10_verifica"):
            st.session_state.cap10_verificato = True
            st.rerun()
    with col2:
        if st.button("🔄 Ricomincia", use_container_width=True, key="cap10_reset"):
            st.session_state.cap10_verificato = False
            st.session_state.cap10_risposte = {}
            st.rerun()


def render_takeaways():
    """Renderizza i punti chiave"""
    
    st.markdown("## 💡 Punti chiave")
    
    takeaways = [
        "L'asset allocation spiega la maggior parte dei risultati nel lungo periodo",
        "Non conta tanto cosa compri, ma come distribuisci il capitale",
        "Il portafoglio deve essere sostenibile sia finanziariamente che emotivamente",
        "L'allocazione dipende da tre elementi: orizzonte, capacità e tolleranza al rischio",
        "Orizzonte minimo: 7 anni per prudente, 10 anni per bilanciato, >10 anni per dinamico",
        "L'asset allocation strategica è la struttura di base, quella tattica prevede aggiustamenti temporanei",
        "Non esiste un'allocazione 'migliore' in assoluto, ma quella più adatta a te",
        "L'oro offre decorrelazione e protezione, ideale per il 5-10% del portafoglio",
        "La liquidità NON fa parte del portafoglio investito: serve per il fondo emergenze",
        "Le probabilità storiche di rendimenti positivi aumentano significativamente con l'orizzonte temporale",
        "La coerenza è più importante dell'ottimizzazione estrema"
    ]
    
    for t in takeaways:
        st.markdown(f"- {t}")
    
    st.markdown("---")
    
    # Esercizio pratico
    with st.expander("📝 Esercizio: Definisci la Tua Asset Allocation"):
        st.markdown("""
        Completa questo esercizio per definire la tua asset allocation target.
        
        **1. Analisi del profilo**
        
        - **Orizzonte temporale:** _____ anni
        - **Tolleranza a perdita del 20%:** ☐ Bassa ☐ Media ☐ Alta
        - **Stabilità del reddito:** ☐ Bassa ☐ Media ☐ Alta
        - **Obiettivo principale:** ☐ Stabilità ☐ Equilibrio ☐ Crescita
        
        **2. Definizione allocazione**
        
        Sulla base del profilo:
        
        - **Azioni:** _____% 
        - **Obbligazioni:** _____%
        - **Oro:** _____%
        - **Totale:** 100%
        
        **3. Liquidità separata**
        
        - **Fondo emergenze (fuori dal portafoglio):** €_____
        - **Obiettivo:** _____ mesi di spese
        
        **4. Regole di comportamento**
        
        Scrivi le tue regole:
        - Ribilancio ogni: _____________
        - In caso di ribasso del 20%, farò: _____________
        - Revisione strategia se: _____________
        
        **5. Commitment**
        
        "Mi impegno a seguire questa allocazione per almeno _____ anni, 
        modificandola solo se cambiano i miei obiettivi o la mia situazione personale, 
        non in base ai movimenti di mercato."
        
        Firma: _________________ Data: _________
        
        ---
        
        💡 *Conserva questo esercizio e rileggilo nei momenti di incertezza del mercato.*
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
