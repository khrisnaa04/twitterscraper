import pandas as pd
from textblob import TextBlob

# Fungsi untuk menganalisis sentimen
def analyze_sentiment(text):
    analysis = TextBlob(text)
    # Klasifikasi sentimen berdasarkan polaritas
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Load data dari file CSV
tweets = pd.read_csv('tweets.csv', encoding='utf-8')  # Pastikan file sudah ada dan berisi data
print(f"Data loaded: {len(tweets)} rows")

# Menambahkan kolom sentimen
tweets['Sentiment'] = tweets['Text'].apply(analyze_sentiment)

# Simpan data dengan kolom sentimen ke file baru
tweets.to_csv('tweets_with_sentiment.csv', index=False, encoding='utf-8')
print("Sentiment analysis completed and saved to 'tweets_with_sentiment.csv'")