#!/usr/bin/python
# coding: utf-8

import praw
import pdb
import re
import os


# Create the Reddit instance
reddit = praw.Reddit('bot1')

# and login
#reddit.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

local_subs = open("alabama.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['Alabama 6th among states affected by tariffs', 'Voter registration numbers on the rise in Alabama', 'darwin brazier', 'armed heckler arrested', 'pulling a gun on immigration protesters', 'Alabama \'Families Belong Together\'', 'internment camps at Orange Beach and Silverhill', 'Gathering of the Masterrace.', 'sen. jones', 'shooting outside Walmart in Alabama', 'dougjones', 'VOTE ON JUNE 5', 'lee auman', 'Rocks tumbling into ocean causing sea level rise', 'mo brooks', 'recorded me going to my doctor and heckled me on the way out', 'alabama congressman', 'Retiring Due To Fear Of Assassination', 'Tell me again about how gun control doesn', 'alabama elections chief', 'alabama state lege. seat', 'candidates in alabama', 'roy moore', 'alabama lawmaker', 'Etowah County sheriff', 'Alabama\'s 2018 elections', 'house seat in alabama', 'sue bell cobb', 'al-03', 'chris christie', 'bill passed by Alabama House', 'Alabama state House', 'jason childs', 'bradley byrne', 'Alabama violated federal law', 'Doug Jones', 'tommy battle', 'gerrymandered Alabama', 'Alabama\'s Secretary of State', 'Congressman Brooks town hall', 'al-gov', 'alabama governor', 'ala. gov', 'too poor to vote', 'Alabama Secretary of State', 'John Merrill', 'top election official learn from monitoring Russian election', 'Alabama election officials remain confused']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Alabama 2018 Election \n\n"
            "[General Election](https://myinfo.alabamavotes.gov/VoterView/PollingPlaceSearch.do): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass
        # Write our updated list back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()