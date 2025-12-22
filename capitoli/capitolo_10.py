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
        "spiegazione": "L'asset allocation è la distribuzione strategica del capitale tra azioni, obbligazioni, liquidità e altri asset."
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
        "domanda": "Un portafoglio con 80% azioni e 20% obbligazioni è adatto a:",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Profilo prudente con orizzonte breve",
            "Profilo dinamico con orizzonte lungo",
            "Qualsiasi investitore",
            "Solo investitori professionali"
        ],
        "risposta_corretta": "Profilo dinamico con orizzonte lungo",
        "spiegazione": "Un'allocazione così aggressiva richiede alta tolleranza al rischio e orizzonte temporale lungo (10+ anni)."
    },
    {
        "id": 5,
        "domanda": "Copiare il portafoglio di altri investitori è sempre una buona strategia.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "Falso. Ogni investitore ha obiettivi, orizzonte e tolleranza al rischio diversi."
    }
]


def calcola_profilo_rischio(domande_risposte: dict) -> dict:
    """Calcola il profilo di rischio basato sulle risposte"""
    punteggio = sum(domande_risposte.values())
    
    if punteggio <= 10:
        profilo = "Prudente"
        descrizione = "Preferisci stabilità e hai bassa tolleranza alle oscillazioni"
        allocazione = {"Azioni": 30, "Obbligazioni": 60, "Liquidità": 10}
        colore = "🟢"
    elif punteggio <= 17:
        profilo = "Bilanciato"
        descrizione = "Cerchi equilibrio tra crescita e stabilità"
        allocazione = {"Azioni": 60, "Obbligazioni": 35, "Liquidità": 5}
        colore = "🔵"
    else:
        profilo = "Dinamico"
        descrizione = "Punti alla crescita di lungo periodo e accetti volatilità"
        allocazione = {"Azioni": 80, "Obbligazioni": 15, "Liquidità": 5}
        colore = "🔴"
    
    return {
        "punteggio": punteggio,
        "profilo": profilo,
        "descrizione": descrizione,
        "allocazione": allocazione,
        "colore": colore
    }


