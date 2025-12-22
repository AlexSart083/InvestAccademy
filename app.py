"""
InvestAccademy - Corso di Finanza Personale
App Streamlit per l'apprendimento della finanza personale
"""

import streamlit as st

# Configurazione pagina
st.set_page_config(
    page_title="InvestAccademy",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import dei capitoli
from capitoli import (
    capitolo_01, capitolo_02, capitolo_03, capitolo_04, 
    capitolo_05, capitolo_06, capitolo_07, capitolo_08,
    capitolo_09, capitolo_10, capitolo_11, capitolo_12,
    capitolo_13, capitolo_14, capitolo_15, capitolo_16
)

# Dizionario dei capitoli disponibili
CAPITOLI = {
    1: {
        "titolo": "Introduzione alla finanza personale",
        "modulo": capitolo_01
    },
    2: {
        "titolo": "Interesse, inflazione e rischio",
        "modulo": capitolo_02
    },
    3: {
        "titolo": "Risparmio e obiettivi finanziari",
        "modulo": capitolo_03
    },
    4: {
        "titolo": "Il fondo di emergenza",
        "modulo": capitolo_04
    },
    5: {
        "titolo": "Scelta del conto e struttura dei conti personali",
        "modulo": capitolo_05
    },
    6: {
        "titolo": "Gestione del debito: strategie e priorità",
        "modulo": capitolo_06
    },
    7: {
        "titolo": "Credito e punteggio creditizio",
        "modulo": capitolo_07
    },
    8: {
        "titolo": "Introduzione agli investimenti",
        "modulo": capitolo_08
    },
    9: {
        "titolo": "Rendimento, rischio e diversificazione",
        "modulo": capitolo_09
    },
    10: {
        "titolo": "Asset allocation e costruzione del portafoglio",
        "modulo": capitolo_10
    },
    11: {
        "titolo": "Strumenti di investimento: ETF, fondi e azioni",
        "modulo": capitolo_11
    },
    12: {
        "titolo": "Piani di accumulo (PAC) e investimenti periodici",
        "modulo": capitolo_12
    },
    13: {
        "titolo": "Ribilanciamento del portafoglio",
        "modulo": capitolo_13
    },
    14: {
        "titolo": "Fiscalità degli investimenti",
        "modulo": capitolo_14
    },
    15: {
        "titolo": "Psicologia dell'investitore e bias comportamentali",
        "modulo": capitolo_15
    },
    16: {
        "titolo": "Errori comuni e checklist finale",
        "modulo": capitolo_16
    }
}


def render_home():
    """Pagina principale"""
    st.title("📊 InvestAccademy")
    st.subheader("Il tuo corso completo di finanza personale")
    
    st.markdown("""
    Benvenuto in **InvestAccademy**, un corso pratico per imparare a gestire 
    le tue finanze personali in modo consapevole e sostenibile.
    
    ---
    
    ### 📚 Cosa imparerai
    
    **Fondamentali della finanza personale:**
    - Controllare il tuo cash flow mensile
    - Comprendere interesse composto e inflazione
    - Costruire un fondo di emergenza
    - Definire obiettivi finanziari SMART
    - Scegliere i conti giusti e strutturarli efficacemente
    
    **Gestione del credito:**
    - Gestire i debiti in modo strategico
    - Migliorare il tuo punteggio creditizio
    - Comprendere le strategie Snowball e Avalanche
    
    **Investimenti:**
    - Comprendere le basi degli investimenti
    - Applicare i principi di diversificazione
    - Costruire una corretta asset allocation
    - Scegliere gli strumenti giusti (ETF, fondi, azioni)
    - Implementare piani di accumulo (PAC)
    - Gestire il ribilanciamento del portafoglio
    
    **Ottimizzazione e disciplina:**
    - Ottimizzare la fiscalità degli investimenti
    - Riconoscere e gestire i bias comportamentali
    - Evitare gli errori comuni
    - Costruire un processo disciplinato di lungo periodo
    
    ---
    
    ### 📖 Capitoli disponibili
    """)
    
    # Organizza capitoli in 3 colonne
    cols = st.columns(3)
    for i, (num, cap) in enumerate(CAPITOLI.items()):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"**Capitolo {num}**")
                st.markdown(f"### {cap['titolo']}")
                if st.button(f"Inizia →", key=f"btn_cap_{num}", use_container_width=True):
                    st.session_state.pagina = f"capitolo_{num}"
                    st.rerun()
    
    st.markdown("---")
    st.caption("© InvestAccademy - Costruisci il tuo futuro finanziario con consapevolezza")


def main():
    # Inizializza stato sessione
    if "pagina" not in st.session_state:
        st.session_state.pagina = "home"
    
    # Sidebar navigazione
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/chart.png", width=80)
        st.title("InvestAccademy")
        st.markdown("---")
        
        if st.button("🏠 Home", use_container_width=True):
            st.session_state.pagina = "home"
            st.rerun()
        
        st.markdown("### 📖 Capitoli")
        
        # Organizza capitoli in sezioni
        st.markdown("**Fondamentali (1-5)**")
        for num in range(1, 6):
            cap = CAPITOLI[num]
            if st.button(
                f"{num}. {cap['titolo'][:30]}{'...' if len(cap['titolo']) > 30 else ''}", 
                key=f"nav_{num}",
                use_container_width=True
            ):
                st.session_state.pagina = f"capitolo_{num}"
                st.rerun()
        
        st.markdown("**Credito e debito (6-7)**")
        for num in range(6, 8):
            cap = CAPITOLI[num]
            if st.button(
                f"{num}. {cap['titolo'][:30]}{'...' if len(cap['titolo']) > 30 else ''}", 
                key=f"nav_{num}",
                use_container_width=True
            ):
                st.session_state.pagina = f"capitolo_{num}"
                st.rerun()
        
        st.markdown("**Investimenti (8-13)**")
        for num in range(8, 14):
            cap = CAPITOLI[num]
            if st.button(
                f"{num}. {cap['titolo'][:30]}{'...' if len(cap['titolo']) > 30 else ''}", 
                key=f"nav_{num}",
                use_container_width=True
            ):
                st.session_state.pagina = f"capitolo_{num}"
                st.rerun()
        
        st.markdown("**Ottimizzazione (14-16)**")
        for num in range(14, 17):
            cap = CAPITOLI[num]
            if st.button(
                f"{num}. {cap['titolo'][:30]}{'...' if len(cap['titolo']) > 30 else ''}", 
                key=f"nav_{num}",
                use_container_width=True
            ):
                st.session_state.pagina = f"capitolo_{num}"
                st.rerun()
        
        st.markdown("---")
        st.caption("Versione 1.0.0 - Corso completo")
    
    # Rendering pagina corrente
    if st.session_state.pagina == "home":
        render_home()
    elif st.session_state.pagina.startswith("capitolo_"):
        num_cap = int(st.session_state.pagina.split("_")[1])
        if num_cap in CAPITOLI:
            CAPITOLI[num_cap]["modulo"].render()
        else:
            st.error("Capitolo non trovato")
            render_home()


if __name__ == "__main__":
    main()
