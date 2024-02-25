import openai
import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.environ.get("OPENAI_API_KEY")


# Set your OpenAI API key here

def generate_animal_description(name, breed, age, sex, simple_personality, preference):
    client = OpenAI(
    # This is the default and can be omitted
    api_key=api_key,
)
    """
    Generates an engaging animal personality description using the OpenAI API, including the pet's name.
    The description will be 200 ~ 300 words long.
    Ensure to present even the more challenging aspects of their personalities in a positive and attractive manner to prospective adopters.
    """
    conversation = [
        {"role": "system", "content": "You are a helpful assistant that generates engaging and detailed pet descriptions."},
        {"role": "user", "content": f"Generate an engaging description for a pet named {name} with the following details: Breed: {breed}, Age: {age}, Sex: {sex}, Personality: {simple_personality}, Preference: {preference}."}
    ]
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Make sure to use the appropriate model
        messages=conversation
    )
    
    # Extracting the generated description from the response
    if response.choices:
        last_message = response.choices[-1]  # Get the last message from the choices
        description = last_message.message.content  # Access the 'content' attribute of the message
    else:
        description = "Failed to generate description."
    
    return description.strip()


# Streamlit interface setup
st.title('Pet Personality Description Generator for BARC Animal Shelter')

# Form for user input
with st.form("animal_info_form"):
    name = st.text_input("Name")
    breed = st.text_input("Breed")
    age = st.text_input("Estimated Age")
    sex = st.selectbox("Sex", ["Male", "Female", "Other"])
    simple_personality = st.text_area("Simple Personality Description")
    preference = st.text_input("Preference")
    
    submitted = st.form_submit_button("Generate Description")
    if submitted:
        description = generate_animal_description(name, breed, age, sex, simple_personality, preference)
        st.text_area("Generated Description", description, height=300)
