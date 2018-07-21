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

local_subs = open("newyork.dat", "r")
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
            terms = ['nyc bill passes', 'Confront Corruption rally in Times Square', 'Democratic headquarters in Albany', 'opioid use in nyc', 'gov. cuomo', 'Can we at least agree on this', 'left needs to get younger', 'Despite Progressive Wins', 'How to Make Trump', 'julia salazar', 'New York Daily News 7.4.18', 'Police evacuate Statue of Liberty', 'Want something done then do it yourself', 'aoc', 'bronx dsa', 'nyc public schoolteachers', 'yearning to breathe free', 'NYC Foster Center In Dead Of Night', 'immigrant child separation issue', 'Flushing man facing deportation after showing up for green card interview', 'so many damn ubers', '6th NYC taxi driver', 'single payer new york health act', 'new york state assembly', 'taxi driver in debt', 'giuliani', 'cuomo endorsement', 'new york\'s housing crisis', 'preet bharara', 'marijuana charges in new york', 'zephyr', 'eric schneiderman', 'new york city dsa', 'new york state senat', 'cuomo signs bill', 'maggie haberman', '1,273 days', 'howie hawkins', 'new york senate', 'steve stern', 'cynthianixon', 'crazy jew', 'new york may legaliz', 'trump tower fire', 'well built building', 'cynthia nixon', 'fire at trump tower', 'ny-24', 'n.y. passes bill', 'kurt schlickter', 'green party of new york', 'nra-backed n.y. pols', '9/11 first responders', 'tenney', 'NY State bill', 'ny-21', 'Billionaires Row', 'ny-19', 'Ocasio', 'ny19', 'new york lawmaker', 'Governor Cuomo', 'New York gov', 'ny27', 'New York City\'s fossil fuel divestment could spur global shift', 'New York City Declares War on the Oil Industry', 'New York Finally Consider Legalizing Cannabis', 'sara idleman', 'peter king', 'katko', '^(?!.*burkina faso).*faso.*$', 'daniel donovan', 'dan donovan', 'ny-11', 'rep. donovan', 'rep donovan', 'representative donovan', 'congressman donovan', 'michael grimm', 'GOP incumbent over Grimm']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post

        text = ("New York 2018 Election \n\n"
            "[State Primary Election Date](https://voterlookup.elections.state.ny.us/votersearch.aspx): September 13, 2018 \n\n"
            "[General Election Registration Deadline](https://voterreg.dmv.ny.gov/MotorVoter/): October 12, 2018 \n\n"
            "[General Election Date](https://voterlookup.elections.state.ny.us/votersearch.aspx): November 6, 2018")
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