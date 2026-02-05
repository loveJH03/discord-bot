import discord
from discord import app_commands

TOKEN = "봇토큰여기"

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync()
    print("봇 온라인!")


@tree.command(name="embed", description="임베드 전송")
@app_commands.describe(
    title="제목",
    description="내용 (줄바꿈은 \\n)",
    image="이미지 URL (선택)"
)
async def embed(interaction: discord.Interaction, title: str, description: str, image: str = ""):

    description = description.replace("\\n", "\n")

    em = discord.Embed(
        title=title,
        description=description,
        color=0x2B2D31
    )

    if image:
        em.set_image(url=image)

    await interaction.response.send_message(embed=em)


client.run(TOKEN)
