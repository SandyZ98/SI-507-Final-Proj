# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# load libraries
import pandas as pd
import datetime as dt
from psaw import PushshiftAPI
import os

# working directory
os.chdir('/Users/rubenbach/Nextcloud/Lehre/FSS 2020/Reddit/')


# set API
api = PushshiftAPI()

# Set beging and end date of period interested in
start_epoch_2020=int(dt.datetime(2020, 4, 20).timestamp())
end_epoch_2020=int(dt.datetime(2020, 5, 20).timestamp())


# Create empty lists
subm_list_republicans = []
subm_list_democrats = []


# Fill lists with data from API
# Here: search submissions made to subreddit democrats which contain kavanaugh
subm_list_democrats = list(api.search_submissions(
                            before=end_epoch_2020,
                            after=start_epoch_2020,               
                            subreddit='uofm'))



# Save as .csv
pd.DataFrame([s.d_ for s in subm_list_democrats]).to_csv('uofm.csv', index=False)



# get list of submissions from objects above to download comments
list_submission_ids_democrats = [s.id for s in subm_list_democrats]

# generate empty list of comments
all_comments_democrats = []


# loop through submission ids
for submission_id in list_submission_ids_democrats:
   # use the link_id option to add submission id
   comments_for_submission =  list(api.search_comments(link_id = submission_id))
   # add list of current comments to list of comments
   all_comments_democrats = all_comments_democrats + [c.d_ for c in comments_for_submission]
# transform to data frame
all_comments_democrats_df = pd.DataFrame(all_comments_democrats)

# save comments as csv
all_comments_democrats_df.to_csv('all_comments_uofm.csv', sep='\t', encoding='utf-8')

    
