# fedmsg_tweet_app
Simple consumer subscribing to messages on fedmsg bus.
Everytime there is a message on the bus, send a tweet with message title

## Getting Started
Clone the project and replace empty twitter api keys with your project keys in the file twitter_credentials.json

```
python fed_consumer.py
```

## To Do
Convert the project into a systemd service
Filter topics and send tweets only if current msg belongs to the list of interested topics
Add unit tests