def simula_portafoglio(azioni_perc: float, obblig_perc: float, liquid_perc: float, 
                       capitale: float, anni: int) -> dict:
    """Simula l'andamento di un portafoglio con diversa asset allocation"""
    
    # Rendimenti storici medi approssimativi
    rend_azioni = 8.0
    rend_obblig = 3.5
    rend_liquid = 1.5
    
    # Volatilità storica approssimativa
    vol_azioni = 18.0
    vol_obblig = 6.0
    vol_liquid = 0.5
    
    # Calcolo rendimento e volatilità del portafoglio
    rendimento_portafoglio = (
        azioni_perc / 100 * rend_azioni +
        obblig_perc / 100 * rend_obblig +
        liquid_perc / 100 * rend_liquid
    )
    
    # Approssimazione semplificata della volatilità del portafoglio
    vol_portafoglio = (
        azioni_perc / 100 * vol_azioni +
        obblig_perc / 100 * vol_obblig +
        liquid_perc / 100 * vol_liquid
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
    (azioni, obbligazioni, liquidità, ecc.).
    
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
    
    st.markdown("## Asset allocation strategica vs tattica")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 🎯 Asset Allocation Strategica")
            st.markdown("""
            Struttura di base del portafoglio, definita con visione di lungo periodo.
            
            **Esempio:**
            - 70% azioni
            - 25% obbligazioni
            - 5% liquidità
            
            **Caratteristiche:**
            - Cambia raramente
            - Riflette obiettivi principali
            - Base della strategia
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
        st.markdown("### 🟢 Profilo Prudente")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            **Allocazione:**
            - 30% Azioni
            - 60% Obbligazioni
            - 10% Liquidità
            
            **Adatto a:**
            - Orizzonte < 5 anni
            - Bassa tolleranza al rischio
            - Bisogno di stabilità
            - Capitale che potrebbe servire
            """)
        
        with col2:
            st.markdown("""
            **Caratteristiche:**
            - Volatilità contenuta
            - Rendimento atteso moderato
            - Protezione del capitale
            - Poche oscillazioni
            
            **Rendimento storico:** ~3-4% annuo
            """)
    
    with tab2:
        st.markdown("### 🔵 Profilo Bilanciato")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            **Allocazione:**
            - 60% Azioni
            - 35% Obbligazioni
            - 5% Liquidità
            
            **Adatto a:**
            - Orizzonte 5-10 anni
            - Tolleranza media al rischio
            - Equilibrio crescita/stabilità
            - Obiettivi di medio periodo
            """)
        
        with col2:
            st.markdown("""
            **Caratteristiche:**
            - Volatilità moderata
            - Rendimento atteso equilibrato
            - Bilanciamento rischio/rendimento
            - Compromesso ragionevole
            
            **Rendimento storico:** ~5-6% annuo
            """)
    
    with tab3:
        st.markdown("### 🔴 Profilo Dinamico")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            **Allocazione:**
            - 80% Azioni
            - 15% Obbligazioni
            - 5% Liquidità
            
            **Adatto a:**
            - Orizzonte 10+ anni
            - Alta tolleranza al rischio
            - Focus sulla crescita
            - Capitale non necessario
            """)
        
        with col2:
            st.markdown("""
            **Caratteristiche:**
            - Volatilità elevata
            - Rendimento atteso alto
            - Oscillazioni significative
            - Richiede disciplina
            
            **Rendimento storico:** ~7-8% annuo
            """)
    
    st.info("""
    💡 **Importante:** Non esiste un'allocazione "migliore" in assoluto. 
    Esiste quella più adatta a te, ai tuoi obiettivi e alla tua situazione.
    """)
    
    st.markdown("---")
    
    st.markdown("## Il ruolo della liquidità nel portafoglio")
    
    st.markdown("""
    La liquidità (conti deposito, money market, ecc.) ha funzioni specifiche:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ✅ Vantaggi")
        st.markdown("""
        - Riduce la volatilità complessiva
        - Permette di cogliere opportunità
        - Copre esigenze di breve termine
        - Dà stabilità psicologica
        """)
    
    with col2:
        st.markdown("### ⚠️ Limiti")
        st.markdown("""
        - Rendimento molto basso
        - Può non battere l'inflazione
        - Troppa liquidità riduce la crescita
        - Costo opportunità elevato
        """)
    
    st.markdown("---")
    
    st.markdown("## Errori comuni nell'asset allocation")
    
    errori = [
        ("❌ Copiare portafogli altrui", "Non tiene conto di obiettivi e tolleranza personali"),
        ("❌ Sovrastimare la propria tolleranza", "Porta a vendere in panico durante i ribassi"),
        ("❌ Cambiare strategia nelle fasi negative", "Cristallizza le perdite e impedisce il recupero"),
        ("❌ Concentrarsi sui singoli strumenti", "Perdere di vista la visione d'insieme"),
        ("❌ Ignorare l'orizzonte temporale", "Allocazione troppo aggressiva o troppo conservativa"),
        ("❌ Non ribilanciare mai", "Il portafoglio si sbilancia nel tempo")
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
        
        liquidita = 100 - azioni - obbligazioni
        
        st.metric("Liquidità (%)", liquidita)
    
    with col2:
        simulazione = simula_portafoglio(azioni, obbligazioni, liquidita, capitale, anni)
        
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
            ⚠️ **Portafoglio aggressivo**: alta esposizione azionaria. 
            Richiede orizzonte lungo (10+ anni) e alta tolleranza al rischio.
            """)
        elif azioni <= 40:
            st.info("""
            🔵 **Portafoglio conservativo**: priorità alla stabilità. 
            Adatto per orizzonti brevi o bassa tolleranza al rischio.
            """)
        else:
            st.success("""
            ✅ **Portafoglio bilanciato**: buon compromesso tra crescita e stabilità.
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
        
        liquidita_val = st.number_input(
            "💵 Liquidità (€)",
            min_value=0.0,
            value=500.0,
            step=100.0,
            key="cap10_anal_liquid"
        )
        
        totale_inserito = azioni_val + obbligazioni_val + liquidita_val
    
    with col2:
        if abs(totale_inserito - capitale_totale) > 1:
            st.error(f"⚠️ Somma degli asset (€{totale_inserito:,.2f}) diversa dal capitale totale (€{capitale_totale:,.2f})")
        else:
            st.markdown("### Analisi Portafoglio")
            
            # Calcolo percentuali
            azioni_perc = (azioni_val / capitale_totale * 100) if capitale_totale > 0 else 0
            obblig_perc = (obbligazioni_val / capitale_totale * 100) if capitale_totale > 0 else 0
            liquid_perc = (liquidita_val / capitale_totale * 100) if capitale_totale > 0 else 0
            
            # Tabella allocazione
            df_current = pd.DataFrame({
                "Asset Class": ["Azioni", "Obbligazioni", "Liquidità"],
                "Valore (€)": [azioni_val, obbligazioni_val, liquidita_val],
                "Percentuale": [f"{azioni_perc:.1f}%", f"{obblig_perc:.1f}%", f"{liquid_perc:.1f}%"]
            })
            
            st.dataframe(df_current, use_container_width=True, hide_index=True)
            
            # Grafico
            chart_data = pd.DataFrame({
                "Valore": [azioni_val, obbligazioni_val, liquidita_val]
            }, index=["Azioni", "Obbligazioni", "Liquidità"])
            
            st.bar_chart(chart_data)
            
            # Classificazione profilo
            st.markdown("---")
            st.markdown("#### 🎯 Classificazione")
            
            if azioni_perc >= 70:
                st.error("""
                🔴 **Profilo Dinamico/Aggressivo**
                
                - Alta esposizione azionaria
                - Volatilità elevata
                - Adatto per orizzonti lunghi (10+ anni)
                """)
            elif azioni_perc >= 50:
                st.info("""
                🔵 **Profilo Bilanciato**
                
                - Buon equilibrio rischio/rendimento
                - Volatilità moderata
                - Adatto per orizzonti medi (5-10 anni)
                """)
            else:
                st.success("""
                🟢 **Profilo Prudente/Conservativo**
                
                - Priorità alla stabilità
                - Volatilità contenuta
                - Adatto per orizzonti brevi (< 5 anni)
                """)
            
            # Confronto con allocazioni standard
            st.markdown("---")
            st.markdown("#### 📊 Confronto con Profili Standard")
            
            df_confronto = pd.DataFrame({
                "Profilo": ["Tuo Portafoglio", "Prudente", "Bilanciato", "Dinamico"],
                "Azioni": [f"{azioni_perc:.0f}%", "30%", "60%", "80%"],
                "Obbligazioni": [f"{obblig_perc:.0f}%", "60%", "35%", "15%"],
                "Liquidità": [f"{liquid_perc:.0f}%", "10%", "5%", "5%"]
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
        "L'asset allocation strategica è la struttura di base, quella tattica prevede aggiustamenti temporanei",
        "Non esiste un'allocazione 'migliore' in assoluto, ma quella più adatta a te",
        "La coerenza è più importante dell'ottimizzazione estrema",
        "Copiare portafogli altrui senza considerare il proprio profilo è un errore"
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
        - **Liquidità:** _____%
        - **Totale:** 100%
        
        **3. Regole di comportamento**
        
        Scrivi le tue regole:
        - Ribilancio ogni: _____________
        - In caso di ribasso del 20%, farò: _____________
        - Revisione strategia se: _____________
        
        **4. Commitment**
        
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
