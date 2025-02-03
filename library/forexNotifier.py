from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon.tl.functions.messages import SendMessageRequest
from telethon import TelegramClient
import pandas as pd
import os


def message_curr_strength(fname: str):
    """Send message containing the currency strength meter bars and datetime

    Args:
        fname (str): Filename of output currency strength meter image
    """
    api_id = os.getenv('TELEGRAM_API_ID')
    api_hash = os.getenv('TELEGRAM_API_HASH')
    # token = os.getenv('TELEGRAM_TOKEN')
    phone_num = os.getenv('MY_PHONE_NUMBER')

    client = TelegramClient('session_name', api_id, api_hash)

    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(phone_num)
        client.sign_in(phone_num, input('Enter the code: '))

    destination_group = os.getenv('TELEGRAM_JOINCHAT_LINK')
    peer = client.get_entity(destination_group)

    time = pd.to_datetime('now').strftime('%Y-%m-%d %H:%M')

    client.send_message(entity=peer, message='Currency Strength Bar {}'.format(time), parse_mode='html')
    client.send_file(entity=peer, file=fname)

    strength_values = ''
    with open('currStrengthOutputs/currStrengthValues.txt', 'r') as f:
        for line in f:
            strength_values += line

    tradable_pairs = ''
    with open('currStrengthOutputs/tradeableCurrPair.txt', 'r') as f:
        for line in f:
            tradable_pairs += line

    client.send_message(entity=peer, message='Currency Strength Values', parse_mode='html')
    client.send_message(entity=peer, message=strength_values, parse_mode='html')

    client.send_message(entity=peer, message='Tradable Pairs and Difference', parse_mode='html')
    client.send_message(entity=peer, message=tradable_pairs, parse_mode='html')

    client.disconnect()
