import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
import string


def Graphcomment(posts):
    """
    Asks the user if they want to see a plot of the number of comments over time for the given posts.
    
    Parameters:
        posts (Any): The posts to be plotted.
    
    Returns:
        Union[Callable, str, None]: Returns the plotted data if the user chooses '1', "Got it" if the user chooses '2', 
        and None if the user chooses '3'.
    """
    print("Would you also like to see the number of comments over time? '\n' 1 = Yes; '\n' 2 = No; '\n' 3 = Quit.")
    userInput = input()
    while True:
        if userInput == '1':
            plot_comments_over_time(posts)
            return plot_comments_over_time
        elif userInput== '2':
            return f"Got it"
        elif userInput == '3':
            return
        else:
            print('Please input between 1, 2, 3')
            Graphcomment(posts)

def plot_comments_over_time(posts):
    """
    Creates a plot of the number of comments over time for the given posts.

    Parameters:
        posts (Dict[str, Any]): A dictionary of post objects, each containing a 'Created On' key with a date and a 
        'Total Comments' key with the number of comments on the post.

    Returns:
        None: This function only creates and displays a plot.
    """
    # Create a list of tuples with the date and the total comments for each post
    data = [(post['Created On'], post['Total Comments']) for post in posts.values()]

    # Sort the data by date
    data = sorted(data, key=lambda x: x[0])

    # Extract the dates and the comment counts into separate lists
    dates, comment_counts = zip(*data)

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(dates, comment_counts)

    # Format the x-axis labels
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    ax.xaxis.set_visible(False)


    # Set the axis labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Comments')
    ax.set_title('Number of Comments Over Time')

    # Show the plot
    plt.show()


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


def plot_top_words_frequency(top_words_freq):
    """
    Creates a bar chart to display the top 7 words and their frequencies in the posts.

    Parameters:
        top_words_freq (list): A list of tuples containing the top 7 words and their corresponding frequencies

    Returns:
        None
    """
    # Create a bar chart of the top 5 words and their frequencies
    words, freqs = zip(*top_words_freq)
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:purple', 'tab:brown', 'tab:olive', 'tab:cyan']
    plt.bar(words, freqs, color=colors[:len(words)])
    plt.title("Top 7 words in the posts")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.show()






