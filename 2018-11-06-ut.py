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

local_subs = open("utah.dat", "r")
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
            terms = ['utah gun rights activist upset', 'treatment of refugee children', 'baby changing table at Utah aquarium', 'New York, South Carolina, Oklahoma, Maryland, Mississippi, Colorado and Utah', 'leaving the party and will now be supporting Democrats', 'Mine Land Previously Protected as a National Monument', 'steve schmidt', 'House Speaker Greg Hughes', 'Freedom Festival excludes all LGBT groups', 'Lets get this fucking medical mj bill passed.', 'Independent Redistricting, Medicaid Expansion, and Medical Marijuana', 'senators who voted against Net Neutrality.', 'UTA name change', 'I love seeing this mans car', 'alicia colvin', '6 states are lining up for battle', 'utah republican booed', 'Small business owners urge Hatch', 'Utah medical marijuana ballot initiative,', 'senate in utah', 'Utah Medical Marijuana Initiative', 'November ballot in Utah', 'medical marijuana in utah', 'comment on bears ears', 'us congress from utah', 'sheldon kirkham', 'donald trump highway bill', 'selling off our public lands', 'utah republicans', 'passes the Utah House', 'romney', 'Sittner', 'marijuana will be legalized in Utah', 'utah legislat', 'national monuments slashed by Trump', 'House Bill 330', 'utah lawmaker', 'rep stewart', 'utah state senate', 'legalize medical marijuana in Utah', 'Hatch\'s Seat', 'jenny wilson', 'Bears Ears Deserves Protection', 'Congressman Stewart', 'bears ears reductions', 'john curtis', 'ut-3', 'ut-03', 'shrink Utah national monument', 'monuments downsizing', 'Attack on Public Land Threatens America', 'No Wonder Millennials Hate Capitalism', 'Ruhle easily stumps Republican', 'The President Stole Your Land', 'StandWithBearsEars', 'chris stewart', 'rob bishop', 'ut-01', 'orrin hatch', 'sen. hatch', 'senator hatch', 'shrink Bears Ears', 'sponsored by Hatch', 'mia love', 'mia b. love', 'rep love', 'rep. love', 'representative love', 'congresswoman love', 'ut-04', 'ut-4']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Utah 2018 Election \n\n"
            "[Voter Registration Deadline](https://secure.utah.gov/voterreg/login.html?selection=REGISTER): October 31, 2018 \n\n"
            "[General Election](https://elections.utah.gov/Media/Default/Documents/Elections%20Resources/Absentee%20Ballot%20Application.pdf): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write post id back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()