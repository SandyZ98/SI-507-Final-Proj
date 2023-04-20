import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from collections import Counter
import nltk
from nltk.corpus import stopwords
print(nltk.__version__)
nltk.download('stopwords')


def topwords2(posts):
    # Flatten the list of lists
    texts = [[word for word in document.lower().split()] for document in posts["Title"] if document]
    tokens = [word for document in texts for word in document]

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Count the frequency of each word
    word_freq = Counter(tokens)

    # Sort the words by frequency
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    # Return the top 5 words
    top_words = [word for word, freq in sorted_words[:5]]
    return top_words


def topwords(posts):
    # Extract the titles from the dictionary and flatten the list of lists
    texts = [[word for word in post["Title"].lower().split()] for post_id, post in posts.items()]
    tokens = [word for document in texts for word in document]

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Count the frequency of each word
    word_freq = Counter(tokens)

    # Sort the words by frequency
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    # Return the top 5 words
    top_words = [word for word, freq in sorted_words[:5]]
    return top_words

