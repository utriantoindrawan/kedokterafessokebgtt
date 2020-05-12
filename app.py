from twitter import Twitter
import time
from media import Media

#test

tw = Twitter()
media = Media()
def start() :
    print("Starting...")
    dms = list()
    while True:
        if len(dms) is not 0:
            print(len(dms))
            for i in range(len(dms)):
                message = dms[i]['message']
                sender_id = dms[i]['sender_id']
                id = dms[i]['id']

                if len(message) is not 0 and len(message) < 280:
                    if "dokfess!" in message:
                        message = message.replace("dokfess!", "dokfess!")
                        if len(message) is not 0:
                            if dms[i]['media'] is None:
                                print("DM will be posted")
                                tw.post_tweet(message)
                                tw.delete_dm(id)
                            else:
                                print("DM will be posted with media")
                                print(dms[i]['shorted_media_url'])
                                tw.post_tweet_with_media(message, dms[i]['media'], dms[i]['shorted_media_url'],dms[i]['type'])
                                tw.delete_dm(id)
                        else:
                            print("DM deleted because its empty..")
                            tw.delete_dm(id)
                    else:
                        print("DM will be deleted because does not contains keyword..")
                        tw.delete_dm(id)
            dms = list()

        else:
            print("DM is empty")
            dms = tw.read_dm()
            if len(dms) is 0:
                time.sleep(10)

if __name__ == "__main__":
    start()


