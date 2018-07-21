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

local_subs = open("louisiana.dat", "r")
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
            terms = ['louisiana fall elections', 'says God sends natural disasters to punish gays', '72 y.o. mother registered as a Democrat', 'a rainbow flag has to be the most ironic thing', 'twitter troll from baton rouge', 'the business of shaming', 'highest number of 90', 'Higgins campaign', 'louisiana congress', 'deepwater horizon', 'House of Representatives in Louisiana', 'Protest march June 30 against Trump policy of separating immigrant children', 'Shreveport mayor', 'Citizens for a New Louisiana', 'louisiana secession plan', 'louisiana governor', 'la district 3', 'louisiana lawmaker', 'louisiana elected officials', 'louisiana budget cuts', 'louisiana nursing home eviction', 'bayou bridge pipeline', 'tom schedler', 'la. house republican', 'louisiana legislator', 'louisiana sinking', 'wendy vitter', 'louisiana senators', 'louisiana law', 'louisiana senate', 'la. state senator', 'Dave Langlinais', 'la 3rd', 'LouisianaPolitics', 'nine current GOP members of Congress who voted against MLK Day', 'Louisiana teacher jailed for speaking out', 'poor little woman', 'Protest in Abbeville this afternoon in support of the teacher', 'Y\'all, we did it', 'deyshia hargrave', 'Arrested for Asking Why the Superintendent Got a Raise', 'We are doing the work, we are number 6 or 7 in the state', 'Vermilion school board', 'Vermillion school board', 'arrested for asking why superintendent received raise', 'Vermilion parish', 'How politics screwed Puerto Rico out of billions in disaster aid', 'Louisiana district over school prayer', 'Reclaiming The New South', 'Prayers, Proselytizing by Louisiana School District', 'll Stop When Someone Makes Me Stop', 'Louisiana superintendent refuses', 'The end of American prison visits', 'most incarcerated state', 'scalise', 'this nation to the telecom lobby for the low, low price', 'clay higgins', 'Louisiana Prison Percentage Full by Month']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Louisiana 2018 Election \n\n"
            "[Voter Registration Deadline](https://voterportal.sos.la.gov/VoterRegistration): October 9, 2018 \n\n"
            "[General Election](https://voterportal.sos.la.gov/Home/VoterLogin): November 6, 2018 \n\n")
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