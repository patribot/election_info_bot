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

local_subs = open("oklahoma.dat", "r")
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
            terms = ['oklahoma board of pharmacy director', 'Medical marijuana rule changes', '20,000 more signatures needed for recreational marijuana petition', 'congressman cole', 'What it feels like, in Oklahoma, right now.', 'Supporters of recreational marijuana say they', 'Republicans stand up to the theocrats and authoritarians', 'oklahoma republicans', 'gov. fallin', 'oklahoma board of health', '797', '788', 'house seats in oklahoma', 'okgov', 'oklahoma teacher primary', 'oklahoma primar', 'kevin stitt', 'oklahoma gop gubernatorial', 'oklahoma gop candidate', 'senate bill 1140', 'oklahoma governor', 'governor of oklahoma', 'oklahoma legislat', 'senate seat in oklahoma', 'Michael Brooks-Jimenez', 'oklahoma strike', 'Oklahoma teacher walkout', 'mary memed', 'tyson meade', 'Oklahoma Education Budget Crisis', 'Oklahoma State Capitol', 'kevin mcdugle', 'rep scott inman', 'ballot in oklahoma', 'oklahoma city district', 'governor fallin', 'Chuck Strohm', 'jenks lawmaker', 'Oklahoma senat', 'sb1016', 'voting in Oklahoma', 'Oklahoma Lawmaker', 'Drew Edmondson', 'Oklahoma City mayor', 'GOP rep from Oklahoma', 'rep. tom cole', 'Gov Fallin', 'markwayne', 'ok-02', 'ok-2', 'oklahoma\'s 2nd District', 'Native American Candidates for Congress', 'bridenstine', 'ok-01', 'ok-1', 'oklahoma\'s 1st District', 'Budget Crisis in Oklahoma', 'steve russell', 'mary fallin', 'Oklahoma House of Representatives and State Senate', 'any opinions on our 2018 gubernatorial election', 'Oklahoma Tried the GOP', 'Voter Registration by County', 'says ou wants students to have abortions']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Oklahoma 2018 Election \n\n"
            "[Voter Registration Deadline](https://www.ok.gov/elections/Voter_Info/Register_to_Vote/index.html): October 12, 2018 \n\n"
            "[General Election Date](https://services.okelections.us/AbsenteeApplication/): November 6, 2018")
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