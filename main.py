# Importa le librerie necessarie
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Imposta il titolo dell'applicazione
st.title("Analisi del Dataset Iris")

# Aggiungi una sezione per caricare il file Excel
st.header("Carica il File Excel")

# Carica il file Excel dal tuo computer
uploaded_file = st.file_uploader("Carica un file Excel", type=["xlsx"])

# Verifica se un file è stato caricato
if uploaded_file is not None:
    # Leggi il file Excel in un DataFrame
    data = pd.read_excel(uploaded_file)


    # Aggiungi una sezione per l'analisi dei dati
    st.header("Analisi dei Dati")

    # Aggiungi un selettore per scegliere la colonna da visualizzare
    feature_to_plot = st.selectbox("Seleziona una caratteristica da visualizzare:", data.columns)

    # Crea un grafico a torta o un grafico di dispersione in base alla scelta dell'utente
    st.set_option('deprecation.showPyplotGlobalUse', False)
    if st.checkbox("Mostra un grafico a torta"):
        st.subheader(f"Grafico a Torta per {feature_to_plot}")
        feature_counts = data[feature_to_plot].value_counts()
        fig, ax = plt.subplots()
        ax.pie(feature_counts, labels=feature_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot()

    if st.checkbox("Mostra un grafico di dispersione"):
        st.subheader("Grafico di Dispersione")
        fig, ax = plt.subplots()
        sns.scatterplot(data=data, x="sepal_length", y="sepal_width", hue="species", ax=ax)
        st.pyplot(fig)


 # Aggiungi una sezione per visualizzare i dati
    st.header("Elaborazione dati")

    # Utilizza st.text_input o st.text_area per consentire all'utente di inserire un prompt
    user_input = st.text_area("Inserisci una richiesta di elaborazione dei dati:", "Esempio: Crea un grafico XYZ")

    # Verifica se l'utente ha inserito una richiesta
if user_input:
    st.subheader("Risultato dell'Elaborazione dei Dati")

    # Qui puoi analizzare il testo inserito dall'utente e generare il grafico in base alla richiesta
    # Ad esempio, se l'utente ha inserito "Crea un grafico XYZ", puoi scrivere codice per creare il grafico XYZ.

    # Esempio di elaborazione dei dati (questo è solo un esempio, dovresti personalizzarlo in base alle richieste degli utenti)
    if "grafico" in user_input.lower() and "xyz" in user_input.lower():
        st.write("Ecco il grafico XYZ:")
        # Inserire qui il codice per generare il grafico XYZ
        
    # Puoi aggiungere ulteriori condizioni per altre richieste


