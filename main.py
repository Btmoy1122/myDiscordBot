from typing import Final
import os
from asyncio import sleep
from dotenv import load_dotenv
from discord import Intents, Message, Member
from discord.ext import commands
from responses import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

#BOT SETUP
intents = Intents.default()
intents.message_content = True #NOQA
bot = commands.Bot(command_prefix = "/", intents = intents)

#MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message was empty because intents were not enabled probably")
        return

    is_private = user_message[0] == "?"

    if is_private:
        user_message = user_message[1:]

    try:
        response = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

#HANDLING STARTUP FOR BOT
@bot.event
async def on_ready() -> None:
    print(f"{bot.user} is now running")

#HANDLING INCOME MESSAGES
@bot.event
async def on_message(message: Message) -> None:
    if message.author == bot.user:
        return

    username:str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f"[{channel}] {username}: {user_message}")

    if user_message.lower() in ["terminate", "turn off"]:
        await message.channel.send("Kurtis going down...")
        await bot.close()

    await send_message(message, user_message)

    #Makes sure other commands are processed after the message
    await bot.process_commands(message)

#HANDLING NEW MEMBERS
@bot.event
async def on_member_join(member: Member):
    await member.send(f"Welcome {member.name}! I am Kurtis: a bot here for fun!")

#REMINDER SYSTEM
@bot.command(name="remindme",help="Set a reminder. Example: /remindme 5 'Take a break!'")
async def remindme(ctx, time: str, *, reminder: str)-> None:
    seconds = float(time)*60
    await ctx.send(f"Okay, reminding you in {time} minutes to {reminder}")

    await sleep(seconds)

    await ctx.send(f"{ctx.author.mention}, reminder: {reminder}")

#MAIN ENTRY POINT
def main() -> None:
    bot.run(TOKEN)

if __name__ == "__main__":
    main()