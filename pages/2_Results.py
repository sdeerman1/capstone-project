import streamlit as st
import joblib
import pandas as pd
# import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Results",
    layout='wide'
)

st.page_link("Home.py", label="Home", icon="🏠")

st.title("Results")

# function to graph confidence level
def confidence_level(prediction_proba):
    data = (prediction_proba[0] * 100).round(2)
    major = pd.DataFrame(data=data, columns=['Major'], index=['Health Sciences', 'Biological Sciences', 'Engineering', 'Physical Sciences / Mathematics', 'Business', 'Social Sciences', 'Visual and Performing Arts', 'Humanities'])

    # specifications for graph
    ax = major.plot(kind='barh', figsize=(3, 2), color='crimson', zorder=10, width=0.5)
    ax.legend().set_visible(False)
    ax.set_xlim(xmin=0, xmax=100)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.spines['bottom'].set_visible(True)

    vals = ax.get_xticks()
    for tick in vals:
        ax.axvline(x=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

    # setting labels for the x-axis. y-axis, and title of graph
    ax.set_xlabel("Percentage (%) Confidence Level", labelpad=2, weight='bold', size=12)
    ax.set_ylabel("Major", labelpad=10, weight='bold', size=12)
    ax.set_title("Prediction Confidence Level", fontdict=None, loc='center', pad=None, weight='bold')

    #  use if global use warning message showing up
    st.set_option('deprecation.showPyplotGlobalUse', False)

    _, center, _ = st.columns([1,2,1])
    center.pyplot()

    return

def reverse_key(item):
    if item[0] == 1:
        return 5
    elif item[0] == 2:
        return 4
    elif item[0] == 3:
        return 3
    elif item[0] == 4:
        return 2
    elif item[0] == 5:
        return 1

@st.cache_data
def calculate_scores(features):

    Hsinc4X = (features.Hsinc1 + features.Hsinc4 + features.Hsinc5 + features.Hsinc6) / 4
    Hfair4X = (features.Hfair1 + features.Hfair4 + features.Hfair6 + features.Hfair8) / 4
    Hgree4X = (features.Hgree2 + features.Hgree4 + features.Hgree5 + features.Hgree7) / 4
    Hmode4X = (features.Hmode2 + features.Hmode3 + features.Hmode6 + features.Hmode8) / 4
    Efear4X = (features.Efear1 + features.Efear4 + features.Efear7 + features.Efear8) / 4
    Eanxi4X = (features.Eanxi1 + features.Eanxi4 + features.Eanxi6 + features.Eanxi8) / 4
    Edepe4X = (features.Edepe3 + features.Edepe6 + features.Edepe7 + features.Edepe8) / 4
    Esent4X = (features.Esent1 + features.Esent2 + features.Esent3 + features.Esent7) / 4
    Xsses4X = (features.Xsses1 + features.Xsses3 + features.Xsses5 + features.Xsses8) / 4
    Xsocb4X = (features.Xsocb2 + features.Xsocb3 + features.Xsocb4 + features.Xsocb8) / 4
    Xsoci4X = (features.Xsoci2 + features.Xsoci3 + features.Xsoci5 + features.Xsoci6) / 4
    Xlive4X = (features.Xlive2 + features.Xlive3 + features.Xlive4 + features.Xlive7) / 4
    Aforg4X = (features.Aforg1 + features.Aforg3 + features.Aforg7 + features.Aforg8) / 4
    Agent4X = (features.Agent4 + features.Agent5 + features.Agent6 + features.Agent7) / 4
    Aflex4X = (features.Aflex1 + features.Aflex5 + features.Aflex7 + features.Aflex8) / 4
    Apati4X = (features.Apati2 + features.Apati3 + features.Apati4 + features.Apati6) / 4
    Corga4X = (features.Corga2 + features.Corga3 + features.Corga6 + features.Corga8) / 4
    Cdili4X = (features.Cdili1 + features.Cdili2 + features.Cdili5 + features.Cdili6) / 4
    Cperf4X = (features.Cperf1 + features.Cperf2 + features.Cperf3 + features.Cperf4) / 4
    Cprud4X = (features.Cprud2 + features.Cprud3 + features.Cprud4 + features.Cprud8) / 4
    Oaesa4X = (features.Oaesa1 + features.Oaesa3 + features.Oaesa4 + features.Oaesa7) / 4
    Oinqu4X = (features.Oinqu1 + features.Oinqu3 + features.Oinqu6 + features.Oinqu8) / 4
    Ocrea4X = (features.Ocrea2 + features.Ocrea6 + features.Ocrea7 + features.Ocrea8) / 4
    Ounco4X = (features.Ounco2 + features.Ounco5 + features.Ounco6 + features.Ounco8) / 4
    Alt4x = (features.Alt3 + features.Alt4 + features.Alt7 + features.Alt8) / 4
    hones16 = (features.Hsinc1 + features.Hsinc4 + features.Hsinc5 + features.Hsinc6 + features.Hfair1 + features.Hfair4 + features.Hfair6 + features.Hfair8 + features.Hgree2 + features.Hgree4 + features.Hgree5 + features.Hgree7 + features.Hmode2 + features.Hmode3 + features.Hmode6 + features.Hmode8) / 16
    emoti16 = (features.Efear1 + features.Efear4 + features.Efear7 + features.Efear8 + features.Eanxi1 + features.Eanxi4 + features.Eanxi6 + features.Eanxi8 + features.Edepe3 + features.Edepe6 + features.Edepe7 + features.Edepe8 + features.Esent1 + features.Esent2 + features.Esent3 + features.Esent7) / 16
    extra16 = (features.Xsses1 +features. Xsses3 + features.Xsses5 + features.Xsses8 + features.Xsocb2 + features.Xsocb3 + features.Xsocb4 + features.Xsocb8 + features.Xsoci2 + features.Xsoci3 + features.Xsoci5 + features.Xsoci6 + features.Xlive2 + features.Xlive3 + features.Xlive4 + features.Xlive7) / 16
    agree16 = (features.Aforg1 + features.Aforg3 + features.Aforg7 + features.Aforg8 + features.Agent4 + features.Agent5 + features.Agent6 + features.Agent7 + features.Aflex1 + features.Aflex5 + features.Aflex7 + features.Aflex8 + features.Apati2 + features.Apati3 + features.Apati4 + features.Apati6) / 16
    consc16 = (features.Corga2 + features.Corga3 + features.Corga6 + features.Corga8 + features.Cdili1 + features.Cdili2 + features.Cdili5 + features.Cdili6 + features.Cperf1 + features.Cperf2 + features.Cperf3 + features.Cperf4 + features.Cprud2 + features.Cprud3 + features.Cprud4 + features.Cprud8) / 16
    openn16 = (features.Oaesa1 + features.Oaesa3 + features.Oaesa4 + features.Oaesa7 + features.Oinqu1 + features.Oinqu3 + features.Oinqu6 + features.Oinqu8 + features.Ocrea2 + features.Ocrea6 + features.Ocrea7 + features.Ocrea8 + features.Ounco2 + features.Ounco5 + features.Ounco6 + features.Ounco8) / 16

    h_sincerity = (reverse_key(features.Hsinc1) + features.Hsinc4 + reverse_key(features.Hsinc5) + features.Hsinc6) / 4
    h_fairness = (reverse_key(features.Hfair1) + reverse_key(features.Hfair4) + features.Hfair6 + reverse_key(features.Hfair8)) / 4
    h_greedavoid = (features.Hgree2 + reverse_key(features.Hgree4) + reverse_key(features.Hgree5) + reverse_key(features.Hgree7)) / 4
    h_modesty = (features.Hmode2 + features.Hmode3 + reverse_key(features.Hmode6) + reverse_key(features.Hmode8)) / 4
    e_fearfulness = (features.Efear1 + reverse_key(features.Efear4) + features.Efear7 + reverse_key(features.Efear8)) / 4
    e_anxiety = (features.Eanxi1 + reverse_key(features.Eanxi4) + reverse_key(features.Eanxi6) + features.Eanxi8) / 4
    e_dependence = (features.Edepe3 + reverse_key(features.Edepe6) + features.Edepe7 + reverse_key(features.Edepe8)) / 4
    e_sentimentality = (features.Esent1 + features.Esent2 + features.Esent3 + reverse_key(features.Esent7)) / 4
    x_sselfesteem = (features.Xsses1 + features.Xsses3 + reverse_key(features.Xsses5) + reverse_key(features.Xsses8)) / 4
    x_sboldness = (reverse_key(features.Xsocb2) + features.Xsocb3 + features.Xsocb4 + reverse_key(features.Xsocb8)) / 4
    x_sociability = (reverse_key(features.Xsoci2) + features.Xsoci3 + features.Xsoci5 + features.Xsoci6) / 4
    x_liveliness = (features.Xlive2 + features.Xlive3 + reverse_key(features.Xlive4) + reverse_key(features.Xlive7)) / 4
    a_forgiveness = (features.Aforg1 + features.Aforg3 + reverse_key(features.Aforg7) + reverse_key(features.Aforg8)) / 4
    a_gentleness = (reverse_key(features.Agent4) + features.Agent5 + features.Agent6 + features.Agent7) / 4
    a_flexibility = (reverse_key(features.Aflex1) + features.Aflex5 + reverse_key(features.Aflex7) + reverse_key(features.Aflex8)) / 4
    a_patience = (reverse_key(features.Apati2) + features.Apati3 + features.Apati4 + reverse_key(features.Apati6)) / 4
    c_organization = (features.Corga2 + features.Corga3 + reverse_key(features.Corga6) + reverse_key(features.Corga8)) / 4
    c_diligence = (features.Cdili1 + features.Cdili2 + reverse_key(features.Cdili5) + reverse_key(features.Cdili6)) / 4
    c_perfectionism = (features.Cperf1 + reverse_key(features.Cperf2) + features.Cperf3 + features.Cperf4) / 4
    c_prudence = (reverse_key(features.Cprud2) + reverse_key(features.Cprud3) + features.Cprud4 + reverse_key(features.Cprud8)) / 4
    o_aesthetic = (reverse_key(features.Oaesa1) + reverse_key(features.Oaesa3) + features.Oaesa4 + features.Oaesa7) / 4
    o_inquisitiveness = (features.Oinqu1 + features.Oinqu3 + reverse_key(features.Oinqu6) + reverse_key(features.Oinqu8)) / 4
    o_creativity = (reverse_key(features.Ocrea2) + features.Ocrea6 + features.Ocrea7 + reverse_key(features.Ocrea8)) / 4
    o_unconventionality = (reverse_key(features.Ounco2) + features.Ounco5 + features.Ounco6 + reverse_key(features.Ounco8)) / 4
    altruism = (features.Alt3 + features.Alt4 + reverse_key(features.Alt7) + reverse_key(features.Alt8)) / 4
    honesty_humility = (h_sincerity + h_fairness + h_greedavoid + h_modesty) / 4
    emotionality = (e_fearfulness + e_anxiety + e_dependence + e_sentimentality) / 4
    extraversion = (x_sselfesteem + x_sboldness + x_sociability + x_liveliness) / 4
    agreeableness = (a_forgiveness + a_gentleness + a_flexibility + a_patience) / 4
    conscientiousness = (c_organization + c_diligence + c_perfectionism + c_prudence) / 4
    openness_to_experience = (o_aesthetic + o_inquisitiveness + o_creativity + o_unconventionality) / 4

    features2 = {
        'Hsinc4X': Hsinc4X,
        'Hfair4X': Hfair4X,
        'Hgree4X': Hgree4X,
        'Hmode4X': Hmode4X,
        'Efear4X': Efear4X,
        'Eanxi4X': Eanxi4X,
        'Edepe4X': Edepe4X,
        'Esent4X': Esent4X,
        'Xsses4X': Xsses4X,
        'Xsocb4X': Xsocb4X,
        'Xsoci4X': Xsoci4X,
        'Xlive4X': Xlive4X,
        'Aforg4X': Aforg4X,
        'Agent4X': Agent4X,
        'Aflex4X': Aflex4X,
        'Apati4X': Apati4X,
        'Corga4X': Corga4X,
        'Cdili4X': Cdili4X,
        'Cperf4X': Cperf4X,
        'Cprud4X': Cprud4X,
        'Oaesa4X': Oaesa4X,
        'Oinqu4X': Oinqu4X,
        'Ocrea4X': Ocrea4X,
        'Ounco4X': Ounco4X,
        'Alt4x': Alt4x,
        'hones16': hones16,
        'emoti16': emoti16,
        'extra16': extra16,
        'agree16': agree16,
        'consc16': consc16,
        'openn16': openn16,
    }

    scores = {
        'h_sincerity': h_sincerity,
        'h_fairness': h_fairness,
        'h_greedavoid': h_greedavoid,
        'h_modesty': h_modesty,
        'e_fearfulness': e_fearfulness,
        'e_anxiety': e_anxiety,
        'e_dependence': e_dependence,
        'e_sentimentality': e_sentimentality,
        'x_sselfesteem': x_sselfesteem,
        'x_sboldness': x_sboldness,
        'x_sociability': x_sociability,
        'x_liveliness': x_liveliness,
        'a_forgiveness': a_forgiveness,
        'a_gentleness': a_gentleness,
        'a_flexibility': a_flexibility,
        'a_patience': a_patience,
        'c_organization': c_organization,
        'c_diligence': c_diligence,
        'c_perfectionism': c_perfectionism,
        'c_prudence': c_prudence,
        'o_aesthetic': o_aesthetic,
        'o_inquisitiveness': o_inquisitiveness,
        'o_creativity': o_creativity,
        'o_unconventionality': o_unconventionality,
        'altruism': altruism,
        'honesty_humility': honesty_humility,
        'emotionality': emotionality,
        'extraversion': extraversion,
        'agreeableness': agreeableness,
        'conscientiousness': conscientiousness,
        'openness_to_experience': openness_to_experience
    }

    data = pd.DataFrame(features2, index=[0])
    scores2 = pd.DataFrame(scores, index=[0])
    return data, scores2

# load model using joblib
model = joblib.load(open("model.joblib", "rb"))

x, user_scores = calculate_scores(st.session_state.input)

facet_scores = user_scores.iloc[:,-31:]
st.session_state.facet_scores = facet_scores

clicked = st.button("For more information about your scores according to the HEXACO scoring system, CLICK HERE")
if clicked:
    st.switch_page("pages/3_HexacoResults.py")

st.subheader('Prediction')
if st.button("Click here to explore the majors offered at UA for your prediction!"):
    st.switch_page("pages/5_ResultsMajors.py")

input = st.session_state.input
sex = input.Sex
input.drop(input.columns[len(input.columns)-1], axis=1, inplace=True)
input = pd.concat([input, x], axis=1)
input = pd.concat([input, sex], axis=1) 
# st.write(input)

# create prediction based on processed user data
prediction = model.predict(input)
prediction_proba = model.predict_proba(input)

# display prediction
if prediction[0] == 1:
    st.write('Prediction: **Health Sciences**')
    st.write('Confidence Level: ', "{:.2f}".format((prediction_proba[0][0] * 100)), '%')
    st.session_state.prediction = "Health Sciences"
elif prediction[0] == 2:
    st.write('Prediction: **Biological Sciences**')
    st.write('Confidence Level: ', "{:.2f}".format((prediction_proba[0][1] * 100)), '%')
    st.session_state.prediction = "Biological Sciences"
elif prediction[0] == 3:
    st.write('Prediction: **Engineering**')
    st.write('Confidence Level: ', "{:.2f}".format((prediction_proba[0][2] * 100)), '%')
    st.session_state.prediction = "Engineering"
elif prediction[0] == 4:
    st.write('Prediction: **Physical Sciences / Mathematics**')
    st.write('Confidence Level: ', "{:.2f}".format((prediction_proba[0][3] * 100)), '%')
    st.session_state.prediction = "Physical Sciences / Mathematics"
elif prediction[0] == 5:
    st.write('Prediction: **Business**')
    st.write('Confidence Level: ', "{:.2f}".format((prediction_proba[0][4] * 100)), '%')
    st.session_state.prediction = "Business"
elif prediction[0] == 6:
    st.write('Prediction: **Social Sciences**')
    st.write('Confidence Level: ', "{:.2f}".format((prediction_proba[0][5] * 100)), '%')
    st.session_state.prediction = "Social Sciences"
elif prediction[0] == 7:
    st.write('Prediction: **Visual and Performing Arts**')
    st.write('Confidence Level: ', "{:.2f}".format((prediction_proba[0][6] * 100)), '%')
    st.session_state.prediction = "Visual and Performing Arts"
elif prediction[0] == 8:
    st.write('Prediction: **Humanities**')
    st.write('Confidence Level: ', "{:.2f}".format((prediction_proba[0][7] * 100)), '%')
    st.session_state.prediction = "Humanities"
else:
    st.write('Error in Prediction')

st.subheader("All Predictions")
st.write("The confidence levels for all majors add up to 100, so they must be viewed relative to one another instead of as a percentage out of 100.")
    
# call function to create graph based on confidence level of prediction 1
confidence_level(prediction_proba)

st.write('**Humanities**: ', "{:.2f}".format((prediction_proba[0][7] * 100)), '%')
st.write('**Visual and Performing Arts**: ', "{:.2f}".format((prediction_proba[0][6] * 100)), '%')
st.write('**Social Sciences**: ', "{:.2f}".format((prediction_proba[0][5] * 100)), '%')
st.write('**Business**: ', "{:.2f}".format((prediction_proba[0][4] * 100)), '%')
st.write('**Physical Sciences / Mathematics**: ', "{:.2f}".format((prediction_proba[0][3] * 100)), '%')
st.write('**Engineering**: ', "{:.2f}".format((prediction_proba[0][2] * 100)), '%')
st.write('**Biological Sciences**: ', "{:.2f}".format((prediction_proba[0][1] * 100)), '%')
st.write('**Health Sciences**: ', "{:.2f}".format((prediction_proba[0][0] * 100)), '%')
