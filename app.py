from twitter import Twitter
import time
from media import Media

tw = Twitter()
media = Media()
def start():
    print("Starting...")
    dms = list()
    while True:
        if len(dms) is not 0:
            print(len(dms))
            for i in range(len(dms)):
                message = dms[i]['message']
                sender_id = dms[i]['sender_id']
                id = dms[i]['id']

                if len(message) is not 0 and len(message) < 200:
                    if "dokfess!" in message:
                        message = message.replace("dokfess!", "")
                        if len(message) is not 0:
                            print("DM will be posted")
                            tw.post_tweet_text_only(message)
                        else:
                            print("Message avoided because its empty")
                            tw.delete_dm(id)
                    else:
                        print("Keyword wrong")
                        tw.delete_dm(id)

                if len(message) is not 0 and len(message) < 200:
                    if "https://" not in message and "http://" not in message:
                        if "kedokteranfess" in message:
                            message = message.replace("kedokteranfess", "")
                            screen_name = tw.get_user_screen_name(sender_id)
                            media.download_image()
                            media.process_image(message, screen_name)
                            tw.post_tweet()
                            tw.delete_dm(id)
                        else:
                            print("Keyword wrong")
                            tw.delete_dm(id)
                    else:
                        tw.delete_dm(id)
            dms = list()

        else:
            print("DM is empty")
            dms = tw.read_dm()
            if len(dms) is 0:
                time.sleep(10)


if __name__ == "__main__":
    start()