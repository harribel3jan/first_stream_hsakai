import streamlit as st
import time
st.title("Streamlit 超入門")

st.write("プログレスバーの表示")
"start‼"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

"DONE!!!!"
left_column,right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1 = st.expander("問い合わせ")
expander1.write("問い合わせ内容1を書く")

expander2 = st.expander("問い合わせ")
expander2.write("問い合わせ内容11を書く")

expander3 = st.expander("問い合わせ")
expander3.write("問い合わせ内容111を書く")

# text = st.text_input("あなたの趣味を教えてください、")
# "あなたの趣味は、",text,"です。"

# condition = st.slider("あなたの今の調子は？",0,10,5)
# "コンディション",condition

# if st.checkbox("show image"):
#     img = Image.open("sample.png")
#     st.image(img,caption = "THE WORLD" , use_column_width=True)


