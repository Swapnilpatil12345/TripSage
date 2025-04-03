import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment
gemini_api_key = os.getenv("API_KEY")

# Now you can use `api_key` in your code

# Configure the Gemini API
genai.configure(api_key=gemini_api_key)

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")
print("Model connected...")

def generate_travel_plan(model_name, user_preferences):
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(user_preferences)
    return response.text

def main():
    st.title("AI-Powered Virtual Travel Guide")

    # Model selection (optional if you want to give flexibility)
    model_name = "gemini-1.5-flash"

    # User input fields for travel preferences
    destination = st.text_input("Enter your destination:")
    activities = st.text_input("What activities are you interested in? (e.g., sightseeing, hiking, beach):")
    budget = st.text_input("What is your budget range? (e.g., $500 - $1000):")
    duration = st.text_input("How long do you plan to stay?")
    type_of_trip = st.selectbox("Type of trip", ["Adventure", "Relaxation", "Cultural", "Family", "Solo"])

    if st.button("Generate Itinerary"):
        if destination and activities and budget and duration:
            with st.spinner("Generating your travel plan..."):
                # Construct the user preferences for the AI
                user_preferences = f"""You are an AI travel planner. Generate a detailed travel itinerary based on the following details:
                                        Destination: {destination}
                                        Activities: {activities}
                                        Budget: {budget}
                                        Duration: {duration}
                                        Trip Type: {type_of_trip}

                                        Make sure to include recommendations for accommodation, dining, and must-visit places. use tables, visuals wherever necessary, 
                                        language should be friendly like you are recommending to your friend, also you can add little details about that place, it is historical place then tell its significance in short"""
                
                try:
                    # Generate the travel itinerary using the AI model
                    response = generate_travel_plan(model_name, user_preferences)
                    st.success("Travel Itinerary Generated!")
                    st.write(response)
                except Exception as e:
                     st.error("An error occurred. Please try again.")
                     st.write(e)
        else:
            st.warning("Please fill in all the required fields.")

if __name__ == "__main__":
    main()
