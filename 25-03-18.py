import discord
import re

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ 봇이 로그인됨: {client.user}')

@client.event
async def on_message(message):
    # 봇 자신이 보낸 메시지는 무시
    if message.author == client.user:
        return

    if message.content.startswith('!tag'):
        # 해시태그 추출(정규표현식 사용)
        tags = re.findall(r'#\w+', message.content)

        if tags:
            tag_text = ', '.join(tags)
            await message.channel.send(f"등록된 태그: {tag_text}")
        else:
            await message.channel.send("!태그가 없습니다. 입력 예시: '!tag #공부 #감성'")

# 여기에 팀원에게 받은 토큰 입력
client.run("MTM0OTIwMjQ5NDA4NTAwOTU0Mg.G9QFTZ.HPptPkK4PLEZD7anBqAYbevdLITT5Ju_Baf45Y")
