import streamlit as st

# Main Title
st.title("Streamlit Demo App")

# Section: User Information
st.header("User Details")

name = st.text_input("What's your name?")
age = st.number_input("Your age", min_value=0, max_value=120, step=1)

if name and age:
    st.success(f"Hi *{name}* 👋")
    st.info(f"You are *{int(age)}* years young.")

# Section: Fun Fact
st.header("Did You Know?")

if age:
    years_left = 100 - age
    if years_left > 0:
        st.write(f"You'll hit the big 100 in just *{int(years_left)}* years! 🎉")
    else:
        st.write("You're already 100 or older – amazing! 🥳")
