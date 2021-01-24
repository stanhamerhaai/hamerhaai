from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatAdminRequiredError, ChatWriteForbiddenError
from time import sleep
from os import listdir
from datetime import datetime
from os.path import isfile, join
print(datetime.now().timestamp())


api_id = input("Enter api id: ")  # mm
api_hash = input("Enter api hash: ")# mm

print('Telegram Advertisement bot\n')
print("""
Make group_list.txt and put in all the groups you want to send messages to in format

@group1
@group2
@group3 etc
""")
phone = input('Enter your phone number: ')
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

time = int(input('Input interval in second: '))

onlyfiles = [f for f in listdir('.') if isfile(join('.', f))]


if ('group_list.txt') not in onlyfiles:
    with open('group_list.txt', 'w') as f:
        f.write('@group_usename')
        f.close()

message = """
Join the new 3k+ story mega!
@preaddhub3k

- experienced admins
- no more “host down”
- 700+ gains per round
- better/new type of DM bot 

Don’t miss out on these gains!
Join @preaddhub3k now!

@preaddhub3k 👈
"""


print('\nCheck group_list.txt if your formatted it correctly\nand be sure that correct message in '+str(phone)+f'.txt\nthe message is:  {message}\n\npress Enter to continue\nif not, change it and press Enter')
input()

print('Script started')
while True:
    with open('group_list.txt','r') as groups:
        for group in groups.readlines():
            try:
                client.send_message(group,message)
            except PeerFloodError as p:
                print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                print('sleep 120 second')
                sleep(120)
            except UserPrivacyRestrictedError:
                print("The user's privacy settings do not allow you to do this. Skipping.")

            except ChatWriteForbiddenError:
                try:
                    client(JoinChannelRequest(group))
                    client.send_message(group, message)
                    print('sleep 300 second after joining the group')
                    sleep(300)
                except:
                    pass
            except ChatAdminRequiredError:
                pass
            except ValueError:
                pass
            except:
                pass

    print("Succesfully send the message to all groups in @group_list.txt")
    sleep(time)
