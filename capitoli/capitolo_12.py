"""
Capitolo 12: Piani di accumulo (PAC) e investimenti periodici
InvestAccademy - Corso di Finanza Personale
"""

import streamlit as st
import pandas as pd
import numpy as np

# Metadata
CAPITOLO_NUM = 12
TITOLO = "Piani di accumulo (PAC) e investimenti periodici"

OBIETTIVI = [
    "Comprendere cos'è un Piano di Accumulo (PAC)",
    "Valutare vantaggi e limiti degli investimenti periodici",
    "Capire l'effetto della media del costo nel tempo",
    "Integrare un PAC all'interno della propria asset allocation",
    "Evitare gli errori più comuni legati agli investimenti ricorrenti"
]

# Quiz
QUIZ = [
    {
        "id": 1,
        "domanda": "Cos'è un PAC?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Investimento periodico di importi regolari",
            "Una forma di prestito",
            "Un conto corrente",
            "Un tipo di azione"
        ],
        "risposta_corretta": "Investimento periodico di importi regolari",
        "spiegazione": "Un PAC consiste nell'investire importi fissi a intervalli regolari (mensili, trimestrali, ecc.)."
    },
    {
        "id": 2,
        "domanda": "Cosa significa media del costo nel tempo (Dollar Cost Averaging)?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Comprare sempre allo stesso prezzo",
            "Acquistare più quote quando i prezzi sono bassi e meno quando sono alti",
            "Vendere regolarmente",
            "Investire solo quando il mercato sale"
        ],
        "risposta_corretta": "Acquistare più quote quando i prezzi sono bassi e meno quando sono alti",
        "spiegazione": "Investendo una somma fissa, compri automaticamente più quote quando i prezzi scendono e meno quando salgono."
    },
    {
        "id": 3,
        "domanda": "Il PAC elimina completamente il rischio di mercato.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "Il PAC riduce il rischio di timing ma non elimina il rischio di mercato. Se il mercato scende, il valore del portafoglio scende."
    },
    {
        "id": 4,
        "domanda": "Quando conviene sospendere un PAC?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Durante i ribassi di mercato",
            "Quando il mercato sale molto",
            "Solo se cambiano gli obiettivi o la situazione finanziaria",
            "Ogni anno"
        ],
        "risposta_corretta": "Solo se cambiano gli obiettivi o la situazione finanziaria",
        "spiegazione": "Sospendere il PAC per ragioni di mercato vanifica i benefici della strategia. Si sospende solo per motivi personali reali."
    },
    {
        "id": 5,
        "domanda": "Un PAC è adatto solo per importi elevati.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "Il PAC è perfetto per piccoli importi regolari. Si può iniziare anche con €50-100 al mese."
    }
]


def simula_pac(importo_mensile: float, mesi: int, rendimento_annuo: float) -> dict:
    """Simula un PAC con rendimento costante"""
    
    rendimento_mensile = (rendimento_annuo / 100) / 12
    
    capitale = 0
    versato_totale = 0
    evoluzione = []
    
    for mese in range(1, mesi + 1):
        versato_totale += importo_mensile
        capitale = (capitale + importo_mensile) * (1 + rendimento_mensile)
        
        evoluzione.append({
            "mese": mese,
            "versato": versato_totale,
            "capitale": capitale,
            "guadagno": capitale - versato_totale
        })
    
    return {
        "evoluzione": evoluzione,
        "versato_totale": versato_totale,
        "capitale_finale": capitale,
        "guadagno_totale": capitale - versato_totale
    }


def confronta_pac_vs_pic(importo_totale: float, rendimento_annuo: float, mesi: int) -> dict:
    """Confronta PAC vs investimento in unica soluzione (PIC)"""
    
    # PIC: tutto investito subito
    capitale_pic = importo_totale * ((1 + rendimento_annuo / 100) ** (mesi / 12))
    
    # PAC: investimento mensile
    importo_mensile = importo_totale / mesi
    risultato_pac = simula_pac(importo_mensile, mesi, rendimento_annuo)
    capitale_pac = risultato_pac['capitale_finale']
    
    return {
        "capitale_pic": capitale_pic,
        "capitale_pac": capitale_pac,
        "differenza": capitale_pic - capitale_pac,
        "pac_migliore": capitale_pac > capitale_pic
    }


