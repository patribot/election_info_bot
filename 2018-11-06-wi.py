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

local_subs = open("wisconsin.dat", "r")
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
            terms = ['Campaign That Gave Us Janus', 'punish the poor', 'leah vukmir', 'résumé of every Republican Party member', 'Holocaust deniers bid for US Congress', 'The House Is Tired of Getting Burned', 'candidate won wisconsin', 'legislation to abolish ICE', 'Ryan\'s Janesville office', '5.4 Trillion Attack on Nation', 'children are being held in cages', 'separation of families at the us border', 'wisconsin senate candidate', 'caleb frostman', 'Milwaukee County ballot', 'Foxconn set to drain 7 million gallons of water from Lake Michigan', 'firing of house chaplain', 'ryan sold his soul', 'trump praises ryan', '4,000 raise donald trump and gop promised', 'politics of outrage is failing him', 'rebecca dallet', 'Wisconsin Supreme Court race', 'Dane County Supervisor Seat Tonight in Wisconsin', 'judge rejects walker', 'The_Donald post I actually like', 'wisconsin green party', 'wisconsin gop plans to change the law', 'Milwaukee voter', 'wisconsin legislator', 'wisconsin legislature', 'Bryce rally', 'kyle frenette', 'Green Party Takes County Commissioner Seat in Wisconsin', 'gleefully celebrated passing a bill that would have taken mental health care', 'If Newt Gingrich Were Still In Congress', 'wi-07', 'dehydration death of Milwaukee jail inmate', 'Milwaukee Sheriff', 'unworthy to serve as speaker', 'give up on longtime Republican goal of eliminating deficit', 'Republicans Have Become the Party of Debt', 'Restrictive voter ID laws', 'submissive Republicans', '1.50 per Week', 'partisan gerrymandering is going down', 'Wisconsin Democratic Gubernatorial Candidate', 'Foxconn cost Wisconsin eight times as much per job', 'This Is What Fake Patriotism Looks Like', '28 Wisconsin Dairy Farms declared bankruptcy', 'The U.S. government is set to borrow nearly', '1.50 pay hike', '1.50 a week is being touted as a success story', 'Ryan rejects calls to remove Devin Nunes', 'McConnell took to shield Trump', '2.8 Million in Fourth Quarter', 'Rig Wisconsin Elections', 'Wisconsin Republicans Abruptly Decide To Oust Top State Elections', 'gop rigs elections', 'How Trump is Destroying the GOP', 'Kochs made huge donations to Republicans shortly after tax plan passed', 'Republicans control the Senate, House and White House', 'Foxconn cost to public', 'House Majority Leader', 'Wisconsin Senate Committee', 'neverryan', 'tammy baldwin', 'entitlement reform', 'matt flynn', 'Sensenbrenner', 'randy bryce', 'scott walker', 'governor walker', 'wisconsin governor', 'wi governor\'s', 'Wisconsin gubernatorial candidate', 'Wisconsin democratic governor candidate', 'Wisconsin Democratic candidates for governor', 'Wisconsin\'s partisan gerrymander', 'Deterred Voters in Wisconsin', 'Wisconsin Strict ID Law', 'Republican Governors Association', 'Republican Gov Association', 'paul ryan', 'rep. ryan', 'congressman ryan', 'rep ryan', 'speaker ryan', '@speakerryan', 'IronStache', 'Republican tax scam', 'Middle-Class Tax Hike', 'Wisconsin\'s First Congressional District', 'brad schimel']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Wisconsin 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://myvote.wi.gov/en-us/registertovote): August 14, 2018 \n\n"
            "[Primary Election](https://myvote.wi.gov/en-us/FindMyPollingPlace): August 14, 2018 \n\n"
            "[General Election Registration Deadline](https://myvote.wi.gov/en-us/registertovote): November 6, 2018 \n\n"
            "[General Election](https://myvote.wi.gov/en-us/FindMyPollingPlace): November 6, 2018 \n\n")
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