import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import string
from collections import Counter
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')



def get_first_n(dictionary, key_to_print, key_to_sort, n):
    """
    Extracts the most frequent words in the post texts and returns a list of the top 7.

    Parameters:
    -----------
    posts : dict
        A dictionary containing the post data.
    key_to_print : str
        The key in the dictionary that contains the post text.

    Returns:
    --------
    list : A list containing the top 7 most frequent words and their frequencies.
    """
    # Sort the dictionary by the 'Created On' key
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1][key_to_sort], reverse=True)
    titles = []
    for i in range(min(n, len(sorted_dict))):
        title = sorted_dict[i][1][key_to_print]
        titles.append(title)
    return titles


def top_words_frequency(posts, key_to_print):
    """
    Extracts the text data from the given posts and returns the top 7 most frequent unique words and their frequencies.

    Parameters:
        posts (dict): A dictionary containing posts as values.
        key_to_print (str): The key in the post dictionary that contains the text data.

    Returns:
        list: A list of tuples containing the top 7 most frequent unique words and their frequencies.
    """
    # Extract the titles from the dictionary and flatten the list of lists
    texts = [[word for word in post[key_to_print].lower().split()] for post_id, post in posts.items()]
    tokens = [word for document in texts for word in document]

    # Remove stop words and punctuations
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words and token not in string.punctuation]

    # Count the frequency of each word
    word_freq = Counter(tokens)

    # Sort the words by frequency
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    # Return the top 5 unique words and their frequencies, without trailing punctuation
    top_words_freq = [(word.rstrip(string.punctuation), freq) for word, freq in sorted_words[:7]]
    top_words = list(set([word for word, freq in top_words_freq]))
    top_words_freq = [(word, freq) for word, freq in top_words_freq if word in top_words]
    top_words_freq = sorted(top_words_freq, key=lambda x: x[1], reverse=True)
    return top_words_freq


