import os
from telethon.tl.types import PeerChat, PeerChannel
from telethon.sync import TelegramClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up your API credentials
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

# Set up the session and connect to Telegram
with TelegramClient('get_members', api_id, api_hash) as client:
    # Get the members from the source group
    source_group = "overpipster"
    # target_group = 'TARGET_GROUP_USERNAME'

    source_entity = client.get_entity(source_group)
    # target_entity = client.get_entity(target_group)

    # Get all the members from the source group
    members = [{'id': user.id, 'first name': user.first_name, 'username': user.username, 'Phone_number': user.phone, 'bot': user.bot}
               for user in client.get_participants(source_entity)]

    for member in members:
        print(member["first name"], member['username'], member['Phone_number'])


    # # Add each member to the target group
    # for member in members:
    #     try:
    #         client(InviteToChannelRequest(target_entity, [member]))
    #         print(f"Added {member.username} to {target_group}")
    #     except Exception as e:
    #         print(f"Failed to add {member.username} to {target_group}: {str(e)}")
