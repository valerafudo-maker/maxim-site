
import streamlit as st
import base64
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{data}");
            background-size: contain;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

set_bg("background.jpg")

st.title("Здрасте")
st.subheader("**Поставьте 5 пожалуйста**")

if "answer" not in st.session_state:
    st.session_state.answer = None

slot = st.empty()

with slot.container():
    # --- Стартовый экран: две кнопки слева и справа ---
    if st.session_state.answer is None:
        col1, col2 = st.columns(2)
        if col1.button("Да"):
            st.session_state.answer = "yes"
            st.rerun()
        if col2.button("Нет"):
            st.session_state.answer = "no"
            st.rerun()

    # --- Ответ "Да" ---
    elif st.session_state.answer == "yes":
        st.write("Правильно")
        col1, col2 = st.columns(2)
        if col1.button("Смысл этого сайта?"):
            st.session_state.answer = "why"
            st.rerun()
        if col2.button("Назад"):
            st.session_state.answer = None
            st.rerun()

    # --- Ответ "Нет" ---
    elif st.session_state.answer == "no":
        st.write("...")
        st.link_button("АД", "https://www.nalog.gov.ru/rn77/")

    # --- Финал: кнопка-ссылка на другой сайт ---
    elif st.session_state.answer == "why":
        st.link_button("поставить 5", "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiZ0de_jKCXAxWSIRAIHX9rK3oQFnoECA8QAQ&url=https%3A%2F%2Fedu.rk.gov.ru%2F&usg=AOvVaw2Lis5Nu07A8qMFo2-fFnBY&opi=89978449")
