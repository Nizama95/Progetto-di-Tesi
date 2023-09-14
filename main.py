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

    # Aggiungi una sezione per visualizzare i dati
    st.header("Visualizzazione dei Dati")

    # Mostra una tabella con i dati
    st.write("Esempio dei primi 5 record dei dati:")
    st.write(data.head())

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


    # Aggiungi una sezione per le statistiche dei dati
    st.header("Statistiche dei Dati")
    st.write("Statistiche di base del dataset:")
    st.write(data.describe())

    # Aggiungi una sezione per il filtraggio dei dati
    st.header("Filtraggio dei Dati")
    species_filter = st.multiselect("Seleziona una o più specie:", data["species"].unique())
    filtered_data = data[data["species"].isin(species_filter)]

    # Visualizza il dataset filtrato
    st.write("Esempio dei primi 5 record dei dati filtrati:")
    st.write(filtered_data.head())

    # Aggiungi una sezione per il conteggio delle specie selezionate
    st.header("Conteggio delle Specie")
    st.write("Conteggio delle specie selezionate:")
    st.write(filtered_data["species"].value_counts())

    # Aggiungi una sezione per l'istogramma delle caratteristiche
    st.header("Istogramma delle Caratteristiche")
    if st.checkbox("Mostra istogramma delle caratteristiche"):
        st.subheader("Istogramma delle Caratteristiche")
        for feature in data.columns[:-1]:
            st.write(f"Istogramma per {feature}")
            plt.hist(data[data['species'] == species_filter[0]][feature], alpha=0.5, label=species_filter[0], color='b')
            plt.hist(data[data['species'] == species_filter[1]][feature], alpha=0.5, label=species_filter[1], color='r')
            plt.xlabel(feature)
            plt.ylabel("Count")
            plt.legend(loc="upper right")
            st.pyplot()

    # Aggiungi una sezione per la correlazione tra le caratteristiche
    st.header("Correlazione tra le Caratteristiche")
    if st.checkbox("Mostra la matrice di correlazione"):
        st.subheader("Matrice di Correlazione")
        correlation_matrix = data.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
        st.pyplot()
