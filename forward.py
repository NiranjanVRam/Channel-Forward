from telethon import TelegramClient
from telethon.errors import FloodWaitError
from tqdm import tqdm
import time

# Define your API ID, API Hash, and phone number
api_id = '1234567' # Replace this with your telegram API ID
api_hash = 'abcdefghijklmnopqrstuvwxyzABCDEF' # Replace this with your telegram API Hash
phone_number = '+001234567890' # Replace this with your phone number

# Define the source and target channels
source_channel_1 = -1001234567890 # Replace this with your own source channel id
source_channel_2 = -1001234567890 # Replace this with your own source channel id
target_channel = -1001234567890 # Replace this with your own target channel id

# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)

    # Ensure you're authorized
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        code = input('Enter the code: ')
        await client.sign_in(phone_number, code)

    # Function to forward messages from one source to target with progress bar
    async def forward_messages(source, target):
        total_messages = (await client.get_messages(source, limit=0)).total
        with tqdm(total=total_messages, desc=f'Forwarding from {source}', unit='msg') as pbar:
            async for message in client.iter_messages(source):
                if message.file:  # Only forward messages that contain files
                    while True:
                        try:
                            # Extract file name and size
                            file_name = message.file.name or "Unknown"
                            file_size = message.file.size / (1024 * 1024)  # Convert to MB
                            formatted_size = f"{file_size:.2f} MB"

                            # Set custom caption using Markdown
                            custom_caption = f"File: **{file_name}**\n\nFile Size: {formatted_size}" # Change caption as needed, if not needed, remove this line and line 48

                            # Send file with custom caption
                            await client.send_file(
                                target,
                                file=message.media,
                                caption=custom_caption,
                                parse_mode='markdown'
                            )
                            pbar.update(1)
                            break  # Break out of the retry loop after successful send
                        except FloodWaitError as e:
                            print(f'FloodWaitError: Waiting for {e.seconds} seconds')
                            time.sleep(e.seconds)

    # Forward messages from both source channels to the target channel
    await forward_messages(source_channel_1, target_channel)
    await forward_messages(source_channel_2, target_channel) # Add more source channels if needed

with client:
    client.loop.run_until_complete(main())
