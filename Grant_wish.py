import streamlit as st
import random

def grant_wish():
    wishes = [
        "You will get unlimited snacks... but only imaginary ones!",
        "All your exams will be open book... except the ones that matter!",
        "You will become a genius overnight... but only in your dreams!",
        "Your study sessions will last forever... unless you take a nap!",
        "You will understand every topic instantly... after 10 hours of study!",
        "Your Wi-Fi will never disconnect... but only when you're procrastinating!"
    ]
    return random.choice(wishes)

st.title("Wish Granting Genie 🧞‍♂️")
name = st.text_input("What is your name, O Wisher?", "")
if st.button("Grant a Wish"):
    st.write(f"✨ Hello, {name}! Your wish is granted:")
    st.success(grant_wish())
