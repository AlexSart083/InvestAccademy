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
from capitoli import capitolo_01, capitolo_02

# Dizionario dei capitoli disponibili
CAPITOLI = {
    1: {
        "titolo": "Introduzione alla finanza personale",
        "modulo": capitolo_01
    },
    2: {
        "titolo": "Interesse, inflazione e rischio",
        "modulo": capitolo_02
    }
}


def render_home():
    """Pagina principale"""
    st.title("📊 InvestAccademy")
    st.subheader("Il tuo corso di finanza personale")
    
    st.markdown("""
    Benvenuto in **InvestAccademy**, un corso pratico per imparare a gestire 
    le tue finanze personali in modo consapevole e sostenibile.
    
    ---
    
    ### 📚 Cosa imparerai
    
    - Controllare il tuo cash flow mensile
    - Comprendere interesse composto e inflazione
    - Costruire un fondo di emergenza
    - Gestire i debiti in modo strategico
    - Investire con consapevolezza
    - Evitare gli errori comportamentali più comuni
    
    ---
    
    ### 📖 Capitoli disponibili
    """)
    
    cols = st.columns(2)
    for i, (num, cap) in enumerate(CAPITOLI.items()):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"**Capitolo {num}**")
                st.markdown(f"### {cap['titolo']}")
                if st.button(f"Inizia →", key=f"btn_cap_{num}"):
                    st.session_state.pagina = f"capitolo_{num}"
                    st.rerun()
    
    st.markdown("---")
    st.caption("© InvestAccademy - Costruisci il tuo futuro finanziario")


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
        
        for num, cap in CAPITOLI.items():
            if st.button(
                f"{num}. {cap['titolo']}", 
                key=f"nav_{num}",
                use_container_width=True
            ):
                st.session_state.pagina = f"capitolo_{num}"
                st.rerun()
        
        st.markdown("---")
        st.caption("Versione 0.1.0")
    
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
