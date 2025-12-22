"""
Capitolo 8: Introduzione agli investimenti
InvestAccademy - Corso di Finanza Personale
"""

import streamlit as st
import pandas as pd

# Metadata
CAPITOLO_NUM = 8
TITOLO = "Introduzione agli investimenti"

OBIETTIVI = [
    "Comprendere cosa significa investire e perché farlo",
    "Distinguere tra risparmio e investimento",
    "Conoscere le principali classi di attivi",
    "Capire il rapporto tra rischio e rendimento",
    "Evitare gli errori più comuni degli investitori alle prime armi"
]

# Quiz
QUIZ = [
    {
        "id": 1,
        "domanda": "Qual è la differenza principale tra risparmio e investimento?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Il risparmio è liquido e a basso rischio, l'investimento è esposto a oscillazioni",
            "Il risparmio rende di più",
            "Non c'è differenza",
            "L'investimento è sempre più sicuro"
        ],
        "risposta_corretta": "Il risparmio è liquido e a basso rischio, l'investimento è esposto a oscillazioni",
        "spiegazione": "Il risparmio mantiene liquidità per il breve termine, mentre l'investimento accetta rischio per potenziali rendimenti maggiori nel lungo periodo."
    },
    {
        "id": 2,
        "domanda": "Quale asset class ha generalmente il rendimento potenziale più elevato?",
        "tipo": "scelta_multipla",
        "opzioni": ["Strumenti monetari", "Obbligazioni", "Azioni", "Conti deposito"],
        "risposta_corretta": "Azioni",
        "spiegazione": "Le azioni hanno storicamente offerto i rendimenti più elevati, ma con maggiore volatilità e rischio."
    },
    {
        "id": 3,
        "domanda": "A maggior rendimento atteso corrisponde sempre maggiore rischio.",
        "tipo": "vero_falso",
        "risposta_corretta": True,
        "spiegazione": "In finanza non esistono pasti gratis: rendimenti più elevati comportano sempre maggiore incertezza e volatilità."
    },
    {
        "id": 4,
        "domanda": "Perché il tempo riduce il rischio degli investimenti?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Perché elimina la volatilità",
            "Perché le fluttuazioni tendono a compensarsi nel lungo periodo",
            "Perché i prezzi salgono sempre",
            "Non lo riduce affatto"
        ],
        "risposta_corretta": "Perché le fluttuazioni tendono a compensarsi nel lungo periodo",
        "spiegazione": "Un orizzonte temporale più lungo permette di attraversare cicli di mercato completi, riducendo l'impatto della volatilità di breve periodo."
    },
    {
        "id": 5,
        "domanda": "È corretto investire il fondo emergenze in azioni per ottenere rendimenti più alti.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "Falso. Il fondo emergenze deve rimanere liquido e a basso rischio. Investire denaro che potrebbe servire nel breve termine è un errore grave."
    }
]


def simula_crescita_investimento(capitale: float, tasso: float, anni: int) -> list:
    """Simula la crescita di un investimento nel tempo"""
    evoluzione = []
    cap = capitale
    
    for anno in range(1, anni + 1):
        guadagno = cap * (tasso / 100)
        cap = cap + guadagno
        evoluzione.append({
            "anno": anno,
            "capitale": round(cap, 2),
            "guadagno_anno": round(guadagno, 2),
            "guadagno_totale": round(cap - capitale, 2)
        })
    
    return evoluzione


def confronta_asset_class(capitale: float, anni: int) -> dict:
    """Confronta performance di diverse asset class con tassi storici medi"""
    
    # Tassi storici approssimativi (solo esempio educativo)
    tassi = {
        "Liquidità": 1.0,
        "Obbligazioni": 3.5,
        "Azioni": 8.0
    }
    
    risultati = {}
    
    for asset, tasso in tassi.items():
        montante = capitale * ((1 + tasso / 100) ** anni)
        risultati[asset] = {
            "tasso": tasso,
            "montante": montante,
            "guadagno": montante - capitale
        }
    
    return risultati


