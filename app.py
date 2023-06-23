# import streamlit as st
# from multiapp import MultiApp
# from apps import home, data_stats

# app = MultiApp() 

# app.add_app("Home", home.app)
# app.add_app("Data Stats", data_stats.app) 

# app.run()

import streamlit as st

st.title("title") # タイトル
st.header("header") # ヘッダー
st.write("write") # 表示
st.markdown("# markdown") # マークダウンで表示
st.text("text") # テキスト表示
