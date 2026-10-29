import streamlit as st

st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
st.title("Dashboard", icon=":material/dashboard:")
st.header("Streamlit is cool")

agree = st.checkbox("I agree with Tabish")

if agree:
    st.write("Great! You agreed with Tabish.")


genre = st.radio("What's your favorite movie genre", ["Comedy", "Drama", "Documentary"])

if genre == "Comedy":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

num1 = st.number_input("Enter a number")
num2 = st.number_input("Enter another number")


if st.button("Add"):
    st.write("The sum of the two numbers is:", num1 + num2)
