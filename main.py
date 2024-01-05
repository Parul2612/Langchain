import langchain_helper as lch 
import streamlit as st

st.title("Pets Name Generator")

user_animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Hamster" ,"Goat", "Hen", "Cow", "Parrot", "Rabbit"))
#cat
if user_animal_type == "Cat":
    pet_color = st.sidebar.text_area(label="What color is your meownjar?", max_chars=15)
#dog
if user_animal_type == "Dog":
    pet_color = st.sidebar.text_area(label="What color is your kutta?", max_chars=15)
#ham
if user_animal_type == "Hamster":
    pet_color = st.sidebar.text_area(label="What color is your ham?", max_chars=15)
#goat
if user_animal_type == "Goat":
    pet_color = st.sidebar.text_area(label="What color is your bakri?", max_chars=15)
#hen
if user_animal_type == "Hen":
    pet_color = st.sidebar.text_area(label="What color is your Kombdi?", max_chars=15)
#cow
if user_animal_type == "Cow":
    pet_color = st.sidebar.text_area(label="What color is your Mooo?", max_chars=15)
#parrot
if user_animal_type == "Parrot":
    pet_color = st.sidebar.text_area(label="What color is your Popat?", max_chars=15)
#rabbit 
    
if user_animal_type == "Rabbit":
    pet_color = st.sidebar.text_area(label="What color is your Sasa?", max_chars=15)

if pet_color:
    response = lch.generate_pet_name(user_animal_type, pet_color)
    st.text(response['pet_name'])