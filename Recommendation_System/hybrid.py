# from content_based import recommend_similar_shoes
# from collaborative_simulated import recommend_by_user_profile
from Recommendation_System.content_based import recommend_similar_shoes
from Recommendation_System.collaborative_simulated import recommend_by_user_profile

import pandas as pd

shoes_df = pd.read_csv("data/shoes.csv")
users_df = pd.read_csv("data/users.csv")

def hybrid_recommendations(user_id, reference_shoe_id, top_n=5):
    cb_recs = recommend_similar_shoes(reference_shoe_id, top_n=top_n)
    cf_recs = recommend_by_user_profile(user_id, top_n=top_n)

    user_info = users_df[users_df['user_id'] == user_id].iloc[0]
    preferred_weather = user_info['preferred_weather']

    hybrid_scores = {}
    for rec in cb_recs:
        score = rec['similarity'] * 0.6
        if rec['weather_suitability'] == preferred_weather:
            score *= 1.2
        hybrid_scores[rec['shoe_id']] = hybrid_scores.get(rec['shoe_id'], 0) + score

    for rec in cf_recs:
        weather_fit = shoes_df[shoes_df['shoe_id'] == rec['shoe_id']]['weather_suitability'].values[0]
        score = rec['score'] * 0.4
        if weather_fit == preferred_weather:
            score *= 1.2
        hybrid_scores[rec['shoe_id']] = hybrid_scores.get(rec['shoe_id'], 0) + score

    sorted_hybrid = sorted(hybrid_scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
    final_recs = []
    for shoe_id, score in sorted_hybrid:
        shoe_info = shoes_df[shoes_df['shoe_id'] == shoe_id].iloc[0]
        final_recs.append({
            'shoe_id': shoe_id,
            'brand': shoe_info['brand'],
            'type': shoe_info['type'],
            'color': shoe_info['color'],
            'weather_suitability': shoe_info['weather_suitability'],
            'hybrid_score': round(score, 2)
        })
    return final_recs

if __name__ == "__main__":
    result = hybrid_recommendations(user_id=1, reference_shoe_id=101)
    print("Hybrid Recommendations for User 1 (Shoe ID 101):")
    for r in result:
        print(r)