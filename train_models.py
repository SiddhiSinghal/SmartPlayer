import pandas as pd
import joblib
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

df = pd.read_csv("data/sample_game_logs.csv")

# ----- Clustering User Behavior -----
X = df[["session_length", "levels_completed", "purchases"]]
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
joblib.dump(kmeans, "models/kmeans_model.pkl")

# ----- Topic Modeling on Chat -----
vectorizer = TfidfVectorizer(stop_words='english')
X_text = vectorizer.fit_transform(df["chat_text"])
nmf = NMF(n_components=2, random_state=42)
nmf.fit(X_text)
joblib.dump(nmf, "models/nmf_model.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")
