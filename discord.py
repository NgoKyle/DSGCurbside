from discord_webhook import DiscordWebhook

def sendDiscord(message, condition):
    if "curbside1" in condition:
        webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/696488049336385586/TJvbPriFLk6tCX57sLqb_DEfU5nw1DxD_PSJ3LHaeqhDEu7NACN8EePLGNoZ2yx6NMFR',
        content=message)
        response = webhook.execute()
    elif "curbside2" in condition:
        webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/696488119364747274/akRhi50mQwDDVBrydTNUMd-m-7V4JH1D6ZHUz5cP2Sdft30BH1oee23x1A7FowoxB_LU',
        content=message)
        response = webhook.execute()
    elif "curbside3" in condition:
        webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/696488195931766987/JD4MAz0AxOMVIwovTEo_DqRWPD4LmJ6MzZf0N_H_CgclD6mx7hAaXXqSPvLGcYgeJe5j',
        content=message)
        response = webhook.execute()
    elif "curbsidelogs" in condition:
        webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/696488338147770458/SNN59lKn8TOUDAnizmn0yIdvQPXCyFBNObKMvHKQanoPu68lhwxAcRmSesNlP1qeHeM2',
        content=message)
        response = webhook.execute()
