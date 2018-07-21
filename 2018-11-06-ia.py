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

local_subs = open("iowa.dat", "r")
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
            terms = ['Farmers say China has already', 'Ferry sounds pretty tight', 'iowa democrats', 'DACA student killed after being deported to Mexico by ICE', 'ICE deports Iowa HS student', 'Iowa student killed after being deported to Mexico', 'iowa\'s medicaid', 'A Democrat in Farm Country Hopes to Beat', 'VOTE ON JUNE 5', 'zach wahls', 'iowa abortion ban', 'trump is for the rich', 'Democrats target union workers who regret voting for Trump', 'iowa race as house candidate', 'Handed China His County-By-County Electoral Map', 'Letter Sent to Several Burma Refugees Living in Des Moines', 'Iowa audience was way ahead of him on gun control', 'Bernie Sanders returns to Iowa', 'Iowa representatives', 'NRA president\'s Iowa business', 'ia-03', 'Factory Farming in Iowa', 'kim reynolds', 'Alasandro', 'Iowa\'s 3rd District race', 'austin frerick', 'secretary has called for the gassing of Jews, gays and Roma', 'governor of iowa', 'Can We Worry About the Banks', 'iowa gubernatorial', 'Iowa Lawmakers', 'nate boulton', 'rob sand', 'Early Investment In Iowa To Help Down-Ballot Democrats', 'Iowa Poll: Democrats preferred over Republicans', 'Iowa went big for Trump, but', 'david young', 'Trump tramples GOP loyalty with anti-Iowa positions', 'Progressive Duo for Iowa Governor', 'Monopoly Candidates Are Testing a New Politics in the Midterms', 'Democratic Party Fundraiser Leaders Snub Iowa Candidate', 'Running For Congress In Iowa', 'Trump sinks in Iowa', 'rod blum', 'rep. blum', 'congressman blum', 'rep blum', 'Democrats Could Win 50 House Seats', 'Democratic Groups Come out Swinging Against Trump', 'Why should I pay...', 'steve king', 'rep. king', 'rep king', 'representative king', 'House GOP ignores health care for 9 million kids', 'The Creepily Influential Trumpist', 'Does Donald Trump Hate Iowa', 'GOP Congressmen Talk Christian Judges', 'Does the GOP Base Love Trump More Than It Hates', 'Left out of meeting, Republicans tweeted Trump', 'Trump stuns Washington with immigration moves', 'GOP Base Love Trump More Than It Hates', 's Base Unleashes Their Anger Over', 'GOP leaders try to reassert control', 'Trump\'s die-hard supporters are fuming', 'diehard supporters are fuming after an apparent about-face', 'live in the shadows', 'After 16 Futile Years', 'Republican suicide', 'congressman king', 'ia-01', 'ia-4', 'ia-04']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Iowa 2018 Election \n\n"
            "[General Election Registration Deadline](https://mymvd.iowadot.gov/Account/Login?ReturnUrl=%2fVoterRegistration): October 27, 2018 \n\n"
            "[General Election](https://sos.iowa.gov/elections/pdf/absenteeballotapp.pdf): November 6, 2018 \n\n")
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
