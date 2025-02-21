import pickle
import streamlit as st

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

menu = st.sidebar.radio("Menu", ["🏠 Home", "ℹ️ Tentang Aplikasi"])

if menu == "🏠 Home":
    st.title('🔍 DiaWise: Prediksi Diabetes')
    st.markdown("### Aplikasi Prediksi Diabetes Berbasis AI 🩺")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("logo.png", caption="DiaWise", use_container_width=True)

    st.markdown("---")

    st.subheader("Masukkan Data Pasien:")
    Pregnancies = st.number_input('Jumlah Kehamilan', min_value=0, step=1)
    Glucose = st.number_input('Kadar Glukosa', min_value=0)
    BloodPressure = st.number_input('Tekanan Darah', min_value=0)
    SkinThickness = st.number_input('Ketebalan Kulit', min_value=0)
    Insulin = st.number_input('Level Insulin', min_value=0)
    BMI = st.number_input('Indeks Massa Tubuh (BMI)', min_value=0.0, format="%.2f")
    DiabetesPedigreeFunction = st.number_input('Riwayat Diabetes Keluarga', min_value=0.0, format="%.3f")
    Age = st.number_input('Usia', min_value=0, step=1)

    diab_diagnosis = ''
    if st.button('🔬 Prediksi Diabetes', help="Klik untuk memprediksi diabetes berdasarkan data yang dimasukkan"): 
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
            diab_diagnosis = '⚠️ Pasien kemungkinan terkena diabetes.'
            st.error(diab_diagnosis)
        else:
            diab_diagnosis = '✅ Pasien dalam kondisi sehat.'
            st.success(diab_diagnosis)

    # Footer
    st.markdown("---")
    st.markdown("🔗 **DiaWise** - Create By Adrian")

elif menu == "ℹ️ Tentang Aplikasi":

    st.title("ℹ️ Tentang DiaWise")
    st.image("logo.png", caption="Mendeteksi Diabetes dengan AI", use_container_width=True)
    
    st.write("""
    DiaWise adalah aplikasi prediksi diabetes berbasis kecerdasan buatan (AI). 
    Aplikasi ini menggunakan model machine learning untuk menganalisis data kesehatan pengguna 
    dan memberikan hasil prediksi kemungkinan terkena diabetes.
    
    Dengan memasukkan beberapa parameter kesehatan seperti kadar glukosa, tekanan darah, 
    indeks massa tubuh (BMI), dan faktor keturunan, aplikasi ini dapat membantu dalam deteksi dini diabetes.
    """)

    st.markdown("---")

    st.subheader("👨‍💻 About Developer")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image("profile.jpg", width=150, caption="Adrian Fahren Setiawan", use_container_width=False)

    with col2:
        st.write("""
        **Nama:** Adrian Fahren Setiawan  
        **Email:** [adrianfahren10@gmail.com](mailto:adrianfahren10@gmail.com)  
        **LinkedIn:** [linkedin.com/in/adrian-fahren-setiawan](https://www.linkedin.com/in/adrian-fahren-setiawan-34a939278/)  
        **GitHub:** [github.com/AdrianIchiro](https://github.com/AdrianIchiro)  
        """)

    st.markdown("Terima kasih telah menggunakan DiaWise! 🚀")



