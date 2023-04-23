import pandas as pd
import RedditAPI as reddit
import Graph as graph
import Topwords as tops
import Combine as Combine
import LoadandSave as save


def TitleInterface(new_dict):
    """
    A function that interacts with the user by displaying information about the posts in the reddit.
    The user is asked for input to determine which information to display, such as recent posts, posts with the most comments, and top words in the post titles.

    Parameters:
    -----------
    new_dict : dict
        A dictionary containing information about the reddit posts.

    Returns:
    --------
    None
    """
    print("Let's look at the titles together")
    print("Would you like to see the title most recent five posts?: '\n' 1 = Yes; '\n' 2 = No; '\n' 3 = Quit.")
    userInput = input()
    if userInput == '1':
        print(tops.get_first_n(new_dict, 'Title', 'Created On', 5))
    elif userInput == '2':
        print("Okay! Let continue then")
    elif userInput == '3':
        print('\nBye Bye!\n')
        return
    else:
        print('Please input between 1, 2, 3')
    
    print("Would you like to see the titles of five posts with the most comments?: '\n' 1 = Yes; '\n' 2 = No; '\n' 3 = Quit.")
    userInput = input()
    if userInput == '1':
        print(tops.get_first_n(new_dict, 'Title', 'Total Comments',5))
    elif userInput == '2':
        print("Okay! Let continue then")
    elif userInput == '3':
        print('\nBye Bye!\n')
        return
    else:
        print('Please input between 1, 2, 3')
    

    print("Would you like to see topwords in the titles?: '\n' 1 = Yes; '\n' 2 = No; '\n' 3 = Quit.")
    userInput = input()
    if userInput == '1':
        top_words_freq = graph.top_words_frequency(new_dict, 'Title')
        print(top_words_freq)
        print("Would you like to see the plot?: '\n' 1 = Yes; '\n' 2 = No; '\n' 3 = Quit.")
        userInput2 = input()
        if userInput2 == '1':
            print(graph.plot_top_words_frequency(top_words_freq))
        elif userInput2 == '2':
            print("Okay! Let's continue then")
        elif userInput2 == '3':
            print('\nBye Bye!\n')
            return
    elif userInput == '2':
        print("Would you like to look at the plot instead?: '\n' 1 = Yes; '\n' 2 = No; '\n' 3 = Quit.")
        userInput2 = input()
        if userInput2 == '1':
            print(graph.plot_top_words_frequency(graph.top_words_frequency(new_dict, 'Title')))
        elif userInput2 == '2':
            print("Okay! Let's continue then")
        elif userInput2 == '3':
            print('\nBye Bye!\n')
            return
    elif userInput == '3':
        print('\nBye Bye!\n')
        return
    else:
        print('Please input between 1, 2, 3')


def PostInterface(new_dict):
    """
    A function that interacts with the user by displaying information about the posts in the reddit.
    The user is asked for input to determine which information to display, such as recent posts, posts with the most comments, and top words in the post titles.

    Parameters:
    -----------
    new_dict : dict
        A dictionary containing information about the reddit posts.

    Returns:
    --------
    None
    """
    print("Let's look at the posts together")
    print("Would you like to see the most recent five posts?: '\n' 1 = Yes; '\n' 2 = No; '\n' 3 = Quit.")
    userInput = input()
    if userInput == '1':
        print(tops.get_first_n(new_dict, 'Post Text', 'Created On', 5))
    elif userInput == '2':
        print("Okay! Let continue then")
    elif userInput == '3':
        print('\nBye Bye!\n')
        return
    else:
        print('Please input between 1, 2, 3')
    
    print("Would you like to see the titles of five posts with the most comments?: '\n' 1 = Yes; '\n' 2 = No; '\n' 3 = Quit.")
    userInput = input()
    if userInput == '1':
        print(tops.get_first_n(new_dict, 'Post Text', 'Total Comments',5))
    elif userInput == '2':
        print("Okay! Let continue then")
    elif userInput == '3':
        print('\nBye Bye!\n')
        return
    else:
        print('Please input between 1, 2, 3')

    print("Would you like to see topwords in the posts?: '\n' 1 = Yes; '\n' 2 = No; '\n' 3 = Quit.")
    userInput = input()
    if userInput == '1':
        top_words_freq = graph.top_words_frequency(new_dict, 'Post Text')
        print(top_words_freq)
        print("Would you like to see the plot?: '\n' 1 = Yes; '\n' 2 = No; '\n' 3 = Quit.")
        userInput2 = input()
        if userInput2 == '1':
            print(graph.plot_top_words_frequency(top_words_freq))
        elif userInput2 == '2':
            print("Okay! Let's continue then")
        elif userInput2 == '3':
            print('\nBye Bye!\n')
            return
    elif userInput == '2':
        print("Would you like to see the plot instead?: '\n' 1 = Yes; '\n' 2 = No; '\n' 3 = Quit.")
        userInput2 = input()
        if userInput2 == '1':
            print(graph.plot_top_words_frequency(graph.top_words_frequency(new_dict, 'Post Text')))
        elif userInput2 == '2':
            print("Okay! Let's continue then")
        elif userInput2 == '3':
            print('\nBye Bye!\n')
            return
    elif userInput == '3':
        print('\nBye Bye!\n')
        return
    else:
        print('Please input between 1, 2, 3')



def UserInterfaceReddit():
    '''total interface
    
    User could choose the function that want to perform
    Parameters:
    ---------- 
    None
    Returns
    -------
    Output based on the choice
    
    '''
    reddit_scraper = reddit.RedditScraper()
    print('\nWelcome to the system!\n')
    start_date = reddit_scraper.date_to_timestamp()
    if start_date is not None:
        new_dict = reddit_scraper.scrape_reddit(start_date=start_date)
        if new_dict is not None:
            num_posts = len(new_dict['Title'])
            print(f"There are {num_posts} posts found from the {new_dict['Subreddit']} since that time")
            if reddit.look() is True:
                print(pd.DataFrame(new_dict))
            else:
                print("Okay, let's continue then")
            new_dict= pd.DataFrame(new_dict).to_dict('index')

            post_result = graph.Graphcomment(new_dict)
            print(post_result)

            print('Let take a further look at the data, tell me what content you would like to assess' '\n', '1 = Comment', '\n', '2 = Post Text', '\n', '3 = Quit')
            userInput = input()

            if userInput == '1':
                TitleInterface(new_dict)
                Combine.CombineInterface(new_dict)
                save.SaveInterface (new_dict)
                UserInterfaceReddit()
            elif userInput == '2':
                PostInterface(new_dict)
                Combine.CombineInterface(new_dict)
                save.SaveInterface (new_dict)
                UserInterfaceReddit()
            elif userInput == '3':
                save.SaveInterface (new_dict)
                print('\nBye Bye!\n')
                return
            else:
                print('Please input between 1, 2, 3')


if __name__ == "__main__":

    UserInterfaceReddit()
    pass