def simula_dca_con_volatilita(importo_mensile: float, mesi: int) -> dict:
    """Simula l'effetto Dollar Cost Averaging con prezzi variabili"""
    
    np.random.seed(42)
    
    # Genera prezzi con volatilità
    prezzo_iniziale = 100
    prezzi = [prezzo_iniziale]
    
    for _ in range(mesi - 1):
        variazione = np.random.normal(0.005, 0.05)  # Media 0.5%, volatilità 5%
        nuovo_prezzo = prezzi[-1] * (1 + variazione)
        prezzi.append(max(nuovo_prezzo, 1))  # Evita prezzi negativi
    
    # Calcola accumulo
    quote_totali = 0
    investito = 0
    
    for prezzo in prezzi:
        quote_acquistate = importo_mensile / prezzo
        quote_totali += quote_acquistate
        investito += importo_mensile
    
    prezzo_medio = investito / quote_totali if quote_totali > 0 else 0
    valore_finale = quote_totali * prezzi[-1]
    
    return {
        "prezzi": prezzi,
        "quote_totali": quote_totali,
        "prezzo_medio": prezzo_medio,
        "prezzo_finale": prezzi[-1],
        "investito": investito,
        "valore_finale": valore_finale,
        "guadagno": valore_finale - investito
    }


