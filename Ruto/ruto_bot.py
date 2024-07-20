import praw
import config

def bot_login():

    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_SecretKey = config.client_secretKey,
                )
    return r


def run_bot(r):
    for comments in r.subreddit(config.subreddit).comments(limit=25):
        if "Ruto" in comment.body:
            print(config.message)
        

r = bot_login()
run_bot()