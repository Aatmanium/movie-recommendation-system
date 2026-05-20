from pathlib import Path
import argparse
import difflib

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT_DIR / "data" / "movies.csv"
FEATURES = ["genres", "keywords", "tagline", "cast", "director"]


def load_movies(data_path=DATA_PATH):
    movies = pd.read_csv(data_path)
    missing_columns = [column for column in FEATURES + ["title"] if column not in movies]

    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    for feature in FEATURES:
        movies[feature] = movies[feature].fillna("")

    movies["combined_features"] = movies[FEATURES].agg(" ".join, axis=1)
    return movies


def recommend_movies(movie_name, top_n=10):
    movies = load_movies()
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(movies["combined_features"])
    similarity = cosine_similarity(feature_vectors)

    titles = movies["title"].astype(str).tolist()
    title_lookup = {title.lower(): title for title in titles}
    normalized_title = movie_name.lower()

    if normalized_title in title_lookup:
        matched_title = title_lookup[normalized_title]
    else:
        matches = difflib.get_close_matches(normalized_title, list(title_lookup), n=1)
        if not matches:
            raise ValueError(f"No close movie title found for '{movie_name}'.")
        matched_title = title_lookup[matches[0]]

    movie_position = movies.index[movies["title"] == matched_title][0]
    similarity_scores = list(enumerate(similarity[movie_position]))
    ranked_movies = sorted(similarity_scores, key=lambda item: item[1], reverse=True)

    recommendations = []
    for index, score in ranked_movies:
        title = movies.iloc[index]["title"]
        if title == matched_title:
            continue
        recommendations.append((title, score))
        if len(recommendations) == top_n:
            break

    return matched_title, recommendations


def main():
    parser = argparse.ArgumentParser(description="Recommend movies by title.")
    parser.add_argument("movie", help="Movie title to search for.")
    parser.add_argument("--top-n", type=int, default=10, help="Number of recommendations.")
    args = parser.parse_args()

    matched_title, recommendations = recommend_movies(args.movie, args.top_n)

    print(f"Recommendations for: {matched_title}\n")
    for rank, (title, score) in enumerate(recommendations, start=1):
        print(f"{rank}. {title} ({score:.3f})")


if __name__ == "__main__":
    main()
