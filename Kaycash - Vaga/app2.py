import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import time
from sklearn import metrics


#import the data
data = pd.read_csv("Desafio2_input.csv", sep=';')
st.title("Bem vindo ao aplicativo para predição no preço de imóveis em SP")

#Transforming some columns
data['Aquecimento'] = data.QualidadeAquecimento.map({'Fa': 0, 'TA': 1, 'Gd': 2, 'Ex': 3})
data['Zona'] = data.Zona.map({'RL': 0, 'RM': 1})
del data['Id']
del data['AnoConstrucao']
del data['QualidadeAquecimento']
data['Area_metro'] = data['Area'] * 0.092903
del data['Area']

#checking the data
st.write("This is an application for knowing how much range of house prices you choose using machine learning. Let's try and see!")
check_data = st.checkbox("See the simple data")
if check_data:
    st.write(data.head())
st.write("Now let's find out how much the prices when we choosing some parameters.")


#input the numbers
Zona = st.slider("O imóvel fica numa zona de média ou baixa densidade? - 0 para baixa densidade e 1 para média densidade",int(data.Zona.min()),int(data.Zona.max()),int(data.Zona.mean()))
Qualidade  = st.slider("Qual é a qualidade do material e acabamento do imóvel?",int(data.Qualidade.min()),int(data.Qualidade.max()),int(data.Qualidade.median()) )
Banheiros      = st.slider("Quantos banheiros o imóvel possui?",int(data.Banheiros.min()),int(data.Banheiros.max()),int(data.Banheiros.median()) )
Comodos    = st.slider("Quantos comodos há no imóvel?",int(data.Comodos.min()),int(data.Comodos.median()), int(data.Comodos.max()))
Lareiras    = st.slider("Quantas lareiras há no imóvel?",int(data.Lareiras.min()),int(data.Lareiras.median()), int(data.Lareiras.max()))
Garagem    = st.slider("Quantas vagas de garagem há no imóvel?",int(data.Garagem.min()),int(data.Garagem.max()), int(data.Garagem.median()))
Area_metro    = st.slider("Quantos metros quadrados há no imóvel?",int(data.Area_metro.min()),int(data.Area_metro.max()), int(data.Area_metro.median()))
Quartos_t1    = st.slider("Quantos quartos do tipo T1 há no imóvel?",int(data.Quartos_t1.min()),int(data.Quartos_t1.max()), int(data.Quartos_t1.median()))
Quartos_t2    = st.slider("Quantos quartos do tipo T2 há no imóvel?",int(data.Quartos_t2.min()),int(data.Quartos_t2.max()), int(data.Quartos_t2.median()))
Aquecimento    = st.slider("Qual é a qualidade do auqecimento do imóvel? 0 - Aceitável, 1 - Mediano, 2 - Bom, 3 - Excelente",int(data.Aquecimento.min()),int(data.Aquecimento.max()), int(data.Aquecimento.median()))



#splitting your data
X = data.drop('Preco', axis = 1)
y = data['Preco']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.25, random_state=25)

#modelling step
#import your model
model=LinearRegression()
#fitting and predict your model
model.fit(X_train, y_train)
model.predict(X_test)
model.score(X_train, y_train)
predictions = model.predict([[Zona,Qualidade,Banheiros,Comodos,Lareiras,Garagem,Area_metro,Quartos_t1,Quartos_t2,Aquecimento]])[0]
errors = np.sqrt(mean_squared_error(y_test,model.predict(X_test)))

#checking prediction house price
if st.button("Run me!"):
    st.header("Your house prices prediction is R$ {}".format(int(predictions)))
    st.subheader("Your range of prediction is R$ {} - RS {}".format(int(predictions-errors),int(predictions+errors) ))
