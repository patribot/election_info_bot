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

local_subs = open("missouri.dat", "r")
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
            terms = ['Gay Rights icon, Mike Pence', 'Kansas City will greet Mike Pence', 'Tariffs Have Led to Layoffs', 'missouri congress', 'layoffs from Trump', 'Nail manufacturing exec who voted for Trump', 'Missouri nail manufacturer planning to lay off', 'michael brown was shot', 'Missouri Is Already Blocking Medicaid', 'curtiswylde', 'Ex-Governor May be Running for Senate as an Independent', 'greitens', 'lauren arthur', 'missouripolitics', 'ferguson city council', 'missouri house moves', 'kc voters', 'osmack', 'missouri bill', 'new approach missouri', 'Missouri lawmaker', 'austin petersen', 'Missouri Medical Marijuana Campaign', 'josh hawley', 'courtland sykes', 'US Senate in Missouri', 'MO GOP Senate Nomination', 'snake-filled heads', 'career obsessed banshees', 'Missouri pregnancy mortality', 'sam graves', 'public owned ISP in St. Louis City and County', 'Blaine Luetkemeyer', 'Louis Cops Lead Nation in Rate of Police Shootings', 'Public defenders say they\'re overworked and underfunded', 'KC based protests over Net Neutrality', 'kathy ellis', '\'Approved demonstration area\'', 'bigly tax giveaway speech for the rich', 'Focusing on St. Louis', 'mccaskill', 'Billionaire pharma owner fueled the opioid epidemic with bribery scheme', 'Vulnerable Dem senators', 'recruit huddles with Koch network in New York', 'top 10 Senate races of 2018', 'ann wagner', 'mo-2', 'jenna marie bourgeois', 'hartzler', 'mo-4', 'How Missouri previewed Democrats']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Missouri 2018 Election \n\n"
            "[Primary Election Date](https://voteroutreach.sos.mo.gov/PRD/VoterOutreach/VOSearch.aspx): August 7, 2018 \n\n"
            "[General Election Registration Deadline](https://s1.sos.mo.gov/votemissouri/request): October 10, 2018 \n\n"
            "[General Election](https://voteroutreach.sos.mo.gov/PRD/VoterOutreach/VOSearch.aspx): November 6, 2018 \n\n\n\n"

            "[Check Your Voter Registration](https://s1.sos.mo.gov/elections/voterlookup/) \n\n")
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