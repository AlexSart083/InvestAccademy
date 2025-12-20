"""
Capitolo 6: Gestione del debito: strategie e priorità
InvestAccademy - Corso di Finanza Personale
"""

import streamlit as st
import pandas as pd

# Metadata
CAPITOLO_NUM = 6
TITOLO = "Gestione del debito: strategie e priorità"

OBIETTIVI = [
    "Distinguere tra debito 'buono' e debito 'cattivo'",
    "Classificare i debiti in base a tasso, importo e priorità",
    "Applicare le strategie di rimborso snowball e avalanche",
    "Valutare quando conviene rinegoziare o consolidare un debito",
    "Costruire un piano di rimborso sostenibile nel tempo"
]

# Quiz
QUIZ = [
    {
        "id": 1,
        "domanda": "Quale strategia riduce il costo totale degli interessi?",
        "tipo": "scelta_multipla",
        "opzioni": ["Snowball", "Avalanche", "Entrambe allo stesso modo", "Nessuna delle due"],
        "risposta_corretta": "Avalanche",
        "spiegazione": "La strategia Avalanche concentra i pagamenti sul debito con il tasso più alto, riducendo il costo totale degli interessi."
    },
    {
        "id": 2,
        "domanda": "Quando conviene consolidare un debito?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Sempre",
            "Mai",
            "Quando il nuovo tasso e i costi complessivi sono inferiori",
            "Solo se si allunga la durata"
        ],
        "risposta_corretta": "Quando il nuovo tasso e i costi complessivi sono inferiori",
        "spiegazione": "Il consolidamento è utile solo se effettivamente riduce il costo totale del debito, considerando tasso e spese."
    },
    {
        "id": 3,
        "domanda": "Allungare la durata di un prestito riduce sempre il costo totale.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "Falso. Rate più basse non significano sempre costo minore: allungare troppo il piano può aumentare gli interessi totali pagati."
    },
    {
        "id": 4,
        "domanda": "La strategia Snowball privilegia prima:",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Il debito con il tasso più alto",
            "Il debito più grande",
            "Il debito più piccolo",
            "Il debito più vecchio"
        ],
        "risposta_corretta": "Il debito più piccolo",
        "spiegazione": "La Snowball si concentra sul debito più piccolo per ottenere vittorie psicologiche rapide."
    },
    {
        "id": 5,
        "domanda": "È corretto accumulare nuovo debito mentre si rimborsa quello esistente.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "Accumulare nuovo debito mentre si rimborsa quello esistente vanifica gli sforzi e peggiora la situazione complessiva."
    }
]


def calcola_interessi_totali(saldo: float, tasso: float, rata_mensile: float) -> dict:
    """Calcola il piano di ammortamento di un debito"""
    
    if rata_mensile <= 0 or saldo <= 0:
        return {"mesi": 0, "interessi_totali": 0, "costo_totale": saldo}
    
    tasso_mensile = tasso / 100 / 12
    
    # Verifica che la rata sia sufficiente a coprire gli interessi
    interesse_minimo = saldo * tasso_mensile
    if rata_mensile <= interesse_minimo:
        return {"mesi": 999, "interessi_totali": 999999, "costo_totale": 999999}
    
    saldo_residuo = saldo
    mesi = 0
    interessi_totali = 0
    piano = []
    
    while saldo_residuo > 0 and mesi < 600:  # Max 50 anni
        interesse_mese = saldo_residuo * tasso_mensile
        quota_capitale = min(rata_mensile - interesse_mese, saldo_residuo)
        
        if quota_capitale <= 0:
            break
        
        saldo_residuo -= quota_capitale
        interessi_totali += interesse_mese
        mesi += 1
        
        piano.append({
            "mese": mesi,
            "saldo_iniziale": saldo_residuo + quota_capitale,
            "interesse": interesse_mese,
            "quota_capitale": quota_capitale,
            "rata": min(rata_mensile, interesse_mese + quota_capitale),
            "saldo_finale": saldo_residuo
        })
        
        if saldo_residuo < 0.01:  # Tolleranza
            break
    
    return {
        "mesi": mesi,
        "interessi_totali": interessi_totali,
        "costo_totale": saldo + interessi_totali,
        "piano": piano
    }


