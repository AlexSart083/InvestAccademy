"""
Capitolo 2: Interesse, inflazione e rischio
InvestAccademy - Corso di Finanza Personale
"""

import streamlit as st

# Metadata
CAPITOLO_NUM = 2
TITOLO = "Interesse, inflazione e rischio"

OBIETTIVI = [
    "Calcolare interesse semplice e interesse composto",
    "Comprendere come l'inflazione influisce sul potere d'acquisto",
    "Distinguere tra rendimento nominale e rendimento reale",
    "Valutare il rapporto tra rischio e rendimento negli investimenti",
    "Comprendere il ruolo della diversificazione"
]

# Quiz
QUIZ = [
    {
        "id": 1,
        "domanda": "Qual è la formula dell'interesse semplice?",
        "tipo": "scelta_multipla",
        "opzioni": ["I = P × (1 + r)^t", "I = P × r × t", "I = P / (r × t)", "I = P + r + t"],
        "risposta_corretta": "I = P × r × t",
        "spiegazione": "L'interesse semplice si calcola moltiplicando capitale per tasso per tempo."
    },
    {
        "id": 2,
        "domanda": "Qual è la formula del montante con interesse composto?",
        "tipo": "scelta_multipla",
        "opzioni": ["A = P + (r × t)", "A = P × r × t", "A = P × (1 + r)^t", "A = P / (1 + r)^t"],
        "risposta_corretta": "A = P × (1 + r)^t",
        "spiegazione": "Il montante composto cresce esponenzialmente grazie alla capitalizzazione degli interessi."
    },
    {
        "id": 3,
        "domanda": "Se il rendimento nominale è 6% e l'inflazione 3%, qual è il rendimento reale approssimato?",
        "tipo": "numero",
        "risposta_corretta": 3,
        "spiegazione": "Rendimento reale ≈ 6% - 3% = 3%"
    },
    {
        "id": 4,
        "domanda": "La diversificazione elimina completamente il rischio.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "La diversificazione riduce il rischio specifico ma non elimina il rischio di mercato (sistematico)."
    }
]


def interesse_semplice(capitale: float, tasso: float, anni: int) -> float:
    """Calcola l'interesse semplice"""
    return capitale * (tasso / 100) * anni


def montante_semplice(capitale: float, tasso: float, anni: int) -> float:
    """Calcola il montante con interesse semplice"""
    return capitale + interesse_semplice(capitale, tasso, anni)


def montante_composto(capitale: float, tasso: float, anni: int) -> float:
    """Calcola il montante con interesse composto"""
    return capitale * ((1 + tasso / 100) ** anni)


def rendimento_reale(nominale: float, inflazione: float) -> float:
    """Calcola il rendimento reale approssimato"""
    return nominale - inflazione


def evoluzione_capitale(capitale: float, tasso: float, anni: int) -> list:
    """Restituisce l'evoluzione anno per anno"""
    evoluzione = []
    cap = capitale
    for anno in range(1, anni + 1):
        interesse = cap * (tasso / 100)
        cap = cap + interesse
        evoluzione.append({
            "anno": anno,
            "capitale": round(cap, 2),
            "interesse": round(interesse, 2)
        })
    return evoluzione


