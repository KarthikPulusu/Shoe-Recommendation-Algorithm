import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics.pairwise import cosine_similarity

# Load shoe data
shoes_df = pd.read_csv("data/shoes.csv")

# Encode categorical features
categorical_cols = ['brand', 'type', 'color', 'material', 'care_level', 'weather_suitability']
encoder = OneHotEncoder()
encoded = encoder.fit_transform(shoes_df[categorical_cols]).toarray()

# Combine with numeric features
numeric = shoes_df[['size']].values
features = pd.DataFrame(encoded)
combined_features = pd.concat([features, pd.DataFrame(numeric)], axis=1)

# Compute similarity
similarity_matrix = cosine_similarity(combined_features)

def recommend_similar_shoes(shoe_id, top_n=5):
    idx = shoes_df[shoes_df['shoe_id'] == shoe_id].index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    recommendations = []
    for i, score in sim_scores:
        recommendations.append({
            'shoe_id': int(shoes_df.iloc[i]['shoe_id']),
            'brand': shoes_df.iloc[i]['brand'],
            'type': shoes_df.iloc[i]['type'],
            'color': shoes_df.iloc[i]['color'],
            'weather_suitability': shoes_df.iloc[i]['weather_suitability'],
            'similarity': float(round(score, 2))
        })
    return recommendations

if __name__ == "__main__":
    result = recommend_similar_shoes(101)
    print("Content-based Recommendations for Shoe ID 101:")
    for r in result:
        print(r)