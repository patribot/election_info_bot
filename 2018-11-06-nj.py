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

local_subs = open("newjersey.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['sex toys and oils with marijuana', 'Jersey City Set to Decriminalize Marijuana', 'Bedminster', 'Republicans are coming for your 401k', 'nj-11', 'seth grossman', 'Protest against Family Separation in Clifton', 'new jersey passed sweeping', 'murphy set to sign law', 'the more socialister it is', 'nj state legislat', 'nj Representative', 'new jersey lawmaker', 'NJ marijuana legalization', 'nj assembly', 'new jersey voters', 'josh gottheimer', 'Representative Chris Smith', 'NJ GOP Candidate', 'Republican Hugin', 'NJ\'s 7th District', 'nj cd-7', 'N.J. congressman', 'keady', 'New Jersey Senat8', 'Congressman Chris Smith', 'NJ State Senator Ron Rice', 'NJ congressmen', 'NJ GOP rep', 'thomas macarthur', 'tom macarthur', 'rep. macarthur', 'rep macarthur', 'representative macarthur', 'congressman macarthur', 'lobiondo', 'leonard lance', 'nj-7', 'nj-07', 'frelinghuysen', 'New Jersey election results could be bad omen for', 'Budget vote raises red flag for GOP on tax reform', 'killing your property tax deduction by ending this perk for the rich', 'Republicans are quietly trying to turn churches into dark money havens', 'Republicans just declared they want to kill your property tax deduction', 'tax plan and nj homeowners']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("New Jersey 2018 Election \n\n"
            "[General Election Registration Deadline](http://www.state.nj.us/state/elections/voting-information.html): October 16, 2018 \n\n"
            "[General Election](http://www.njelections.org/voting-information-vote-by-mail.html): November 6, 2018 \n\n")
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