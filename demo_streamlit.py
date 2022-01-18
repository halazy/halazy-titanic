import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("train.csv")

st.title("Hello mọi người, Hà code được chiếc web rồi nè hehe")
st.header("Data Science Certificate")

menu = ["Display Text", "Display Data", "Display Chart","Display Interactive Widget"]

choice = st.sidebar.selectbox("Danh mục", menu)

if choice == "Display Text":
    st.subheader("Hành trang tốt nghiệp Data Science")
    st.text("Khoá học được thiết kế nhằm ôn tập và bổ sung kiến thức cho học viên Data Science")
    st.markdown("### Có 5 chủ đề:")
    st.write("""
    - Chủ đề 1
    - Chủ đề 2
    - ...""")
    st.write("### Ngôn ngữ lập trình: Python")
    st.code("st.display_text_function('Nội dung')",language = "python")
elif choice == "Display Data":
    st.write("## Display Data")
    st.dataframe(data.head(3))
    st.table(data.head(3))
    st.json(data.head(2).to_json())
elif choice == "Display Chart":
    st.write("## Display Chart")
    count_Pcalss = data[['PassengerId', 'Pclass']].groupby(['Pclass']).count()
    st.bar_chart(count_Pclass)
    fig, ax = plt.subplots()
    ax = sns.boxplot(x='Pclass',y='Fare', data = data)
    st.pyplot(fig)
else:
    st.write("## Display Interactive Widget")
    st.write("### Input your infomation")
    name = st.text_input("Name:")
    sex = st.radio("Sex", options=['Male','Female'])
    age = st.slider("Age", 1, 100, 1)
    jobtime = st.selectbox("You have", options=['Part time job', 'Full time job'])
    hobbies = st.multiselect("Hobbies", options = ["Cooking", "Reading", "Writing", "Travel", "Others"])
    submit = st.button("Submit")
    if submit:
        st.write("#### Yourr Infomation:")
        st.write("Name:", name,
        "- Sex:", sex,
        "- Age:", age,
        " - You have a", jobtime,
        "and a house/apartment" if house else "",
        "- Hobbies:", ', '.join(map(str,hobbies)))

# Link tham khảo: https://docs.streamlit.io/en/stable/api.html


