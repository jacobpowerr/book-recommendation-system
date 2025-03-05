# book-recommendation-system
# Book Recommendor
#### Video Demo: 
#### Description:
Book Recommendation System
Project Overview
This project implements a personalized book recommendation system that analyzes user preferences and reading habits to suggest appropriate reading material. The system leverages a comprehensive dataset of books with various metrics including readability scores, genre classifications, and popularity ratings to deliver tailored recommendations that match users' reading preferences and difficulty requirements.
Core Functionality
The recommendation engine works by collecting user input about their favorite books, preferred genres, desired reading difficulty, and minimum acceptable rating. It then processes this information through a filtering and ranking algorithm to identify books that best align with the user's preferences.
The system features:

Personalized recommendations based on user-stated preferences
Multi-factor filtering across genre, difficulty level, and rating thresholds
Similarity scoring that prioritizes books resembling the user's favorites
Readability analysis using multiple linguistic metrics to categorize books by difficulty
User-friendly interface for gathering preferences and displaying recommendations

Data Processing and Cleansing
The data processing pipeline is a critical component of this recommendation system. The original dataset required extensive cleansing and transformation to become usable for recommendations.
Data Cleansing Process
The data cleansing process addressed several challenges:

Removing irrelevant columns: The original dataset (CONLIT_META.csv) contained numerous columns that didn't contribute meaningfully to the recommendation algorithm. These included 'Genre2', 'Translation', 'Author_Gender', 'Prize', 'WinnerShortlist', 'Author_Nationality', 'PubHouse', 'protagonist_concentration', 'tuldava_score', 'event_count', 'speed_min', 'total_ratings', and 'Probability1P'. Eliminating these fields streamlined the dataset and improved processing efficiency.
Handling missing data: The cleansing involved dropping rows with missing values in critical fields. However, for important but incomplete rows, placeholder values were inserted to maintain the integrity of the dataset. This was particularly important for preserving books with unique characteristics that would otherwise be lost to the recommendation system.
Standardizing genre classifications: The original dataset used abbreviated genre codes that weren't user-friendly. A mapping function was implemented to convert these abbreviations to their full names (e.g., 'SF' to 'Science Fiction', 'YA' to 'Young Adult', 'MEM' to 'Memoir'), making the recommendations more intuitive for users.

Difficulty Calculation
A sophisticated approach to assessing book difficulty was implemented using multiple linguistic metrics:

Metrics used: The system calculates difficulty based on five key features:

Average sentence length
Average word length
Circuitousness (a measure of text complexity)
Reading speed
Token count (related to vocabulary diversity)


Feature normalization: Each metric is normalized to a 0-1 scale to ensure balanced contribution.
Weighted scoring: The metrics are combined using a weighted formula that prioritizes sentence complexity (30%), with equal importance (20%) given to word complexity, circuitousness, and reading speed, and slightly less weight (10%) to token count.
Categorization: The continuous difficulty scores are then discretized into three intuitive categories: "Easy," "Medium," and "Hard" using quantile-based binning to ensure balanced distribution.

Recommendation Algorithm
The recommendation engine employs a multi-stage approach:

Filtering: Books are initially filtered by the user's preferred genre, difficulty level, and minimum rating threshold.
Similarity assessment: A custom similarity function evaluates how closely each book's title matches the user's favorite books, assigning higher scores to closer matches.
Ranking: The filtered books are ranked based on both similarity to favorites and Goodreads rating, with priority given to similarity.
Results presentation: The top five recommendations are formatted and presented to the user with comprehensive details including title, author, genre, rating, difficulty level, and a Goodreads URL for further exploration.

User Interface
The interface focuses on simplicity and ease of use:

Input collection: Users are prompted to enter their five favorite books, preferred genre (with available options displayed), preferred reading difficulty level, and minimum acceptable rating.
Title formatting: Special attention was paid to properly formatting book titles, which required developing a sophisticated function to handle camelCase titles and extract readable titles from Goodreads URLs when necessary.
Recommendation display: Results are clearly presented with visual separators between recommendations and consistent formatting for each detail.

Future Enhancements
Potential improvements to the system could include:

Expanding the similarity algorithm to consider plot summaries and themes
Implementing collaborative filtering based on reading patterns of similar users
Adding more granular difficulty levels for finer recommendation tuning
Developing a graphical user interface for improved user experience
Incorporating machine learning to improve recommendation accuracy over time

This book recommendation system demonstrates a practical application of data processing, algorithm design, and user experience principles to create a personalized tool for literature discovery.
