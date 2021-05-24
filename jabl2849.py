import requests
import sys
payload = {'Username': 'jabl28', 'Password': 'd4e5f6g7','a':'Login','key':'2b3a92904acc4342809d2be42a2e739c'};
url="https://www.999dice.com/api/web.aspx";
r = requests.post(url, data=payload)
data1=r.json()
print (data1)
cookie=data1['SessionCookie']
basebet=1
loss=0
lossa=0
i=0
j=0
k=0
l=0
m=0
n=0
def dobetlow(basebet,currency) :
    payloadbet={'s':cookie,'a':'PlaceAutomatedBets','BasePayIn':basebet,'Low':'0','High':'499499','MaxBets':'5','ResetOnWin':'true','ResetOnLose':'false',
    'IncreaseOnWinPercent':'0','IncreaseOnLosePercent':'1','MaxPayIn':basebet*100,'ResetOnLosebasebet':'true','StopOnLosebasebet':'false','StopMaxBalance':'1000000000000000',
    'Compact':'true','ClientSeed':'4d53feterddaviaiban54324vf','Currency':currency,'ProtocolVersion':'2'}
    requests.post(url, data=payloadbet)
def dobethigh(basebet,currency) :
    payloadbet={'s':cookie,'a':'PlaceAutomatedBets','BasePayIn':basebet,'Low':'500500','High':'999999','MaxBets':'5','ResetOnWin':'true','ResetOnLose':'false',
    'IncreaseOnWinPercent':'0','IncreaseOnLosePercent':'1','MaxPayIn':basebet*100,'ResetOnLosebasebet':'true','StopOnLosebasebet':'false','StopMaxBalance':'1000000000000000',
    'Compact':'true','ClientSeed':'4d53feterddaviaiban54324vf','Currency':currency,'ProtocolVersion':'2'}
    requests.post(url, data=payloadbet) 
while i<99999 :
    basebet=1
    dobethigh(basebet,"ltc");
    basebet=3
    dobetlow(basebet,"ltc");
    basebet=1
    dobetlow(basebet,"eth");
    basebet=5000
    dobetlow(basebet,"doge");
    basebet=4
    dobethigh(basebet,"eth");
    basebet=1
    dobetlow(basebet,"btc");
    dobethigh(basebet,"btc");
    basebet=2
    dobethigh(basebet,"ltc");
    basebet=4000
    dobetlow(basebet,"doge");
    basebet=4
    dobetlow(basebet,"ltc");
    basebet=2000
    dobethigh(basebet,"doge");
    basebet=3
    dobetlow(basebet,"eth");
    basebet=2
    dobethigh(basebet,"eth");
    basebet=3000
    dobetlow(basebet,"doge");
    i+=1
  