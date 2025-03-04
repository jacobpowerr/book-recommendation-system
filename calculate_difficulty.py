import pandas as pd

df = pd.read_csv("cleaned_books.csv")

difficulty_features = ["avg_sentence_length", "avg_word_length", "circuitousness", "speed_avg", "token_count"]

df = df.dropna(subset=difficulty_features)

for col in difficulty_features:
    df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

df["speed_avg"] = 1 - df["speed_avg"]

weights = {
    "avg_sentence_length": 0.3,
    "avg_word_length": 0.2,
    "circuitousness": 0.2,
    "speed_avg": 0.2,
    "token_count": 0.1
}

df["difficulty_score"] = (
    df["avg_sentence_length"] * weights["avg_sentence_length"] +
    df["avg_word_length"] * weights["avg_word_length"] +
    df["circuitousness"] * weights["circuitousness"] +
    df["speed_avg"] * weights["speed_avg"] +
    df["token_count"] * weights["token_count"]
)

df["difficulty_level"] = pd.qcut(df["difficulty_score"], q=3, labels=["Easy", "Medium", "Hard"])

print(df[["Work_Title", "difficulty_score", "difficulty_level"]].head(10))

df.to_csv("books_with_difficulty_csv", index=False)