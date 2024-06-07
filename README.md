Project Title: Movie Recommendation System

Objective:

To build a system that recommends movies based on user-selected movies.
Data Sources:

TMDB 5000 Movies Dataset: Contains metadata about movies.
TMDB 5000 Credits Dataset: Contains information about the cast and crew of the movies.
Libraries Used:

Pandas: For data manipulation and analysis.
NumPy: For numerical operations.
AST: For safely evaluating strings containing Python literals.
Requests: For making HTTP requests to the TMDB API.
Streamlit: For building and deploying the web application.
NLTK: For natural language processing tasks like stemming.
Scikit-Learn: For text vectorization and similarity computation.
Key Steps:

Data Loading: Load movies and credits datasets using Pandas.
Data Merging: Merge the datasets on the movie title.
Data Cleaning: Remove rows with missing values.
Data Transformation:
Convert genre, keyword, cast, and crew information from string format to list format.
Extract the top 3 cast members and the director for each movie.
Combine genres, keywords, cast, and crew into a single 'tags' column for each movie.
Apply stemming to the words in the 'tags' column to standardize them.
Text Vectorization: Convert the 'tags' column into a matrix of token counts using CountVectorizer.
Similarity Calculation: Compute cosine similarity between movie tags to measure their similarity.
Poster Fetching: Retrieve movie posters from the TMDB API.
Recommendation Algorithm:

Find the index of the selected movie.
Calculate the similarity scores of all movies with the selected movie.
Sort the movies based on similarity scores.
Recommend the top 5 most similar movies.
Streamlit Web App:

User Interface:
Title: "MOVIE RECOMMEND SYSTEM"
Dropdown menu to select a movie from the dataset.
"Recommend" button to generate recommendations.
Recommendation Display:
Display the titles and posters of the recommended movies in a row.


#SCREENSHOTS

![Screenshot 2024-06-07 101746](https://github.com/ZubairZubii/movie_recomendation/assets/148703653/5fe765ce-904c-4cc5-8253-34a5d6664a85)


![Screenshot 2024-06-07 101802](https://github.com/ZubairZubii/movie_recomendation/assets/148703653/4101336b-6de0-4b59-b6d8-a6c5bf96fbd3)


![Screenshot 2024-06-07 102002](https://github.com/ZubairZubii/movie_recomendation/assets/148703653/5c167eda-b3ca-4f8e-8bc9-a3f57ae0b9b9)
