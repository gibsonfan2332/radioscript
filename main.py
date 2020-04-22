print("Goodbye, World!")
import requests
import time

timeout = time.time() + 60*1   # 10 seconds


stream_url = 'https://ice64.securenetsystems.net/KSRV?playSessionID=5B5F0B31-F100-10F7-7DB620B99DDEE047'

r = requests.get(stream_url, stream=True)

with open('stream.mp3', 'wb') as f:
    try:
        for block in r.iter_content(1024):
            if time.time() > timeout:
                break
            f.write(block)
    except KeyboardInterrupt:
        pass