# -------------------------------------
# Created by Angel Santana ------------
#! twiiter: @iamAngelSH ---------------
#! Github: iamAngelSH -----------------
#! LinkedIn: Angel Santana Hernandez --
# -------------------------------------
# -------------------------------------
# IMPORT LIBRARIES
# ----------------
# Data Manipulation
import pandas as pd, numpy as np
# Date time
import datetime
# Unpickle the model
import pickle
import cloudpickle
# Streamlit library
import streamlit as st
# -------------------------------------

st.set_page_config(
        page_title = 'Phishing URL Predictor',
        page_icon = '🐟📈',
        layout = 'wide'
    )
st.title('𝙿𝚑𝚒𝚜𝚑𝚒𝚗𝚐 𝚄𝚁𝙻 𝙿𝚛𝚎𝚍𝚒𝚌𝚝𝚒𝚘𝚗 🐟📈')

st.markdown('---')
# Configure Page Layout and Instructions
def config_page():
    # --- DESCRIBE WEB APPLICATION ---
    st.header('What does this application do?') 

    POINTS = '''
    - What is a phishing URL?
        - A phishing URL is a way cybercriminals will try to obtain sensitive information from a user.
        - Phishing URLs can lead to forms, malicious software, emails, etc..

    - How does this application work?
        - Given a url or a list of urls, the application will analyze the URL and return a prediction.
            - 0 (not a phish url) 
            - 1 (a phish url).

    ---
    '''
    st.markdown(POINTS)

# config_page()

# Create layout for columns (2 columns equal size)
def create_columns(func1, func2):
    layout1, layout2 = st.columns((1, 1))
    with layout1:
        func1()
    with layout2:
        func2()


# Set Warnings for Application
def app_warnings():
    WARNING_DNU = '''
    This application is not served to dictate whether a given URL is safe or not in a PROFESSIONAL setting.

    Please use with caution and ONLY for experimentation.
    
    CONSULT YOUR IT/SECURITY TEAM IF YOU THINK YOU HAVE RUN INTO A PHISHING URL IN A PROFESSION SETTING.
    '''
    with st.expander('❗DISCLAIMER ❗'):
        st.warning(WARNING_DNU)

# Set socials/contributions
def socials_contr():
    github_angel = 'https://github.com/iamAngelSH'
    personal_ws_angel = 'https://angelsantana.io'
    linkedin_angel = 'https://www.linkedin.com/in/angelsantanahernandez/'
    twitter_angel = 'https://twitter.com/iamAngelSH'
    SC_Cont = f'''
    - Angel Santana (creator of application)
        - Github: [iamAngelSH]({github_angel})
        - Website: [angelsantana.io]({personal_ws_angel})
        - LinkedIn: [Angel Santana]({linkedin_angel})
        - Twitter: [iamAngelSH]({twitter_angel})

    '''
    with st.expander('Connect with me!'):
        st.markdown(SC_Cont)
        

def header():
    st.header('The URL Prediction!')
    p = '''
    Here you will be able put in the URL that you would like to see predict whether or not it is a phishsing url.
    - Input:
        - A single URL input
    ---

    - Here is a list of sample URLS to try out -- COPY & PASTE BELOW:
        - https://drive--google.com/luke.johnson
        - https://efax.hosting.com.mailru382.co/efaxdelivery/2017Dk4h325RE3
        - https://drive.google.com.download-photo.sytez.net/AONh1e0hVP
        - https://www.dropbox.com/buy

    '''
    st.markdown(p)


create_columns(config_page, header)

def url_input():
    t = st.text_input(label = 'URL Input', placeholder = 'https://sample-url.com/PASTE-YOUR-URL-HERE')
    return t

def url_cleaning():
    url = url_input()
    url = str(url)

    url = url.split('//')[-1]
    if url.endswith('/') is False:
        url = url + '/'
    df = pd.DataFrame({'domain': url}, index=[0])

    return df

def url_prediction():
    df = url_cleaning()
    st.text("")
    st.text("")

    with open('phish-model-1653354947.cloudpickle', 'rb') as pickle_file:
        model = pickle.load(pickle_file)
    
    pred = model.predict(df).tolist() 

    if 0 in pred:
        t = f'##### {df.domain[0]} is not a PHISH URL -- 🐟❌'
        # df["Prediction"] = 'Not a Phish URL'
        st.markdown(t)
    else:
        # df["Prediction"] = 'Phish URL'
        t = f'##### {df.domain[0]} is a PHISH URL -- 🐟✅'
        st.markdown(t)

    st.markdown('---')

    # st.write(df)

url_prediction()

st.text("")
st.text("")
st.text("")

create_columns(app_warnings, socials_contr)
# =========================================================================================
#                                           Footer
# =========================================================================================

footer="""<style>
a:link , a:visited{
color: white;
background-color: transparent;
text-decoration: underline;
}
a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://angelsantana.io" target="_blank">Angel Santana Hernandez</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
