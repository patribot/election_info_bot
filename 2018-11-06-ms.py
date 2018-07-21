# coding: utf-8
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

local_subs = open("mississippi.dat", "r")
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
            terms = ['New York, South Carolina, Oklahoma, Maryland, Mississippi, Colorado and Utah', 'VOTE ON JUNE 5', 'the mississippi house', 'ms-sen', 'The 4 Biggest Banks Have Already Made', 'Full solidarity with our students protesting today but...', 'christ mcdaniel', 'mississippi sheriff', 'nine poorest states', ' ms senator', ' ms senate', 'Mississippi Senate race', 'Taking Care to Get a Mississippi Scandal Right', 'four years without trial in a Mississippi jail', 'GOP fight bolsters Democratic Senate hopes', 'roger wicker', 'nearby Mississippi is 37', 'gregg harper', 'rep. harper', 'rep harper', 'congressman harper', 'representative harper', 'states brace for Russian hacking fight']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Mississippi 2018 Election \n\n"
            "[Primary Election](http://www.sos.ms.gov/pollingplace/Pages/default.aspx): June 26, 2018 \n\n"
            "[General Election Registration Deadline](http://www.sos.ms.gov/Elections-Voting/Pages/Voter-Registration-Information.aspx): October 8, 2018 \n\n"
            "[General Election](http://www.sos.ms.gov/pollingplace/Pages/default.aspx): November 6, 2018 \n\n")
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