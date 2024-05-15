import streamlit as st
import pandas as pd

# Cargar los datos
data = pd.read_excel('BBDD DICCIONARIO COMPETENCIAS CPLT.xlsx')

# Ordenar las competencias alfabéticamente y eliminar duplicados
competencias_unicas = sorted(data['Competencia'].unique())

# Título de la aplicación
st.title('Diccionario de Competencias')

# Selector de competencia
selected_competencia = st.selectbox('Selecciona una Competencia', competencias_unicas)

# Agrupar por competencia para fácil acceso
competencias = data.groupby('Competencia')

# Mostrar definición y niveles
if selected_competencia:
    # Filtrar datos para la competencia seleccionada
    competencia_data = competencias.get_group(selected_competencia)
    # Extraer y mostrar la definición (asumimos que es la misma para todos los niveles)
    st.header('Definición:')
    st.write(competencia_data['Definición'].iloc[0])
    # Mostrar niveles y conductas esperadas
    for nivel, subset in competencia_data.groupby('Nivel de competencia'):
        st.subheader(f'Nivel {nivel}')
        # Asegurarse de que el texto se ajusta completamente
        for _, row in subset.iterrows():
            st.write(row['Conducta esperada'])
