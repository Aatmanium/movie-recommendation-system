---

#  Movie Recommendation System

This project is a **content-based movie recommendation system** built using **Python and machine learning techniques**. It recommends movies similar to a selected title based on features such as **genres, keywords, cast, tagline, and director** using **TF-IDF vectorization** and **cosine similarity**.

---

#  Project Overview

Recommendation systems are widely used in platforms like Netflix and Amazon.
This project demonstrates how to build a **content-based filtering model** that suggests similar movies by analyzing textual metadata from a dataset.

The system takes a movie name as input and returns a list of similar movies.

---

#  Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity
* Jupyter Notebook

---

#  Dataset

The dataset contains movie metadata including:

* Genres
* Keywords
* Tagline
* Cast
* Director

These features are combined into one text column and transformed into numerical vectors for similarity comparison.

---

#  How the Model Works

The recommendation pipeline follows these steps:

1. Load movie dataset
2. Select relevant features
3. Handle missing values
4. Combine selected features into one text column
5. Convert text into vectors using **TF-IDF**
6. Compute similarity scores using **cosine similarity**
7. Recommend top similar movies based on user input

---

#  Example

**Input:**

```
Avatar
```

**Recommended movies:**

```
Guardians of the Galaxy
John Carter
Star Trek
The Avengers
Jupiter Ascending
```

---

#  How to Run the Project

Clone the repository:

```
git clone https://github.com/your-username/movie-recommendation-system.git
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the notebook:

```
jupyter notebook movie_recommendation_system.ipynb
```

---

#  Future Improvements

Possible upgrades for this project:

* Add Streamlit web interface
* Deploy the model online
* Improve recommendation accuracy
* Add hybrid recommendation system
* Use larger datasets


Aatman Sabhaya<br>
(Applied AI Student)<br>
Machine Learning Enthusiast | Python Developer

---
