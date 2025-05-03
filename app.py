import streamlit as st
from player_persona import generate_personas
from chat_sentiment import analyze_sentiment
from mystery_mode import get_random_question
from utils import load_data

st.set_page_config(page_title="SmartPlayer: Decode the Game", layout="wide")
st.title("🎮 SmartPlayer – Decode the Game Within the Game")

tab1, tab2, tab3 = st.tabs(["📊 Player Personas", "💬 Sentiment Map", "❓ Mystery Mode"])

with tab1:
    st.subheader("Cluster Players Based on Behavior")
    df = load_data("data/player_data.csv")
    personas_df, model = generate_personas(df)
    st.dataframe(personas_df)
    st.bar_chart(personas_df['persona'].value_counts())

with tab2:
    st.subheader("Analyze Sentiment of Game Chats")
    chat_df = load_data("data/game_chats.csv")
    result = analyze_sentiment(chat_df)
    st.write(result[['chat', 'sentiment']])
    st.line_chart(result['sentiment'])

with tab3:
    st.subheader("Guess the Game!")
    question = get_random_question()
    st.write("Chat Clue: ", f"*{question['chat']}*")
    guess = st.text_input("Your Guess:")
    if st.button("Submit Guess"):
        if guess.strip().lower() == question['answer'].lower():
            st.success("🎉 Correct!")
        else:
            st.error(f"❌ Nope! It was {question['answer']}.")
