import streamlit as st
st.cache_data.clear()
st.session_state.clear()

def apply_theme():
    if "theme" not in st.session_state:
        st.session_state.theme = "Dark"

    selected_theme = st.sidebar.radio(
        "Choose Theme", ("Light", "Dark"),
        index=0 if st.session_state.theme == "Light" else 1
    )
    st.session_state.theme = selected_theme
    

   

    if st.session_state.theme == "Dark":
        st.markdown("""
            <style>
            .stApp {
                background-color: #0e1117;
                color: white;
            }
            /* App header */
            header[data-testid="stHeader"] {
            background-color: #1c1e26 !important;  /* Dark background */
            color: white !important;               /* Text color */
            }

            div[data-testid="stSidebar"] {
                background-color: #1c1e26;
            }
            h1, h2, h3, h4, h5, h6, p, label, span, div {
                color: white !important;
            }
            




            /* Buttons */
            button[kind="primary"], .stButton>button {
                background-color: #4a4a4a !important;
                color: white !important;
                border-color: #6c757d !important;
            }
            button:hover {
                background-color: #5c5c5c !important;
                color: white !important;
            }

            /* File uploader */
            .stFileUploader > div {
                background-color: #262730 !important;
                color: white !important;
                border: 1px solid #444444 !important;
            }

            /* Slider label */
            .stSlider label {
                color: white !important;
            }
            </style>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
            <style>
            .stApp {
                background-color: white;
                color: black;
            }
            /* App header */
            header[data-testid="stHeader"] {
            background-color: #dedede !important;  /* Dark background */
            color: white !important;               /* Text color */
            }
                    
            section[data-testid="stSidebar"] {
            background-color: #d3d3d3 !important;
            }
            section[data-testid="stFileUploaderDropzone"] {
            background-color: #d3d3d3 !important;
            }
            
            h1, h2, h3, h4, h5, h6, p, label, span, div {
                color: black !important;
            }
            div[data-testid="stSelectbox"] div[data-baseweb="select"] > div:first-child{
            background-color: #d3d3d3 !important;
            }
            div[data-testid="stSelectbox"] 
            div[data-baseweb="select"] 
            > div:first-child 
            > div:first-child 
            > div:nth-child(2) 
            > input {
            background-color: #d3d3d3 !important;
            }
           
          
       
            button[kind="primary"], .stButton>button {
                background-color: #f0f2f6 !important;
                color: black !important;
                border-color: #d3d3d3 !important;
            }
            button:hover {
                background-color: #e1e1e1 !important;
                color: black !important;
            }
            
           




           
           

           


            .stFileUploader > div {
                background-color: white !important;
                color: black !important;
                border: 1px solid #ccc !important;
            }

            .stSlider label {
                color: black !important;
            }
            </style>
        """, unsafe_allow_html=True)