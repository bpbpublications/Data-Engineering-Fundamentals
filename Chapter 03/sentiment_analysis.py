import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Sample DataFrame with text data
data = {
    "text": [
        "I love this product! It's amazing and works perfectly.",
        "I'm not happy with the service, it was really bad.",
        "The movie was okay, not the best but not the worst either.",
        "This is the worst thing I've ever bought!",
        "Fantastic quality and great customer support. Highly recommend!",
    ]
}

df = pd.DataFrame(data)

# Function to calculate sentiment scores


def analyze_sentiment(text):
    return analyzer.polarity_scores(text)


# Apply the sentiment analysis to each text entry
df["sentiment"] = df["text"].apply(analyze_sentiment)

# Separate the sentiment scores into individual columns
df = pd.concat(
    [df.drop(["sentiment"], axis=1), df["sentiment"].apply(pd.Series)], axis=1
)

# Display the resulting DataFrame with sentiment scores
print(df)
