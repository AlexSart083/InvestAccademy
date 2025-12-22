"""
Capitolo 16: Errori comuni negli investimenti e checklist finale
InvestAccademy - Corso di Finanza Personale
"""

import streamlit as st
import pandas as pd

# Metadata
CAPITOLO_NUM = 16
TITOLO = "Errori comuni negli investimenti e checklist finale"

OBIETTIVI = [
    "Riconoscere gli errori più comuni che compromettono i risultati",
    "Capire perché anche buone strategie possono fallire nell'esecuzione",
    "Utilizzare una checklist pratica per valutare le proprie decisioni",
    "Costruire un sistema semplice per evitare errori ricorrenti",
    "Consolidare un approccio disciplinato di lungo periodo"
]

QUIZ = [
    {
        "id": 1,
        "domanda": "Perché evitare errori è più importante che cercare rendimenti elevati?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Perché gli errori hanno un impatto negativo difficile da recuperare",
            "Perché i rendimenti elevati non esistono",
            "Non è più importante",
            "Perché costa meno"
        ],
        "risposta_corretta": "Perché gli errori hanno un impatto negativo difficile da recuperare",
        "spiegazione": "Evitare grandi perdite è più importante che cercare grandi guadagni: una perdita del 50% richiede un guadagno del 100% per recuperare."
    },
    {
        "id": 2,
        "domanda": "Qual è il rischio principale di cambiare spesso strategia?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "Impedisce al tempo e all'interesse composto di lavorare",
            "Costa troppo",
            "Non c'è rischio",
            "Migliora i risultati"
        ],
        "risposta_corretta": "Impedisce al tempo e all'interesse composto di lavorare",
        "spiegazione": "Cambiare strategia continuamente impedisce di beneficiare della costanza e del tempo, fattori chiave per il successo."
    },
    {
        "id": 3,
        "domanda": "A cosa serve una checklist prima di investire?",
        "tipo": "scelta_multipla",
        "opzioni": [
            "A mantenere disciplina e coerenza con il piano",
            "A complicare le decisioni",
            "A perdere tempo",
            "Non serve"
        ],
        "risposta_corretta": "A mantenere disciplina e coerenza con il piano",
        "spiegazione": "Una checklist aiuta a filtrare le decisioni emotive e a verificare la coerenza con il piano prestabilito."
    },
    {
        "id": 4,
        "domanda": "Investire senza un piano scritto aumenta il rischio di errori comportamentali.",
        "tipo": "vero_falso",
        "risposta_corretta": True,
        "spiegazione": "Senza un piano scritto, le decisioni sono guidate dalle emozioni del momento invece che da una strategia razionale."
    },
    {
        "id": 5,
        "domanda": "È meglio una strategia perfetta cambiata spesso che una buona strategia seguita costantemente.",
        "tipo": "vero_falso",
        "risposta_corretta": False,
        "spiegazione": "La costanza è più importante della perfezione. Una strategia buona seguita con disciplina batte una perfetta abbandonata."
    }
]


def valuta_readiness(risposte: dict) -> dict:
    """Valuta la preparazione dell'investitore"""
    
    punteggio = sum(risposte.values())
    max_punteggio = len(risposte) * 3
    percentuale = (punteggio / max_punteggio) * 100
    
    if percentuale >= 80:
        livello = "Pronto per investire"
        descrizione = "Hai una solida base e sei pronto per iniziare o continuare a investire con consapevolezza."
        colore = "🟢"
        prossimi_passi = [
            "Implementa il tuo piano di investimento",
            "Mantieni la disciplina nel tempo",
            "Rivedi il piano annualmente",
            "Continua a formarti"
        ]
    elif percentuale >= 60:
        livello = "Quasi pronto"
        descrizione = "Hai una buona base ma ci sono ancora alcuni aspetti da consolidare prima di investire."
        colore = "🟡"
        prossimi_passi = [
            "Completa il fondo emergenze",
            "Definisci meglio gli obiettivi",
            "Studia gli aspetti meno chiari",
            "Fai un piano scritto dettagliato"
        ]
    else:
        livello = "Serve più preparazione"
        descrizione = "È importante consolidare le basi prima di investire per evitare errori costosi."
        colore = "🔴"
        prossimi_passi = [
            "Concentrati su risparmio e fondo emergenze",
            "Studia i capitoli che hai trovato più difficili",
            "Non investire ancora - costruisci le fondamenta",
            "Considera di consultare un professionista"
        ]
    
    return {
        "punteggio": punteggio,
        "max_punteggio": max_punteggio,
        "percentuale": percentuale,
        "livello": livello,
        "descrizione": descrizione,
        "colore": colore,
        "prossimi_passi": prossimi_passi
    }


