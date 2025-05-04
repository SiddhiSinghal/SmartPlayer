import streamlit as st
from player_persona import generate_personas
from chat_sentiment import analyze_sentiment
from mystery_mode import get_random_question
from utils import load_data
from emotion_game import load_chat_samples, get_chat_question  # Add this at the top
import os
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

st.set_page_config(page_title="SmartPlayer: Decode the Game", layout="wide")
st.title("🎮 SmartPlayer – Decode the Game Within the Game")

tab1, tab2, tab3, tab4 = st.tabs(["📊 Player Personas", "💬 Sentiment Map", "❓ Mystery Mode","🧠 Emotion Game"])

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

with tab4:
    st.subheader("Guess the Emotion in the Chat!")
    df_emotions = load_chat_samples("data/game_chats.csv")
    question = get_chat_question(df_emotions)

    if question:
        st.markdown(f"**Chat Clue**: *{question['chat']}*")
        user_guess = st.text_input("What's the emotion? (e.g., joy, sadness, anger, etc.)")

        if st.button("Submit Emotion Guess"):
            if user_guess.strip().lower() == question['emotion'].lower():
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Incorrect. The correct emotion was **{question['emotion']}**.")
    else:
        st.warning("Couldn't fetch a valid chat sample. Try refreshing.")
