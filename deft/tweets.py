import requests
import os
from google.cloud import language_v1
from typing import List
from config import get_config

base_url = "https://api.twitter.com/2"
headers = {"Authorization": "Bearer {}".format(os.getenv("TWITTER_API_TOKEN"))}


# @user -> user_id
def fetch_user_ids(usernames: List[str]) -> List[str]:
    try:
        res = requests.get(
            base_url
            + "/users/by?usernames={}&user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=author_id,created_at".format(
                ",".join(usernames)
            ),
            headers=headers,
        )
        return [i["id"] for i in res.json()["data"]]
    except Exception as e:
        raise Exception("Something broke! {}".format(e))


def fetch_tweets(users: List[str], keywords: List[str]) -> dict:
    user_ids, ret = fetch_user_ids(users), {}
    for user_id in user_ids:
        try:
            res = requests.get(
                base_url + "/users/{}/tweets".format(user_id), headers=headers
            )
            ret[user_id] = sanitize_tweets(
                res.json()["data"], keywords
            )  # sanitize here
        except Exception:
            continue
    return ret


# keeps a tweet if a keyword is present
def sanitize_tweets(tweets: List[str], keywords: List[str]) -> List[str]:
    ret = []
    for tweet in tweets:
        text = tweet["text"].split()
        if text[0] == "RT":
            continue
        if any(x in text or x.lower() in text for x in keywords):
            ret.append(tweet)
    return ret


def sentiment_analysis():
    client, config, ret = language_v1.LanguageServiceClient(), get_config(), []

    # get all keywords
    keywords = []
    for k, v in config["currencies"].items():
        keywords += v["keywords"]

    # analyze tweets
    d = fetch_tweets(config["twitter"]["accounts"], keywords)
    for user_id, tweets in d.items():
        for tweet in tweets:
            text = u"{}".format(tweet["text"])

            doc = language_v1.Document(
                content=text, type_=language_v1.Document.Type.PLAIN_TEXT
            )

            sent = client.analyze_sentiment(
                request={"document": doc}
            ).document_sentiment

            """
            print("Text: {}".format(text))
            print("Sentiment: {:.2%}, {:.2%}".format(
                sent.score, sent.magnitude))
            """

            ret.append((text, sent.score, sent.magnitude))
    return ret
