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

local_subs = open("kansas.dat", "r")
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
            terms = ['kansas rally', 'label and jabs Koch family', ' Century II Wichita KS', 'Green Beret running for Congress', ' are arming criminals ', 'Harley-Davidson shutdown', 'jamesthompsonks', 'candidate in Kansas', 'Get out of my country', 'kansas is one of the worst', 'vermin supreme', 'lesbians from adopting passes in Kansas', 'svaty', 'state representative in kansas', 'teacher forcedd to flee small kansas town', 'kansas senate', 'kansas house', '6 teens enter governor', 'lawrence dad fighting deportation', '4 billboards in kansas', 'kansas statehouse', 'andrew finch', 'kansas schools need massive funding increase', 'kansas republicans fear defeat', 'kansas gop partners', 'ks03', 'first gay Kansas rep', 'kansas state house', 'ksleg', 'Kansas Attorney General', 'ks legislat', 'brent welder', 'Kansas Legislat', 'steve alford', 'Kansas lawmaker', 'voter fraud commission', 'voter-fraud commission', 'election fraud commission', 'kelly rippel', 'Kansas Congressional Delegation', 'kansas budget crisis', '2018 elections in Kansas', 'yoder', 'ks-3', 'ks-03', 'chris haulmark', 'ks-2', 'ks-02', 'jenkins, lynn', 'congressman jenkins', 'lynn jenkins', 'rep jenkins', 'steve fitzgerald', 'ks-4', 'ks-04', 'Kansas\' 4th Congressional District', 'kansas 4th congressional district', 'congressman estes', 'ron estes', 'rep estes', 'kansas veteran james thompson', 'brownback', 'kobach', 'colyer', '^(?!.*arkansas governor).*kansas governor.*$', 'carl brewer', 'Trump voter fraud panel', 'trump voting commission', 'destroyed the Kansas economy', 'Trump Election Fraud Panel Leader', 's Election Commission', 'Kansas tax cut experiment', 'governor in kansas', 'voter-fraud propandist', 'kansas republican governance experiment', 'house minority leader jim ward', 'Trump Voter Fraud Probe', '\"election integrity commission\"', '\'election integrity commission\'', 'Trump\'s voter-fraud panel', 'Trump\'s election commission co-chair', '\'election integrity\' panel', 'Trump voting panel']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Kansas 2018 Election \n\n"
            "[Primary Election](http://www.kssos.org/forms/elections/AV1.pdf): August 7, 2018 \n\n"
            "[General Election Voter Registration Deadline](https://ksvotes.org/): October 16, 2018 \n\n"
            "[General Election](http://www.kssos.org/forms/elections/AV1.pdf): November 6, 2018 \n\n")
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