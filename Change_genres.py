import pandas as pd

genre_map = {
    'BIO': 'Biography',
    'BS': 'Biography/Autobiography',
    'HIST': 'Historical',
    'MEM': 'Memoir',
    'MID': 'Middle Grade',
    'MIX': 'Mixed Genre',
    'MY': 'Mystery',
    'NYT': 'New York Times Best Seller',
    'PW': 'Publishers Weekly',
    'ROM': 'Romance',
    'SF': 'Science Fiction',
    'YA': 'Young Adult'
}

df = pd.read_csv("cleaned_books.csv")

def map_genre(genre_abbr):
    return genre_map.get(genre_abbr, genre_abbr)

df['Genre'] = df['Genre'].apply(map_genre)

df.to_csv("cleaned_books.csv", index=False)

print(df.head())