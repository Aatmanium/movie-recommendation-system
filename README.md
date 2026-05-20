# Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Recommendation-orange)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

A content-based movie recommendation system that suggests similar movies from metadata such as genres, keywords, tagline, cast, and director.

## Project Highlights

- Built a content-based recommendation pipeline using movie metadata.
- Combined multiple text features into one model-ready representation.
- Applied TF-IDF vectorization to convert metadata into numerical vectors.
- Used cosine similarity to rank movies by closeness to a selected title.
- Added both notebook exploration and a reusable command-line script.

## Tech Stack

- Python
- NumPy
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- Jupyter Notebook

## Project Structure

```text
movie-recommendation-system/
|-- data/
|   `-- movies.csv
|-- notebooks/
|   `-- movie_recommendation_system.ipynb
|-- src/
|   `-- recommend.py
|-- requirements.txt
`-- README.md
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/Aatmanium/movie-recommendation-system.git
cd movie-recommendation-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run recommendations from the command line:

```bash
python src/recommend.py "Avatar"
```

Open the notebook:

```bash
jupyter notebook notebooks/movie_recommendation_system.ipynb
```

## How It Works

1. Load movie metadata from `data/movies.csv`.
2. Select recommendation features: genres, keywords, tagline, cast, and director.
3. Replace missing values with empty strings.
4. Combine selected features into a single text field.
5. Convert text into TF-IDF vectors.
6. Compute cosine similarity between movies.
7. Return the closest movie matches for a user-provided title.

## Example Output

```text
Recommendations for: Avatar

1. Alien
2. Aliens
3. Guardians of the Galaxy
4. Star Trek Beyond
5. Star Trek Into Darkness
```

## Future Improvements

- Build a Streamlit interface for interactive recommendations.
- Add posters and metadata cards for better user experience.
- Evaluate recommendations with user feedback or click data.
- Extend the model into a hybrid recommender with ratings data.

## Author

**Aatmanium**  
Applied AI Student | Machine Learning Enthusiast | Python Developer
