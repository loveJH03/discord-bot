import discord
from discord import app_commands
import os

TOKEN = os.getenv("TOKEN")

class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("슬래쉬 명령어 동기화 완료")

client = MyClient()

@client.event
async def on_ready():
    print(f"{client.user} 온라인!")

# ===== 슬래쉬 명령어 =====
@client.tree.command(name="embed", description="임베드 전송")
@app_commands.describe(
    title="제목",
    content="내용",
    image="이미지 URL (선택)"
)
async def embed(
    interaction: discord.Interaction,
    title: str,
    content: str,
    image: str = ""
):

    em = discord.Embed(
        title=title,
        description=content,
        color=0x2B2D31
    )

    if image:
        em.set_image(url=image)

    await interaction.response.send_message(embed=em)

client.run(TOKEN)
