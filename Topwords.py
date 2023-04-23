import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from collections import Counter
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


def topwords(posts):
    """
    Extracts the most frequent words in the post texts and returns a list of the top 5.

    Parameters:
    -----------
    posts : dict
        A dictionary containing the post data.

    Returns:
    --------
    list : A list containing the top 5 most frequent words.
    """
    view = input("Please say Yes if you would like to see the topwords from the posts(q to quit)")
    if view.lower() == "yes":
        # Extract the titles from the dictionary and flatten the list of lists
        texts = [[word for word in post["Post Text"].lower().split()] for post_id, post in posts.items()]
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
    if view.lower() == "q":
        print("Thank you! See you next time!")
        return None



def top_comments(posts):
    """
    Extracts the post with the most comments and returns the post title and text.

    Parameters:
    posts : dict A dictionary containing the post data.

    Returns:
    str : A string containing the post title and text of the post with the most comments.
    If the post text is None, only the post title and number of comments will be returned.
    """
    view = input("Please say Yes if you would like to see the post with the most comment(q to quit)")
    topcomment = max(posts.items(), key=lambda x: x[1]['Total Comments'])
    if view.lower() == "yes":
        post = topcomment[1]['Post Text']
        if post == None:
            #return topcomment
            return (f"The title of the post with the most comments is posted by user {topcomment[1]['ID']} with a number of {topcomment[1]['Total Comments']}")
        else:
            return (f"The title of the post with the most comments is posted by user {topcomment[1]['ID']} with a number of {topcomment[1]['Total Comments']}.The post is {post}")
    if view.lower() == "q":
        print("Thank you! See you next time!")
        return None




def view_title(topcomment):
    view = input("Please say Yes if you would like to view the title as well")
    if view == "Yes":
        if 'Title' != '':
            return "But the title is empty..."
        else:
            return topcomment[1]['Title']
    else:
        return None

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


