# WN2023 SI507 Final Project :computer: :computer: :computer:

## Overview 
This project is a tour guide system that utilizes data from Reddit (https://www.reddit.com ) to provide information about six Michigan university subreddits. The system provides an interactive command line interface for users to retrieve and explore data related to university subreddits. The data is presented in the form of a data frame, line chart, and summary information such as recent posts, top posts, and most commonly used words in post titles or text. The system also offers options to save the data and combine it with previously scraped data.

A demo video is available [here](https://drive.google.com/file/d/1Mm1pYdSvSaBIZb-4k-hKAi-XycVgQnI0/view?usp=share_link).


## Data Source
Reddit, one of the most widely used social platforms in the US, is the source of the data. 
(See https://www.reddit.com/ and https://en.wikipedia.org/wiki/Reddit for more information)

## Instruction

### API 
The current system does not require API keys as most of the data has already been stored in the cache. However, a Reddit API must be applied to access the data, and if a new key is not applied, the system will use the default one.  

If you would like to scrape new data, Please go to https://www.reddit.com/dev/api to apply an API key (~it is free :grin:).

### PIP Installations
requests pandas,praw,nltk,matplotlib,and webbrowser

### Built-in packages
json,datetime,ssl,and string

### Interaction and Presentation

This program has a variety of command line prompts. Here is a breakdown of the interactive components:

* UserInterfaceReddit
  * TitleInterface
    * A function that interacts with the user by displaying information about the title of the posts in the reddit.The user is asked for input to determine which information to display, such as recent posts, posts with the most comments, and top words in the post titles.
  * PostInterface
    * A function that interacts with the user by displaying information about the text of the posts in the reddit.The user is asked for input to determine which information to display, such as recent posts, posts with the most comments, and top words in the post titles.
  * CombineInterface
    * User could choose to save the current dictionary alone, combine it with the previous dictionary, or not save.
  * SaveInterface
    * Provides a user interface for saving a given `post` object as a JSON file.
* Exit