def render_contenuto():
    """Renderizza il contenuto teorico"""
    
    st.markdown("""
    ## Perché gli errori contano più delle scelte giuste
    
    Negli investimenti, **evitare grandi errori è spesso più importante che fare scelte brillanti**.
    
    Anche una strategia solida può produrre risultati mediocri se viene:
    - Applicata in modo incoerente
    - Interrotta nei momenti sbagliati
    - Modificata continuamente
    
    > La maggior parte degli errori è **ripetitiva e prevedibile**. 
    > Proprio per questo può essere prevenuta con regole semplici e processi chiari.
    """)
    
    st.markdown("---")
    
    st.markdown("## I principali errori da evitare")
    
    # Errore 1
    with st.container(border=True):
        st.markdown("### 1️⃣ Investire senza un piano")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            Entrare sui mercati senza obiettivi, orizzonte temporale e asset allocation 
            definiti porta a decisioni impulsive.
            
            **Conseguenze:**
            - Vendite in panico
            - Acquisti emotivi
            - Risultati casuali
            - Abbandono prematuro
            """)
        
        with col2:
            st.error("❌ Errore")
            st.success("✅ **Rimedio:**\nScrivi un piano di investimento, anche semplice, PRIMA di investire")
    
    # Errore 2
    with st.container(border=True):
        st.markdown("### 2️⃣ Cercare di prevedere il mercato (Market Timing)")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            Il market timing è uno degli errori più diffusi e costosi.
            
            **Conseguenze tipiche:**
            - Ingressi tardivi (dopo i rialzi)
            - Uscite premature (durante i ribassi)
            - Rendimento inferiore rispetto a strategie semplici
            - Costi e tasse elevate
            
            *"Il momento migliore per piantare un albero era 20 anni fa. 
            Il secondo momento migliore è oggi."*
            """)
        
        with col2:
            st.error("❌ Errore")
            st.success("✅ **Rimedio:**\nConcentrati sul processo, non sulle previsioni. Usa PAC.")
    
    # Errore 3
    with st.container(border=True):
        st.markdown("### 3️⃣ Reagire emotivamente alla volatilità")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            Vendere durante i ribassi e comprare durante l'euforia **distrugge valore**.
            
            **Il ciclo distruttivo:**
            1. Mercato sale → Euforia → Compro
            2. Mercato scende → Panico → Vendo
            3. Ripeti → Perdite cumulate
            
            **Dati:** L'investitore medio sottoperforma il mercato proprio 
            per questo comportamento.
            """)
        
        with col2:
            st.error("❌ Errore")
            st.success("✅ **Rimedio:**\nAutomatizza PAC e ribilanciamenti. Riduci la frequenza di controllo.")
    
    # Errore 4
    with st.container(border=True):
        st.markdown("### 4️⃣ Ignorare costi e fiscalità")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            Costi elevati e tasse frequenti **erodono il rendimento composto**.
            
            **Esempio reale:**
            - €10.000 per 30 anni al 6%
            - Con 0,2% di costi: €53.000
            - Con 2% di costi: €32.000
            - **Differenza: €21.000 (40%)**
            
            Un errore da €21.000 per non aver prestato attenzione ai costi.
            """)
        
        with col2:
            st.error("❌ Errore")
            st.success("✅ **Rimedio:**\nScegli strumenti efficienti (ETF) e limita le operazioni")
    
    # Errore 5
    with st.container(border=True):
        st.markdown("### 5️⃣ Sovraconcentrazione")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            Puntare troppo su:
            - Singoli titoli
            - Singoli settori
            - Singole aree geografiche
            
            ...aumenta il **rischio specifico** senza aumentare il rendimento atteso.
            
            *"Non mettere tutte le uova nello stesso paniere"*
            """)
        
        with col2:
            st.error("❌ Errore")
            st.success("✅ **Rimedio:**\nDiversificazione ampia e coerente con asset allocation")
    
    # Errore 6
    with st.container(border=True):
        st.markdown("### 6️⃣ Cambiare strategia troppo spesso")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            Saltare da una strategia all'altra impedisce al **tempo** di lavorare.
            
            **Conseguenze:**
            - Nessuna strategia ha il tempo di funzionare
            - Costi e tasse per cambiamenti continui
            - Risultati casuali
            - Frustrazione crescente
            
            *La costanza batte la perfezione.*
            """)
        
        with col2:
            st.error("❌ Errore")
            st.success("✅ **Rimedio:**\nModifica solo se cambiano obiettivi o situazione personale")
    
    st.markdown("---")
    
    st.markdown("## La checklist dell'investitore consapevole")
    
    st.markdown("""
    Usa questa checklist **prima di prendere decisioni importanti**.
    """)
    
    # Sezione 1: Piano e obiettivi
    with st.container(border=True):
        st.markdown("### 📋 Piano e Obiettivi")
        st.markdown("""
        - [ ] Ho obiettivi chiari e misurabili?
        - [ ] L'orizzonte temporale è definito?
        - [ ] Il capitale investito non mi serve nel breve termine?
        - [ ] Ho un fondo emergenze adeguato (3-6 mesi)?
        """)
    
    # Sezione 2: Struttura portafoglio
    with st.container(border=True):
        st.markdown("### 🎯 Struttura del Portafoglio")
        st.markdown("""
        - [ ] L'asset allocation riflette il mio profilo di rischio?
        - [ ] Il portafoglio è adeguatamente diversificato?
        - [ ] Conosco e comprendo ogni strumento che possiedo?
        - [ ] L'allocazione è sostenibile anche durante i ribassi?
        """)
    
    # Sezione 3: Processo
    with st.container(border=True):
        st.markdown("### ⚙️ Processo")
        st.markdown("""
        - [ ] Ho regole scritte per investimenti e ribilanciamenti?
        - [ ] Le decisioni sono automatizzate quando possibile?
        - [ ] Ho definito quando e come ribilanciare?
        - [ ] Controllo il portafoglio con frequenza ragionevole (non quotidiana)?
        """)
    
    # Sezione 4: Costi e tasse
    with st.container(border=True):
        st.markdown("### 💰 Costi e Tasse")
        st.markdown("""
        - [ ] Conosco i costi totali dei miei strumenti?
        - [ ] Sto considerando l'impatto fiscale delle operazioni?
        - [ ] Ho scelto strumenti efficienti (TER < 0,5%)?
        - [ ] Evito operazioni inutili che generano tasse?
        """)
    
    # Sezione 5: Comportamento
    with st.container(border=True):
        st.markdown("### 🧠 Comportamento")
        st.markdown("""
        - [ ] Sto reagendo a un'emozione o seguendo il piano?
        - [ ] Questa decisione sarà sensata anche tra 10 anni?
        - [ ] Ho aspettato almeno 24 ore prima di decidere?
        - [ ] Ho scritto il motivo di questa decisione?
        """)
    
    st.success("""
    ✅ **Regola d'oro:**
    
    Se la risposta a una di queste domande è "No", **fermati e rifletti** prima di procedere.
    """)
    
    st.markdown("---")
    
    st.markdown("## Esempio pratico: filtro decisionale")
    
    with st.container(border=True):
        st.markdown("""
        **Scenario:** Il mercato è sceso del 20% e sei tentato di vendere.
        
        **Applica la checklist:**
        
        1. **È cambiato qualcosa nei miei obiettivi?** → No
        2. **Il piano prevedeva questa volatilità?** → Sì
        3. **Sto agendo per paura?** → Sì
        4. **Questa decisione sarà sensata tra 10 anni?** → No
        5. **È coerente con il mio piano scritto?** → No
        
        **Conclusione:** La decisione va **rimandata**. È guidata dall'emozione, non dalla razionalità.
        
        **Azione corretta:** Seguire il piano, mantenere o continuare il PAC.
        """)


