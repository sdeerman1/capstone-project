import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Hexaco Results",
    layout='wide'
)

st.page_link("Home.py", label="Home", icon="🏠")

st.title("HEXACO Quiz Results")
st.write('These results are scored out of 5, with 5.0 being the highest level.')
st.markdown("""For more information about your results and what high and low scores mean, visit <a href="https://hexaco.org/scaledescriptions">the official HEXACO website</a>.""", unsafe_allow_html=True)

if st.button('UA Majors for your prediction'):
    st.switch_page('pages/5_ResultsMajors.py')

image = Image.open('HEXACO.png')
left, center, right = st.columns([2, 3, 1])
center.image(image, use_column_width=True)

left.subheader('Factor Results:')
left.write('**Honesty-Humility** Score: {:.2f}'.format(st.session_state.facet_scores.iloc[:,-6][0]))
left.write('**Emotionality** Score: {:.2f}'.format(st.session_state.facet_scores.iloc[:,-5][0]))
left.write('**Extraversion** Score: {:.2f}'.format(st.session_state.facet_scores.iloc[:,-4][0]))
left.write('**Agreeableness** Score: {:.2f}'.format(st.session_state.facet_scores.iloc[:,-3][0]))
left.write('**Conscientiousness** Score: {:.2f}'.format(st.session_state.facet_scores.iloc[:,-2][0]))
left.write('**Openness to Experience** Score: {:.2f}'.format(st.session_state.facet_scores.iloc[:,-1][0]))
left.write('Altruism Score: {:.2f}'.format(st.session_state.facet_scores.iloc[0][24]))

st.write('')
st.subheader('Facet-Level Results')

col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1])

col1.write('**Honesty-Humility Facets:**')
col1.write('Sincerity:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][0]))
col1.write('Fairness:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][1]))
col1.write('Greed Avoidance:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][2]))
col1.write('Modesty:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][3]))

st.write('')
col2.write('**Emotionality Facets:**')
col2.write('Fearfulness:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][4]))
col2.write('Anxiety:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][5]))
col2.write('Dependence:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][6]))
col2.write('Sentimentality:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][7]))

st.write('')
col3.write('**Extraversion Facets:**')
col3.write('Social Self-Esteem:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][8]))
col3.write('Social Boldness:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][9]))
col3.write('Sociability:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][10]))
col3.write('Livliness:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][11]))

st.write('')
col4.write('**Agreeableness Facets:**')
col4.write('Forgiveness:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][12]))
col4.write('Gentleness:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][13]))
col4.write('Flexibility:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][14]))
col4.write('Patience:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][15]))

st.write('')
col5.write('**Conscientiousness Facets:**')
col5.write('Organization:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][16]))
col5.write('Diligence:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][17]))
col5.write('Perfectionism:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][18]))
col5.write('Prudence:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][19]))

st.write('')
col6.write('**Openness to Experience Facets:**')
col6.write('Aesthetic Appreciation:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][20]))
col6.write('Inquisitiveness:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][21]))
col6.write('Creativity:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][22]))
col6.write('Unconventionality:  {:.2f}'.format(st.session_state.facet_scores.iloc[0][23]))