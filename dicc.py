import streamlit as st
import pandas as pd

# Cargar los datos
data = pd.read_excel('BBDD DICCIONARIO COMPETENCIAS CPLT.xlsx')

# Agrupar por competencia para fácil acceso
competencias = data.groupby('Competencia')

# Título de la aplicación
st.title('Diccionario de Competencias')

# Selector de competencia
selected_competencia = st.selectbox('Selecciona una Competencia', data['Competencia'].unique())

# Mostrar definición y niveles
if selected_competencia:
    # Filtrar datos para la competencia seleccionada
    competencia_data = competencias.get_group(selected_competencia)
    # Extraer y mostrar la definición (asumimos que es la misma para todos los niveles)
    st.write('Definición:', competencia_data['Definición'].iloc[0])
    # Mostrar niveles y conductas esperadas
    for nivel, subset in competencia_data.groupby('Nivel de competencia'):
        st.subheader(f'Nivel {nivel}')
        for _, row in subset.iterrows():
            st.text(row['Conducta esperada'])

# Correr la aplicación
if __name__ == '__main__':
    st.run()