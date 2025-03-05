from user_input import get_user_input
from recommendation import recommend_books

def format_title(title, goodreads_url):
    """Format title using information from the title or Goodreads URL"""
   
    if " " in title:
        return title
        
    if "q=" in goodreads_url:
        
        url_title = goodreads_url.split("q=")[1]
        
        url_title = url_title.replace("+", " ")
        
        if title.lower() in url_title.lower().replace(" ", ""):
            for word in title.split():
                if word.lower() in url_title.lower():
                    start_idx = url_title.lower().find(word.lower())
                    if start_idx > 0:
                        return url_title[start_idx:]
        
        import re
        return re.sub(r'(?<!^)(?=[A-Z])', ' ', title)
    
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', title)

if __name__ == "__main__":
    favorite_books, preferred_genre, preferred_difficulty, min_rating = get_user_input()

    recommended_books = recommend_books(favorite_books, preferred_genre, preferred_difficulty, min_rating)

    if not recommended_books.empty:
        print("\nTop 5 Book Recommendations:")
        for i, book in enumerate(recommended_books.itertuples(), 1):
            formatted_title = format_title(book.Work_Title, book.goodreads_URL)
            print(f"{i}. Title: {formatted_title}")
            print(f"    Author: {book.Author_First} {book.Author_Last}")
            print(f"    Genre: {book.Genre}")
            print(f"    Rating: {book.goodreads_avg}")
            print(f"    Difficulty: {book.difficulty_level}")
            print(f"    Goodreads URL: {book.goodreads_URL}")
            print("-" * 40)

    else:

        print("Sorry, no books match your preferences.")
