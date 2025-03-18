import discord
import re

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

user_tags = {}

@client.event
async def on_ready():
    print(f'✅ 봇이 로그인됨: {client.user}')

@client.event
async def on_message(message):
    # 봇 자신이 보낸 메시지는 무시
    if message.author == client.user:
        return

        # 태그 등록 코드
    if message.content.startswith('!tag') and not message.content.startswith('!tag-list'):
        # 1. 해시태그 추출(정규표현식 사용)
        tags = re.findall(r'#\w+', message.content)

        # 2. 저장 (user ID 기준, user ID에 따라 딕셔너리를 계속 만듬)
        user_id = str(message.author.id)
        if user_id not in user_tags:
            user_tags[user_id] = []
        user_tags[user_id].extend(tags) # 새로운 태그 추가
        user_tags[user_id] = sorted(list(set(user_tags[user_id]))) # 중복 제거 & 정렬

        # 3. 출력
        if tags:
            tag_text = ', '.join(tags)
            await message.channel.send(f"등록된 태그: {tag_text}")
        else:
            await message.channel.send("!태그가 없습니다. 입력 예시: '!tag #공부 #감성'")

    # 태그 리스트 코드
    if message.content.startswith('!tag-list'):
        if message.mentions: # 멘션한 사람의 태그를 확인할 수 있는 기능
            target_user = message.mentions[0]
            target_id = str(target_user.id)
        else:
            target_id = str(message.author.id)
            
        if target_id in user_tags and user_tags[target_id]:
            tag_list = ', '.join(user_tags[target_id])
            await message.channel.send(f"{target_user.name if message.mentions else message.author.name}님의 태그 목록: {tag_list}")
        else:
            await message.channel.send("등록된 태그가 없습니다. '!tag #감성 #공부' 처럼 먼저 태그를 등록해주세요.")
    

# 여기에 팀원에게 받은 토큰 입력
client.run("토큰 입력")
