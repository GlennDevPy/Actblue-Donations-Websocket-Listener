from websocket import create_connection
import re
headers = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "Upgrade",
    "Host": "ws.pusherapp.com",
    "Origin": "https://secure.actblue.com",
    "Pragma": "no-cache",
    "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
    "Sec-WebSocket-Key": "Xt9puSvzfNGfeCqksd5/sg==",
    "Sec-WebSocket-Version": "13",
    "Upgrade": "websocket",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}


ws = create_connection('wss://ws.pusherapp.com/app/449985a46708136f3d74?protocol=7&client=js&version=4.4.0&flash=false',headers=headers)
ws.send(json.dumps({"event":"pusher:subscribe","data":{"channel":"indigo_production"}}))
while True:
    result = ws.recv()
    if "new_contribution" in str(result):
        newcontrib = re.search("\"new_contribution\",\"data\":\"{\\\\\"amount\\\\\":(.*?)\,", str(result))[1]
        total = re.search('total\\\\\":(.*?)\,', str(result))[1]
        timestamp = re.search('time\\\\\":\\\\\"(.*?)\\\\', str(result))[1]
        print(f"New Bundle Donated Through Actblue | Amount: ${newcontrib} | Total Donated: ${total} | Timestamp: {timestamp}")