def calcola_impatto_inflazione(capitale: float, rendimento: float, inflazione: float, anni: int) -> dict:
    """Calcola l'impatto dell'inflazione sul rendimento"""
    
    rendimento_reale = rendimento - inflazione
    
    montante_nominale = capitale * ((1 + rendimento / 100) ** anni)
    montante_reale = capitale * ((1 + rendimento_reale / 100) ** anni)
    
    return {
        "rendimento_nominale": rendimento,
        "rendimento_reale": rendimento_reale,
        "montante_nominale": montante_nominale,
        "montante_reale": montante_reale,
        "perdita_inflazione": montante_nominale - montante_reale
    }


def render_contenuto():
    """Renderizza il contenuto teorico"""
    
    st.markdown("""
    ## Perché investire
    
    Investire significa impiegare capitale oggi con l'obiettivo di ottenere un rendimento futuro, 
    accettando un certo livello di rischio.
    
    > Il motivo principale per investire non è "diventare ricchi", ma **difendere e far crescere 
    > il potere d'acquisto** nel tempo, contrastando inflazione e tassazione.
    
    ### La minaccia silenziosa: l'inflazione
    
    Tenere i soldi fermi equivale spesso a perdere valore reale. Con un'inflazione media del 2% annuo:
    - €10.000 oggi valgono come €8.171 tra 10 anni
    - €10.000 oggi valgono come €6.676 tra 20 anni
    
    Senza investimento, il capitale si erode silenziosamente.
    """)
    
    st.markdown("---")
    
    st.markdown("## Risparmio vs Investimento")
    
    st.markdown("""
    È fondamentale distinguere tra i due concetti:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 💰 Risparmio")
            st.markdown("""
            **Caratteristiche:**
            - Liquidità a basso rischio
            - Disponibile nel breve termine
            - Rendimento limitato
            - Volatilità minima
            
            **Strumenti:**
            - Conti correnti
            - Conti deposito
            - Buoni fruttiferi
            
            **Orizzonte:** 0-3 anni
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### 📈 Investimento")
            st.markdown("""
            **Caratteristiche:**
            - Capitale esposto a oscillazioni
            - Orizzonte medio-lungo
            - Potenziale rendimento elevato
            - Volatilità significativa
            
            **Strumenti:**
            - Azioni
            - Obbligazioni
            - ETF
            - Fondi
            
            **Orizzonte:** 3+ anni
            """)
    
    st.warning("""
    ⚠️ **Errore comune:** confondere i due concetti porta a decisioni sbagliate, come investire 
    il fondo emergenze o mantenere risparmi a lungo termine senza rendimento.
    """)
    
    st.markdown("---")
    
    st.markdown("## Le principali classi di attivi")
    
    st.markdown("""
    Gli investimenti si suddividono in grandi categorie, ciascuna con caratteristiche specifiche.
    """)
    
    # Azioni
    with st.container(border=True):
        st.markdown("### 📊 Azioni")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            Le azioni rappresentano una quota di proprietà di un'azienda.
            
            **Vantaggi:**
            - Potenziale di rendimento elevato
            - Partecipazione alla crescita economica
            - Liquidità elevata (mercati organizzati)
            
            **Svantaggi:**
            - Elevata volatilità nel breve termine
            - Rischio di perdita di capitale
            - Necessità di orizzonte temporale lungo
            """)
        
        with col2:
            st.metric("Rendimento storico medio", "~7-8% annuo", help="Dati storici mercati sviluppati")
            st.metric("Volatilità", "Alta", delta_color="off")
            st.metric("Orizzonte minimo", "5+ anni", delta_color="off")
    
    # Obbligazioni
    with st.container(border=True):
        st.markdown("### 🏦 Obbligazioni")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            Le obbligazioni sono prestiti concessi a stati o aziende.
            
            **Vantaggi:**
            - Rendimento più stabile delle azioni
            - Funzione di stabilizzazione del portafoglio
            - Cedole periodiche (reddito)
            
            **Svantaggi:**
            - Rendimento inferiore alle azioni nel lungo periodo
            - Rischio di credito (insolvenza emittente)
            - Sensibilità ai tassi di interesse
            """)
        
        with col2:
            st.metric("Rendimento storico medio", "~3-4% annuo")
            st.metric("Volatilità", "Media", delta_color="off")
            st.metric("Orizzonte minimo", "3+ anni", delta_color="off")
    
    # Strumenti monetari
    with st.container(border=True):
        st.markdown("### 💵 Strumenti Monetari")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            Strumenti a breve termine e bassa volatilità.
            
            **Vantaggi:**
            - Rischio contenuto
            - Elevata liquidità
            - Stabilità del capitale
            
            **Svantaggi:**
            - Rendimento molto limitato
            - Spesso inferiore all'inflazione
            - Non adatti per crescita di lungo periodo
            """)
        
        with col2:
            st.metric("Rendimento medio", "~1-2% annuo")
            st.metric("Volatilità", "Minima", delta_color="off")
            st.metric("Orizzonte", "Breve termine", delta_color="off")
    
    st.markdown("---")
    
    st.markdown("## Rischio e Rendimento: il trade-off fondamentale")
    
    st.markdown("""
    In finanza **non esistono pasti gratis**: a maggior rendimento atteso corrisponde maggiore rischio.
    
    Il rischio si manifesta come **volatilità**, cioè oscillazioni del valore nel tempo.
    """)
    
    # Tabella comparativa
    st.markdown("### Confronto per asset class")
    
    df_confronto = pd.DataFrame({
        "Asset Class": ["Liquidità", "Obbligazioni", "Azioni"],
        "Rendimento atteso": ["Basso (1-2%)", "Medio (3-4%)", "Alto (7-8%)"],
        "Rischio": ["Molto basso", "Medio", "Alto"],
        "Volatilità": ["Minima", "Moderata", "Elevata"],
        "Orizzonte consigliato": ["< 1 anno", "3-5 anni", "5+ anni"]
    })
    
    st.dataframe(df_confronto, use_container_width=True, hide_index=True)
    
    st.info("""
    💡 **Principio chiave:** La chiave non è evitare il rischio, ma **gestirlo** attraverso:
    - Orizzonte temporale adeguato
    - Diversificazione
    - Asset allocation coerente con i tuoi obiettivi
    """)
    
    st.markdown("---")
    
    st.markdown("## L'importanza dell'orizzonte temporale")
    
    st.markdown("""
    Il tempo è l'alleato più potente dell'investitore.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ⏱️ Breve termine (< 3 anni)")
        st.markdown("""
        - Elevata incertezza
        - Volatilità impattante
        - Rischio di vendere in perdita
        - **Meglio liquidità/obbligazioni brevi**
        """)
    
    with col2:
        st.markdown("### 🕐 Lungo termine (5+ anni)")
        st.markdown("""
        - Volatilità meno rilevante
        - Tempo per recuperare ribassi
        - Potenza dell'interesse composto
        - **Possibile maggiore esposizione azionaria**
        """)
    
    st.success("""
    ✅ **Regola pratica:** Investi in azioni solo denaro che non ti servirà per almeno 5 anni. 
    Per orizzonti più brevi, privilegia strumenti meno volatili.
    """)
    
    st.markdown("---")
    
    st.markdown("## Errori comuni dei principianti")
    
    errori = [
        ("❌ Cercare rendimenti rapidi", "Il trading speculativo è rischioso e richiede competenze specifiche"),
        ("❌ Seguire le mode", "Investire in ciò che va di moda porta spesso a comprare alto"),
        ("❌ Investire senza piano", "Senza obiettivi chiari e asset allocation definita si naviga alla cieca"),
        ("❌ Reagire emotivamente alle oscillazioni", "Vendere in panico cristallizza le perdite"),
        ("❌ Confondere fortuna e strategia", "Un guadagno occasionale non conferma la validità dell'approccio"),
        ("❌ Investire il fondo emergenze", "Il capitale a breve termine deve rimanere liquido e sicuro")
    ]
    
    for errore, spiegazione in errori:
        with st.container(border=True):
            st.markdown(f"**{errore}**")
            st.caption(spiegazione)
    
    st.warning("⚠️ La maggior parte degli errori è **comportamentale**, non tecnica.")