def render_contenuto():
    """Renderizza il contenuto teorico"""
    
    st.markdown("""
    ## Cos'è un Piano di Accumulo
    
    Un **Piano di Accumulo del Capitale (PAC)** consiste nell'investire importi regolari 
    (mensili, trimestrali, ecc.) in uno o più strumenti finanziari.
    
    A differenza dell'investimento in un'unica soluzione, il PAC **distribuisce l'ingresso 
    sul mercato nel tempo**, riducendo il rischio di investire tutto in un momento sfavorevole.
    """)
    
    st.markdown("---")
    
    st.markdown("## Perché il PAC è così diffuso")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### ✅ Vantaggi del PAC")
            st.markdown("""
            - **Semplice da implementare** - basta automatizzare
            - **Richiede importi contenuti** - si può iniziare con poco
            - **Riduce l'impatto emotivo** della volatilità
            - **Favorisce disciplina e costanza**
            - **Evita il problema del timing** (quando entrare)
            - **Accessibile a tutti** - dal reddito mensile
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### ⚠️ Limiti del PAC")
            st.markdown("""
            - **Non elimina il rischio di mercato**
            - Statisticamente meno efficiente del PIC in mercati crescenti
            - **Richiede costanza** nel tempo
            - Può sembrare "lento" inizialmente
            - **Non protegge da crolli** prolungati
            """)
    
    st.info("""
    💡 **Il PAC è particolarmente adatto a chi:**
    - Investe partendo dal reddito periodico
    - Non ha una grande somma disponibile subito
    - Vuole ridurre l'ansia da timing di mercato
    - Preferisce un approccio disciplinato e automatico
    """)
    
    st.markdown("---")
    
    st.markdown("## Media del costo nel tempo (Dollar Cost Averaging)")
    
    st.markdown("""
    Investendo una **somma fissa** a intervalli regolari, acquisti automaticamente:
    - **Più quote quando i prezzi scendono**
    - **Meno quote quando i prezzi salgono**
    
    Questo meccanismo porta a un **prezzo medio di carico più stabile** nel tempo.
    """)
    
    with st.container(border=True):
        st.markdown("### 📊 Esempio pratico")
        
        esempio_dca = pd.DataFrame({
            "Mese": [1, 2, 3, 4, 5],
            "Investimento €": [200, 200, 200, 200, 200],
            "Prezzo quota €": [100, 80, 125, 90, 110],
            "Quote acquistate": [2.00, 2.50, 1.60, 2.22, 1.82]
        })
        
        st.dataframe(esempio_dca, use_container_width=True, hide_index=True)
        
        totale_investito = 1000
        totale_quote = esempio_dca["Quote acquistate"].sum()
        prezzo_medio = totale_investito / totale_quote
        
        st.markdown(f"""
        **Risultato:**
        - Totale investito: €1.000
        - Quote totali: {totale_quote:.2f}
        - Prezzo medio: €{prezzo_medio:.2f}
        
        Hai comprato di più quando costava meno!
        """)
    
    st.warning("""
    ⚠️ **Importante:** La media del costo NON elimina il rischio, ma lo rende 
    più gestibile dal punto di vista comportamentale.
    """)
    
    st.markdown("---")
    
    st.markdown("## PAC vs Investimento in unica soluzione (PIC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💰 PIC (Tutto subito)")
        st.markdown("""
        **Vantaggi statistici:**
        - Statisticamente più redditizio nei mercati crescenti
        - Tempo di esposizione massimo
        - Interesse composto da subito
        
        **Svantaggi psicologici:**
        - Alta ansia se il mercato scende subito
        - Rischio di timing sbagliato
        - Richiede grande somma disponibile
        """)
    
    with col2:
        st.markdown("### 📅 PAC (Periodico)")
        st.markdown("""
        **Vantaggi pratici:**
        - Riduce ansia e stress
        - Nessun bisogno di grandi capitali
        - Gestione automatica
        
        **Trade-off:**
        - Potenzialmente meno redditizio
        - Ma molto più sostenibile psicologicamente
        """)
    
    st.success("""
    ✅ **La scelta dipende dal profilo:**
    
    - **PIC:** Se hai la somma, alta tolleranza psicologica, orizzonte lungo
    - **PAC:** Se investi dal reddito, vuoi più tranquillità, preferisci automazione
    """)
    
    st.markdown("---")
    
    st.markdown("## Come integrare un PAC nella strategia")
    
    st.markdown("""
    Un PAC efficace deve:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ✅ **Rispettare l'asset allocation definita**
        - Se il target è 60/40, il PAC deve seguirlo
        
        ✅ **Essere automatico**
        - Bonifico automatico ogni mese
        
        ✅ **Avere orizzonte lungo**
        - Minimo 5 anni, ideale 10+
        """)
    
    with col2:
        st.markdown("""
        ✅ **Essere sostenibile**
        - Importo che puoi mantenere anche in difficoltà
        
        ✅ **Non interrompersi nei ribassi**
        - I ribassi sono opportunità, non minacce
        
        ✅ **Ribilanciare periodicamente**
        - Non dimenticare l'asset allocation
        """)
    
    st.markdown("---")
    
    st.markdown("## Errori comuni nei PAC")
    
    errori = [
        ("❌ Cambiare importo troppo spesso", "La costanza è la forza del PAC"),
        ("❌ Sospendere durante i ribassi", "È proprio quando conviene di più continuare"),
        ("❌ Aumentare nei rialzi", "Rischio di comprare troppo quando costa di più"),
        ("❌ Investire il fondo emergenze", "Il PAC serve per il lungo periodo, non per liquidità"),
        ("❌ Considerarlo strategia breve termine", "Il PAC dà risultati su 5+ anni"),
        ("❌ Non automatizzare", "L'intervento manuale aumenta gli errori comportamentali")
    ]
    
    for errore, spiegazione in errori:
        with st.container(border=True):
            st.markdown(f"**{errore}**")
            st.caption(spiegazione)
    
    st.success("""
    ✅ **La forza del PAC è la costanza, non la reattività.**
    
    Imposta, automatizza, dimentica (fino al ribilanciamento programmato).
    """)


def render_calcolatore():
    """Renderizza i calcolatori"""
    
    st.markdown("## 🧮 Calcolatori")
    
    calc_type = st.radio(
        "Seleziona calcolatore:",
        ["Simulatore PAC", "PAC vs PIC", "Effetto Dollar Cost Averaging"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if calc_type == "Simulatore PAC":
        render_calc_pac()
    elif calc_type == "PAC vs PIC":
        render_calc_confronto()
    else:
        render_calc_dca()


def render_calc_pac():
    """Simulatore PAC"""
    
    st.markdown("### Simulatore Piano di Accumulo")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        importo = st.number_input(
            "💰 Importo mensile (€)",
            min_value=10.0,
            value=200.0,
            step=10.0,
            key="cap12_importo"
        )
        
        anni = st.slider(
            "📅 Durata (anni)",
            min_value=1,
            max_value=40,
            value=20,
            key="cap12_anni"
        )
        
        rendimento = st.slider(
            "📊 Rendimento annuo atteso (%)",
            min_value=0.0,
            max_value=12.0,
            value=6.0,
            step=0.5,
            key="cap12_rend"
        )
    
    with col2:
        mesi = anni * 12
        risultato = simula_pac(importo, mesi, rendimento)
        
        st.markdown("### Risultati")
        
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.metric("Versato totale", f"€{risultato['versato_totale']:,.0f}")
        with c2:
            st.metric(
                "Capitale finale",
                f"€{risultato['capitale_finale']:,.0f}",
                f"+€{risultato['guadagno_totale']:,.0f}"
            )
        with c3:
            rendimento_perc = (risultato['guadagno_totale'] / risultato['versato_totale'] * 100) if risultato['versato_totale'] > 0 else 0
            st.metric("Guadagno %", f"{rendimento_perc:.1f}%")
    
    st.markdown("---")
    st.markdown("### 📈 Evoluzione del Capitale")
    
    df_evoluzione = pd.DataFrame(risultato['evoluzione'])
    
    # Mostra solo alcuni punti se troppi mesi
    if len(df_evoluzione) > 120:
        # Mostra solo ogni anno
        df_plot = df_evoluzione[df_evoluzione['mese'] % 12 == 0].copy()
    else:
        df_plot = df_evoluzione
    
    chart_data = pd.DataFrame({
        "Mese": df_plot['mese'],
        "Versato": df_plot['versato'],
        "Capitale": df_plot['capitale']
    })
    
    st.line_chart(chart_data.set_index("Mese"))
    
    # Tabella riassuntiva
    anni_milestone = [1, 5, 10, 15, 20, 25, 30]
    anni_milestone = [a for a in anni_milestone if a <= anni]
    
    if anni_milestone:
        st.markdown("#### 📊 Milestones")
        
        milestones = []
        for anno in anni_milestone:
            mese_target = anno * 12
            if mese_target <= len(df_evoluzione):
                row = df_evoluzione.iloc[mese_target - 1]
                milestones.append({
                    "Anno": anno,
                    "Versato": f"€{row['versato']:,.0f}",
                    "Capitale": f"€{row['capitale']:,.0f}",
                    "Guadagno": f"€{row['guadagno']:,.0f}"
                })
        
        df_milestones = pd.DataFrame(milestones)
        st.dataframe(df_milestones, use_container_width=True, hide_index=True)


def render_calc_confronto():
    """Confronto PAC vs PIC"""
    
    st.markdown("### Confronto: PAC vs Investimento Unico (PIC)")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        importo_totale = st.number_input(
            "💰 Capitale totale disponibile (€)",
            min_value=1000.0,
            value=12000.0,
            step=1000.0,
            key="cap12_conf_tot"
        )
        
        anni = st.slider(
            "📅 Orizzonte temporale (anni)",
            min_value=1,
            max_value=30,
            value=10,
            key="cap12_conf_anni"
        )
        
        rendimento = st.slider(
            "📊 Rendimento annuo atteso (%)",
            min_value=0.0,
            max_value=12.0,
            value=6.0,
            step=0.5,
            key="cap12_conf_rend"
        )
    
    with col2:
        mesi = anni * 12
        confronto = confronta_pac_vs_pic(importo_totale, rendimento, mesi)
        
        st.markdown("### Risultati Confronto")
        
        col_pic, col_pac = st.columns(2)
        
        with col_pic:
            st.markdown("#### 💰 PIC (Tutto subito)")
            st.metric("Capitale finale", f"€{confronto['capitale_pic']:,.0f}")
            guadagno_pic = confronto['capitale_pic'] - importo_totale
            st.metric("Guadagno", f"€{guadagno_pic:,.0f}")
        
        with col_pac:
            st.markdown("#### 📅 PAC (Mensile)")
            importo_mensile = importo_totale / mesi
            st.caption(f"€{importo_mensile:.0f}/mese per {mesi} mesi")
            st.metric("Capitale finale", f"€{confronto['capitale_pac']:,.0f}")
            guadagno_pac = confronto['capitale_pac'] - importo_totale
            st.metric("Guadagno", f"€{guadagno_pac:,.0f}")
        
        st.markdown("---")
        
        if confronto['pac_migliore']:
            st.success(f"✅ In questo scenario, il PAC genera €{abs(confronto['differenza']):,.0f} in più!")
            st.caption("Questo può accadere se i prezzi scendono inizialmente e poi recuperano.")
        else:
            st.info(f"""
            📊 **PIC genera €{confronto['differenza']:,.0f} in più**
            
            Statisticamente, in mercati crescenti il PIC tende a performare meglio 
            perché il capitale è investito da subito.
            
            **Ma:** Il PAC offre maggiore tranquillità psicologica e riduce 
            il rischio di entrare tutto nel momento sbagliato.
            """)


def render_calc_dca():
    """Simulatore Dollar Cost Averaging"""
    
    st.markdown("### Effetto Dollar Cost Averaging con Volatilità")
    
    st.markdown("""
    Questa simulazione mostra come il PAC funziona con prezzi variabili.
    """)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        importo = st.number_input(
            "💰 Importo mensile (€)",
            min_value=50.0,
            value=300.0,
            step=50.0,
            key="cap12_dca_imp"
        )
        
        mesi = st.slider(
            "📅 Numero di mesi",
            min_value=12,
            max_value=120,
            value=36,
            key="cap12_dca_mesi"
        )
    
    with col2:
        simulazione = simula_dca_con_volatilita(importo, mesi)
        
        st.markdown("### Risultati Simulazione")
        
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.metric("Quote accumulate", f"{simulazione['quote_totali']:.2f}")
        with c2:
            st.metric("Prezzo medio carico", f"€{simulazione['prezzo_medio']:.2f}")
        with c3:
            st.metric("Prezzo finale", f"€{simulazione['prezzo_finale']:.2f}")
        
        st.markdown("---")
        
        col_inv, col_val, col_gain = st.columns(3)
        
        with col_inv:
            st.metric("Investito", f"€{simulazione['investito']:,.0f}")
        with col_val:
            st.metric("Valore finale", f"€{simulazione['valore_finale']:,.0f}")
        with col_gain:
            rendimento_perc = (simulazione['guadagno'] / simulazione['investito'] * 100) if simulazione['investito'] > 0 else 0
            st.metric("Guadagno", f"€{simulazione['guadagno']:,.0f}", f"{rendimento_perc:+.1f}%")
    
    st.markdown("---")
    st.markdown("### 📈 Andamento Prezzi e Media")
    
    df_prezzi = pd.DataFrame({
        "Mese": range(1, len(simulazione['prezzi']) + 1),
        "Prezzo di mercato": simulazione['prezzi'],
        "Prezzo medio carico": [simulazione['prezzo_medio']] * len(simulazione['prezzi'])
    })
    
    st.line_chart(df_prezzi.set_index("Mese"))
    
    st.info("""
    💡 **Interpretazione:**
    
    Il **prezzo medio di carico** è il prezzo medio al quale hai comprato le quote.
    
    - Se il prezzo finale > prezzo medio → Guadagno
    - Se il prezzo finale < prezzo medio → Perdita (temporanea)
    
    Con il PAC, compri automaticamente di più quando i prezzi scendono, 
    abbassando il tuo prezzo medio!
    """)


def render_quiz():
    """Renderizza il quiz di verifica"""
    
    st.markdown("## 📝 Quiz di verifica")
    
    if "cap12_risposte" not in st.session_state:
        st.session_state.cap12_risposte = {}
    if "cap12_verificato" not in st.session_state:
        st.session_state.cap12_verificato = False
    
    for i, q in enumerate(QUIZ):
        with st.container(border=True):
            st.markdown(f"**Domanda {i+1}:** {q['domanda']}")
            
            if q["tipo"] == "vero_falso":
                risposta = st.radio(
                    "Seleziona:",
                    ["Vero", "Falso"],
                    key=f"cap12_q{q['id']}",
                    horizontal=True
                )
                st.session_state.cap12_risposte[q['id']] = risposta == "Vero"
                
            elif q["tipo"] == "scelta_multipla":
                risposta = st.radio(
                    "Seleziona:",
                    q["opzioni"],
                    key=f"cap12_q{q['id']}"
                )
                st.session_state.cap12_risposte[q['id']] = risposta
            
            if st.session_state.cap12_verificato:
                user_ans = st.session_state.cap12_risposte.get(q['id'])
                corretto = user_ans == q["risposta_corretta"]
                
                if corretto:
                    st.success(f"✅ Corretto! {q['spiegazione']}")
                else:
                    st.error(f"❌ Sbagliato. Risposta corretta: {q['risposta_corretta']}")
                    st.info(q['spiegazione'])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Verifica risposte", type="primary", use_container_width=True, key="cap12_verifica"):
            st.session_state.cap12_verificato = True
            st.rerun()
    with col2:
        if st.button("🔄 Ricomincia", use_container_width=True, key="cap12_reset"):
            st.session_state.cap12_verificato = False
            st.session_state.cap12_risposte = {}
            st.rerun()


def render_takeaways():
    """Renderizza i punti chiave"""
    
    st.markdown("## 💡 Punti chiave")
    
    takeaways = [
        "Il PAC distribuisce l'ingresso sul mercato nel tempo, riducendo il rischio di timing sbagliato",
        "Il Dollar Cost Averaging fa comprare automaticamente più quote quando i prezzi scendono",
        "Il PAC non elimina il rischio di mercato, ma lo rende più gestibile psicologicamente",
        "Statisticamente il PIC può essere più redditizio, ma il PAC è più sostenibile per molti",
        "La forza del PAC è la costanza: non sospenderlo durante i ribassi",
        "Il PAC è perfetto per chi investe partendo dal reddito periodico",
        "Automatizzare il PAC riduce l'intervento emotivo e gli errori comportamentali"
    ]
    
    for t in takeaways:
        st.markdown(f"- {t}")
    
    st.markdown("---")
    
    # Esercizio pratico
    with st.expander("📝 Esercizio: Progetta il tuo PAC"):
        st.markdown("""
        **Definisci il tuo Piano di Accumulo:**
        
        1. **Quanto puoi investire regolarmente?**
           - Importo mensile sostenibile: €_____
           - Verifica che sia compatibile con il cash flow
        
        2. **Qual è il tuo orizzonte temporale?**
           - Anni previsti: _____
           - Obiettivo finale: €_____
        
        3. **Quale strumento userai?**
           - ETF azionario: _____
           - ETF obbligazionario: _____
           - Altri: _____
        
        4. **Come automatizzerai?**
           - Bonifico automatico: ☐
           - Data versamento: giorno _____ del mese
           - Conto di appoggio: _____________
        
        5. **Definisci le regole:**
           - Aumenterò il versamento quando: _____________
           - Ribilancerò ogni: _____________
           - NON sospenderò anche se: _____________
        
        ---
        
        💡 **Impegno:**
        
        "Mi impegno a mantenere questo PAC per almeno _____ anni, 
        modificandolo solo per cambiamenti nella mia situazione personale, 
        non per movimenti di mercato."
        
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
