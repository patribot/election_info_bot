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

local_subs = open("california.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.selftext)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['medicare for all caucus', 'cutting checks to the following 25 people', 'california into three states', 'orange county vote', 'electoral college', 'gave the Republicans an assload of money', 'Elon Musk revealed as one of the largest donors', 'fifth-largest economy', 'airbnbing', 'san diego rent control', 'chad the cookout killer', 'ca-ad-58', 'maxine waters', 'California Pregnancy-Center Rules', 'California disclosure law', 'Camp for Migrants in Concord', 'black kids selling water', 'ted lieu', 'asm. santiago', 'california lawmaker', 'kevin jang', 'kevin hee young jang', 'miguel santiago', 'separated from their parents at the border', 'breaking up families at the border', 'female candidates for Congress', 'three californias', 'london breed', 'one california or three', 'california into 3 states', 'Democratic tide in Orange County', 'california\'s blue wave', 'When Will I See My Papa', 'pasadena vote', 'ca-04', 'california primar', 'bay area housing', 'dsa-la', 'gov. brown', 'sb 822', 'renters in san francisco', 'oakland mayor', 'ca gov', 'ca04', 'affordable rent in san francisco', 'Secure Data Act', 'CALIFORNIA\'S REPUBLICAN VOTER', 'California Assembly', 'California\'s housing crisis', 'uc workers strike', 'pelosi', '5th largest economy', 'california needs rent control', 'candidate for SF mayor', 'feinstein', 'ca state senate', 'california voters', 'california senate', 'jerry brown', 'California Consumer Privacy Act', 'california considering bill', 'san diego council candidates', 'house intelligence Committee Republicans', 'california bill ', 'repbarbaralee', 'erin cruz', 'dave min', 'ca48', 'ca25', 'California gun reform', 'delaine eastin', 'California ballot initiative', 'julia peacock', 'ca49', 'nunes campaign', 'gavin newsom', 'steve poizner', 'gayleforca', 'mike cernovich', 'dreamactnow', 'California Republican', 'gavinnewsom', 'Kashyap Patel', 'imagine a blue Congress', 'California House Republicans', 'nunes challenger', 'devinnunes', 'Orange County congressional races', 'house intelligence chair', 'Nunes FBI memo', 'nunes\' memo', 'Nunes gave Trump', 'chairman nunes', 'ca-4', 'khanna', 'nunesmemo', 'nunes memo', 'Nunes\'s memo', 'releasethememo', 'nunes fisa memo', 'anthony rendon', 'midterm nunes', 'jeff denham', 'ca-10', 'rep. denham', 'rep denham', 'congressman denham', 'representative denham', 'March against Trump in LA', 'la women\'s march', 'Women\'s March Los Angeles', 'San Diego Women\'s March', 'dotty nygard', 'Dem Midterm Wave', 'Dems retake the House', 'jess phoenix', 'ed royce', 'rep. royce', 'congressman royce', 'rep royce', 'ca-39', 'Daniel Wenzek', 'california governor', 'duncan hunter', 'rep. hunter', 'congressman hunter', 'rep hunter', 'ca-50', 'Can The Dems Take The House in 2018', 'Rackauckas', 'todd spitzer', 'orange county da ', 'orange county d.a.', 'orange county district attorney', 'CASEN 2018', 'mimi walters', 'Kia Hamadanchy', 'congressional districts to target for 2018', 'devin nunez', 'Orange County Alt-Right', 'devin nunes', 'rep. nunes', 'congressman nunes', 'House Intel chief', 'Nunes Subpoenaed', 'rep nunes', 'darrell issa', 'rep. issa', 'rep issa', 'california gop', 'rohrabacher', 'michael kotick', '@danarohrabacher', 'rohrabracher', 'Transcript of McCarthy', 'pro-assange gop congressman', 'pro-putin california congressman', 'Pro-Russia GOP Rep.', 'Putin\'s congressman', 'rhorabacher', 'steveknight25', 'steve knight', 'rep. knight', 'congressman knight', 'rep knight', 'representative knight', 'ca-25', 'valadao']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("California 2018 Election \n\n"
            "[General Election Registration Deadline](http://registertovote.ca.gov/): October 22, 2018 \n\n"
            "[General Election](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply): November 6, 2018 \n\n")
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