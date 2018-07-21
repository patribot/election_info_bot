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

local_subs = open("washington.dat", "r")
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
            terms = ['got my ballott today', 'Bezos Bezos Bezos!', 'thurston county vote', 'lisa brown', 'Dan Satterberg', 'Tariffs are the Wrong Approach', 'states most impacted by Trump', 'Days Until His Term Ends', 'Seattle ICE lawyer facing prison time', 'Washington ranked middle of the pack', 'the head tax', 'Trump jeopardizes way of life', 's up bootlickers', 'a father, a veteran, and an anarchist', 'Washington is leading the way on net neutrality', 'Only Place in America with Net Neutrality', 'Violence erupts at rally held by Washington', 'Seattle-area prosecutor', 'Doug Baldwin ripped into President Trump', 'campaign to persuade American union members to quit', 'plot against us unions', 'teacher of the year', 'Proud Boys vs a single cardboard sign', 'PROUD BOY GETS BTFO BY PROTEST SIGN', 'Seattle Vacates Hundreds of Marijuana Charges', 'Footage of The March On Saturday', 'march in Vancouver against gun violence', 'initiative 1600', 'March March Olympia, WA', 'Seattle Democratic Socialists of America', 'shot itself in the foot on net Neutrality', 'washington state\'s net Neutrality law', 'washington state has now passed', 'Washington becomes first state', 'First State-Level Net Neutrality Law', 'washington lawmakers', 'washington Legislature', 'Washington State Legislature', 'McMorris Rodgers', 'joey gibson', 'cathymcmorris', 'Washington\'s 3rd Congressional Dist', 'Washington Bill', 'gasque', 'wa-8', 'ed orcutt', 'Governor of Washington State', 'States Are Writing Their Own Net Neutrality Laws', 't whore out my internet', 'matt manweller', 'Democrats dominate again in Washington state', 'sarah smith', 'herrera beutler', '@herrerabeutler', 'wa-3', 'wa-03', 'wa\'s 3rd district']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Washington 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://weiapplets.sos.wa.gov/MyVoteOLVR/MyVoteOLVR): July 30, 2018 \n\n"
            "[Primary Election](https://weiapplets.sos.wa.gov/MyVote/#/login): August 7, 2018 \n\n"
            "[General Election Registration Deadline](https://weiapplets.sos.wa.gov/MyVoteOLVR/MyVoteOLVR): October 29, 2018 \n\n"
            "[General Election](https://weiapplets.sos.wa.gov/MyVote/#/login): November 6, 2018 \n\n")
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