def render_calcolatore():
    """Renderizza i calcolatori"""
    
    st.markdown("## 🧮 Calcolatori")
    
    calc_type = st.radio(
        "Seleziona calcolatore:",
        ["Crescita investimento", "Confronto asset class", "Impatto inflazione"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if calc_type == "Crescita investimento":
        render_calc_crescita()
    elif calc_type == "Confronto asset class":
        render_calc_confronto()
    else:
        render_calc_inflazione()


def render_calc_crescita():
    """Calcolatore crescita investimento nel tempo"""
    
    st.markdown("### Simula la Crescita di un Investimento")
    
    col1, col2 = st.columns(2)
    
    with col1:
        capitale = st.number_input(
            "💰 Capitale iniziale (€)",
            min_value=100.0,
            value=10000.0,
            step=500.0,
            key="cap8_capitale"
        )
        
        tasso = st.slider(
            "📊 Rendimento annuo atteso (%)",
            min_value=0.5,
            max_value=12.0,
            value=6.0,
            step=0.5,
            key="cap8_tasso"
        )
        
        anni = st.slider(
            "📅 Orizzonte temporale (anni)",
            min_value=1,
            max_value=40,
            value=20,
            key="cap8_anni"
        )
    
    with col2:
        evoluzione = simula_crescita_investimento(capitale, tasso, anni)
        montante_finale = evoluzione[-1]["capitale"]
        guadagno_totale = evoluzione[-1]["guadagno_totale"]
        
        st.markdown("### Risultato")
        
        st.metric(
            "Capitale finale",
            f"€{montante_finale:,.2f}",
            f"+€{guadagno_totale:,.2f}"
        )
        
        moltiplicatore = montante_finale / capitale
        st.metric(
            "Moltiplicatore",
            f"{moltiplicatore:.2f}x",
            f"+{((moltiplicatore - 1) * 100):.1f}%"
        )
        
        # Performance annualizzata
        tasso_effettivo = ((montante_finale / capitale) ** (1 / anni) - 1) * 100
        st.caption(f"Rendimento annualizzato: {tasso_effettivo:.2f}%")
    
    st.markdown("---")
    st.markdown("### 📈 Evoluzione nel tempo")
    
    df_evoluzione = pd.DataFrame(evoluzione)
    st.line_chart(df_evoluzione.set_index("anno")["capitale"])
    
    # Tabella dettagliata (solo primi e ultimi anni se troppo lunga)
    if anni <= 10:
        st.dataframe(
            df_evoluzione[["anno", "capitale", "guadagno_anno", "guadagno_totale"]],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.markdown("#### Prime e ultime annualità")
        df_display = pd.concat([
            df_evoluzione.head(5),
            pd.DataFrame([{"anno": "...", "capitale": "...", "guadagno_anno": "...", "guadagno_totale": "..."}]),
            df_evoluzione.tail(5)
        ])
        st.dataframe(df_display, use_container_width=True, hide_index=True)


def render_calc_confronto():
    """Confronto performance asset class"""
    
    st.markdown("### Confronto Asset Class nel Tempo")
    
    st.markdown("""
    Questo calcolatore confronta come €10.000 investiti oggi potrebbero evolversi 
    in diverse asset class, utilizzando rendimenti storici medi.
    
    *Nota: i rendimenti passati non garantiscono risultati futuri.*
    """)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        capitale = st.number_input(
            "💰 Capitale iniziale (€)",
            min_value=1000.0,
            value=10000.0,
            step=1000.0,
            key="cap8_conf_capitale"
        )
        
        anni = st.slider(
            "📅 Orizzonte (anni)",
            min_value=5,
            max_value=30,
            value=20,
            key="cap8_conf_anni"
        )
    
    with col2:
        risultati = confronta_asset_class(capitale, anni)
        
        st.markdown("### Risultati dopo " + str(anni) + " anni")
        
        df_risultati = pd.DataFrame({
            "Asset Class": list(risultati.keys()),
            "Rendimento medio": [f"{r['tasso']}%" for r in risultati.values()],
            "Capitale finale": [f"€{r['montante']:,.2f}" for r in risultati.values()],
            "Guadagno": [f"€{r['guadagno']:,.2f}" for r in risultati.values()]
        })
        
        st.dataframe(df_risultati, use_container_width=True, hide_index=True)
        
        # Grafico comparativo
        st.markdown("#### 📊 Confronto visivo")
        
        chart_data = pd.DataFrame({
            "Asset Class": list(risultati.keys()),
            "Capitale finale": [r['montante'] for r in risultati.values()]
        })
        
        st.bar_chart(chart_data.set_index("Asset Class"))
    
    # Analisi differenze
    diff_azioni_obblig = risultati["Azioni"]["montante"] - risultati["Obbligazioni"]["montante"]
    diff_azioni_liquid = risultati["Azioni"]["montante"] - risultati["Liquidità"]["montante"]
    
    st.markdown("---")
    st.markdown("### 💡 Analisi")
    
    st.info(f"""
    Con un orizzonte di **{anni} anni**:
    
    - Le **azioni** generano €{diff_azioni_obblig:,.2f} in più delle obbligazioni
    - Le **azioni** generano €{diff_azioni_liquid:,.2f} in più della liquidità
    
    Questo illustra il potere dell'interesse composto e l'importanza dell'orizzonte temporale.
    """)
    
    st.warning("""
    ⚠️ **Importante:** Questi sono rendimenti medi storici. La volatilità delle azioni 
    significa che nel breve termine i risultati possono variare significativamente.
    """)


def render_calc_inflazione():
    """Calcolatore impatto inflazione"""
    
    st.markdown("### Impatto dell'Inflazione sul Rendimento")
    
    st.markdown("""
    L'inflazione erode il potere d'acquisto. Ciò che conta davvero è il **rendimento reale**, 
    cioè il rendimento al netto dell'inflazione.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        capitale = st.number_input(
            "💰 Capitale iniziale (€)",
            min_value=1000.0,
            value=10000.0,
            step=1000.0,
            key="cap8_infl_capitale"
        )
        
        rendimento = st.slider(
            "📊 Rendimento nominale annuo (%)",
            min_value=0.0,
            max_value=12.0,
            value=6.0,
            step=0.5,
            key="cap8_infl_rend"
        )
        
        inflazione = st.slider(
            "📉 Inflazione annua (%)",
            min_value=0.0,
            max_value=10.0,
            value=2.5,
            step=0.5,
            key="cap8_infl_inf"
        )
        
        anni = st.slider(
            "📅 Orizzonte (anni)",
            min_value=5,
            max_value=30,
            value=20,
            key="cap8_infl_anni"
        )
    
    with col2:
        analisi = calcola_impatto_inflazione(capitale, rendimento, inflazione, anni)
        
        st.markdown("### Risultati")
        
        col_nom, col_real = st.columns(2)
        
        with col_nom:
            st.metric(
                "Rendimento nominale",
                f"{analisi['rendimento_nominale']:.1f}%"
            )
            st.metric(
                "Capitale nominale",
                f"€{analisi['montante_nominale']:,.2f}"
            )
        
        with col_real:
            st.metric(
                "Rendimento reale",
                f"{analisi['rendimento_reale']:.1f}%"
            )
            st.metric(
                "Potere d'acquisto reale",
                f"€{analisi['montante_reale']:,.2f}"
            )
        
        st.markdown("---")
        
        perdita_perc = (analisi['perdita_inflazione'] / analisi['montante_nominale']) * 100
        
        if analisi['rendimento_reale'] > 0:
            st.success(f"✅ Guadagno reale positivo nonostante l'inflazione")
        elif analisi['rendimento_reale'] == 0:
            st.warning(f"⚠️ Rendimento nullo: mantieni il potere d'acquisto")
        else:
            st.error(f"❌ Perdita di potere d'acquisto: {abs(analisi['rendimento_reale']):.1f}% annuo")
        
        st.metric(
            "Perdita per inflazione",
            f"€{analisi['perdita_inflazione']:,.2f}",
            f"-{perdita_perc:.1f}% del capitale nominale",
            delta_color="inverse"
        )
    
    st.markdown("---")
    st.info("""
    💡 **Conclusione:** Quando valuti un investimento, considera sempre il rendimento **reale**, 
    non quello nominale. Un investimento che rende il 3% con inflazione al 4% sta in realtà 
    perdendo potere d'acquisto.
    """)


def render_quiz():
    """Renderizza il quiz di verifica"""
    
    st.markdown("## 📝 Quiz di verifica")
    
    if "cap8_risposte" not in st.session_state:
        st.session_state.cap8_risposte = {}
    if "cap8_verificato" not in st.session_state:
        st.session_state.cap8_verificato = False
    
    for i, q in enumerate(QUIZ):
        with st.container(border=True):
            st.markdown(f"**Domanda {i+1}:** {q['domanda']}")
            
            if q["tipo"] == "vero_falso":
                risposta = st.radio(
                    "Seleziona:",
                    ["Vero", "Falso"],
                    key=f"cap8_q{q['id']}",
                    horizontal=True
                )
                st.session_state.cap8_risposte[q['id']] = risposta == "Vero"
                
            elif q["tipo"] == "scelta_multipla":
                risposta = st.radio(
                    "Seleziona:",
                    q["opzioni"],
                    key=f"cap8_q{q['id']}"
                )
                st.session_state.cap8_risposte[q['id']] = risposta
            
            if st.session_state.cap8_verificato:
                user_ans = st.session_state.cap8_risposte.get(q['id'])
                corretto = user_ans == q["risposta_corretta"]
                
                if corretto:
                    st.success(f"✅ Corretto! {q['spiegazione']}")
                else:
                    st.error(f"❌ Sbagliato. Risposta corretta: {q['risposta_corretta']}")
                    st.info(q['spiegazione'])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Verifica risposte", type="primary", use_container_width=True, key="cap8_verifica"):
            st.session_state.cap8_verificato = True
            st.rerun()
    with col2:
        if st.button("🔄 Ricomincia", use_container_width=True, key="cap8_reset"):
            st.session_state.cap8_verificato = False
            st.session_state.cap8_risposte = {}
            st.rerun()


def render_takeaways():
    """Renderizza i punti chiave"""
    
    st.markdown("## 💡 Punti chiave")
    
    takeaways = [
        "Investire serve a difendere e far crescere il potere d'acquisto, contrastando l'inflazione",
        "Risparmio e investimento hanno funzioni diverse: non confonderli",
        "A maggior rendimento atteso corrisponde sempre maggiore rischio (trade-off fondamentale)",
        "Il tempo è l'alleato più potente: le azioni richiedono orizzonti di almeno 5 anni",
        "La maggior parte degli errori è comportamentale, non tecnica",
        "Ciò che conta è il rendimento reale (al netto dell'inflazione), non quello nominale"
    ]
    
    for t in takeaways:
        st.markdown(f"- {t}")
    
    st.markdown("---")
    
    # Auto-valutazione
    with st.expander("📝 Auto-valutazione: Sei pronto per investire?"):
        st.markdown("""
        Rispondi a queste domande per valutare la tua preparazione:
        
        **Fondamentali:**
        - [ ] Ho un fondo emergenze di almeno 3-6 mesi
        - [ ] Non ho debiti ad alto tasso (>10%)
        - [ ] Il capitale che voglio investire non mi servirà per almeno 5 anni
        - [ ] Ho un reddito stabile o fonti di entrata regolari
        
        **Conoscenze:**
        - [ ] Comprendo la differenza tra azioni e obbligazioni
        - [ ] So cosa significa asset allocation
        - [ ] Comprendo che le oscillazioni sono normali
        - [ ] So che non posso prevedere il mercato
        
        **Psicologia:**
        - [ ] Accetto l'idea di vedere il capitale oscillare
        - [ ] Non venderei in panico durante un ribasso
        - [ ] Ho obiettivi chiari e misurabili
        - [ ] Sono disposto a seguire un piano di lungo periodo
        
        ---
        
        **Valutazione:**
        - 10-12 ✅: Sei pronto per iniziare
        - 7-9 ⚠️: Lavora ancora su alcuni aspetti
        - < 7 🔴: Concentrati prima su risparmio e fondo emergenze
        """)
    
    # Piano prossimi passi
    with st.expander("🎯 Prossimi passi"):
        st.markdown("""
        Se sei pronto per investire, ecco cosa fare:
        
        1. **Definisci i tuoi obiettivi**
           - Cosa vuoi ottenere?
           - Entro quando?
           - Quanto puoi investire regolarmente?
        
        2. **Determina il tuo profilo**
           - Orizzonte temporale
           - Tolleranza al rischio
           - Capacità di risparmio
        
        3. **Studia nei prossimi capitoli**
           - Asset allocation
           - Strumenti di investimento (ETF)
           - Piani di accumulo
           - Ribilanciamento
        
        4. **Inizia con semplicità**
           - Meglio un piano semplice seguito costantemente
           - Che un piano perfetto abbandonato
        
        ---
        
        💡 *Ricorda: l'investimento è una maratona, non uno sprint.*
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
