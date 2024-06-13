"""
Recommendation System Script

This script loads interaction data from CSV files, computes user-user cosine similarity, and generates product recommendations for a specified user. The recommendations are based on the interactions of the most similar users.

Modules:
    - pandas: Used for data manipulation and analysis.
    - sklearn.metrics.pairwise: Used for computing cosine similarity between users.
    - numpy: Used for numerical operations.

Functions:
    - get_recommendations(user_id, top_n=10): Generates product recommendations for the given user based on cosine similarity.

Usage:
    Run the script and it will load the interaction data, compute the similarity matrix, and generate and save recommendations for the specified user.

"""
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

print("Loading data...")
bootstrap_data = pd.read_csv('bootstrap.csv')
cleaned_data = pd.read_csv('cleaned_data.csv')
training_interaction_matrix = cleaned_data.pivot_table(index='idcol', columns='item_descrip', values='interaction', aggfunc='count', fill_value=0)
testing_interaction_matrix = bootstrap_data.pivot_table(index='idcol', columns='item_descrip', values='interaction', aggfunc='count', fill_value=0)

print("Computing cosine similarity...")
user_similarity = cosine_similarity(training_interaction_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=training_interaction_matrix.index, columns=training_interaction_matrix.index)
print("Cosine similarity computed.")

def get_recommendations(user_id, top_n=10):
    """
    Generates product recommendations for the given user based on cosine similarity.

    Parameters:
        user_id (int): The ID of the user for whom recommendations are to be generated.
        top_n (int): The number of top recommendations to return. Default is 10.

    Returns:
        list of tuples: A list of tuples where each tuple contains a recommended product and its similarity score.

    Raises:
        ValueError: If the user_id does not exist in the training data.
    """
    if user_id not in user_similarity_df.index:
        raise ValueError(f"User ID {user_id} does not exist in the training data.")
    
    # Get the similarity scores for the user, while excluding the users themselves
    similarity_scores = user_similarity_df[user_id].sort_values(ascending=False)[1:]
    similar_users = similarity_scores.index
    
    print(f"Similarity scores for user {user_id}:")
    print(similarity_scores.head(10))
    similar_users_interactions = training_interaction_matrix.loc[similar_users].sum().sort_values(ascending=False)
    common_items = similar_users_interactions.index.intersection(training_interaction_matrix.columns)
    similar_users_interactions = similar_users_interactions.loc[common_items]
    
    recommendations = similar_users_interactions.head(top_n).index
    print(f"Top {top_n} recommendations (before scoring):")
    print(recommendations)
    
    recommendations_with_scores = []
    for rec in recommendations:
        avg_similarity_score = similarity_scores[similar_users].mean()
        recommendations_with_scores.append((rec, avg_similarity_score))
    
    print(f"Recommendations with scores for user {user_id}:")
    print(recommendations_with_scores)
    
    return recommendations_with_scores

if __name__ == '__main__':
    user_id = 25678849118  
    try:
        print(f"Getting recommendations for user {user_id}...")
        recommendations = get_recommendations(user_id)
        print(f"Recommendations for user {user_id}: {recommendations}")
        recommendations_df = pd.DataFrame(recommendations, columns=['Product', 'Similarity'])
        recommendations_df.to_csv(f'recommendations_{user_id}.csv', index=False)
        print(f"Recommendations saved to recommendations_{user_id}.csv")
    except ValueError as e:
        print(e)

    print("Script completed successfully.")