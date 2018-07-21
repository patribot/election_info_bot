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

local_subs = open("hi.dat", "r")
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
            terms = ['blocked a resolution to have Trump enforce the Russian sanctions', 'use was legal in Hawaii until', 'reef madness', 'afford middle-class basics', 'Afford Rent, Transportation, Childcare, Cell Phone', 'Hero Stops Lava Flow with Assault Rifle', 'A Hawaiian island got about 50 inches of rain in 24 hours', 'hawaii legislature', 'Hawaii 2018 Ballot', 'gabbard', 'Ending Federal Marijuana Prohibition Act', 'Hawaiian Politician Is Introducing a Bill', 'Hawaii Expects Adult Use Cannabis Legalization', 'kaniela']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Hawaii 2018 Election \n\n"
            "[Primary Voter Registration Deadline](https://olvr.hawaii.gov/register.aspx): August 4, 2018 \n\n"
            "[Primary Election Date](http://elections.hawaii.gov/wp-content/uploads/2016/02/VR-PAB-English.pdf): August 11, 2018 \n\n"
            "[General Election Registration Deadline](https://olvr.hawaii.gov/register.aspx): October 31, 2018 \n\n"
            "[General Election](http://elections.hawaii.gov/wp-content/uploads/2016/02/VR-PAB-English.pdf): November 6, 2018 \n\n")
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