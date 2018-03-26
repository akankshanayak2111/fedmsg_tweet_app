import fedmsg
import twitter_utils
import fedmsg.config
import fedmsg.meta
config = fedmsg.config.load_config([], None)
fedmsg.meta.make_processors(**config)


def main():
    tweet = twitter_utils.Tweet()
    config = fedmsg.config.load_config([], None)
    fedmsg.meta.make_processors(**config)
    for name, endpoint, topic, msg in fedmsg.tail_messages():
        #currently only few topics are frequented
        #so sending tweets without filtering on topics 
        print "Sending Tweet"
        title = fedmsg.meta.msg2title(msg, **config)
        tweet.send_tweet("Msg recieved on bus is titled:%s"%title)

if __name__ == '__main__':
    main() 


