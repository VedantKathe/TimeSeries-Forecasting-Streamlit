import streamlit as st 
import streamlit.components.v1 as stc
import pandas as pd

nav=st.sidebar.radio('NAVIGATION',['Home','Inventory'])


if nav=='Home':
    HtmlFile = open("design.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    stc.html(source_code)
    st.text(' ')
    st.text(' ')
    st.image("walmart.jfif",width=700)
    
    
if nav=='Inventory':
    medicine_name = st.sidebar.selectbox(
    'SELECT ALGORITHM',
    ('Time Series Model', 'Machine Learning Algorithm')
    )
    
    if  medicine_name == 'Time Series Model':
        st.write('Hello Bhois..!')
    
    st.title("Result")
    if  medicine_name == 'Machine Learning Algorithm':
        models = pd.DataFrame({
    'Model Name': ['Linear Regression','KNN Regression',
              'Decision Tree Regression','Random Forest Regression'],
    
    'RMSE Score': ['21847.47', '18955.10', ' 5018.82', '4197.05'],  'R2 Score': ['0.09', '0.09', ' 0.95', '0.97']
   
    })

    Index = pd.Series([1, 2, 3, 4])
    models.set_index(Index, inplace=True)
    models
