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

local_subs = open("illinois.dat", "r")
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
            terms = ['gaslight the soybean farmers', 'Cook County 17th District Commissioner Race', 're doing fantastically well', 'Chicago highway with gun control march', 'China cancels US soybean imports', 'Holocaust deniers bid for US Congress', 'Illinois farmers face grim economic prospects', 'Mexican neighbors 4th of July fireworks', 'Prime example of why', 'chicago pride', 'Chicago Protest Against Family Separations', 'sean casten', 'UChicago yearbook picture from 1964', 'walsh trumpgret', 'Chicago police handcuffing unarmed 10-year-old', 'illinois lawmaker', '37th state to ratify Equal Rights Amendment', 'the illinois house', 'Illinois Counties Becoming Gun Sanctuaries', 'illinois rep.', 'Pro Palestinian Protest Downtown', 'illinois progressive network', 'haymarket riot', 'hb 4819', 'congress in illinois', 'il 2018 primary', 'aaron ortiz', 'chuyforcongress', 'il-03', 'office in illinois in 2018', 'illinoisprimary', 'minnesota mosque bombing', 'chicago registered voters', 'illinois legislature', 'illinois primary', '^(?!.*tara lipinski).*lipinski.*$', 'Black, Female Attorney General Candidate', 'conservative Democrat in Illinois', 'The top 10 governor\'s races of 2018', 'illinois voters', 'illinoispolitics', 'Illinois Primaries', 'flip illinois', 'marie newman', 'chuy garcia', '#ilgov', 'Illinois\'s 3rd Congressional District', 'Republican congressional primary in Illinois', 'arthur jones', 'Illinois Congress', 'Illinois GOP Rep', 'illinois green Party', 'Illinois Democratic Gubernatorial', 'Illinois 13th\'s Congressman', '2018 illinois election', 'Illinois Dem gubernatorial candidate', 'rotering', 'Illinois attorney general', 'Illinois Senate', 'Chicago Congressional Primary', 'rep lahood', 'hultgren', 'il-14', 'shimkus', '\'chuy\' garcia', 'Rep. Gutierrez', 'anthony clark', '@cdrosa', 'Carlos Ramirez-Rosa', 'Rep. LaHood', 'mike bost', 'rep. bost', 'congressman bost', 'rep bost', 'representative bost', 'rodney davis', 'davis\'s seat', 'roskam', 'il-6', 'il-06', 'chris kennedy', '^(?!.*trauner).*rauner.*$', 'IL gubernatorial', '@govrauner', '^(?!.*bissexual).*biss.*$', 'illinois governor', 'IL\'s next governor ', 'governor of illinois', 'il gov', 'jeanne ives', 'pritzker', 'il governor\'s']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Illinois 2018 Election \n\n"
            "[General Election Pre-Registration Deadline](https://ova.elections.il.gov/Step0.aspx): October 21, 2018 \n\n"
            "[General Election](https://www.elections.il.gov/VotingInformation/VotingByMail.aspx): November 6, 2018 \n\n")
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