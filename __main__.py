import requests
import random
import datetime

url = "https://api.telegram.org/bot577041906:AAGmb5FZ2rIQgpQOLfO59pf2aqAVc1mNn5A/"

def get_updates_json(request):  
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()


def last_update(data):  

    results = data['result']

    total_updates = len(results) - 1

    return results[total_updates]
    
def get_chat_id(update):  

    chat_id = update['message']['chat']['id']

    return chat_id



def send_mess(chat, text):  

    params = {'chat_id': chat, 'text': text}

    response = requests.post(url + 'sendMessage', data=params)

    return response
def comand(com):
	h1 = com['message']['text']
	return h1
	
update_id = last_update(get_updates_json(url))['update_id']

while True:
	while update_id == last_update(get_updates_json(url))['update_id']:
		chat_id = get_chat_id(last_update(get_updates_json(url)))

		h1 = comand(last_update(get_updates_json(url)))
		if h1 == '/start':
			send_mess(chat_id, 'Приветствую нига! \n Чтобы узнать список команд тапни на /help')
		if h1 == '/joke':
			jokes = ['шутка 1', 'шутка 2', 'шутка 3']
			for i in range(1):
				rj = random.randint(0, 2)
			joke = jokes[rj]
			send_mess(chat_id, joke)
		if h1 == '/time':
			now = str(datetime.datetime.now())
			send_mess(chat_id, 'Дата и время: ' + now)
		if h1 == '/help':
			send_mess(chat_id, 'Вот список всех команд, доступных на данный момент: \n /joke - Рандомная шутка \n /time - Чтобы узнать дату и время')
		update_id += 1

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()