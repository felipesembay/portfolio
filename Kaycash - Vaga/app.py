import streamlit as st
import pandas as pd
import pickle


pickle_in = open('lr.pkl', 'rb')
model = pickle.load(pickle_in)

# print title of web app
st.title("Simulação de Predição de preços de imóveis na cidade de SP- Demonstração de um aplicativo para Machine Learning")
st.markdown("Simulação de Predição de imóveis é um projeto criado para concorrer a uma vaga de Estágio.")

def predict(model, input_df):
    predictions_df = predict_model(estimator = model, data = input_df)
    predictions = predictions_df['Valor']
    return predictions

def run():
    
    from PIL import Image
    image_perfil = Image.open('keycash.jpg')
    

    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))

    st.sidebar.info('This app is created to predict credit classification')
    st.sidebar.success('https://www.linkedin.com/in/felipe-sembay/')
    
    st.sidebar.image(image_perfil)
    

    st.title("Credit Loan Prediction App")

    if add_selectbox == 'Online':

        const = st.number_input('const', min_value=1.0, max_value=1.0, value=1.0)
        if st.checkbox('Zona_media_densidade'):
            Media_densidade = 1.0
        else:
            Media_densidade = 0.0
        Qualidade = st.number_input('Qualidade', min_value=4.0, max_value=8.0 ,value=6.0)
        Banheiros = st.number_input('Banheiros', min_value=1.0, value=1.0)
        Comodos = st.number_input('Comodos', min_value=3.0, value=6.0)
        Lareiras = st.number_input('Lareiras', min_value=0.0, value=1.0)
        Garagem = st.number_input('Garagem', min_value=0.0, value=1.0)
        M2 = st.number_input('Area_metro', min_value=60.0, value=150.0)
        Quartos_t1 = st.number_input('Quartos_t1', min_value=1.0, value=1.0)
        Quartos_t2 = st.number_input('Quartos_t2', min_value=2.0, value=2.0)
        Aquecimento = st.selectbox('Aquecimento', ("Aceitavel", "Mediano", "Bom", "Excelente"))
        
        

        output=""

        input_dict = {'const' : const, 'Zona_media_densidade' : Media_densidade, 'Qualidade': Qualidade, 'Banheiros': Banheiros, 'Comodos': Comodos, 'Lareiras': Lareiras, 'Garagem': Garagem, 'Area_metro': M2, 'Quartos_t1': Quartos_t1, 'Quartos_t2': Quartos_t2, 'Aquecimento': Aquecimento}
        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output = float(output)
            
          
        st.success('O valor do seu imóvel é de {}'.format(output))
        st.markdown("Valores acima de 0.50 são classificados como liberados; valores inferiores a 0.50 são classificados como negados.")

    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)

if __name__ == '__main__':
    run()

