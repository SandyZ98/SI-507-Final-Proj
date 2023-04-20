
import pandas as pd
import requests
import datetime
import json

import reddit_api as reddit
import topwords as topwords
from Post import Post




# subreddit = reddit_read_only.subreddit("msu")
# print(subreddit)
# for post in subreddit.hot(limit=5):
#     print(post.title)
#     print()



#subreddit = reddit_read_only.subreddit("BakerCollege")

# Scraping the top posts of all time
#posts = subreddit.top(time_filter = "all", limit = None)

start_date = '01-08-22 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [], "Upvote Ratio": [],
              "Total Comments": [],"Created On":[], "Post URL": [],
              "Original Content": []
              }

# posts_msu = reddit.scrape_reddit(subreddit_name="msu", start_date=start_date)
# posts_um = reddit.scrape_reddit(subreddit_name="uofm", start_date=start_date)
# posts_wayne = reddit.scrape_reddit(subreddit_name="waynestate", start_date=start_date)
# posts_cmu= reddit.scrape_reddit(subreddit_name="centralmich", start_date=start_date)
# posts_gvsu = reddit.scrape_reddit(subreddit_name="GVSU", start_date=start_date)
# posts_wmu = reddit.scrape_reddit(subreddit_name="WMU", start_date=start_date)
# posts_emu = reddit.scrape_reddit(subreddit_name="emu", start_date=start_date)
# posts_baker = reddit.scrape_reddit(subreddit_name="BakerCollege", start_date=start_date)

# combined_posts = {"msu": posts_msu,
#                  "uofm": posts_um,
#                  "waynestate": posts_wayne,
#                  "centralmich": posts_cmu,
#                  "gvsu": posts_gvsu,
#                  "wmu": posts_wmu,
#                  "emu": posts_emu,
#                  "bakerBaker College": posts_baker}

# with open("combined_posts.json", "w") as outfile:
#      json.dump(combined_posts, outfile)
#Saving the data in a pandas dataframe
# all_posts = pd.DataFrame(combined_posts)
# all_posts['Created On'] = pd.to_datetime(all_posts['Created On'],  unit='s')
# all_posts.to_csv('all_posts.csv', index=False)


posts_baker = reddit.scrape_reddit(start_date=start_date)
print(posts_baker)
posts_baker_2 = posts_baker.to_dict('index')
print(posts_baker_2)
#posts_baker.to_json(r"posts_baker.json")
# with open("posts_baker.json", "w") as outfile:
#      json.dump(posts_baker, outfile)

def reddit_interface():
     subreddit_posts_df = reddit.scrape_reddit(start_date)
     subreddit_posts = subreddit_posts_df.to_dict('index')
     save = input("Please say Yes if you would like to save the data")
     if save == "Yes":
          with open("combined_posts.json", "w") as outfile:
               json.dump(subreddit_posts, outfile)
     subreddit_posts = Post(subreddit_posts)
     topword = input("Please say Yes if you would like to take a look at the top words")
     if topword == "Yes":
          print(topwords.topwords(posts_baker))

     return reddit.scrape_reddit(start_date)

#posts_baker = reddit_interface(start_date=start_date)

print(topwords.topwords(posts_baker_2))
