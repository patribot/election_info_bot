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

local_subs = open("tennessee.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['nathan farnor', 'Pence to Visit Chattanooga', 'Just got my bumper sticker in time for early voting', 'Voter Registration Gripe', 'Upcoming Election Voter Guide', 'tn-sen', 'diane black', 'nashville pride', 'McCormick pulls re-election bid', 'protest planned as a reaction to the treatment of families at the border', 'ICE Came for a Tennessee Town', 'pride of knoxville', 'knoxville straight pride', 'trump rally in nashville', 'corker and alexander', 'tennessee\'s candidate', 'trey palmedo', 'waffle house shooting', 'pro-trump tennessee', 'tennessee house removes', 'tn house passes bill', 'vanhuss', 'tn6', 'bill halted in tennessee', 'tn state Representative', 'memphis trees community', 'lee beaman', 'dawnbarlow', 'tennessee Republicans fail', 'tennessee Republicans refuse', 'tn01', 'state Representative for tennessee', 'tennessee gop kill bill', 'corker out', 'oddie shoupe', 'Tennessee Heritage Protection Act', 'TN State Legislature', 'phil roe', 'Greenville local races', 'House Bill 2381', 'Tennessee bill', 'Tennessee to legalize medical marijuana', 'TN Representative Candidate', 'tennessee lawmaker', 'Tennessee Republican files bill', 'running for the House seat for Anderson County', 'john duncan', 'Republican net neutrality bill', 'Tennessee House Republicans', 'corker kick back', 'Corker asks', 'corker kickback', 'corkerkickback', 'corker demands', 'CORker says', 'Tennessee Chooses, 2018', 'Senate in Tennessee', 'TN Democrats Vote', 'bredesen', 'kustoff', 'tennessee governor', 'tn gubernatorial', 'gov. of tn', 'tennessee gubernatorial candidate', 'governor haslam', 'randy boyd', 'kay white', 'tn governor', 'House Budget chair', 'bill lee', 'beth harwell', 'karl dean', 'mae beavers', 'tennessee senate race', 'bob corker', 'sen. corker', 'mackler', 'blackburn', 'corker\'s u.s. senate seat', 'replace corker', 'Corker fight', 'baby body parts', 'andy ogles', 'senator corker', 'Corkers seat', 'tn-6', 'tn-7', 'tn-07']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Tennessee 2018 Election \n\n"
            "[Early Primary Voting Begins](https://sos.tn.gov/products/elections/early-voting-person): July 13, 2018 \n\n"
            "[Primary Election](http://web.go-vote-tn.elections.tn.gov/): August 2, 2018 \n\n"
            "[General Election Registration Deadline](https://ovr.govote.tn.gov/Registration/#BM): October 9, 2018 \n\n"
            "[General Election](http://web.go-vote-tn.elections.tn.gov/): November 6, 2018 \n\n")
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