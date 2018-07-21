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

local_subs = open("nevada.dat", "r")
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
            terms = ['congressperson in nevada', 'nevada ballot', 'picket in las vegas', 'las vegans protest trump', 'brothel owner hof', 'cortez masto', 'protesting trump in Vegas', 'nevada gop', 'family separations at border', 'nevada kids have health insurance', 'las vegas union', 'nevada primary', 'Nevada 4th Congressional District', 'pat spearman', 'washoe county sheriff', 'nevada voter', 'Vegas shooter', 'John Anzalone', 'Clark County DA', 'nv assembly', 'living wage in nv', 'nevada assembly', 'Las Vegas massacre', 'banning bump stocks', 'nevada politic', 'nv04', 'nv-03', 'nv-02', 'NV GOP wants to', 'kate marshall', 'Las Vegas shooting', 'Nevada House, Senate races', 'jay craddock', 'nevada legislat', 'War on Pot Could Split Republicans in 2018', 'Ending Federal Marijuana Prohibition Act of 2017', 'Las Vegas plan to develop, open marijuana lounges on hold', '16 Senate Dems Still Uncommitted', 'Democrats need to embrace what should be the least controversial position ever', 'Pot Crackdown An Election Issue', 'candidates have to pick between the Breitbart machine and the president', 'amodei', 'Due process saves the Bundys', 'not stadiums, says Las Vegas Knights owner Bill Foley', 'Nicole Cannizzaro', 'Media Completely Ignores Amazing Justice Dem', 'Justice Dem now running unopposed in Nevada', 'Nevada\'s 4th District Race', 'voting blue this 2018', 'laxalt', 'kihuen', 'Senate Looks Like a Tossup in 2018', 'oscarson', 'Senate Pickup Opportunities', 'Act of God', 'paul blart', 'Public schools could lose billions in funding under tax proposals', 'I am voluntarily capping donations to my campaign', 'Friends Of Gold Butte Work', 'We Need To Elect More Women As Leaders', 'Nevada Supreme Court justices', 'Ejected A Terminally Ill Cancer Patient', 'let him know destroying the internet is not an option', '2018 is gonna be a massacre', 'amy vilela', 'State Senate Recall', 'Carson City School Board facing', 'Partisan recalls thrust a quiet Las Vegas', 'michael roberson', 'Richard McArthur', 'tony smith', 'sisolak', 'Tax reform will harm Nevada', 'programs providing pro bono legal assistance to veterans', 'Democrats have had success promoting Universal Basic Income', '^(?!.*hellerweather).*heller.*$', 'sbaih', 'Nevada GOP candidate criticizes', 'Anyone Who Supports Donald Trump Jeopardizes Their Own', 'jared fisher', 'governor sandoval', 'nevada governor', 'NV\'s next governor ', 'governor of nevada', 'nv gov', 'nv governor\'s', 'Marijuana clubs are a bad idea']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Nevada 2018 Election \n\n"
            "[General Election Voter Registration Deadline](https://nvsos.gov/sosvoterservices/Registration/step1.aspx): October 7, 2018 \n\n"
            "[General Election](https://nvsos.gov/votersearch/index.aspx): November 6, 2018 \n\n")
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