def confronta_strategie(debiti: list, risorse_extra: float) -> dict:
    """Confronta le strategie Snowball e Avalanche"""
    
    # Snowball: ordina per saldo crescente
    debiti_snowball = sorted(debiti, key=lambda x: x['saldo'])
    
    # Avalanche: ordina per tasso decrescente
    debiti_avalanche = sorted(debiti, key=lambda x: x['tasso'], reverse=True)
    
    return {
        "snowball": debiti_snowball,
        "avalanche": debiti_avalanche
    }


def render_contenuto():
    """Renderizza il contenuto teorico"""
    
    st.markdown("""
    ## Il ruolo del debito nella finanza personale
    
    Il debito è uno **strumento**: può accelerare il raggiungimento di obiettivi importanti 
    oppure diventare un freno significativo alla stabilità finanziaria.
    
    La differenza non sta solo nell'importo, ma nel:
    - **Costo** (tasso di interesse)
    - **Durata** (tempo di rimborso)
    - **Scopo** (per cosa è stato contratto)
    
    > Gestire correttamente il debito significa ridurre interessi inutili, liberare cash flow 
    > e aumentare la capacità di risparmio e investimento.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Debito "buono" e debito "cattivo"
    
    Una distinzione pratica (non assoluta):
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### ✅ Debito generalmente 'buono'")
            st.markdown("""
            - Mutuo per abitazione sostenibile
            - Prestiti per formazione con ritorno economico
            - Debito a tasso basso e con piano chiaro
            
            **Caratteristiche:**
            - Tasso contenuto
            - Finalità produttiva o di lungo periodo
            - Piano di rimborso sostenibile
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### ❌ Debito generalmente 'cattivo'")
            st.markdown("""
            - Carte di credito revolving
            - Prestiti ad alto tasso
            - Debiti usati per consumi non essenziali
            
            **Caratteristiche:**
            - Tasso elevato (>10%)
            - Finalità di consumo immediato
            - Rischio di accumulo
            """)
    
    st.warning("""
    ⚠️ **La priorità va sempre data ai debiti ad alto tasso**, 
    indipendentemente dall'importo.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Mappare i debiti: il primo passo
    
    Prima di qualsiasi strategia è necessario avere una **visione completa**.
    
    Crea una lista con:
    - Tipo di debito
    - Saldo residuo
    - Tasso di interesse
    - Rata minima
    - Scadenza
    
    > Senza questa mappa è impossibile prendere decisioni razionali.
    """)
    
    st.markdown("---")
    
    st.markdown("## Le due strategie principali di rimborso")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 🏔️ Strategia Snowball")
            st.markdown("""
            **Metodo:**
            1. Paga il minimo su tutti i debiti
            2. Concentra le risorse extra sul **debito più piccolo**
            3. Una volta estinto, passa al successivo
            
            **Vantaggio:** Forte motivazione psicologica
            
            **Svantaggio:** Non sempre minimizza gli interessi totali
            
            **Adatta a:** Chi ha bisogno di vittorie rapide
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### ⛰️ Strategia Avalanche")
            st.markdown("""
            **Metodo:**
            1. Paga il minimo su tutti i debiti
            2. Concentra le risorse extra sul **debito con tasso più alto**
            3. Procedi in ordine decrescente di tasso
            
            **Vantaggio:** Riduce il costo totale degli interessi
            
            **Svantaggio:** Risultati psicologici meno immediati
            
            **Adatta a:** Chi vuole ottimizzare matematicamente
            """)
    
    st.info("""
    💡 **Dal punto di vista matematico**, l'Avalanche è la strategia più efficiente.
    
    Tuttavia, la Snowball può essere preferibile se la motivazione psicologica è fondamentale 
    per mantenere la disciplina.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Consolidamento e rinegoziazione
    
    Il **consolidamento** unisce più debiti in uno solo.
    
    ### Può essere utile solo se:
    - Il nuovo tasso è inferiore
    - I costi accessori sono contenuti
    - La durata non aumenta eccessivamente il costo totale
    
    ### La rinegoziazione può:
    - Ridurre il tasso
    - Allungare la durata
    
    **Attenzione:**
    - Rate più basse ≠ costo minore
    - Allungare troppo il piano può aumentare gli interessi totali
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## Errori comuni da evitare
    """)
    
    errori = [
        ("❌ Ignorare i tassi di interesse", "Concentrarsi solo sull'importo è un errore costoso"),
        ("❌ Pagare solo il minimo per lunghi periodi", "Gli interessi si accumulano esponenzialmente"),
        ("❌ Estinguere investimenti per coprire debiti senza analisi", "Valuta prima il costo opportunità"),
        ("❌ Accumulare nuovo debito mentre si rimborsa quello esistente", "Vanifica tutti gli sforzi")
    ]
    
    for errore, spiegazione in errori:
        with st.container(border=True):
            st.markdown(f"**{errore}**")
            st.caption(spiegazione)
    
    st.warning("⚠️ La disciplina è parte integrante della strategia.")


def render_calcolatore():
    """Renderizza i calcolatori"""
    
    st.markdown("## 🧮 Calcolatori")
    
    calc_type = st.radio(
        "Seleziona calcolatore:",
        ["Piano di rimborso", "Confronto Snowball vs Avalanche", "Simulatore consolidamento"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if calc_type == "Piano di rimborso":
        render_calc_piano()
    elif calc_type == "Confronto Snowball vs Avalanche":
        render_calc_strategie()
    else:
        render_calc_consolidamento()


def render_calc_piano():
    """Calcolatore piano di rimborso"""
    
    st.markdown("### Piano di Rimborso Debito")
    
    col1, col2 = st.columns(2)
    
    with col1:
        saldo = st.number_input(
            "💳 Saldo debito (€)",
            min_value=100.0,
            value=5000.0,
            step=100.0,
            key="cap6_saldo"
        )
        
        tasso = st.slider(
            "📊 Tasso annuo (%)",
            min_value=0.5,
            max_value=25.0,
            value=12.0,
            step=0.5,
            key="cap6_tasso"
        )
        
        rata = st.number_input(
            "💵 Rata mensile (€)",
            min_value=10.0,
            value=200.0,
            step=10.0,
            key="cap6_rata"
        )
    
    with col2:
        risultato = calcola_interessi_totali(saldo, tasso, rata)
        
        st.markdown("### Risultati")
        
        if risultato['mesi'] < 600:
            anni = risultato['mesi'] // 12
            mesi = risultato['mesi'] % 12
            
            c1, c2 = st.columns(2)
            with c1:
                if anni > 0:
                    st.metric("Durata", f"{anni}a {mesi}m")
                else:
                    st.metric("Durata", f"{mesi} mesi")
            
            with c2:
                st.metric("Interessi totali", f"€{risultato['interessi_totali']:,.2f}")
            
            st.metric("Costo totale", f"€{risultato['costo_totale']:,.2f}")
            
            # Percentuale interessi
            perc_interessi = (risultato['interessi_totali'] / saldo * 100) if saldo > 0 else 0
            
            if perc_interessi > 50:
                st.error(f"🔴 Gli interessi sono il {perc_interessi:.1f}% del capitale!")
            elif perc_interessi > 25:
                st.warning(f"⚠️ Gli interessi sono il {perc_interessi:.1f}% del capitale")
            else:
                st.success(f"✅ Gli interessi sono il {perc_interessi:.1f}% del capitale")
            
        else:
            st.error("❌ Rata insufficiente o durata eccessiva")
            interesse_minimo = saldo * (tasso / 100 / 12)
            st.warning(f"La rata deve essere almeno €{interesse_minimo:.2f} per coprire gli interessi")
    
    # Simulazione aumento rata
    if risultato['mesi'] < 600:
        st.markdown("---")
        st.markdown("### 💡 Cosa succede se aumento la rata?")
        
        aumento = st.slider(
            "Aumento rata mensile (€)",
            min_value=0,
            max_value=500,
            value=50,
            step=10,
            key="cap6_aumento"
        )
        
        if aumento > 0:
            nuova_rata = rata + aumento
            nuovo_risultato = calcola_interessi_totali(saldo, tasso, nuova_rata)
            
            if nuovo_risultato['mesi'] < 600:
                risparmio_mesi = risultato['mesi'] - nuovo_risultato['mesi']
                risparmio_interessi = risultato['interessi_totali'] - nuovo_risultato['interessi_totali']
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Mesi risparmiati", risparmio_mesi, delta=f"-{risparmio_mesi}")
                with col2:
                    st.metric("Interessi risparmiati", f"€{risparmio_interessi:,.2f}", delta=f"-€{risparmio_interessi:,.2f}")


def render_calc_strategie():
    """Confronto strategie Snowball vs Avalanche"""
    
    st.markdown("### Confronto Strategie: Snowball vs Avalanche")
    
    st.markdown("""
    Inserisci i tuoi debiti per vedere quale strategia conviene di più.
    """)
    
    # Inizializza session state per i debiti
    if "cap6_debiti" not in st.session_state:
        st.session_state.cap6_debiti = [
            {"nome": "Carta credito", "saldo": 3000, "tasso": 18, "rata_min": 90},
            {"nome": "Prestito personale", "saldo": 8000, "tasso": 10, "rata_min": 200},
            {"nome": "Finanziamento auto", "saldo": 12000, "tasso": 6, "rata_min": 300}
        ]
    
    # Input debiti
    st.markdown("#### 📋 I tuoi debiti")
    
    for i, debito in enumerate(st.session_state.cap6_debiti):
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
        
        with col1:
            debito['nome'] = st.text_input(f"Nome debito {i+1}", value=debito['nome'], key=f"cap6_nome_{i}")
        with col2:
            debito['saldo'] = st.number_input(f"Saldo", value=float(debito['saldo']), min_value=0.0, step=100.0, key=f"cap6_sal_{i}")
        with col3:
            debito['tasso'] = st.number_input(f"Tasso %", value=float(debito['tasso']), min_value=0.0, max_value=30.0, step=0.5, key=f"cap6_tas_{i}")
        with col4:
            debito['rata_min'] = st.number_input(f"Rata min", value=float(debito['rata_min']), min_value=0.0, step=10.0, key=f"cap6_rat_{i}")
    
    risorse_extra = st.number_input(
        "💰 Risorse extra mensili disponibili (€)",
        min_value=0.0,
        value=300.0,
        step=50.0,
        key="cap6_extra"
    )
    
    st.markdown("---")
    
    # Calcolo strategie
    strategie = confronta_strategie(st.session_state.cap6_debiti, risorse_extra)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏔️ Strategia Snowball")
        st.caption("(dal più piccolo al più grande)")
        
        for i, debito in enumerate(strategie['snowball']):
            priorita = i + 1
            emoji = "🎯" if priorita == 1 else f"{priorita}️⃣"
            st.markdown(f"{emoji} **{debito['nome']}**")
            st.caption(f"€{debito['saldo']:,.0f} al {debito['tasso']}%")
    
    with col2:
        st.markdown("### ⛰️ Strategia Avalanche")
        st.caption("(dal tasso più alto al più basso)")
        
        for i, debito in enumerate(strategie['avalanche']):
            priorita = i + 1
            emoji = "🎯" if priorita == 1 else f"{priorita}️⃣"
            st.markdown(f"{emoji} **{debito['nome']}**")
            st.caption(f"€{debito['saldo']:,.0f} al {debito['tasso']}%")
    
    st.markdown("---")
    
    st.info("""
    💡 **Quale scegliere?**
    
    - **Snowball**: se hai bisogno di motivazione psicologica con vittorie rapide
    - **Avalanche**: se vuoi minimizzare il costo totale degli interessi
    
    In generale, l'Avalanche è matematicamente più efficiente, ma la Snowball può essere 
    migliore se ti aiuta a mantenere la disciplina.
    """)


def render_calc_consolidamento():
    """Simulatore consolidamento debiti"""
    
    st.markdown("### Simulatore Consolidamento Debiti")
    
    st.markdown("""
    Valuta se consolidare più debiti in uno solo conviene davvero.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📊 Situazione attuale")
        
        debito1_saldo = st.number_input("Debito 1 - Saldo (€)", min_value=0.0, value=5000.0, step=100.0, key="cap6_cons_d1s")
        debito1_tasso = st.number_input("Debito 1 - Tasso %", min_value=0.0, value=15.0, step=0.5, key="cap6_cons_d1t")
        debito1_rata = st.number_input("Debito 1 - Rata (€)", min_value=0.0, value=150.0, step=10.0, key="cap6_cons_d1r")
        
        debito2_saldo = st.number_input("Debito 2 - Saldo (€)", min_value=0.0, value=3000.0, step=100.0, key="cap6_cons_d2s")
        debito2_tasso = st.number_input("Debito 2 - Tasso %", min_value=0.0, value=12.0, step=0.5, key="cap6_cons_d2t")
        debito2_rata = st.number_input("Debito 2 - Rata (€)", min_value=0.0, value=100.0, step=10.0, key="cap6_cons_d2r")
        
        saldo_totale = debito1_saldo + debito2_saldo
        rata_totale = debito1_rata + debito2_rata
        
        # Calcola costi attuali
        risultato1 = calcola_interessi_totali(debito1_saldo, debito1_tasso, debito1_rata)
        risultato2 = calcola_interessi_totali(debito2_saldo, debito2_tasso, debito2_rata)
        
        interessi_attuali = risultato1['interessi_totali'] + risultato2['interessi_totali']
        costo_totale_attuale = risultato1['costo_totale'] + risultato2['costo_totale']
        
        st.metric("Saldo totale", f"€{saldo_totale:,.2f}")
        st.metric("Rata totale mensile", f"€{rata_totale:,.2f}")
        st.metric("Interessi totali attuali", f"€{interessi_attuali:,.2f}")
    
    with col2:
        st.markdown("#### 🔄 Proposta consolidamento")
        
        nuovo_tasso = st.number_input("Nuovo tasso consolidato %", min_value=0.0, value=9.0, step=0.5, key="cap6_cons_nt")
        nuova_rata = st.number_input("Nuova rata mensile (€)", min_value=0.0, value=250.0, step=10.0, key="cap6_cons_nr")
        spese_pratica = st.number_input("Spese di istruttoria (€)", min_value=0.0, value=200.0, step=50.0, key="cap6_cons_sp")
        
        # Calcola nuovo piano
        nuovo_saldo = saldo_totale + spese_pratica
        nuovo_risultato = calcola_interessi_totali(nuovo_saldo, nuovo_tasso, nuova_rata)
        
        st.metric("Nuovo saldo (con spese)", f"€{nuovo_saldo:,.2f}")
        st.metric("Nuova rata mensile", f"€{nuova_rata:,.2f}")
        st.metric("Interessi totali nuovi", f"€{nuovo_risultato['interessi_totali']:,.2f}")
    
    st.markdown("---")
    
    st.markdown("### 📊 Confronto")
    
    risparmio_interessi = interessi_attuali - nuovo_risultato['interessi_totali']
    risparmio_rata = rata_totale - nuova_rata
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if risparmio_interessi > 0:
            st.metric("Risparmio interessi", f"€{risparmio_interessi:,.2f}", delta=f"-€{risparmio_interessi:,.2f}")
        else:
            st.metric("Costo aggiuntivo", f"€{abs(risparmio_interessi):,.2f}", delta=f"+€{abs(risparmio_interessi):,.2f}", delta_color="inverse")
    
    with col2:
        if risparmio_rata > 0:
            st.metric("Risparmio rata mensile", f"€{risparmio_rata:,.2f}", delta=f"-€{risparmio_rata:,.2f}")
        else:
            st.metric("Aumento rata", f"€{abs(risparmio_rata):,.2f}", delta=f"+€{abs(risparmio_rata):,.2f}", delta_color="inverse")
    
    with col3:
        if nuovo_risultato['mesi'] < 600:
            durata_nuova = nuovo_risultato['mesi']
            durata_media_attuale = (risultato1['mesi'] + risultato2['mesi']) / 2
            diff_mesi = durata_media_attuale - durata_nuova
            
            if diff_mesi > 0:
                st.metric("Mesi risparmiati", int(diff_mesi), delta=f"-{int(diff_mesi)}")
            else:
                st.metric("Mesi aggiuntivi", int(abs(diff_mesi)), delta=f"+{int(abs(diff_mesi))}", delta_color="inverse")
    
    # Verdetto
    st.markdown("---")
    
    if risparmio_interessi > spese_pratica and nuovo_tasso < max(debito1_tasso, debito2_tasso):
        st.success(f"✅ Il consolidamento conviene! Risparmio netto: €{risparmio_interessi - spese_pratica:,.2f}")
    elif risparmio_interessi > 0:
        st.info(f"⚠️ Risparmio modesto: €{risparmio_interessi:,.2f}. Valuta bene i pro e contro.")
    else:
        st.error("❌ Il consolidamento non conviene. Costeresti di più in interessi.")


def render_quiz():
    """Renderizza il quiz di verifica"""
    
    st.markdown("## 📝 Quiz di verifica")
    
    if "cap6_risposte" not in st.session_state:
        st.session_state.cap6_risposte = {}
    if "cap6_verificato" not in st.session_state:
        st.session_state.cap6_verificato = False
    
    for i, q in enumerate(QUIZ):
        with st.container(border=True):
            st.markdown(f"**Domanda {i+1}:** {q['domanda']}")
            
            if q["tipo"] == "vero_falso":
                risposta = st.radio(
                    "Seleziona:",
                    ["Vero", "Falso"],
                    key=f"cap6_q{q['id']}",
                    horizontal=True
                )
                st.session_state.cap6_risposte[q['id']] = risposta == "Vero"
                
            elif q["tipo"] == "scelta_multipla":
                risposta = st.radio(
                    "Seleziona:",
                    q["opzioni"],
                    key=f"cap6_q{q['id']}"
                )
                st.session_state.cap6_risposte[q['id']] = risposta
            
            if st.session_state.cap6_verificato:
                user_ans = st.session_state.cap6_risposte.get(q['id'])
                corretto = user_ans == q["risposta_corretta"]
                
                if corretto:
                    st.success(f"✅ Corretto! {q['spiegazione']}")
                else:
                    st.error(f"❌ Sbagliato. Risposta corretta: {q['risposta_corretta']}")
                    st.info(q['spiegazione'])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Verifica risposte", type="primary", use_container_width=True, key="cap6_verifica"):
            st.session_state.cap6_verificato = True
            st.rerun()
    with col2:
        if st.button("🔄 Ricomincia", use_container_width=True, key="cap6_reset"):
            st.session_state.cap6_verificato = False
            st.session_state.cap6_risposte = {}
            st.rerun()


def render_takeaways():
    """Renderizza i punti chiave"""
    
    st.markdown("## 💡 Punti chiave")
    
    takeaways = [
        "Il debito è uno strumento: può aiutare o danneggiare a seconda di come viene gestito",
        "La priorità va sempre ai debiti ad alto tasso, indipendentemente dall'importo",
        "La strategia Avalanche minimizza gli interessi totali (matematicamente ottimale)",
        "La strategia Snowball offre vittorie psicologiche rapide (motivazione)",
        "Consolidare conviene solo se il nuovo tasso e i costi totali sono effettivamente inferiori",
        "Allungare la durata riduce la rata ma può aumentare il costo totale",
        "Non accumulare nuovo debito mentre rimborsi quello esistente"
    ]
    
    for t in takeaways:
        st.markdown(f"- {t}")
    
    st.markdown("---")
    
    # Esercizio pratico
    with st.expander("📝 Esercizio pratico: Mappa i tuoi debiti"):
        st.markdown("""
        Compila questa tabella con i tuoi debiti reali:
        
        | Tipo debito | Saldo residuo | Tasso % | Rata minima | Priorità |
        |-------------|---------------|---------|-------------|----------|
        | | | | | |
        | | | | | |
        | | | | | |
        
        **Passi successivi:**
        
        1. **Ordina per tasso** (strategia Avalanche) e **per saldo** (strategia Snowball)
        2. **Scegli la strategia** più adatta al tuo profilo
        3. **Calcola le risorse extra** disponibili ogni mese
        4. **Concentrale sul primo debito** secondo la strategia scelta
        5. **Una volta estinto**, passa al successivo
        
        ---
        
        💡 *La disciplina è parte integrante della strategia.*
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
