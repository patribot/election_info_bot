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

local_subs = open("montana.dat", "r")
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
            terms = ['montana rally', 'Trump said in his Montana speech', 'Yes, you sure are...', 'The brain, more important than the mouth', 'assaulting a reporter the day before his election', 'climate change surround Montana fishermen', 'russell c fagg', 'Scientists Demand Congress Shield Endangered Species Act From GOP Attacks', 'questioned by Border Patrol in Havre, MT for speaking Spanish', 'richard spencer', 'richard spenser', 'MISSOULA CRACKER BARRELL', 'montana green party', 'jon tester', 'US bill may open pristine lands to development', 'Montana Implements Net Neutrality', 'Montana becomes first state to implement net neutrality', 'rich landowners blocking access to public lands', 'Montana U.S. House seat', 'clawing at the GOP as 2018', 'This is what budget cuts look like', 'I-183', 'heenan', 'discuss Montana politics and candidates', 'Fight for Public Land in Montana', 'gianforte', 'ganforte', 'Republican says would have shot reporter', 'Kier, a Democrats', 'Montana Republican\'s mugshot']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Montana 2018 General Election \n\n"
            "[General Election](https://sos.mt.gov/elections/absentee): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Store the current id into our list
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")


for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()