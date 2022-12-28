import requests, random, string
from colorama import Fore, init
init(convert=True)
URL = 'https://kahootbotter.com/api/graphql'
game = int(input(f"[ {Fore.LIGHTYELLOW_EX} ? {Fore.RESET} ] {Fore.LIGHTYELLOW_EX}Enter Game Pin: {Fore.RESET}"))
bots = int(input(f"\n[ {Fore.LIGHTYELLOW_EX} ? {Fore.RESET} ] {Fore.LIGHTYELLOW_EX}Ammount of Bots? (Max 50): {Fore.RESET}"))
if bots > 50:
    bots = 50
def send():
    try:
        user = random.choice(open('user.txt', 'r').read().splitlines())
        name = "".join(random.choices(string.ascii_letters, k=3))
        proxy = random.choice(open('proxies.txt', 'r').read().splitlines())
        proxies = {'http': f'http://{proxy}', 'http': f'http://{proxy}'}
        headers = {'authority': 'kahootbotter.com','accept': '*/*','accept-language'   : 'en-US,en;q=0.9','content-type': 'application/json','origin': 'https://kahootbotter.com','referer': 'https://kahootbotter.com/','user-agent': user,}
        print(user)
        json_data = {
            'operationName': 'spawnBots',
            'variables': {
                'botName': name,
                'gamePin': game,
                'botAmount': bots, #You can change the ammount to 50 max, modify it depending the rol
                'sessionId': '',
            },
            'query': 'mutation spawnBots($botName: String!, $gamePin: Int!, $botAmount: Int!, $sessionId: String!) {\n  spawnBots(\n    botName: $botName\n    gamePin: $gamePin\n    botAmount: $botAmount\n    sessionId: $sessionId\n  ) {\n    title\n    status\n    description\n    __typename\n  }\n}\n',
        }
        response = requests.post(URL, headers=headers, json=json_data, proxies=proxies)
        print(response.text)
        try:
            if response.json()['data']['spawnBots']['status'] == 'success':
                print(f"\n[ {Fore.LIGHTGREEN_EX} + {Fore.RESET} ] {Fore.LIGHTGREEN_EX}{bots} bots have been successfully sended{Fore.RESET}\n")
            else:
                print(f"\n[ {Fore.LIGHTRED_EX} - {Fore.RESET} ] {Fore.LIGHTRED_EX}Error Sending the bots!{Fore.RESET}\n")
        except:
            print(f"\n[ {Fore.LIGHTRED_EX} - {Fore.RESET} ] {Fore.LIGHTRED_EX}Error Sending the bots!, Probably you are being limited!{Fore.RESET}\n")
    except:
        print(f"\n[ {Fore.LIGHTRED_EX} - {Fore.RESET} ] {Fore.LIGHTRED_EX}Bad Kahoot Pin!{Fore.RESET}\n")
send()
input(f"{Fore.RESET}[ {Fore.LIGHTYELLOW_EX} ... {Fore.RESET} ] {Fore.LIGHTYELLOW_EX}Press Enter for Exit {Fore.RESET}")
