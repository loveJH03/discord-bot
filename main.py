import discord
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("봇 온라인!")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith("!embed"):
        parts = message.content.split("|")

        if len(parts) < 3:
            await message.channel.send("사용법:\n!embed 제목 | 내용 | 이미지URL(선택)")
            return

        title = parts[0].replace("!embed", "").strip()
        desc = parts[1].strip()
        image = parts[2].strip() if len(parts) >= 3 else ""

        embed = discord.Embed(title=title, description=desc, color=0x2B2D31)

        if image:
            embed.set_image(url=image)

        await message.channel.send(embed=embed)

client.run(TOKEN)
