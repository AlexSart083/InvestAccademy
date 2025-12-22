# 📊 InvestAccademy

Corso interattivo completo di finanza personale realizzato con Streamlit.

## 🚀 Deploy su Streamlit Cloud

1. Fai fork di questo repository su GitHub
2. Vai su [share.streamlit.io](https://share.streamlit.io)
3. Connetti il tuo account GitHub
4. Seleziona il repository e il file `app.py`
5. Clicca "Deploy"

## 📖 Struttura del corso

### Sezione 1: Fondamentali (Capitoli 1-5)

| # | Titolo | Contenuti principali |
|---|--------|---------------------|
| 1 | Introduzione alla finanza personale | Cash flow, priorità finanziarie, sostenibilità |
| 2 | Interesse, inflazione e rischio | Interesse semplice/composto, rendimento reale, diversificazione |
| 3 | Risparmio e obiettivi finanziari | Metodo SMART, piano di risparmio, regola 50/30/20 |
| 4 | Il fondo di emergenza | Dimensionamento, costruzione, gestione del fondo |
| 5 | Scelta del conto e struttura dei conti personali | Criteri di scelta, struttura multi-conto, automazione |

### Sezione 2: Credito e debito (Capitoli 6-7)

| # | Titolo | Contenuti principali |
|---|--------|---------------------|
| 6 | Gestione del debito: strategie e priorità | Strategie Snowball e Avalanche, consolidamento, rinegoziazione |
| 7 | Credito e punteggio creditizio | Fattori del punteggio, utilizzo del credito, miglioramento profilo |

### Sezione 3: Investimenti (Capitoli 8-13)

| # | Titolo | Contenuti principali |
|---|--------|---------------------|
| 8 | Introduzione agli investimenti | Asset class, rischio/rendimento, orizzonte temporale |
| 9 | Rendimento, rischio e diversificazione | Tipologie di rischio, correlazione, principi di diversificazione |
| 10 | Asset allocation e costruzione del portafoglio | Asset allocation strategica/tattica, profili di rischio |
| 11 | Strumenti di investimento: ETF, fondi e azioni | Confronto strumenti, analisi costi, scelta strumenti |
| 12 | Piani di accumulo (PAC) e investimenti periodici | Dollar Cost Averaging, PAC vs PIC, simulazioni |
| 13 | Ribilanciamento del portafoglio | Strategie temporali/soglia, gestione drift, automazione |

### Sezione 4: Ottimizzazione e disciplina (Capitoli 14-16)

| # | Titolo | Contenuti principali |
|---|--------|---------------------|
| 14 | Fiscalità degli investimenti | Impatto tasse, differimento fiscale, efficienza fiscale |
| 15 | Psicologia dell'investitore e bias comportamentali | Bias principali, strategie anti-emotività, test comportamentale |
| 16 | Errori comuni e checklist finale | Errori da evitare, checklist investitore, piano d'azione |

## 🛠️ Esecuzione locale

```bash
# Installa dipendenze
pip install -r requirements.txt

# Avvia l'app
streamlit run app.py
```

## 📁 Struttura progetto

```
investacademy/
├── app.py                 # App principale Streamlit
├── requirements.txt       # Dipendenze
├── README.md
└── capitoli/
    ├── __init__.py
    ├── capitolo_01.py     # Introduzione finanza personale
    ├── capitolo_02.py     # Interesse, inflazione, rischio
    ├── capitolo_03.py     # Risparmio e obiettivi finanziari
    ├── capitolo_04.py     # Il fondo di emergenza
    ├── capitolo_05.py     # Scelta del conto e struttura
    ├── capitolo_06.py     # Gestione del debito
    ├── capitolo_07.py     # Credito e punteggio creditizio
    ├── capitolo_08.py     # Introduzione agli investimenti
    ├── capitolo_09.py     # Rendimento, rischio e diversificazione
    ├── capitolo_10.py     # Asset allocation
    ├── capitolo_11.py     # Strumenti di investimento
    ├── capitolo_12.py     # Piani di accumulo (PAC)
    ├── capitolo_13.py     # Ribilanciamento
    ├── capitolo_14.py     # Fiscalità
    ├── capitolo_15.py     # Psicologia e bias
    └── capitolo_16.py     # Errori comuni e checklist
```

## ✨ Funzionalità

### Contenuti Educativi
- 📚 **Contenuti teorici** - 16 capitoli progressivi con spiegazioni chiare
- 🎯 **Obiettivi SMART** - Framework per definire obiettivi finanziari
- 💡 **Takeaways** - Punti chiave per ogni capitolo
- 📝 **Esercizi guidati** - Applicazioni pratiche dei concetti

### Calcolatori Interattivi

**Gestione base:**
- 💰 Cash Flow - Analisi entrate/uscite mensili
- 📊 Interesse Composto - Simulazione crescita capitale
- 🎯 Rendimento Reale - Calcolo al netto dell'inflazione
- 🏦 Fondo Emergenze - Dimensionamento e piano costruzione

**Credito e debito:**
- 💳 Utilizzo Credito - Analisi punteggio creditizio
- 📉 Piano Rimborso Debiti - Strategie Snowball/Avalanche
- 🔄 Simulatore Consolidamento - Valutazione convenienza

**Investimenti:**
- 📈 Crescita Investimenti - Simulazione portafogli
- 🔗 Correlazione - Effetto diversificazione
- 🎨 Asset Allocation - Costruzione portafoglio personalizzato
- 💼 Profilo di Rischio - Questionario e allocazione suggerita
- 📊 Confronto Strumenti - ETF vs Fondi vs Azioni
- 🔄 PAC vs PIC - Dollar Cost Averaging simulation
- ⚖️ Ribilanciamento - Calcolo drift e strategie

**Ottimizzazione:**
- 💸 Impatto Fiscale - Tassazione annua vs differita
- 🧠 Test Comportamentale - Valutazione profilo emotivo
- ✅ Scorecard Preparazione - Readiness investimenti

### Verifica Apprendimento
- 📝 **Quiz interattivi** - 5 domande per capitolo con feedback immediato
- ✅ **Esercizi guidati** - Applicazioni pratiche con soluzioni
- 📋 **Checklist** - Strumenti di auto-valutazione
- 📊 **Test comportamentali** - Analisi profilo investitore

## 🎓 Approccio pedagogico

Il corso segue una progressione logica:

1. **Fondamentali** - Stabilire basi solide di gestione finanziaria
2. **Credito** - Gestire passività e costruire credibilità
3. **Investimenti** - Costruire patrimonio nel lungo periodo
4. **Ottimizzazione** - Massimizzare risultati e disciplina

Ogni capitolo include:
- Teoria chiara e strutturata
- Esempi pratici con numeri reali
- Calcolatori interattivi per personalizzazione
- Quiz di verifica con spiegazioni
- Takeaways e checklist operative

## 🎯 A chi è rivolto

- Chiunque voglia prendere controllo delle proprie finanze
- Giovani professionisti all'inizio della carriera
- Risparmiatori che vogliono iniziare a investire
- Investitori principianti che cercano un metodo
- Chi vuole costruire un approccio disciplinato

**Nessun prerequisito richiesto** - il corso parte dalle basi.

## 💡 Filosofia del corso

InvestAccademy non promette:
- ❌ Rendimenti rapidi o formule magiche
- ❌ Strategie di trading speculativo
- ❌ Scorciatoie per "diventare ricchi"

InvestAccademy insegna:
- ✅ Un metodo sostenibile di lungo periodo
- ✅ Disciplina finanziaria e comportamentale
- ✅ Decisioni razionali basate su obiettivi personali
- ✅ Gestione del rischio e delle emozioni

**Risultato atteso:** Non perfezione, ma progressi costanti e decisioni consapevoli.

## 📊 Dati tecnici

- **Framework:** Streamlit
- **Linguaggio:** Python 3.8+
- **Librerie:** pandas, numpy, streamlit
- **Deployment:** Streamlit Community Cloud
- **Licenza:** Open source (da definire)

## 🔄 Versioni

- **v1.0.0** - Corso completo (16 capitoli)
  - Fondamentali finanza personale (1-5)
  - Gestione credito e debito (6-7)
  - Investimenti completi (8-13)
  - Ottimizzazione e disciplina (14-16)

## 🤝 Contribuire

Questo è un progetto educativo. Contributi, feedback e suggerimenti sono benvenuti.

## 📧 Contatti

Per domande, feedback o collaborazioni, apri una issue su GitHub.

---

*InvestAccademy - Costruisci il tuo futuro finanziario con consapevolezza.*

**Il denaro è uno strumento. Serve a comprare tempo, ridurre stress e aumentare libertà.**
