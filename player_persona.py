import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def generate_personas(df, n_clusters=3):
    scaler = StandardScaler()
    X = scaler.fit_transform(df[['avg_session_time', 'games_played', 'level']])
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['persona'] = kmeans.fit_predict(X)
    return df, kmeans
