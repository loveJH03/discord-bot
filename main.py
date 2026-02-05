import discord
from discord import app_commands
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")  # 호스팅 Variables에 TOKEN 넣어둔 상태

intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()
        print("슬래시 명령어 동기화 완료")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"{bot.user} 온라인!")

# /embed 명령어
@bot.tree.command(name="embed", description="임베드 메시지 만들기")
@app_commands.describe(
    title="제목",
    description="내용",
    image="이미지 URL (선택)"
)
async def embed(
    interaction: discord.Interaction,
    title: str,
    description: str,
    image: str = None
):
    em = discord.Embed(title=title, description=description, color=0x2B2D31)

    if image:
        em.set_image(url=image)

    await interaction.response.send_message(embed=em)

bot.run(TOKEN)
