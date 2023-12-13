import streamlit as st

def front():
    overlay_opacity = 0.5
    
    # Пользовательский CSS для изменения заднего фона
    page_bg_img = f"""
    <style>
    .main {{
        background-image: url("https://img.freepik.com/free-photo/abstract-textured-backgound_1258-30452.jpg?w=740&t=st=1702492947~exp=1702493547~hmac=f2755c3a12e7f8c3ab1f592f1b7fa3a97e610236ebbbd9652e494a12916f1df3");
        background-size: cover;
    }}
    .main::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: black;
        opacity: {overlay_opacity};
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    current_page = st.session_state.get("current_page", "home")

      # Пользовательский CSS для главной страницы
    custom_css = """
    <style>
    h1 {
        color: white;
        font-size: 50px;
        text-shadow: 4px 4px 4px rgba(0, 0, 0, 0.8);
        white-space: nowrap;
        text-align: center;
        margin-left: -25%;
    }
    .underline {
        border: 1px solid white;
        margin-top: -20px;  /* Отрицательное значение отступа для приближения к заголовку */
    }
    .subtitle {
        color: rgba(255, 255, 255, 0.7);
        font-size: 30px;
        text-align: center;
        margin-top: -10px;
        line-height: 1.2;
        font-weight: bold;
    }
    .subtitle2 {
        color: rgba(255, 255, 255, 0.7);
        font-size: 30px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        white-space: nowrap;
        margin-left: -8%;
    }
    </style>
    """
    st.title("Веб-приложение для преобразования текста в речь")
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown("<hr class='underline'>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Мы преобразуем текст в речь<br> с помощью нейросети</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle2'>Вы можете загрузить свой текстовый файл и услышать его</p>", unsafe_allow_html=True)

def main():
    front()
    # Форма для загрузки файла
    uploaded_file = st.file_uploader("", type="txt")

if __name__ == "__main__":
    main()
