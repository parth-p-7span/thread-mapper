import json
from discord import create_thread, send_thread_message
import constants
from utils import beautify_number
import time


# function to create thread in discord channel and send all the tweets in that thread
def create_discord_thread(tweets):
    if len(tweets) >= 2:
        if len(tweets[0]) < 100:
            thread = create_thread(constants.DISCORD_CHANNEL, tweets[0], f'{beautify_number(1)}\n{tweets[1]}\n')

            for index, t in enumerate(tweets[2:]):
                message = f'{beautify_number(index + 2)}\n{t}\n'
                send_thread_message(thread['id'], message)
                time.sleep(0.5)

        else:
            thread = create_thread(constants.DISCORD_CHANNEL, "Twitter Thread 🧵", tweets[0])

            for index, t in enumerate(tweets[1:]):
                message = f'{beautify_number(index + 1)}\n{t}\n'
                msg = send_thread_message(thread['id'], message)
                time.sleep(0.5)


    else:
        print('Thread length is less than 2')


# function to map Twitter api response and store all the thread tweets in a python list
def map_thread(client, tweet_id):
    tweets = []
    response = client.get_tweet(id=tweet_id, tweet_fields=['context_annotations', 'referenced_tweets', 'conversation_id'])
    data = json.loads(response.text)['data']
    while 'referenced_tweets' in data:
        response = client.get_tweet(id=int(data['referenced_tweets'][0]['id']),
                                    tweet_fields=['context_annotations', 'referenced_tweets', 'conversation_id'])
        data = json.loads(response.text)['data']
        tweets.append(data['text'])
    tweets.reverse()
    create_discord_thread(tweets)
    print('done')


# returns tweets that our BOT is mentioned in
def check_mentions(tw_client, last_id, start_time):
    tweets = tw_client.get_users_mentions(id=1523607877738708997,
                                          tweet_fields=['context_annotations', 'referenced_tweets', 'conversation_id'],
                                          max_results=5,
                                          start_time=start_time
                                          )
    json_data = json.loads(tweets.text)
    if 'data' in json_data:
        data = json_data['data']
        index = 0
        while data[index]['id'] != last_id:
            print(data[index]['id'])
            if 'referenced_tweets' in data[index]:
                map_thread(tw_client, int(data[index]['id']))
            if index >= len(data)-1:
                break
            index += 1
        return data[0]['id']


# function to get the DM messages
def get_direct_messages(tw_client):
    messages = tw_client.list_direct_messages(count=5)
    for message in reversed(messages):
        # who is sending?
        sender_id = message.message_create["sender_id"]
        # what is she saying?
        text = message.message_create["message_data"]["text"]
        print(sender_id, " : ", text)
