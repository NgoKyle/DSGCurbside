from discord_webhook import DiscordWebhook

def sendDiscord(message, buyType, sku, zipcode):
    #default error url
    if "curbside" in buyType:
        if sku in ('16380346', '11465449'): #adjustable
            print("adjustable")
            if zipcode in '97236': #pdx
                url = 'https://discordapp.com/api/webhooks/696488049336385586/TJvbPriFLk6tCX57sLqb_DEfU5nw1DxD_PSJ3LHaeqhDEu7NACN8EePLGNoZ2yx6NMFR'
            elif zipcode in '98101': #sea
                url = 'https://discordapp.com/api/webhooks/697145833908338839/yYcNa3Kp60ymQ8guITMJbC3Nw-Hj6d5v-_QaWMpvmPQQ7zO_a5R9jCLqeIRE9DIFTARS'
            elif zipcode in '99201': #spok
                url = 'https://discordapp.com/api/webhooks/697145930612474007/BuYoVBFTpBAkovHYyXgobnu2Y-iMdHJb7VEh11XOONAe2z_gnBiuD5NntFnGYEecgFlh'
            elif zipcode in '97701': #bend
                url = 'https://discordapp.com/api/webhooks/697146053409112266/1_QjYxznO04s4-M3A6oME8GYuHA8RscTj6IoilZm3zpCEwxWN-iZlro66RL4jobJJDxF'
            else: #other
                url = 'https://discordapp.com/api/webhooks/697209785308807200/N43rRgJLgO-BgXhue9WY3Bs5tFlJTE-m6SXnqjRJRHJ0Qp_xoC0l6h0H5enu3WkaY5rA'

        else:
            print("non-adjustable")
            url = 'https://discordapp.com/api/webhooks/696488119364747274/akRhi50mQwDDVBrydTNUMd-m-7V4JH1D6ZHUz5cP2Sdft30BH1oee23x1A7FowoxB_LU'
    else:
        url = 'https://discordapp.com/api/webhooks/697146323924811856/2POHtN42U2ouMp3loe4u704JwspP9vxwpPNdtFGlqpaLw8rSEmldq4f71gKTTU_wwrcP'

    webhook = DiscordWebhook(url=url,content=message)
    webhook.execute()
