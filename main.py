import customtkinter as ctk
import discord
import asyncio
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class DiscordGUI:

    def __init__(self):

        self.app = ctk.CTk()
        self.app.geometry("600x620")
        self.app.title("디스코드 임베드 전송기")

        ctk.CTkLabel(self.app, text="봇 토큰").pack(pady=5)
        self.token = ctk.CTkEntry(self.app, width=500)
        self.token.pack()

        ctk.CTkLabel(self.app, text="채널 ID").pack(pady=5)
        self.channel = ctk.CTkEntry(self.app, width=500)
        self.channel.pack()

        ctk.CTkLabel(self.app, text="임베드 제목").pack(pady=5)
        self.title = ctk.CTkEntry(self.app, width=500)
        self.title.pack()

        ctk.CTkLabel(self.app, text="내용").pack(pady=5)
        self.content = ctk.CTkTextbox(self.app, width=500, height=170)
        self.content.pack()

        ctk.CTkLabel(self.app, text="이미지 URL").pack(pady=5)
        self.image_url = ctk.CTkEntry(self.app, width=500)
        self.image_url.pack()

        ctk.CTkButton(self.app, text="임베드 전송", command=self.send).pack(pady=15)

        self.app.mainloop()

    def send(self):
        token = self.token.get()
        channel_id = int(self.channel.get())
        title = self.title.get()
        desc = self.content.get("1.0", "end")
        image = self.image_url.get()

        threading.Thread(
            target=lambda: asyncio.run(self.bot(token, channel_id, title, desc, image))
        ).start()

    async def bot(self, token, channel_id, title, desc, image):
        intents = discord.Intents.default()
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            channel = client.get_channel(channel_id)

            embed = discord.Embed(
                title=title,
                description=desc,
                color=0x2B2D31
            )

            if image.strip():
                embed.set_image(url=image)

            await channel.send(embed=embed)
            await client.close()

        await client.start(token)


DiscordGUI()
