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

local_subs = open("pennsylvania.dat", "r")
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
            terms = ['young and naive', 'Unarmed black man tased', 'Hey, would you mind not murdering us', 'bob casey', 'brendan boyle', 'pa-7', 'pa-07', '^(?!.*john meehan).*meehan.*$', 'pa hd150', 'pa-7', 'pa state rep', 'pennsylvania primaries', 'pennsylvania governor', 'primary in Pennsylvania', 'primaries in pennsylvania', 'pa34', 'summer lee', 'progressives in pennsylvania', 'innamorto', 'pa state house', 'pa hd-178', 'socialists in pennsylvania', 'terri mitko', 'fetterman', 'pa 184', 'candidate in pennsylvania', 'pa11', 'house race in pennsylvania', 'impeach PA Supreme Court', 'santorum', 'pa01', 'pennsylvania Republican state legislator', 'larry krasner', 'pa gerrymandering', 'Women Run in Pennsylvania', 'nick miccarelli', 'saccone', 'conor lamb', 'pa.\'s redistricting', 'christina hartman', 'rep costello', 'congressman costello', 'representative costello', 'rep. costello', 'New Congressional Map in Pennsylvania', 'Pennsylvania\'s Gerrymandered Congressional Map', 'Daryl Metcalfe', 'pennsylvania voters', 'PA\'s new congressional map', 'New map for Pennsylvania', 'Pennsylvania House District', 'hal english', 'pennsylvania voting map', 'new Pennsylvania map', 'pa. congress', 'turzai', 'Pennsylvania congress', 'Pennsylvania GOP lawmaker', 'pa redistricting', 'Pennsylvania GOP\'s leading Senate candidate', 'Pa. governor', 'lou barletta', 'legalizing marijuana in PA', 'Vincent Hughes', 'PA\'s 16th Congressional', 'stable genius act', 'Pennsylvania redistricting', 'pennsylvania state senate', 'smucker', 'pa-16', 'joe billie', 'pennsylvania gerrymandering', 'ryan costello']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Pennsylvania 2018 Election \n\n"
            "[General Election Registration Deadline](https://www.pavoterservices.pa.gov/Pages/VoterRegistrationApplication.aspx): October 7, 2018 \n\n"
            "[General Election](https://www.pavoterservices.pa.gov/Pages/PollingPlaceInfo.aspx): November 6, 2018 \n\n")
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