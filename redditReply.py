import praw, pdb, re, os

reddit = praw.Reddit('bot1')

if not os.path.isfile("repliedPosts.txt"):
    repliedPosts = []

else:
    with open("repliedPosts.txt", "r") as f:
        repliedPosts = f.read()
        repliedPosts = repliedPosts.split("\n")
        repliedPosts = list(filter(None, repliedPosts))

subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=10):
    if submission.id not in repliedPosts:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply(body="I love python too bro")
            print("Bot replying to: ", submission.title)

            repliedPosts.append(submission.id)

with open("repliedPosts.txt", "w") as f:
    for post_id in repliedPosts:
        f.write(post_id + "\n")