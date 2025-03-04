import pandas as pd
import os

def clean_data(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} does not exist.")
        return
    
    df = pd.read_csv(input_file)
    columns_to_drop = ['Genre2', 'Translation', 'Author_Gender', 'Prize', 'WinnerShortlist', 'Author_Nationality', 'PubHouse', 'protagonist_concentration', 'tuldava_score', 'event_count', 'speed_min', 'total_ratings', 'Probability1P']
    df = df.drop(columns=columns_to_drop, errors='ignore')
    df.to_csv(output_file, index=False)

    df = df.dropna()

    df.to_csv(output_file, index=False)
    print("Data cleaned and saved to", output_file)

if __name__ == "__main__":
    clean_data("CONLIT_META.csv", "cleaned_books.csv")


