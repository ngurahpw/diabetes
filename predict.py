import streamlit as st

from web_functions import predict

def app(df, x, y):

    st.title("LAST for Diabetes Prediction")

    col1, col2, col3 = st.columns(3)
    with col1:
        Urea = st.text_input("Input Value of Urea")
    with col1:
        Cr = st.text_input("Input Value of Creatinine ratio (Cr)")
    with col1:
        HbA1c = st.text_input("Input Value of HbA1c")
    with col2:
        Chol = st.text_input("Input Value of Cholesterol (Chol)")
    with col2:
        TG = st.text_input("Input Value of Triglycerides (TG)")
    with col2:
        HDL = st.text_input("Input Value of HDL Cholesterol")
    with col3:
        LDL = st.text_input("Input Value of LDL")
    with col3:
        VLDL = st.text_input("Input Value of VLDL")
    with col3:
        BMI = st.text_input("Input Value of Body Mass Index")

    features = [Urea,Cr,HbA1c,Chol,TG,HDL,LDL,VLDL,BMI]

    # tombol prediksi
    if st.button("Prediction"):
        prediction, score = predict(x, y, features)
        score = score
        st.info("Prediction is Succesfully")

        if(prediction == 0):
            st.warning("Patien with diabetes")
        elif(prediction == 1):
            st.success("Patien no diabetes")
        else:
            st.warning("Pasien maybe with diabetes")

        st.write("The accuration of prediction is ", (score*100), "%")
                 