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

local_subs = open("alaska.dat", "r")
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
            terms = ['House Republicans Just Voted to Gut Protections', 'pebble mine', 'arctic national wildlife refuge', 'Alaska Is Crafting a Plan to Fight Climate Change', 'alaska lawmaker', 'transgender bathroom bill just turned up in', 'alaska politicians', 'Bill Wielechowski', 'Alaska among states compromised before 2016 election', 'don young']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Alaska 2018 Election \n\n"
            "[Primary Voter Registration Deadline](https://voterregistration.alaska.gov/Registration/RegistrationDetails?haveValidAKDL=true): July 22, 2018 \n\n"
            "[Primary Election Date](http://elections.alaska.gov/Core/votingbymail.php): August 21, 2018 \n\n"
            "[General Election Registration Deadline](https://voterregistration.alaska.gov/Registration/RegistrationDetails?haveValidAKDL=true): October 7, 2018 \n\n"
            "[General Election](http://elections.alaska.gov/Core/votingbymail.php): November 6, 2018 \n\n")
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