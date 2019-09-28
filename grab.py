import json
import os

import praw

RESULTS_DIR = 'results'

with open('config.json', 'r') as input_file:
    config = json.load(input_file)

with open('subreddits.json', 'r') as subreddit_file:
    subreddit_list = json.load(subreddit_file)

reddit = praw.Reddit(client_id=config['client_id'],
                     client_secret=config['client_secret'],
                     password=config['password'],
                     user_agent=config['user_agent'],
                     username=config['username'])

def process_subreddit(subreddit):

    subreddit = reddit.subreddit(subreddit)

    with open(os.path.join(RESULTS_DIR, 'results-{}.txt'.format(subreddit)), 'w') as output_file:

        for submission in subreddit.new(limit=100):

            for comment in submission.comments:

                try:
                    output_file.write(comment.body)
                    output_file.write('\n')
                except:
                    print('no comments here!')

for url in subreddit_list['subreddits']:
    process_subreddit(url)
