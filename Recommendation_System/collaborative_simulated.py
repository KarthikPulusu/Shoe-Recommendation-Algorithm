import pandas as pd
from collections import defaultdict

interactions = pd.read_csv("data/interactions.csv")
users = pd.read_csv("data/users.csv")
shoes = pd.read_csv("data/shoes.csv")

interaction_weights = {'view': 0.1, 'wishlist': 0.3, 'purchase': 1.0}

def recommend_by_user_profile(user_id, top_n=5):
    user_info = users[users['user_id'] == user_id].iloc[0]
    preferred_weather = user_info['preferred_weather']
    history = interactions[interactions['user_id'] == user_id]

    weighted_scores = defaultdict(float)
    for _, row in history.iterrows():
        weight = interaction_weights.get(row['interaction_type'], 0)
        shoe_info = shoes[shoes['shoe_id'] == row['shoe_id']].iloc[0]
        if shoe_info['weather_suitability'] == preferred_weather:
            weight *= 1.2  # boost for weather alignment
        weighted_scores[row['shoe_id']] += weight

    sorted_scores = sorted(weighted_scores.items(), key=lambda x: x[1], reverse=True)
    recommendations = [{'shoe_id': sid, 'score': round(score, 2)} for sid, score in sorted_scores[:top_n]]
    return recommendations

if __name__ == "__main__":
    result = recommend_by_user_profile(1)
    print("Collaborative Recommendations for User 1:")
    for r in result:
        print(r)