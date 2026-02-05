import discord
from discord import app_commands
import aiohttp

TOKEN = "여기에 네 봇토큰"

class Bot(discord.Client):

    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("슬래쉬 동기화 완료")

bot = Bot()

@bot.event
async def on_ready():
    print("봇 온라인")

# ================= EMBED =================

@bot.tree.command(name="임베드")
async def embed(interaction: discord.Interaction, 제목: str, 내용: str, 이미지: str = None):

    em = discord.Embed(title=제목, description=내용, color=0x2B2D31)

    if 이미지:
        em.set_image(url=이미지)

    await interaction.response.send_message(embed=em, ephemeral=True)

# ================= USER CHECK =================

@bot.tree.command(name="확인")
async def 확인(interaction: discord.Interaction, 유저: discord.User):

    created = 유저.created_at.strftime("%Y-%m-%d %H:%M")

    em = discord.Embed(title="유저 정보", color=0x2B2D31)

    em.add_field(name="닉네임", value=유저.name)
    em.add_field(name="ID", value=str(유저.id))
    em.add_field(name="계정 생성일", value=created)
    em.set_thumbnail(url=유저.avatar.url)

    await interaction.response.send_message(embed=em, ephemeral=True)

# ================= EXECUTOR =================

@bot.tree.command(name="실행기정보")
async def 실행기정보(interaction: discord.Interaction, 이름: str):

    async with aiohttp.ClientSession() as session:
        async with session.get("https://weao.xyz/api/executors") as resp:
            data = await resp.json()

    found = None

    for exe in data:
        if 이름.lower() in exe["title"].lower():
            found = exe
            break

    if not found:
        await interaction.response.send_message("못찾음", ephemeral=True)
        return

    em = discord.Embed(title=found["title"], color=0x2B2D31)

    em.add_field(name="버전", value=str(found["version"]))
    em.add_field(name="감지됨", value=str(found["detected"]))
    em.add_field(name="무료", value=str(found["free"]))
    em.add_field(name="플랫폼", value=found["platform"], inline=False)

    em.add_field(name="웹사이트", value=found["websitelink"], inline=False)
    em.add_field(name="디스코드", value=found["discordlink"], inline=False)
    em.add_field(name="구매", value=found["purchaselink"], inline=False)

    await interaction.response.send_message(embed=em, ephemeral=True)

bot.run(MTQ2NzQzNzM1MzUwNDM0NjIzNA.Gr1jT_.Fy_9aVo16QqSjQpQRayAJA1I2PIUNUwCkXZlD4)


