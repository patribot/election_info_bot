#!/usr/bin/python
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

local_subs = open("newhampshire.dat", "r")
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
            terms = ['new hampshire supreme court', 'dinesh d', '100,000 death benefit if they die in a school shooting', 'Democratic Party Voter Data Fees in Some States', 'congress says biomass', 'nhpolitics', 'New Hampshire seat in Trump district', 'spagnuolo', 'New Hampshire House votes', 'New Hampshire Lawmakers', 'New Hampshire voter fraud claim']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("New Hampshire 2018 Election \n\n"
            "[Primary Election Registration Deadline](http://sos.nh.gov/HowRegVote.aspx): September 11, 2018 \n\n"
            "[Primary Election](https://app.sos.nh.gov/Public/PollingPlaceSearch.aspx): September 11, 2018 \n\n"
            "[General Election Registration Deadline](http://sos.nh.gov/HowRegVote.aspx): November 6, 2018 \n\n"
            "[General Election](https://app.sos.nh.gov/Public/PollingPlaceSearch.aspx): November 6, 2018 \n\n")
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