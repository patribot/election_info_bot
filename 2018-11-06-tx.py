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

local_subs = open("texas.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['120-degree temps within 25 years', 'too young to talk called into court to defend themselves', 'dallas rejects petition', 'Federal Highway Spending', 'Decent Chance of Becoming Texas', 'texas run for office', 'spiritual adviser rewrites the gospel to defend him', 'Discharging Immigrant Recruits', 'tornillo detention center', 'beto-mania', 'In case you missed it, this was awesome.', 'tx-sen', 'guns down black teen over fireworks', 'Calls On Republican Senate To Protect Mueller', 'fec faults cruz', 'treated us as though we were animals', 'americans want roe', 'congress is completely feckless', 'shots i took from the families belong together march', 'overturn roe', 'abbott asks trump', 'texas chud', 'illegal crossing crisis', 'texas union membership', 'Texas cities try to lure millennials', 'T. Don Hutto facility', 'Texans are planning to protest', 'Texas Democrat', 'If Trump supporters fact-checked even one of his claims', 'detention center in Texas', 'Texas\' 8th Congressional District', 'NEVER reported that the crying girl was separated from her mother', 'greatest political ad of all time', 'beers with beto', 'mj hagar', 'ice to the gestapo', 'Welcome To The US', 'Canceling Real Detention Center Visit', 'southwest key', 'Children at Migrant Detention Center', 'I really don\'t care, do you', 'separating families at the border', 'tender age', 'migrants seeking asylum', 'bargaining chip to build his wall', 'Separated Children Crisis Actors', 'Separated From Their Parents at the Border', 'child detention center in texas', 'separating migrant families', 'children wait in cages', 'camp donald', 'zero humanity', 'zero-tolerance policy', 'keep families together', 'deb armintor', 'school safety commission', 'Republicans In Texas Races', 'lawsuit to end daca', 'family separation', 'boats to watch the hurricane', 'mom of santa fe victim', 'like talking to a toddler', 'texas made it law', 'texas lieutenant governor', 'santa fe school shooting', 'texas gop candidate', 'houston police chief', 'dallas county politician', 'texas school shoot', 'shooting in texas', 'texas candidate', 'cruz and cornyn', 'salman bhojani', 'texas lawmaker', '254 counties', 'denton school district voters', 'Senate candidate Beto', 'cruz voted', 'texas vot', 'laura moser', 'texas gerrymandering', 'dallas county candidate', 'rourke town hall', 'hopeful o\'rourke', 'crystal mason', 'beto believe', 'Houston congressional election', 'rafael cruz', 'cruz to trump', 'linsey fagan', 'beto o', 'voter turnout in texas', 'incumbent culberson', 'tx-14', 'veronica escobar', 'tx16', 'betoorourke', 'cruz, o\'rourke', 'primary in texas', 'texas primary', 'shooting at sutherland springs', 'cruz campaign', 'texas early voting', 'Democratic turnout in Texas', 'Democrats in Texas', 'thomas dillingham', 'Gov. Abbott', 'Superintendent Curtis Rhodes', 'blue texas', 'mike collier', 'tx votes', 'Texas Dem Senate Candidate', 'texas gubernatorial', 'texas redistricting', 'Red District in Texas', 'Texas goes Democratic', 'rick trevino', '2018 Primaries for Texas', 'will hurd', '2018 Texas primaries', 'Texas\' Next Senator', 'Texas congress', 'Texas 3rd Congressional District', 'cruz vs. o', 'saari', 'vote for beto', 'House Republicans in Texas', 'dan patrick', 'derrick crowe', 'TX district judge', 'sam johnson', 'colin allred', 'Texas Justice Democrat', 'tx-32', 'tx-16', 'rep. dukes', 'Voting in Texas', 'tx23', 'joe straus', 'txgov', 'larry kilgore', 'Texas House of Representatives and State Senate', 'michael c. burgess', 'texas gop congressman', 'randy weber', 'rep. weber', 'Representative weber', 'congressman weber', 'rep weber', 'tx31', 'vanessa adia', 'kevin brady', 'roger williams', 'lupe valdez', 'medrick yhap', 'joe barton', 'rep. roger williams', 'ted cruz', 'sen. cruz', 'senator cruz', 'ted. cruz', 'tedcruz', 'texas district 07', 'pete sessions', 'rep. sessions', 'rep sessions', 'representative sessions', 'congressman sessions', 'john culberson', 'rep. culberson', '@congculberson', 'culberson\'s texas', 'congressman culberson', 'rep culberson', 'kenny marchant', 'rep. marchant', 'Rep (Marchant)', 'congressman marchant', 'rep marchant', 'letitia plummer', 'pete olson', 'rep. olson', 'rep olson', 'representative olson', 'congressman olson', 'tx-22', 'tx22', 'ted poe', 'H.R. 620', 'hr 620', 'tx-02', 'rep poe', 'representative poe', 'congressman poe', 'rep. poe', '^(?!.*anthony lamar smith).*lamar smith.*$', 'house science committee chair', 'tx-21', 'tx21', 'john carter', 'tx-31', 'hensarling', 'gohmert', 'tx-01', 'brian babin', 'rep. babin', 'rep babin', 'representative babin', 'congressman babin', 'greg abbott', 'texas governor', 'TX\'s next governor ', 'rolando pablos', 'governor of texas', 'tx gov', 'governor in Texas', '@gregabbott_tx', 'sb-4', 'sb4', 'sb 4', 'Senate Bill 4', 'rape insurance', 'Texas\' redistricting fight', 'ken paxton', 'texas attorney general', 'michael burgess', 'rep. burgess', 'rep burgess', 'representative burgess', 'congressman burgess', 'tx-26', 'tx26', 'will fisher', 'Michael McCaul', 'rep. mccaul', 'Representative mccaul', 'congressman mccaul', 'rep mccaul', 'mike mccaul']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Texas 2018 Election \n\n"
            "[General Election Registration Deadline](http://www.votetexas.gov/register-to-vote/): October 9, 2018 \n\n"
            "[Early Voting Starts](https://teamrv-mvp.sos.texas.gov/MVP/mvp.do): October 22, 2018 \n\n"
            "[General Election](https://teamrv-mvp.sos.texas.gov/MVP/mvp.do): November 6, 2018 \n\n")


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