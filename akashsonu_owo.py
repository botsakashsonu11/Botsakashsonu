import requests
import time

header = {'authorization': 'MTAxODg1MzA2NjUxNjIyMjA2Mg.GBBlFq.JDdZisTxgmJZxJIGLxnNFNv_LT_AlUMxif4J2Y'}

def send_message(content):
    response = requests.post('https://discord.com/api/v9/channels/1171804189266022515/messages', data={'content': content}, headers=header)
    print(f"Message '{content}' {'sent successfully' if response.ok else f'failed with status code {response.status_code}'}")

intervals = {'oh': 15, 'ob': 25}
last_sent = {message: time.time() for message in intervals}

while True:
    for message, interval in intervals.items():
        if time.time() - last_sent[message] >= interval:
            send_message(message)
            last_sent[message] = time.time()
    time.sleep(1)
