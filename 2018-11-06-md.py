# coding: utf-8
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

local_subs = open("maryland.dat", "r")
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
            terms = ['Voting can\'t get easier than this', 'blocked a resolution to have Trump enforce the Russian sanctions', 'maryland election', 'self-funder in Montgomery County', 'capital gazette shooting', 'shooting at capital gazette', 'Forget Being Called an Enemy of the People', 'Annapolis Newsroom Shooting', 'need to be curb-stomped', 'call for shooting journalists', 'Sanders congratulates progressive candidates on primary wins', 'md primary', 'New York, South Carolina, Oklahoma, Maryland, Mississippi, Colorado and Utah', 'maryland candidate for governor', 'ben jelous', 'maryland vote', 'Baltimore State\'s Attorney', 'bmoreceasefire', 'Crabbers in Maryland are unable to get the help they need', 'chelsea manning', 'pour money behind Blue Dog Democrats to ensure', 'maryland green party', 'I went to Washington DC for the', 'maryland senate', 'maryland may put a cannabis', 'md. lawmakers', 'gerrymandering in maryland', 'benjealous', 'Maryland Single-Payer Bill', 'Baltimore cops kept toy guns', 'ben cardin', 'md-gov', 'gov. hogan', 'andy harris', 'ben jealous', 'larry hogan', 'maya for maryland', 'alec ross', 'maryland governor', 'MD\'s next governor ', 'governor of maryland', 'md gov', 'md governor\'s', 'Maryland governor’s race', 'md. governor', 'maryland gubernatorial candidate', '9 Democratic primaries to watch in 2018', 'DSA candidates and Justice Democrats running in these 2018 primaries', 'Only two African Americans have been elected governor', 'Maryland workers need paid sick leave']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Maryland 2018 Election \n\n"
            "[General Election Registration Deadline](https://elections.maryland.gov/voter_registration/application.html): October 16, 2018 \n\n"
            "[General Election](https://voterservices.elections.maryland.gov/OnlineVoterRegistration/InstructionsStep1): November 6, 2018 \n\n")
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