def render_contenuto():
    """Renderizza il contenuto teorico"""
    
    st.markdown("""
    ## Il valore del tempo e dell'interesse
    
    Uno degli errori più comuni nella gestione del denaro è **sottovalutare il ruolo del tempo**. 
    Il tempo, combinato con l'interesse composto, è il principale alleato dell'investitore 
    di lungo periodo.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 📊 Interesse Semplice")
            st.markdown("""
            Gli interessi sono calcolati **solo sul capitale iniziale**.
            
            **Formula:** `I = P × r × t`
            
            - P = capitale iniziale
            - r = tasso annuo (decimale)
            - t = tempo in anni
            """)
            st.latex(r"I = P \times r \times t")
    
    with col2:
        with st.container(border=True):
            st.markdown("### 📈 Interesse Composto")
            st.markdown("""
            Gli interessi vengono **reinvestiti** e producono nuovi interessi.
            
            **Formula:** `A = P × (1 + r)^t`
            
            - A = capitale finale
            - P = capitale iniziale
            - r = tasso annuo
            - t = tempo in anni
            """)
            st.latex(r"A = P \times (1 + r)^t")
    
    st.markdown("---")
    
    st.markdown("""
    ## L'effetto dell'inflazione
    
    L'inflazione rappresenta l'**aumento generale dei prezzi** nel tempo. 
    Il suo effetto principale è la **riduzione del potere d'acquisto** del denaro.
    
    > Con €100 oggi puoi comprare più beni e servizi rispetto a quanto potrai 
    > fare con gli stessi €100 tra dieci anni.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### Rendimento Nominale")
            st.markdown("Il rendimento **dichiarato** dell'investimento")
    
    with col2:
        with st.container(border=True):
            st.markdown("### Rendimento Reale")
            st.markdown("Il rendimento **corretto per l'inflazione**")
            st.latex(r"\text{Rend. reale} \approx \text{Rend. nominale} - \text{Inflazione}")
    
    st.markdown("---")
    
    st.markdown("""
    ## Rischio e Diversificazione
    
    Il **rischio** negli investimenti è la variabilità dei rendimenti nel tempo.
    
    | Tipo di investimento | Rendimento atteso | Rischio |
    |---------------------|-------------------|---------|
    | Azioni | Alto | Alto |
    | Obbligazioni | Medio | Medio |
    | Liquidità | Basso | Basso |
    
    La **diversificazione** consiste nel distribuire il capitale tra più strumenti 
    per ridurre il rischio specifico. Non elimina il rischio di mercato, ma rende 
    il portafoglio più resiliente.
    """)


def render_calcolatore():
    """Renderizza i calcolatori"""
    
    st.markdown("## 🧮 Calcolatori")
    
    calc_type = st.radio(
        "Seleziona calcolatore:",
        ["Confronto Interessi", "Rendimento Reale", "Evoluzione Capitale"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if calc_type == "Confronto Interessi":
        render_calc_confronto()
    elif calc_type == "Rendimento Reale":
        render_calc_rendimento()
    else:
        render_calc_evoluzione()


def render_calc_confronto():
    """Calcolatore confronto interesse semplice vs composto"""
    
    st.markdown("### Confronto Interesse Semplice vs Composto")
    
    col1, col2 = st.columns(2)
    
    with col1:
        capitale = st.number_input(
            "💰 Capitale iniziale (€)",
            min_value=100.0,
            value=1000.0,
            step=100.0,
            key="cap2_capitale"
        )
        tasso = st.slider(
            "📊 Tasso annuo (%)",
            min_value=0.5,
            max_value=15.0,
            value=5.0,
            step=0.5,
            key="cap2_tasso"
        )
        anni = st.slider(
            "📅 Durata (anni)",
            min_value=1,
            max_value=40,
            value=10,
            key="cap2_anni"
        )
    
    with col2:
        mont_semp = montante_semplice(capitale, tasso, anni)
        mont_comp = montante_composto(capitale, tasso, anni)
        differenza = mont_comp - mont_semp
        
        st.markdown("### Risultati")
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric(
                "Interesse Semplice",
                f"€{mont_semp:,.2f}",
                f"+€{mont_semp - capitale:,.2f}"
            )
        with c2:
            st.metric(
                "Interesse Composto",
                f"€{mont_comp:,.2f}",
                f"+€{mont_comp - capitale:,.2f}"
            )
        
        st.success(f"💡 **Vantaggio composto:** €{differenza:,.2f} in più!")
        
        # Grafico comparativo
        import pandas as pd
        
        dati_grafico = []
        for a in range(anni + 1):
            dati_grafico.append({
                "Anno": a,
                "Semplice": montante_semplice(capitale, tasso, a),
                "Composto": montante_composto(capitale, tasso, a)
            })
        
        df = pd.DataFrame(dati_grafico)
        st.line_chart(df.set_index("Anno"))


def render_calc_rendimento():
    """Calcolatore rendimento reale"""
    
    st.markdown("### Rendimento Reale vs Nominale")
    
    col1, col2 = st.columns(2)
    
    with col1:
        rend_nom = st.slider(
            "📈 Rendimento nominale (%)",
            min_value=0.0,
            max_value=15.0,
            value=6.0,
            step=0.5,
            key="cap2_rend_nom"
        )
        inflazione = st.slider(
            "📉 Inflazione (%)",
            min_value=0.0,
            max_value=10.0,
            value=2.0,
            step=0.5,
            key="cap2_inflazione"
        )
        capitale_inv = st.number_input(
            "💰 Capitale investito (€)",
            min_value=100.0,
            value=10000.0,
            step=1000.0,
            key="cap2_cap_inv"
        )
        anni_inv = st.slider(
            "📅 Orizzonte (anni)",
            min_value=1,
            max_value=30,
            value=20,
            key="cap2_anni_inv"
        )
    
    with col2:
        rend_real = rendimento_reale(rend_nom, inflazione)
        
        mont_nominale = montante_composto(capitale_inv, rend_nom, anni_inv)
        mont_reale = montante_composto(capitale_inv, rend_real, anni_inv)
        perdita_inflazione = mont_nominale - mont_reale
        
        st.markdown("### Risultati")
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Rendimento nominale", f"{rend_nom:.1f}%")
            st.metric("Montante nominale", f"€{mont_nominale:,.2f}")
        with c2:
            st.metric("Rendimento reale", f"{rend_real:.1f}%")
            st.metric("Potere d'acquisto", f"€{mont_reale:,.2f}")
        
        if rend_real > 0:
            st.success(f"✅ Guadagno reale in {anni_inv} anni")
        elif rend_real == 0:
            st.warning(f"⚠️ Rendimento nullo: mantieni il potere d'acquisto")
        else:
            st.error(f"❌ Perdita di potere d'acquisto")
        
        st.info(f"💸 Perdita per inflazione: €{perdita_inflazione:,.2f}")


def render_calc_evoluzione():
    """Calcolatore evoluzione capitale"""
    
    st.markdown("### Evoluzione del Capitale nel Tempo")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        capitale = st.number_input(
            "💰 Capitale iniziale (€)",
            min_value=100.0,
            value=5000.0,
            step=500.0,
            key="cap2_evol_cap"
        )
        tasso = st.slider(
            "📊 Tasso annuo (%)",
            min_value=0.5,
            max_value=12.0,
            value=3.0,
            step=0.5,
            key="cap2_evol_tasso"
        )
        anni = st.slider(
            "📅 Durata (anni)",
            min_value=1,
            max_value=30,
            value=5,
            key="cap2_evol_anni"
        )
    
    with col2:
        evoluzione = evoluzione_capitale(capitale, tasso, anni)
        
        import pandas as pd
        df = pd.DataFrame(evoluzione)
        df.columns = ["Anno", "Capitale (€)", "Interesse anno (€)"]
        
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )
        
        montante_finale = evoluzione[-1]["capitale"]
        interesse_totale = montante_finale - capitale
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Montante finale", f"€{montante_finale:,.2f}")
        with c2:
            st.metric("Interessi totali", f"€{interesse_totale:,.2f}")


def render_quiz():
    """Renderizza il quiz di verifica"""
    
    st.markdown("## 📝 Quiz di verifica")
    
    if "cap2_risposte" not in st.session_state:
        st.session_state.cap2_risposte = {}
    if "cap2_verificato" not in st.session_state:
        st.session_state.cap2_verificato = False
    
    for i, q in enumerate(QUIZ):
        with st.container(border=True):
            st.markdown(f"**Domanda {i+1}:** {q['domanda']}")
            
            if q["tipo"] == "vero_falso":
                risposta = st.radio(
                    "Seleziona:",
                    ["Vero", "Falso"],
                    key=f"cap2_q{q['id']}",
                    horizontal=True
                )
                st.session_state.cap2_risposte[q['id']] = risposta == "Vero"
                
            elif q["tipo"] == "scelta_multipla":
                risposta = st.radio(
                    "Seleziona:",
                    q["opzioni"],
                    key=f"cap2_q{q['id']}"
                )
                st.session_state.cap2_risposte[q['id']] = risposta
                
            elif q["tipo"] == "numero":
                risposta = st.number_input(
                    "Inserisci il valore:",
                    key=f"cap2_q{q['id']}",
                    step=0.5
                )
                st.session_state.cap2_risposte[q['id']] = risposta
            
            if st.session_state.cap2_verificato:
                user_ans = st.session_state.cap2_risposte.get(q['id'])
                if q["tipo"] == "numero":
                    corretto = abs(user_ans - q["risposta_corretta"]) < 0.5
                else:
                    corretto = user_ans == q["risposta_corretta"]
                
                if corretto:
                    st.success(f"✅ Corretto! {q['spiegazione']}")
                else:
                    st.error(f"❌ Sbagliato. Risposta corretta: {q['risposta_corretta']}")
                    st.info(q['spiegazione'])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Verifica risposte", type="primary", use_container_width=True, key="cap2_verifica"):
            st.session_state.cap2_verificato = True
            st.rerun()
    with col2:
        if st.button("🔄 Ricomincia", use_container_width=True, key="cap2_reset"):
            st.session_state.cap2_verificato = False
            st.session_state.cap2_risposte = {}
            st.rerun()


def render_takeaways():
    """Renderizza i punti chiave"""
    
    st.markdown("## 💡 Punti chiave")
    
    takeaways = [
        "Il tempo è il principale alleato dell'investitore grazie all'interesse composto",
        "L'interesse composto genera crescita esponenziale reinvestendo gli interessi",
        "L'inflazione erode il potere d'acquisto: considera sempre il rendimento reale",
        "Maggiore rendimento atteso = maggiore rischio (trade-off rischio/rendimento)",
        "La diversificazione riduce il rischio specifico ma non elimina quello di mercato"
    ]
    
    for t in takeaways:
        st.markdown(f"- {t}")
    
    st.markdown("---")
    
    # Esercizio guidato
    with st.expander("📝 Esercizio guidato"):
        st.markdown("""
        **Domanda:** Quanto diventa un capitale di €5.000 investito al 3% annuo 
        composto per 20 anni?
        
        **Soluzione:**
        """)
        
        risultato = montante_composto(5000, 3, 20)
        st.latex(r"A = 5.000 \times (1 + 0,03)^{20} \approx " + f"€{risultato:,.2f}")
        
        st.info("💡 Osserva come il tempo incida più del tasso stesso!")


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
