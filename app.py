import streamlit as st
from utils.translator import Translator, DEFAULT_PROMPT

# @st.fragment
def translate_button():
    # 翻訳ボタン
    if st.button("翻訳"):
        if not st.session_state["input_text"]:
            st.warning("翻訳するテキストを入力してください")
        elif not st.session_state["api_key"]:
            st.warning("APIキーを設定してください")
        else:
            translator = Translator(
                api_key = st.session_state["api_key"],
                model_name = st.session_state["model_name"]
            )
            # 翻訳の実行
            try:
                response = translator.translate(
                    message=st.session_state["message"],
                    input=st.session_state["input_text"]
                    )
                st.session_state["output_text"] = response.text
                # st.write(response.text)
            except Exception as e:
                st.error(f"翻訳エラー: {e}")

def main():
    st.set_page_config(
        page_title="論文翻訳ツール",
        layout="wide"
    )

    if "api_key" not in st.session_state:
        st.session_state["api_key"] = None
    if "message" not in st.session_state:
        st.session_state["message"] = None
    if "input_text" not in st.session_state:
        st.session_state["input_text"] = None
    if "output_text" not in st.session_state:
        st.session_state["output_text"] = ""

    # Streamlit UIの構築
    st.title("論文翻訳ツール")

    # サイドバーの設定
    with st.sidebar:
        st.session_state["api_key"] = st.text_input(label="API key")
        st.session_state["model_name"] = st.selectbox(
            label="Model",
            options=[
                "gemini-2.0-flash",
                "gemini-2.0-flash-exp",
                "gemini-2.5-flash",
            ],
        )
        st.session_state["message"] = st.text_area(label="プロンプト", value=DEFAULT_PROMPT, height=500)

    col1, col2 = st.columns([1,1])

    with col2:
        st.markdown("<h5>日本語</h5>", unsafe_allow_html=True)
        # テキスト入力欄
        st.session_state["input_text"] = st.text_area("翻訳するテキストを入力してください", height=350)
        translate_button()

    with col1:
        st.markdown("<h5>英語</h5>", unsafe_allow_html=True)
        # if st.session_state["output_text"]:
        st.text_area("翻訳後のテキスト", value=st.session_state["output_text"], height=350)

if __name__=="__main__":
    main()
