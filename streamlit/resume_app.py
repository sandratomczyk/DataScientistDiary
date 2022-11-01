import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Sandra Tomczyk
##### *Resume* 
''')

image = Image.open('sandra.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Data Scientist and Scrum Master at Arla Foods, passionate about telling stories with data, curious about possibilities appearing when mathematics meets business. 
- Experienced with R programming stems back to the Mathematics degree alongside the use of Python, Tableau, Statistica, SPSS and derive.
- Strong verbal and written communication skills as demonstrated by leading Data Science Community, facilitating trainings, webinars, online meet ups and mentoring programs for Citizen Developers. 
- Passionate for knowledge sharing, content development and writing articles on a personal blog promoting data science, machine learning and AI: https://datascientistdiary.com)
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/sandra-radgowska/" target="_blank">Sandra Tomczyk</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Master in Computer Science & Econometry** (Big Data), *University of Gdańsk*, Poland',
'2017-2019')
st.markdown('''
- Research thesis entitled `The impact of Performance Management on quality and control over various business processes by the example of Company X`.
''')

txt('**Bachelor in Mathematics** (Financial Mathematics), *Gdańsk University of Technology*, Poland',
'2014-2017')
st.markdown('''
- Research thesis entitled `Min-max theorems in graph theory based on König and Gallai Theorems`
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Scientist**, Arla Foods',
'2021-Present')
st.markdown('''
- Designing data modeling processes, creating algorithms and predictive models to extract the data the business needs, and help analyze the data and share insights. 
- Actively taking part in the Data Academy development, leading Citizen Data Science initiative in order to help employees to plan and develop their career path in data science.
- Providing mentorship and supervision to Citizen Developers, training materials development, workshops facilitation.
- Built own R programming e-learning course for Citizen Developers.
- Scrum Master of the Machine Learning Operations team (MLOps).
''')

txt('**Junior Data Scientist**, Arla Foods',
'2020-2021')
txt('**Data Science Intern**, Arla Foods',
'2019-2020')
txt('**Master Data Operations Specialist, SAP Super User**, Arla Foods',
'2017-2019')
st.markdown('''
- Main responsibility: Customer Accounts.
- Customer accounts creation and maintenance in SAP, Lotus Notes and Navision.
- Conditions, hierarchies and other relevant master data objects set up and maintenance related to O2C and P2P processes.
- Performance of periodic controls and reporting.
- Team's Lean Ambassador- improvement of team daily work using Lean Methodology.
- VBA scripts development.
''')

txt('**Tutor**, Creactive',
'2016-2017')
st.markdown('''
- Leading workshops for kids (age 6-9) around engineering, robotics, programming, physics and related topics. 
- Support for administration and learning materials development (workshop scenarios, handouts, instructions, etc.)
- Workshops lead based on LEGO Mindstorms, Scratch programming language and Minecraft game.
''')

txt('**Content Creator**, [Data Scientist Diary Blog](https://datascientistdiary.com/)',
'2020-Present')
st.markdown('''
- Sharing awareness on data literacy and analytics, helping people to kickstart their data science career.
- Writing blog posts withing topics such as latest trends on data science, machine learning, conferences' summits, tips & tricks for writing better code, own machine learning projects and experiments.
- Leading interviews with experienced data professionals.
- Blog supported with other social media: Instagram, Facebook & Tiktok.
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`, `tidyverse`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `ggplot2`, `Tableau`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Natural Language Processing', '`spaCy`, `gensim`, `scikit-learn`, `TensorFlow`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`shiny`, `streamlit`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `flask`, `R Shiny`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/sandra-radgowska/')
txt2('Website (Blog)', 'http://datascientistdiary.com')
txt2('GitHub', 'https://github.com/sandratomczyk/DataScientistDiary')
txt2('Instagram (PL)', 'https://www.instagram.com/datascientistdiarypl/')
txt2('Instagram (ENG)', 'https://www.instagram.com/datascientistdiary/')
txt2('Tiktok', 'https://www.tiktok.com/@datascientistdiarypl?_t=8WxwW6H1h4P&_r=1')
txt2('Facebook Site', 'https://www.facebook.com/DataScientistDiary')
txt2('Twitter', 'https://twitter.com/SandraRadgowska')
