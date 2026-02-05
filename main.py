import discord
from discord.ext import commands
from discord import Option
import requests
import datetime

TOKEN = "여기에_봇토큰"

intents = discord.Intents.default()
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print("봇 온라인")
    await bot.sync_commands()

# ================= EMBED =================

@bot.slash_command(name="임베드")
async def embed(
    ctx,
    제목: Option(str),
    내용: Option(str),
    이미지: Option(str, required=False)
):

    embed = discord.Embed(title=제목, description=내용, color=0x2B2D31)

    if 이미지:
        embed.set_image(url=이미지)

    await ctx.respond(embed=embed, ephemeral=True)

# ================= USER INFO =================

@bot.slash_command(name="확인")
async def 확인(ctx, 유저: Option(discord.User)):

    created = 유저.created_at.strftime("%Y-%m-%d %H:%M")

    embed = discord.Embed(title="유저 정보", color=0x2B2D31)
    embed.add_field(name="닉네임", value=유저.name)
    embed.add_field(name="ID", value=유저.id)
    embed.add_field(name="계정 생성일", value=created)
    embed.set_thumbnail(url=유저.avatar.url)

    await ctx.respond(embed=embed, ephemeral=True)

# ================= EXECUTOR INFO =================

@bot.slash_command(name="실행기정보")
async def 실행기정보(ctx, 이름: Option(str)):

    url = "https://weao.xyz/api/executors"

    data = requests.get(url).json()

    found = None

    for exe in data:
        if 이름.lower() in exe["title"].lower():
            found = exe
            break

    if not found:
        await ctx.respond("못찾음", ephemeral=True)
        return

    embed = discord.Embed(title=found["title"], color=0x2B2D31)

    embed.add_field(name="버전", value=found["version"])
    embed.add_field(name="감지됨", value=str(found["detected"]))
    embed.add_field(name="무료", value=str(found["free"]))
    embed.add_field(name="업데이트 상태", value=str(found["updateStatus"]))
    embed.add_field(name="플랫폼", value=found["platform"], inline=False)

    embed.add_field(name="웹사이트", value=found["websitelink"], inline=False)
    embed.add_field(name="디스코드", value=found["discordlink"], inline=False)
    embed.add_field(name="구매", value=found["purchaselink"], inline=False)

    await ctx.respond(embed=embed, ephemeral=True)

bot.run(TOKEN)
