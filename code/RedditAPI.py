import praw
import datetime


reddit_read_only = praw.Reddit(client_id="61-p7o_TjdbEqg",	# your client id
                               client_secret="MJ3pLijA7bNuupcINh13U00upfRFgQ",	# your client secret
                               user_agent="Sandy Zhao")	# your user agent

class RedditScraper:
    def check_university(self, name):
        universities = {
            "university of michigan": "uofm",
            "michigan state university": "msu",
            "wayne state university": "waynestate",
            "central michigan university": "centralmich",
            "eastern michigan university": "emu",
            "oakland university": "oaklanduniversity"
        }
        return universities.get(name.lower())

    def date_to_timestamp(self):
        while True:
            input_date = input("Please enter a start date in the format of 'dd-mm-yyyy' or 'q' to quit: ")
            if input_date.lower() == "q":
                return None
            try:
                date_obj = datetime.datetime.strptime(input_date, "%d-%m-%Y")
                return date_obj.timestamp()
            except ValueError:
                print("Invalid date entered. Please try again.")

    def scrape_reddit(self, subreddit_name=None, start_date=None):
        if subreddit_name is None:
            subreddit_name = input("Please give the name of the university from the list below (q to quit): '\n' University of Michigan; '\n' Michigan State University; '\n' Wayne State University; '\n' Central Michigan University; '\n'Eastern Michigan University; '\n'Oakland University")
            if subreddit_name.lower() == "q":
                print("Thank you! See you next time!")
                return None

        subreddit = self.check_university(subreddit_name)
        if subreddit is None:
            print("The name is not on the list, please try again!")
            return None


        subreddit = reddit_read_only.subreddit(subreddit)
        posts = subreddit.top(time_filter="all", limit=None)

        posts_dict = {
            "Title": [],
            "Post Text": [],
            "ID": [],
            "Total Comments": [],
            "Created On": [],
            "Post URL": [],
            "Original Content": [],
            "Subreddit": []
        }
        for post in posts:
            date = post.created_utc
            if start_date is None or date > start_date:
                # Title of each post
                    posts_dict["Title"].append(post.title)
                # Text inside a post
                    posts_dict["Post Text"].append(post.selftext)
                # Unique ID of each post
                    posts_dict["ID"].append(post.id)
                # Total number of comments inside the post
                    posts_dict["Total Comments"].append(post.num_comments)
                # Date the post was Created
                    posts_dict["Created On"].append(post.created_utc)
                # URL of each post
                    posts_dict["Post URL"].append(post.url)
                # Flair of each post
                    posts_dict["Original Content"].append(post.is_original_content)
                # From
                    posts_dict["Subreddit"] = subreddit_name
            #return pd.DataFrame(posts_dict)
        return posts_dict

def look():
    while True:
        update = input("Do you want to take a look at the data? Enter 'Yes' or 'No': ")
        if update.lower() == "yes":
            return True
        elif update.lower() == "no":
            return False
        else:
            print("Invalid input! Please enter 'Yes' or 'No'.")
