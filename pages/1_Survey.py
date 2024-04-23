import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Survey",
    layout='wide'
)

st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 18px;
}
div[class*="stSelectbox"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 20px;
}
    </style>
    """, unsafe_allow_html=True)

st.page_link("Home.py", label="Home", icon="🏠")

st.title("Survey")

# function to collect user input using Streamlit
@st.cache_data(experimental_allow_widgets=True)
def user_input():

    # _, center, _ = st.columns([3,8,2])

    Oaesa1 = st.radio('1\. I would be quite bored by a visit to an art gallery.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Corga2 = st.radio('2\. I clean my office or home quite frequently', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Aforg1 = st.radio('3\. I rarely hold a grudge, even against people who have badly wronged me.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Xsses1 = st.radio('4\. I feel reasonably satisfied with myself overall.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Efear1 = st.radio('5\. I would feel afraid if I had to travel in bad weather conditions.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Hsinc1 = st.radio('6\. If I want something from a person I dislike, I will act very nicely toward that person in order to get it.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Oinqu1 = st.radio('7\. I\'m interested in learning about the history and politics of other countries.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Cdili1 = st.radio('8\. When working, I often set ambitious goals for myself.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Agent4 = st.radio('9\. People sometimes tell me that I am too critical of others.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Xsocb2 = st.radio('10\. I rarely express my opinions in group meetings.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Eanxi1 = st.radio('11\. I sometimes can\'t help worrying about little things.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Hfair1 = st.radio('12\. If I knew that I could never get caught, I would be willing to steal a million dollars.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Ocrea2 = st.radio('13\. I would like a job that requires following a routine rather than being creative.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Cperf1 = st.radio('14\. I often check my work over repeatedly to find any mistakes.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Aflex1 = st.radio('15\. People sometimes tell me that I\'m too stubborn.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Xsoci2 = st.radio('16\. I avoid making "small talk" with people.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Edepe3 = st.radio('17\. When I suffer from a painful experience, I need someone to make me feel comfortable.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Hgree2 = st.radio('18\. Having a lot of money is not especially important to me.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Ounco2 = st.radio('19\. I think that paying attention to radical ideas is a waste of time.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Cprud2 = st.radio('20\. I make decisions based on the feeling of the moment rather than on careful thought.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Apati2 = st.radio('21\. People think of me as someone who has a quick temper.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Xlive2 = st.radio('22\. I am energetic nearly all the time.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Esent1 = st.radio('23\. I feel like crying when I see other people crying.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Hmode2 = st.radio('24\. I am an ordinary person who is no better than others.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Oaesa3 = st.radio('25\. I wouldn\'t spend my time reading a book of poetry.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Corga3 = st.radio('26\. I plan ahead and organize things, to avoid scrambling at the last minute.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Aforg3 = st.radio('27\. My attitude toward people who have treated me badly is "forgive and forget".', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Xsses3 = st.radio('28\. I think that most people like some aspects of my personality.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Efear4 = st.radio('29\. I don\'t mind doing jobs that involve dangerous work.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Hsinc4 = st.radio('30\. I wouldn\'t use flattery to get a raise or promotion at work, even if I thought it would succeed.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Oinqu3 = st.radio('31\. I enjoy looking at maps of different places.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Cdili2 = st.radio('32\. I often push myself very hard when trying to achieve a goal.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Agent5 = st.radio('33\. I generally accept people\'s faults without complaining about them.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Xsocb3 = st.radio('34\. In social situations, I\'m usually the one who makes the first move.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Eanxi4 = st.radio('35\. I worry a lot less than most people do.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Hfair4 = st.radio('36\. I would be tempted to buy stolen property if I were financially tight.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Ocrea6 = st.radio('37\. I would enjoy creating a work of art, such as a novel, a song, or a painting.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Cperf2 = st.radio('38\. When working on something, I don\'t pay much attention to small details.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Aflex5 = st.radio('39\. I am usually quite flexible in my opinions when people disagree with me.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Xsoci3 = st.radio('40\. I enjoy having lots of people around to talk with.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Edepe6 = st.radio('41\. I can handle difficult situations without needing emotional support from anyone else.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Hgree4 = st.radio('42\. I would like to live in a very expensive, high-class neighborhood.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Ounco5 = st.radio('43\. I like people who have unconventional views.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Cprud3 = st.radio('44\. I make a lot of mistakes because I don\'t think before I act.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Apati3 = st.radio('45\. I rarely feel anger, even when people treat me quite badly.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Xlive3 = st.radio('46\. On most days, I feel cheerful and optimistic.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Esent2 = st.radio('47\. When someone I know well is unhappy, I can almost feel that person\'s pain myself.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Hmode3 = st.radio('48\. I wouldn\'t want people to treat me as though I were superior to them.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Oaesa4 = st.radio('49\. If I had the opportunity, I would like to attend a classical music concert.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Corga6 = st.radio('50\. People often joke with me about the messiness of my room or desk.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Aforg7 = st.radio('51\. If someone has cheated me once, I will always feel suspicious of that person.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Xsses5 = st.radio('52\. I feel that I am an unpopular person.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Efear7 = st.radio('53\. When if comes to physical danger, I am very fearful.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Hsinc5 = st.radio('54\. If I want something from someone, I will laugh at that person\'s worst jokes.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Oinqu6 = st.radio('55\. I would be very bored by a book about the history of science and technology.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Cdili5 = st.radio('56\. Often when I set a goal, I end up quitting without having reached it.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Agent6 = st.radio('57\. I tend to be lenient in judging other people.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Xsocb4 = st.radio('58\. When I\'m in a group of people, I\'m often the one who speaks on behalf of the group.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Eanxi6 = st.radio('59\. I rarely, If ever, have trouble sleeping due to stress or anxiety.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Hfair6 = st.radio('60\. I would never accept a bribe, even if it were very large.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Ocrea7 = st.radio('61\. People have often told me that I have a good imagination.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Cperf3 = st.radio('62\. I always try to be accurate in my work, even at the expense of time.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Aflex7 = st.radio('63\. When people tell me that I\'m wrong, my first reaction is to argue with them.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Xsoci5 = st.radio('64\. I prefer jobs that involve active social interaction to those that involve working alone.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Edepe7 = st.radio('65\. Whenever I feel worried about something, I want to share my concern with another person.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Hgree5 = st.radio('66\. I would like to be seen driving around in a very expensive car.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Ounco6 = st.radio('67\. I think of myself as a somewhat eccentric person.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Cprud4 = st.radio('68\. I don\'t allow my impulses to govern my behavior.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Apati4 = st.radio('69\. Most people tend to get angry more quickly than I do.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Xlive4 = st.radio('70\. People often tell me that I should try to cheer up.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Esent3 = st.radio('71\. I feel strong emotions when someone close to me is going away for a long time.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Hmode6 = st.radio('72\. I think that I am entitled to more respect than the average person is.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Oaesa7 = st.radio('73\. Sometimes I like to just watch the wind as it blows through the trees.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Corga8 = st.radio('74\. When working, I sometimes have difficulties due to being disorganized.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Aforg8 = st.radio('75\. I find it hard to fully forgive someone who has done something mean to me.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Xsses8 = st.radio('76\. I sometimes feel that I am a worthless person.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Efear8 = st.radio('77\. Even in an emergency I wouldn\'t feel like panicking.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Hsinc6 = st.radio('78\. I wouldn\'t pretend to like someone just to get that person to do favors for me.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Oinqu8 = st.radio('79\. I\'ve never really enjoyed looking through an encyclopedia.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Cdili6 = st.radio('80\. I do only the minimum amount of work needed to get by.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Agent7 = st.radio('81\. Even when people make a lot of mistakes, I rarely say anything negative.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Xsocb8 = st.radio('82\. I tend to feel quite self-conscious when speaking in front of a group of people.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Eanxi8 = st.radio('83\. I get very anxious when waiting to hear about an important decision.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Hfair8 = st.radio('84\. I\'d be tempted to use counterfeit money, if I were sure I could get away with it.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Ocrea8 = st.radio('85\. I don\'t think of myself as the artistic or creative type.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Cperf4 = st.radio('86\. People often call me a perfectionist.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Aflex8 = st.radio('87\. I find it hard to compromise with people when I really think I\'m right.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Xsoci6 = st.radio('88\. The first thing that I always do in a new place is to make friends.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Edepe8 = st.radio('89\. I rarely discuss my problems with other people.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Hgree7 = st.radio('90\. I would get a lot of pleasure from owning expensive luxury goods.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Ounco8 = st.radio('91\. I find it boring to discuss philosophy.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Cprud8 = st.radio('92\. I prefer to do whatever comes to mind, rather than stick to a plan.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Apati6 = st.radio('93\. I find it hard to keep my temper when people insult me.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Xlive7 = st.radio('94\. Most people are more upbeat and dynamic than I generally am.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Esent7 = st.radio('95\. I remain unemotional even in situations where most people get very sentimental.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Hmode8 = st.radio('96\. I want people to know that I am an important person of high status.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Alt3 = st.radio('97\. I have sympathy for people who are less fortunate than I am.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Alt4 = st.radio('98\. I try to give generously to those in need.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Alt7 = st.radio('99\. It wouldn\'t bother me to harm someone I didn\'t like.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Alt8 = st.radio('100\. People see me as a hard-hearted person.', [1,2,3,4,5], horizontal=True, format_func=stringify, index=None)
    Sex = st.selectbox('Sex', ('Male', 'Female'))
    
    features = {
        'Oaesa1': Oaesa1,
        'Corga2': Corga2,
        'Aforg1': Aforg1,
        'Xsses1': Xsses1,
        'Efear1': Efear1,
        'Hsinc1': Hsinc1,
        'Oinqu1': Oinqu1,
        'Cdili1': Cdili1,
        'Agent4': Agent4,
        'Xsocb2': Xsocb2,
        'Eanxi1': Eanxi1,
        'Hfair1': Hfair1,
        'Ocrea2': Ocrea2,
        'Cperf1': Cperf1,
        'Aflex1': Aflex1,
        'Xsoci2': Xsoci2,
        'Edepe3': Edepe3,
        'Hgree2': Hgree2,
        'Ounco2': Ounco2,
        'Cprud2': Cprud2,
        'Apati2': Apati2,
        'Xlive2': Xlive2,
        'Esent1': Esent1,
        'Hmode2': Hmode2,
        'Oaesa3': Oaesa3,
        'Corga3': Corga3,
        'Aforg3': Aforg3,
        'Xsses3': Xsses3,
        'Efear4': Efear4,
        'Hsinc4': Hsinc4,
        'Oinqu3': Oinqu3,
        'Cdili2': Cdili2,
        'Agent5': Agent5,
        'Xsocb3': Xsocb3,
        'Eanxi4': Eanxi4,
        'Hfair4': Hfair4,
        'Ocrea6': Ocrea6,
        'Cperf2': Cperf2,
        'Aflex5': Aflex5,
        'Xsoci3': Xsoci3,
        'Edepe6': Edepe6,
        'Hgree4': Hgree4,
        'Ounco5': Ounco5,
        'Cprud3': Cprud3,
        'Apati3': Apati3,
        'Xlive3': Xlive3,
        'Esent2': Esent2,
        'Hmode3': Hmode3,
        'Oaesa4': Oaesa4,
        'Corga6': Corga6,
        'Aforg7': Aforg7,
        'Xsses5': Xsses5,
        'Efear7': Efear7,
        'Hsinc5': Hsinc5,
        'Oinqu6': Oinqu6,
        'Cdili5': Cdili5,
        'Agent6': Agent6,
        'Xsocb4': Xsocb4,
        'Eanxi6': Eanxi6,
        'Hfair6': Hfair6,
        'Ocrea7': Ocrea7,
        'Cperf3': Cperf3,
        'Aflex7': Aflex7,
        'Xsoci5': Xsoci5,
        'Edepe7': Edepe7,
        'Hgree5': Hgree5,
        'Ounco6': Ounco6,
        'Cprud4': Cprud4,
        'Apati4': Apati4,
        'Xlive4': Xlive4,
        'Esent3': Esent3,
        'Hmode6': Hmode6,
        'Oaesa7': Oaesa7,
        'Corga8': Corga8,
        'Aforg8': Aforg8,
        'Xsses8': Xsses8,
        'Efear8': Efear8,
        'Hsinc6': Hsinc6,
        'Oinqu8': Oinqu8,
        'Cdili6': Cdili6,
        'Agent7': Agent7,
        'Xsocb8': Xsocb8,
        'Eanxi8': Eanxi8,
        'Hfair8': Hfair8,
        'Ocrea8': Ocrea8,
        'Cperf4': Cperf4,
        'Aflex8': Aflex8,
        'Xsoci6': Xsoci6,
        'Edepe8': Edepe8,
        'Hgree7': Hgree7,
        'Ounco8': Ounco8,
        'Cprud8': Cprud8,
        'Apati6': Apati6,
        'Xlive7': Xlive7,
        'Esent7': Esent7,
        'Hmode8': Hmode8,
        'Alt3': Alt3,
        'Alt4': Alt4,
        'Alt7': Alt7,
        'Alt8': Alt8,
        'Sex': Sex
    }

    # put data into dataframes and return
    data = pd.DataFrame(features, index=[0])
    return data

# helper function for select radio
def stringify(i:int = 0) -> str:
    return radio_strings[i-1]

radio_strings = ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]

user_input_df = user_input()

# if ( (user_input_df.Oaesa1 != 0) & (user_input_df.Corga2 != 0) & (user_input_df.Aforg1 != 0) & (user_input_df.Xsses1 != 0) & (user_input_df.Efear1 != 0) & (user_input_df.Hsinc1 != 0) & (user_input_df.Oinqu1 != 0) & (user_input_df.Cdili1 != 0) & (user_input_df.Agent4 != 0) & (user_input_df.Xsocb2 != 0) & (user_input_df.Eanxi1 != 0) & (user_input_df.Hfair1 != 0) & (user_input_df.Ocrea2 != 0) & (user_input_df.Cperf1 != 0) & (user_input_df.Aflex1 != 0) & (user_input_df.Xsoci2 != 0) & (user_input_df.Edepe3 != 0) & (user_input_df.Hgree2 != 0) & (user_input_df.Ounco2 != 0) & (user_input_df.Cprud2 != 0) & (user_input_df.Apati2 != 0) & (user_input_df.Xlive2 != 0) & (user_input_df.Esent1 != 0) & (user_input_df.Hmode2 != 0) & (user_input_df.Oaesa3 != 0) & (user_input_df.Corga3 != 0) & (user_input_df.Aforg3 != 0) & (user_input_df.Xsses3 != 0) & (user_input_df.Efear4 != 0) & (user_input_df.Hsinc4 != 0) & (user_input_df.Oinqu3 != 0) & (user_input_df.Cdili2 != 0) & (user_input_df.Agent5 != 0) & (user_input_df.Xsocb3 != 0) & (user_input_df.Eanxi4 != 0) & (user_input_df.Hfair4 != 0) & (user_input_df.Ocrea6 != 0) & (user_input_df.Cperf2 != 0) & (user_input_df.Aflex5 != 0) & (user_input_df.Xsoci3 != 0) & (user_input_df.Edepe6 != 0) & (user_input_df.Hgree4 != 0) & (user_input_df.Ounco5 != 0) & (user_input_df.Cprud3 != 0) & (user_input_df.Apati3 != 0) & (user_input_df.Xlive3 != 0) & (user_input_df.Esent2 != 0) & (user_input_df.Hmode3 != 0) & (user_input_df.Oaesa4 != 0) & (user_input_df.Corga6 != 0) & (user_input_df.Aforg7 != 0) & (user_input_df.Xsses5 != 0) & (user_input_df.Efear7 != 0) & (user_input_df.Hsinc5 != 0) & (user_input_df.Oinqu6 != 0) & (user_input_df.Cdili5 != 0) & (user_input_df.Agent6 != 0) & (user_input_df.Xsocb4 != 0) & (user_input_df.Eanxi6 != 0) & (user_input_df.Hfair6 != 0) & (user_input_df.Ocrea7 != 0) & (user_input_df.Cperf3 != 0) & (user_input_df.Aflex7 != 0) & (user_input_df.Xsoci5 != 0) & (user_input_df.Edepe7 != 0) & (user_input_df.Hgree5 != 0) & (user_input_df.Ounco6 != 0) & (user_input_df.Cprud4 != 0) & (user_input_df.Apati4 != 0) & (user_input_df.Xlive4 != 0) & (user_input_df.Esent3 != 0) & (user_input_df.Hmode6 != 0) & (user_input_df.Oaesa7 != 0) & (user_input_df.Corga8 != 0) & (user_input_df.Aforg8 != 0) & (user_input_df.Xsses8 != 0) & (user_input_df.Efear8 != 0) & (user_input_df.Hsinc6 != 0) & (user_input_df.Oinqu8 != 0) & (user_input_df.Cdili6 != 0) & (user_input_df.Agent7 != 0) & (user_input_df.Xsocb8 != 0) & (user_input_df.Eanxi8 != 0) & (user_input_df.Hfair8 != 0) & (user_input_df.Ocrea8 != 0) & (user_input_df.Cperf4 != 0) & (user_input_df.Aflex8 != 0) & (user_input_df.Xsoci6 != 0) & (user_input_df.Edepe8 != 0) & (user_input_df.Hgree7 != 0) & (user_input_df.Ounco8 != 0) & (user_input_df.Cprud8 != 0) & (user_input_df.Apati6 != 0) & (user_input_df.Xlive7 != 0) & (user_input_df.Esent7 != 0) & (user_input_df.Hmode8 != 0) & (user_input_df.Alt3 != 0) & (user_input_df.Alt4 != 0) & (user_input_df.Alt7 != 0) & (user_input_df.Alt8) ):
#     st.write("All questions must be answered. Unanswered questions: ", user_input_df.isnull())

# FIXME not actually centered when full screen???
_, center, _ = st.columns([6, 2, 6])
submitted = center.button("Submit")

if submitted:
    if (user_input_df.isnull().values.any()):
        # change this to only show question number
        missing = user_input_df.isnull().any(axis=0)
        st.write("All questions must be answered. Unanswered questions: ")
        for i in range(101):
            if missing[i]:
                st.write("#{}".format(i+1))
    else:
        processed_data = user_input_df
        processed_data.Sex = processed_data.Sex.map({'Male':1, 'Female':2})

        st.session_state.input = processed_data

        st.switch_page("pages/2_Results.py")

st.write("""<a href="https://hexaco.org/">The HEXACO Personality Inventory</a> - Dr. Kibeom Lee and Dr. Michael C. Ashton.""", unsafe_allow_html=True)