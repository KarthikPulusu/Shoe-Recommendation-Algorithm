import streamlit as st
from Recommendation_System.hybrid import hybrid_recommendations
import pandas as pd

# Load users and shoes data
users_df = pd.read_csv("data/users.csv")
shoes_df = pd.read_csv("data/shoes.csv")

st.title("Smart Shoe Recommender")

# Dynamic user input
user_id = st.selectbox("Select User ID", users_df["user_id"].unique())
reference_shoe_id = st.selectbox("Select a Shoe ID you like", shoes_df["shoe_id"].unique())

# Extra user inputs (Region, Preferred Weather, Typical Usage)
region = st.selectbox("Select Your Region", users_df["region"].unique())
preferred_weather = st.selectbox("Preferred Weather", ['rainy', 'cold', 'sunny', 'humid', 'moderate'])
typical_usage = st.selectbox("Typical Shoe Usage", ['casual', 'formal', 'sport'])

# Button to trigger
if st.button("Get Recommendations"):
    # Display selected details
    st.markdown(f"**User ID:** {user_id}, **Region:** {region}, **Weather:** {preferred_weather}, **Usage:** {typical_usage}")
    
    # Run hybrid recommendation logic    
    recs = hybrid_recommendations(user_id, reference_shoe_id, top_n=5)
    st.subheader("📋 Recommended Shoes")
    st.dataframe(pd.DataFrame(recs))
else:
    st.info("👈 Select user and shoe ID to get recommendations.")
