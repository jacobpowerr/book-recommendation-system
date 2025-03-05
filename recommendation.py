import pandas as pd
import numpy as np
from user_input import get_user_input

df = pd.read_csv("books_with_difficulty.csv")

def similarity_score(book_title, favourite_books):

    score = 0

    for fav_book in favourite_books:
        if fav_book.lower() in book_title.lower():
            score += 1
    return score

def recommend_books(favorite_books, preferred_genre, preferred_difficulty, min_rating,):

    filtered_books = df[(df['Genre'].str.lower() == preferred_genre.lower()) &
        (df['difficulty_level'].str.lower() == preferred_difficulty.lower()) &
        (df['goodreads_avg'] >= min_rating)]

    if filtered_books.empty:
        print("No books match your preferences.")
        return []
    
    filtered_books = filtered_books.copy()
    filtered_books['similarity'] = filtered_books['Work_Title'].apply(lambda x: similarity_score(x, favorite_books))

    filtered_books = filtered_books.sort_values(by = ['similarity', 'goodreads_avg'], ascending=[False, False])

    top_books = filtered_books.head(5)

    recommendations = top_books[['Work_Title', "Author_First", 'Author_Last', 'Genre', 'goodreads_avg', 'difficulty_level', 'goodreads_URL']]
    return recommendations