def render_calcolatore():
    """Renderizza gli strumenti di autovalutazione"""
    
    st.markdown("## 🎯 Autovalutazione Finale")
    
    calc_type = st.radio(
        "Seleziona:",
        ["Scorecard Preparazione", "Piano d'Azione Personale"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if calc_type == "Scorecard Preparazione":
        render_scorecard()
    else:
        render_piano_azione()


def render_scorecard():
    """Scorecard di autovalutazione della preparazione"""
    
    st.markdown("### Scorecard: Sei Pronto per Investire?")
    
    st.markdown("""
    Valuta onestamente il tuo livello di preparazione in ciascuna area.
    
    **Scala:**
    - 1 = Non preparato
    - 2 = Preparazione base
    - 3 = Buona preparazione
    """)
    
    aree = [
        {
            "categoria": "Fondamentali",
            "domande": [
                "Ho un fondo emergenze di almeno 3-6 mesi",
                "Non ho debiti ad alto tasso (>10%)",
                "Il capitale da investire non mi servirà per almeno 5 anni",
                "Ho un reddito stabile o fonti di entrata regolari"
            ]
        },
        {
            "categoria": "Conoscenze",
            "domande": [
                "Comprendo la differenza tra azioni e obbligazioni",
                "So cos'è e come funziona l'asset allocation",
                "Comprendo che le oscillazioni sono normali",
                "So che non posso prevedere il mercato"
            ]
        },
        {
            "categoria": "Piano",
            "domande": [
                "Ho obiettivi finanziari chiari e scritti",
                "Ho definito la mia asset allocation target",
                "Ho un piano di investimento documentato",
                "So quando e come ribilanciare"
            ]
        },
        {
            "categoria": "Psicologia",
            "domande": [
                "Accetto l'idea di vedere il capitale oscillare",
                "Non venderei in panico durante un ribasso del 30%",
                "Sono disposto a seguire un piano di lungo periodo",
                "Ho regole scritte per gestire le emozioni"
            ]
        }
    ]
    
    risposte = {}
    
    for i, area in enumerate(aree):
        st.markdown(f"### {area['categoria']}")
        
        for j, domanda in enumerate(area['domande']):
            key = f"{i}_{j}"
            risposta = st.radio(
                domanda,
                [1, 2, 3],
                format_func=lambda x: {1: "1 - Non preparato", 2: "2 - Base", 3: "3 - Buono"}[x],
                key=f"cap16_score_{key}",
                horizontal=True
            )
            risposte[key] = risposta
        
        st.markdown("---")
    
    if st.button("📊 Calcola Punteggio", type="primary", use_container_width=True):
        risultato = valuta_readiness(risposte)
        
        st.markdown("### 🎯 Risultato Valutazione")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.metric("Punteggio", f"{risultato['punteggio']}/{risultato['max_punteggio']}")
            st.metric("Percentuale", f"{risultato['percentuale']:.0f}%")
            st.markdown(f"## {risultato['colore']} {risultato['livello']}")
        
        with col2:
            st.markdown(f"**{risultato['descrizione']}**")
            
            st.markdown("#### 📋 Prossimi Passi")
            for passo in risultato['prossimi_passi']:
                st.markdown(f"- {passo}")
        
        # Feedback specifico
        if risultato['percentuale'] >= 80:
            st.success("""
            ✅ **Ottimo lavoro!** Hai una solida preparazione.
            
            Sei pronto per implementare il tuo piano di investimento con consapevolezza.
            Mantieni la disciplina e rivedi periodicamente il piano.
            """)
        elif risultato['percentuale'] >= 60:
            st.warning("""
            ⚠️ **Sei sulla buona strada**, ma ci sono ancora aspetti da consolidare.
            
            Prima di investire somme significative:
            - Completa il fondo emergenze
            - Approfondisci gli aspetti meno chiari
            - Scrivi un piano dettagliato
            """)
        else:
            st.error("""
            🔴 **Attenzione:** È importante consolidare le basi prima di investire.
            
            Concentrati su:
            1. Costruire il fondo emergenze
            2. Studiare i capitoli fondamentali
            3. Stabilizzare la situazione finanziaria
            
            Non investire finché non hai almeno il 60% in questa valutazione.
            """)
        
        # Dettaglio per categoria
        st.markdown("---")
        st.markdown("### 📊 Dettaglio per Categoria")
        
        categorie_score = {}
        for i, area in enumerate(aree):
            punteggio_cat = sum([risposte[f"{i}_{j}"] for j in range(len(area['domande']))])
            max_cat = len(area['domande']) * 3
            perc_cat = (punteggio_cat / max_cat) * 100
            categorie_score[area['categoria']] = perc_cat
        
        df_categorie = pd.DataFrame({
            "Categoria": list(categorie_score.keys()),
            "Preparazione (%)": list(categorie_score.values())
        })
        
        st.bar_chart(df_categorie.set_index("Categoria"))
        
        # Identifica aree deboli
        aree_deboli = [cat for cat, perc in categorie_score.items() if perc < 70]
        if aree_deboli:
            st.info(f"""
            💡 **Aree da rafforzare:** {", ".join(aree_deboli)}
            
            Rivedi i capitoli relativi a queste aree prima di procedere.
            """)


def render_piano_azione():
    """Template piano d'azione personale"""
    
    st.markdown("### 📝 Il Tuo Piano d'Azione Personale")
    
    st.markdown("""
    Compila questo piano per consolidare tutto ciò che hai imparato e creare 
    una roadmap chiara per i prossimi passi.
    """)
    
    with st.expander("🎯 1. Situazione Attuale", expanded=True):
        st.markdown("**Dove sei oggi:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.text_area("Situazione finanziaria", placeholder="Reddito, spese, debiti, risparmio attuale...")
            st.text_area("Conoscenze acquisite", placeholder="Cosa ho imparato da questo corso...")
        
        with col2:
            st.text_area("Punti di forza", placeholder="Cosa sto già facendo bene...")
            st.text_area("Aree da migliorare", placeholder="Cosa devo ancora consolidare...")
    
    with st.expander("🎯 2. Obiettivi (prossimi 12 mesi)"):
        st.markdown("**Definisci 3-5 obiettivi SMART:**")
        
        for i in range(5):
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                st.text_input(f"Obiettivo {i+1}", key=f"cap16_obj_{i}")
            with col2:
                st.text_input("Importo/Misura", key=f"cap16_obj_mis_{i}")
            with col3:
                st.date_input("Scadenza", key=f"cap16_obj_data_{i}")
    
    with st.expander("🎯 3. Piano d'Azione Mensile"):
        st.markdown("**Azioni concrete che farò ogni mese:**")
        
        azioni = [
            "Accantonamento fondo emergenze",
            "Versamento PAC",
            "Revisione spese",
            "Formazione finanziaria",
            "Altro"
        ]
        
        for azione in azioni:
            col1, col2 = st.columns([2, 1])
            with col1:
                st.checkbox(azione, key=f"cap16_azione_{azione}")
            with col2:
                st.text_input("€ o dettaglio", key=f"cap16_azione_det_{azione}")
    
    with st.expander("🎯 4. Regole di Investimento"):
        st.markdown("**Le mie regole non negoziabili:**")
        
        st.text_area("Asset allocation target", placeholder="Es: 60% azioni, 35% obbligazioni, 5% liquidità")
        st.text_area("Frequenza controllo portafoglio", placeholder="Es: Trimestrale")
        st.text_area("Quando ribilancio", placeholder="Es: Annualmente o quando scostamento > 5%")
        st.text_area("In caso di ribasso del 20% farò", placeholder="Es: Mantengo e continuo PAC")
        st.text_area("NON farò mai", placeholder="Es: Vendere in panico, inseguire mode, trading frequente")
    
    with st.expander("🎯 5. Milestone e Revisioni"):
        st.markdown("**Quando rivederò e aggiornerò il piano:**")
        
        st.checkbox("Revisione trimestrale (controllo aderenza al piano)")
        st.checkbox("Revisione semestrale (verifica obiettivi)")
        st.checkbox("Revisione annuale (aggiornamento strategico completo)")
        st.checkbox("In caso di cambiamenti significativi (lavoro, famiglia, salute)")
    
    if st.button("💾 Salva Piano", type="primary"):
        st.success("""
        ✅ **Piano salvato!**
        
        Stampa o esporta questo piano e conservalo. Rileggilo:
        - Ogni trimestre per verificare i progressi
        - Nei momenti di dubbio o stress
        - Prima di prendere decisioni importanti
        """)


def render_quiz():
    """Renderizza il quiz di verifica"""
    
    st.markdown("## 📝 Quiz di verifica")
    
    if "cap16_risposte" not in st.session_state:
        st.session_state.cap16_risposte = {}
    if "cap16_verificato" not in st.session_state:
        st.session_state.cap16_verificato = False
    
    for i, q in enumerate(QUIZ):
        with st.container(border=True):
            st.markdown(f"**Domanda {i+1}:** {q['domanda']}")
            
            if q["tipo"] == "vero_falso":
                risposta = st.radio(
                    "Seleziona:",
                    ["Vero", "Falso"],
                    key=f"cap16_q{q['id']}",
                    horizontal=True
                )
                st.session_state.cap16_risposte[q['id']] = risposta == "Vero"
                
            elif q["tipo"] == "scelta_multipla":
                risposta = st.radio(
                    "Seleziona:",
                    q["opzioni"],
                    key=f"cap16_q{q['id']}"
                )
                st.session_state.cap16_risposte[q['id']] = risposta
            
            if st.session_state.cap16_verificato:
                user_ans = st.session_state.cap16_risposte.get(q['id'])
                corretto = user_ans == q["risposta_corretta"]
                
                if corretto:
                    st.success(f"✅ Corretto! {q['spiegazione']}")
                else:
                    st.error(f"❌ Sbagliato. Risposta corretta: {q['risposta_corretta']}")
                    st.info(q['spiegazione'])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Verifica risposte", type="primary", use_container_width=True, key="cap16_verifica"):
            st.session_state.cap16_verificato = True
            st.rerun()
    with col2:
        if st.button("🔄 Ricomincia", use_container_width=True, key="cap16_reset"):
            st.session_state.cap16_verificato = False
            st.session_state.cap16_risposte = {}
            st.rerun()


def render_takeaways():
    """Renderizza i punti chiave e la conclusione"""
    
    st.markdown("## 💡 Punti chiave finali")
    
    takeaways = [
        "Evitare grandi errori è più importante che cercare grandi guadagni",
        "La costanza batte la perfezione negli investimenti",
        "Una checklist aiuta a filtrare le decisioni emotive",
        "Il piano scritto è la tua bussola nei momenti difficili",
        "L'automazione riduce drasticamente gli errori comportamentali",
        "Modificare il piano solo se cambiano obiettivi o situazione personale",
        "Il tempo è l'alleato più potente, ma serve disciplina per sfruttarlo"
    ]
    
    for t in takeaways:
        st.markdown(f"- {t}")
    
    st.markdown("---")
    
    st.markdown("## 🎯 Costruire una vita finanziaria consapevole")
    
    st.success("""
    ### Complimenti per essere arrivato fino qui! 🎉
    
    Hai fatto qualcosa che pochissime persone fanno davvero: **ti sei preso la responsabilità 
    della tua vita finanziaria**.
    
    Questo corso non promette scorciatoie o rendimenti miracolosi. 
    Ti ha fornito un **metodo** per:
    - Prendere decisioni migliori
    - Evitare errori costosi
    - Costruire nel tempo una relazione sana con il denaro
    """)
    
    st.markdown("---")
    
    st.markdown("## 📚 La finanza personale è un processo")
    
    st.info("""
    **Ricorda:**
    
    La finanza personale non è qualcosa che "si sistema una volta per tutte".
    
    È un **processo continuo**, fatto di:
    - Scelte ripetute
    - Piccoli aggiustamenti
    - Disciplina nel tempo
    
    Non serve fare tutto subito. Serve fare le cose giuste con costanza.
    """)
    
    st.markdown("---")
    
    st.markdown("## 🏆 Il vero vantaggio competitivo è il comportamento")
    
    st.markdown("""
    Nel lungo periodo, ciò che farà la differenza **non sarà:**
    - L'ETF migliore
    - Il momento perfetto
    - La previsione più brillante
    
    Sarà la tua capacità di:
    - Restare investito
    - Gestire le emozioni
    - Seguire il piano anche quando è difficile
    
    > **La disciplina batte il talento quando si parla di denaro.**
    """)
    
    st.markdown("---")
    
    st.markdown("## 📖 Usa questo corso come strumento")
    
    st.warning("""
    **Torna a queste pagine:**
    - Quando il mercato scende
    - Quando ti senti insicuro
    - Quando sei tentato di cambiare tutto
    
    Usa le checklist, rileggi i takeaway, rivedi il tuo piano.
    
    Questo corso non vuole dirti cosa fare domani, ma aiutarti a prendere 
    **decisioni migliori per molti anni**.
    """)
    
    st.markdown("---")
    
    st.markdown("## 🚀 Inizia (o continua) oggi")
    
    st.success("""
    ### Se c'è un momento giusto per mettere ordine nelle proprie finanze, è sempre **adesso**.
    
    **Non aspettare** di sapere tutto. Non aspettare il momento perfetto.
    
    **I prossimi passi:**
    1. Definisci un piano semplice
    2. Automatizza ciò che puoi
    3. Resta coerente
    4. Rivedi periodicamente
    
    ---
    
    **Il futuro finanziario non si prevede: si costruisce.** 🏗️
    
    Buona fortuna nel tuo percorso! 💪
    """)
    
    st.balloons()


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
        "🎯 Autovalutazione", 
        "📝 Quiz",
        "🏆 Conclusione"
    ])
    
    with tab1:
        render_contenuto()
    
    with tab2:
        render_calcolatore()
    
    with tab3:
        render_quiz()
    
    with tab4:
        render_takeaways()
