#print('hello world')


import currencyapicom
client = currencyapicom.Client('cur_live_JF472CRTkrMySu5Osv36eAuOJD2WLAn1AZ0p2EUO')

def currency():
    return(client.status())

currency()