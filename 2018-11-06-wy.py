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

local_subs = open("wyoming.dat", "r")
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
            terms = ['wyoming protest', 'Yes, you sure are...', 'Overhaul of Endangered Species Act', 'i feel this is a punitive action', 'Trump wants to kill Yellowstone Bison', 'grizzlies under threat from controversial hunting proposal', 'Entire Life Savings, Claiming He Gave It To Them', '91,800 from an innocent man', 'matt mead', 'wyoming governor', 'mary throne', 'barrasso', 'erik prince', 'Senate Environment Committee Approves Toxic EPA Nominee', 'Senate Committee Advances Controversial Trump EPA Nominee', 'Pushing Ahead with a Health Care Deal']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Wyoming 2018 Election \n\n"
            "[Primary Voter Registration Deadline](http://soswy.state.wy.us/elections/registeringtovote.aspx): August 6, 2018 \n\n"
            "[Primary Election](http://soswy.state.wy.us/Elections/AbsenteeVoting.aspx): August 21, 2018 \n\n"
            "[General Election Registration Deadline](http://soswy.state.wy.us/elections/registeringtovote.aspx): October 22, 2018 \n\n"
            "[General Election](http://soswy.state.wy.us/Elections/AbsenteeVoting.aspx): November 6, 2018 \n\n")
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