import streamlit as st

def apply_theme():
    if "theme" not in st.session_state:
        st.session_state.theme = "Light"

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
            div[data-testid="stSidebar"] {
                background-color: #1c1e26;
            }
            h1, h2, h3, h4, h5, h6, p, label, span, div {
                color: white !important;
            }

            /* Sidebar text and icons */
            div[data-testid="stSidebarNav"] div {
                color: white !important;
            }

            /* Input fields */
            input, textarea {
                background-color: #262730 !important;
                color: white !important;
                border: 1px solid #444444 !important;
            }

            /* Select boxes and dropdowns */
            .stSelectbox > div, .stMultiSelect > div {
                background-color: #262730 !important;
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
            div[data-testid="stSidebar"] {
                background-color: #333333; /* Dark gray background */
            }
            h1, h2, h3, h4, h5, h6, p, label, span, div {
                color: black !important;
            }

            /* Sidebar text and icons */
            div[data-testid="stSidebarNav"] div {
                color: white !important;
            }

            input, textarea {
                background-color: white !important;
                color: black !important;
                border: 1px solid #ccc !important;
            }

            .stSelectbox > div, .stMultiSelect > div {
                background-color: white !important;
                color: black !important;
                border-color: #ccc !important;
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