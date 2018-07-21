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

local_subs = open("georgia.dat", "r")
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
            terms = ['killed in Southeast Georgia for running away from the police', 'bill to hurt gov race rival', 'suppress black voters in 3 swing states', 'GA family loses custody of son', 'ga06', ' Speechless. Just Wow.', '46 Our Revolution endorsed', 'ethan pham', 'Georgia Republican', 'deportation bus tour', 'blue-collar georgia tenants', 'stacey abrams', 'performance artist sean hannity', 'burned swastikas in a west Georgia field', 'gov. deal', 'cloud act', 'law in georgia', 'georgia democrats', 'georgia congressman', 'georgia voters', 'advances in ga. house', 'ga-12', 'casey cagle', 'trent nesmith', 'Gwinnett State House district', 'georgia legislator', 'georgia governor', 'georgia 6th', 'georgia lawmakers', 'Georgia Midterms', 'fran millar', 'Black Women Vote More, But Remain Underrepresented in Politics', 'Lawmakers propose switching Georgia', 'doug collins', 'rep. collins', 'rep collins', 'Reddest district in Georgia', 'representative collins', 'congressman collins', 'ga-9', 'ga-09', 'Georgia turns blue', 'kevin abel', 'Crackdown On Unlicensed Ga. Facilities', 'Republicans dust off Georgia special election playbook for midterms', 'State Legislators Across the Country Are Joining Forces to Fight for Reproductive', 'Trump approval rating 36.7' 'approval ratings in Georgia erode', ' Disapproval in Georgia', 'female political activism that could shift the course of US politics', 'GA House of Representatives', 'Georgia\'s Election System', 'Poverty Is Both a Political and a Moral Choice Made By the Powerful', 'Journalist found guilty of obstruction of justice after suing Sheriff Candidate', 'In Georgia, battle of the \'Staceys\'', 'jeffares' 'buddy carter', 'lisaringga', 'lisa ring', '@repbuddycarter']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Georgia 2018 Election \n\n"
            "[General Election Registration Deadline](https://www.mvp.sos.ga.gov/MVP/mvp.do): October 9, 2018 \n\n"
            "[General Election Early Voting Starts](https://www.mvp.sos.ga.gov/MVP/mvp.do): October 15, 2018 \n\n"
            "[General Election](https://www.mvp.sos.ga.gov/MVP/mvp.do): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write our post id to the tracking file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()