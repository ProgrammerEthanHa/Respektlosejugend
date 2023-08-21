import streamlit as st
import pandas as pd
import altair as alt

st.header("Respektlose Jugend")
st.subheader("Junge Leute haben zu wenig Respekt vor älteren Menschen. Würden Sie dem Satz zustimmen oder nicht?")

source = pd.DataFrame({
        'Anteil(%)': [75, 16, 4],
        'Meinung': ['Stimme zu', 'Stimme nicht zu', 'Weiß nicht']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Meinung:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: YouGov")