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

local_subs = open("ct.dat", "r")
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
            terms = ['Jahana Hayes', 'Connecticut Democratic party', 'sandy hook conspiracy', 'sandy hook shooting', 'ct senate', 'Senate passes bill to restore net neutrality in Connecticut', 'Fairfield County, CT Green Party', 'Connecticut lawmaker', 'green party of ct', 'Connecticut legislat', 'elizabeth esty', 'sandy hook victims', 'green party of Connecticut', 'Legislative Seats in CT', 'phil young', 'Connecticut Democrat flip Seat', 'legislative seats in Connecticut', 'flip GOP-held Connecticut seat', 'philyoungct', 'Connecticut Targeted In National Popular Vote Effort', 'Community Rallies Around Asian Couple Facing Deportation', 'ned lamont']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Connecticut 2018 Election \n\n"
            "[Primary Voter Registration Deadline](https://voterregistration.ct.gov/OLVR/welcome.do): August 14, 2018 \n\n"
            "[Primary Election Date](http://www.dir.ct.gov/sots/LookUp.aspx): August 14, 2018 \n\n"
            "[General Election Registration Deadline](https://voterregistration.ct.gov/OLVR/welcome.do): November 6, 2018 \n\n"
            "[General Election](http://www.dir.ct.gov/sots/LookUp.aspx): November 6, 2018 \n\n")
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