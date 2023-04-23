# SI-507-Final-Proj

## Overview
This project is a tour guide system that utilizes data from Reddit (https://www.reddit.com ) to provide information about Michigan university subreddits. The system provides an interactive command line interface for users to retrieve and explore data related to university subreddits. The data is presented in the form of a data frame, line chart, and summary information such as recent posts, top posts, and most commonly used words in post titles or text. The system also offers options to save the data and combine it with previously scraped data.


## Data Source
Reddit, one of the most widely used social platforms in the US, is the source of the data. 
(See https://www.reddit.com/ and https://en.wikipedia.org/wiki/Reddit for more information)

## Instruction

### API 
The current system does not require API keys as most of the data has already been stored in the cache. However, a Reddit API must be applied to access the data, and if a new key is not applied, the system will use the default one.  

If you would like to scrape new data, Please go to https://www.reddit.com/dev/api to apply an API key (~free).

### PIP Installations
requests pandas,praw,nltk,matplotlib,and webbrowser

### Built-in packages
json,datetime,ssl,and string


