# 🎮 SmartPlayer – Decode the Game Within the Game

SmartPlayer is a **gamified game analytics tool** built with **Streamlit, Scikit-learn, and Hugging Face Transformers**.  
It helps uncover hidden player behaviors and chat insights through clustering, sentiment analysis, and interactive mini-games.

---

## 🚀 Features
✔ **Player Persona Generator**: Uses KMeans to categorize players as *Aggressive Challenger*, *Casual Explorer*, etc.  
✔ **Chat Sentiment & Topic Modeling**: Extracts hidden topics and emotional tones using **TF-IDF + NMF** and **transformers**.  
✔ **Mystery Mode (Mini-Game)**: Guess the game/emotion from chat snippets to earn points.  
✔ **Emotion Game**: Real-time emotion detection from chat messages.  
✔ **Interactive Streamlit UI**: Built for seamless exploration and engagement.  
✔ **Modular Codebase**: Each feature is cleanly separated for easy debugging and extension.  

---

## 📂 Project Structure
📁 SmartPlayer/
├── data/
│ ├── game_chats.csv # Chat logs
│ └── player_data.csv # Player features
│
├── app.py # Main Streamlit app
├── chat_sentiment.py # Chat topic modeling
├── emotion_game.py # Emotion classifier game
├── mystery_mode.py # Quiz module
├── player_persona.py # Clustering logic
├── train_models.py # Model training script
├── utils.py # Helper functions
│
├── requirements.txt # Dependencies
└── .gitignore, .gitattributes # Config files


---

## 🧪Tech Stack
Streamlit – Web interface

Scikit-learn – Clustering & ML models

Transformers – Emotion classification

Pandas, NumPy – Data handling

Matplotlib, Seaborn – Visualizations

---
## 🛠️ Setup & Installation
Follow these steps to run SmartPlayer locally:

```bash
# 1️⃣ Clone the repository
git clone https://github.com/SiddhiSinghal/SmartPlayer.git
cd SmartPlayer

# 2️⃣ Create a virtual environment
python3 -m venv smartplayer-env
source smartplayer-env/bin/activate  # Windows: smartplayer-env\\Scripts\\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the Streamlit app
streamlit run app.py

'''


