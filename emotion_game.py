# emotion_game.py
import random
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd

# Load pretrained emotion model
tokenizer = AutoTokenizer.from_pretrained("nateraw/bert-base-uncased-emotion")
model = AutoModelForSequenceClassification.from_pretrained("nateraw/bert-base-uncased-emotion")

# Load chat samples (you can update this file)
def load_chat_samples(file_path="data/game_chats.csv"):
    df = pd.read_csv(file_path)
    df = df[df['chat'].str.len() > 5].dropna().sample(frac=1)  # Shuffle
    return df.reset_index(drop=True)

# Predict emotion using the model
def predict_emotion(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_label = torch.argmax(probs, dim=1).item()
    label_map = model.config.id2label
    return label_map[predicted_label]

# Get one random chat with correct emotion
def get_chat_question(df):
    for _, row in df.iterrows():
        text = row['chat']
        try:
            label = predict_emotion(text)
            return {"chat": text, "emotion": label}
        except:
            continue
    return None
