import tweepy
import speedtest
import threading

# TWITTER AUTH SETUP #

# Enter your details
consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# SPEEDTEST SETUP #

speedtester = speedtest.Speedtest()
speedtester.get_best_server()

def getSpeed(down=100, up=100, time=1800, threshold=15):
    # down and up are the expected values for download and upload speed, respectively, in Megabytes.
    # threshold is the "cutoff" point. If obtained download speed < down-threshold or obtained upload speed < up-threshold, then we'll nag your ISP!
    threading.Timer(time, getSpeed).start() # Runs the function every 30 minutes (unless you specify another one).

    speedtester = speedtest.Speedtest()
    speedtester.get_best_server()

    #speedtester.download() and speedtester.upload() return a float which represents the internet speed in B/s.
    # I use this to create a very rough approximation to MB/s.

    #Say the download speed is 96540000.423932.
    #Since there are 1024 Bytes per KB and 1024 KB per MB dividing by 1024**2 will report a MB/S
    #In this case: 92.07

    dSpeed = "%.2f" % (speedtester.download() / (1024**2))
    # Same process for the upload speed.
    uSpeed = "%.2f" % (speedtester.upload() / (1024**2))
    if dSpeed < down-threshold and uSpeed < down-threshold:
        api.update_status(f'@MEOpt porque é que as minhas velocidades de download e upload estão a {dSpeed}MB/s e {uSpeed}MB/s, respetivamente, quando tenho um contrato para {down}/{up} MB/s? #meo #meofibra')
        print(f"Mensagem enviada: @MEOpt porque é que as minhas velocidades de download e upload estão a {dSpeed}MB/s e {uSpeed}MB/s, respetivamente, quando tenho um contrato para {down}/{up} MB/s? #meo #meofibra")

    elif dSpeed < down-threshold: # Compares the download speed from the speedtest with the expected download speed passed as a function argument minus the threshold value. 

        # api.update_status sends a status update.
        api.update_status(f'@MEOpt porque é que a minha velocidade de download está a {dSpeed}MB/s quando tenho um contrato para {down}MB/s? #meo #meofibra') 

        print(f"Mensagem enviada: @MEOpt porque é que a minha velocidade de download está a {dSpeed}MB/s quando tenho um contrato para {down}MB/s? #meo #meofibra")

    elif uSpeed < up-threshold: # Compares the upload speed from the speedtest with the expected download speed passed as a function argument minus the threshold value.
        api.update_status(f'@MEOpt porque é que a minha velocidade de upload está a {uSpeed}MB/s quando tenho um contrato para {up}MB/s? #meo #meofibra')
        print(f"Mensagem enviada: @MEOpt porque é que a minha velocidade de upload está a {uSpeed}MB/s quando tenho um contrato para {up}MB/s? #meo #meofibra")

    else:
        pass

getSpeed()
