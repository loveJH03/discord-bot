import discord
from discord import app_commands
import os
from datetime import timezone

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync()
    print(f"{client.user} 온라인!")


# ================= EMBED =================

@tree.command(name="임베드", description="임베드 메시지 보내기")
@app_commands.describe(
    제목="임베드 제목",
    내용="임베드 내용",
    이미지="이미지 URL (선택)"
)
async def embed(
    interaction: discord.Interaction,
    제목: str,
    내용: str,
    이미지: str = None
):

    e = discord.Embed(
        title=제목,
        description=내용,
        color=0x2B2D31
    )

    if 이미지:
        e.set_image(url=이미지)

    await interaction.response.send_message(embed=e)


# ================= USER CHECK =================

@tree.command(name="확인", description="유저 정보 확인")
@app_commands.describe(user="확인할 유저")
async def check(interaction: discord.Interaction, user: discord.User):

    created = user.created_at.astimezone(timezone.utc)

    text = (
        f"👤 닉네임: {user}\n"
        f"🆔 아이디: {user.id}\n"
        f"📅 계정 생성일: {created.strftime('%Y-%m-%d %H:%M:%S UTC')}"
    )

    await interaction.response.send_message(text)


client.run(TOKEN)
