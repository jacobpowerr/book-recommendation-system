import pandas as pd

df = pd.read_csv("cleaned_books.csv")

def get_user_input():

    favorite_books = []

    print("What are your top5 favorite books?")

    for i in range(5):
        book = input(f"{i+1}. ").strip()
        favorite_books.append(book)

    available_genres = df['Genre'].unique()
    print("\nAvailable genres:", ", ".join(available_genres))
    preferred_genre = input("\nEntre your preferred genre: ").strip()

    available_difficulties = ["Easy", "Medium", "Hard"]
    print("\nAvailable difficulties:", ", ".join(available_difficulties))
    preferred_difficulty = input("\nEntre your preferred difficulty: ").strip()

    try:
        min_rating = float(input("Enter the minumum goodreads rating (1-5): ").strip())
    except:
        min_rating = 3.5

    return favorite_books, preferred_genre, preferred_difficulty, min_rating

