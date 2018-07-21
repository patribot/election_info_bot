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

local_subs = open("massachusetts.dat", "r")
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
            terms = ['ambulance after her leg was trapped', 'mass. voters', 'Kindergarden shooter drills are fun', 'Group rallies against veteran homelessness, extreme war spending', 'Green-Rainbow Party of Massachusetts', 'ma-3', 'bob massie', 'boston march for our lives', 'poster left outside the playground at Frog Pond on Boston Common', 'elizabeth warren', 'stop blaming poor people for their poverty', 'new life to unions', 'Boston Globe pre-covers the next mass shooting', 'invited Jackie Hill-Perry', 'Transgender rights are being targeted nationwide with ballot', 'jim mcgovern', 'For those who claim their votes don', 'sanctuary from marijuana prosecution', 'MA voters could register and vote on same day', 'legal marijuana in Massachusetts', 'Cambridge women\'s march looking majestic af', 'Boston PD only required 100 out of 2,000 cops to wear body cams', 'oldest cities what sea-level rise really means', 'alexandra chandler']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Massachusetts 2018 Election \n\n"
            "[Primary Voter Registration Deadline](https://www.sec.state.ma.us/OVR/): August 15, 2018 \n\n"
            "[Primary Election Date](http://www.sec.state.ma.us/wheredoivotema/bal/MyElectionInfo.aspx): September 4, 2018 \n\n"
            "[General Election Registration Deadline](https://www.sec.state.ma.us/OVR/): October 17, 2018 \n\n"
            "[General Election](http://www.sec.state.ma.us/wheredoivotema/bal/MyElectionInfo.aspx): November 6, 2018 \n\n")
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