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

local_subs = open("nebraska.dat", "r")
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
            terms = ['nebraska democra', 'Housing Shortages Hitting Some Rural Areas Hard', 'Pennsylvania, Nebraska Elections See BIG Progressive Wins', 'Progressives Notch a Big Victory in Nebraska', 'brad asslord', 'kara eastman', 'rural voters under farm policy', 'nebraskans need to register to vote', 'nebraska greens', 'nebraska senators', 'Farmers are fighting for the right to repair', 'bob krist', 'don bacon', 'rep. bacon', 'congressman bacon', 'rep bacon', 'Extreme Redistricting Sets the Stage for a Huge Republican Stranglehold', 'Freedom Caucus Chair Warns Congress Not To', 'House Republicans Warn Congress Not To']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Nebraska 2018 Election \n\n"
            "[General Election Registration Deadline](https://www.nebraska.gov/apps-sos-voter-registration/): October 26, 2018 \n\n"
            "[General Election](http://www.sos.ne.gov/elec/voter_info.html#early): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write the post id back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()