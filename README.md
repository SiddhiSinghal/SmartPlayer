# 🎮 SmartPlayer – Decode the Game Within the Game
SmartPlayer is an interactive Streamlit application designed to analyze player behavior and in-game chat data using clustering, sentiment analysis, and NLP. It helps game designers and analysts uncover hidden insights—and even adds a fun twist through gamification!
---
##📦 Project Structure

SmartPlayer/
│
├── data/
│   ├── game_chats.csv            # In-game chat data
│   └── player_data.csv           # Player stats and behavioral data
│
├── app.py                        # Main Streamlit dashboard
├── chat_sentiment.py            # TF-IDF + NMF topic modeling
├── emotion_game.py              # Emotion classifier using transformers
├── mystery_mode.py              # Game guessing quiz logic
├── player_persona.py            # KMeans clustering for player types
├── train_models.py              # Training scripts for NLP/ML models
├── utils.py                     # Utility functions (e.g., load_data)
│
├── requirements.txt             # Python dependencies
├── .gitignore
└── .gitattributes
---
##🚀 Features
🧠 Player Persona Generator
Uses KMeans clustering on player stats to identify unique personas like:

Aggressive Challenger

Casual Explorer

Strategic Planner

💬 Chat Sentiment & Topic Modeling
Extracts key discussion topics using TF-IDF + NMF

Classifies emotions in messages using transformer models (e.g., DistilBERT)

🕵️ Mystery Mode – The Gamified Insight Quiz
Displays anonymous chat snippets

Lets the user guess the game context or emotion

Awards points and encourages data-driven exploration
---
##📊 Built With
Streamlit – for web interface

Scikit-learn – for clustering and modeling

Hugging Face Transformers – for emotion detection

Pandas, NumPy – data handling

Matplotlib, Seaborn – visualizations
---
##🛠️ Setup Instructions
Follow these steps to run the project on your local machine:  
```sh
🔧 1. Clone the Repo

git clone https://github.com/SiddhiSinghal/SmartPlayer.git
cd SmartPlayer
📦 2. Create Environment & Install Dependencies

python3 -m venv smartplayer-env
source smartplayer-env/bin/activate   # On Windows: smartplayer-env\Scripts\activate
pip install -r requirements.txt
▶️ 3. Run the App

streamlit run app.py



