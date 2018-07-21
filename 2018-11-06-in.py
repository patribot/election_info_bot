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

local_subs = open("indiana.dat", "r")
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
            terms = ['indiana congress', 'failed gas stations cost taxpayers ', 'What the hell is this propaganda', 'ag curtis hill', 'Man With Multiple Bankruptcies is Wrecking Their Businesses', 'Child finds gun, fires shot in Ikea', 'Indiana precinct', 'in-sen', 'lizforindiana', 'matt cummings', 'Chicago sees its most violent week', 'In Red State primaries, candidates out-Trump each other', 'trump planning trip to indiana', 'states with lax gun laws ', 'Donald Trump Deserves Nobel Peace Prize, Says GOP Congressman', 'in-9', 'pride parade in mike pence', 'Donnelly has his best fundraising', 'Mike Pence\'s hometown', 'stephen chancellor', 'in09', 'Indiana Senate', 'Medicaid work requirements for Indiana', 'Illegal Guns From Indiana', 'Indiana Green Party', 'in-09', 'pelath', 'Joe Donnelly', '2018 elections in Indiana', 'Better Know a State: Indiana']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Indiana 2018 Election \n\n"
            "[General Election Registration Deadline](https://indianavoters.in.gov/PublicSite/OVR/Introduction.aspx): October 9, 2018 \n\n"
            "[General Election](https://indianavoters.in.gov/PublicSite/Public/FT1/PublicLookupMain.aspx?Link=Polling): November 6, 2018 \n\n")
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