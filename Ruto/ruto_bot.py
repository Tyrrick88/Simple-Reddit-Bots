import praw
import config

def bot_login():
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_SecretKey = config.client_secretKey,
                )
    return r

r = bot_login()
bot_login()