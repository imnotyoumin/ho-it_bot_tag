# 📌 디스코드 봇 태그 기능 정리

## ✅ 주요 기능 요약
- `!tag #태그명` : 태그 등록
- `!tag-list` : 전체 태그 목록 출력
- `!tag-remove #태그명` : 특정 태그 삭제

---

## 💻 코드 예시

```python
import discord
import re
import os
from dotenv import load_dotenv

# env 파일 읽기
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

all_tags = []

@client.event
async def on_ready():
    print(f'✅ 봇이 로그인됨: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # 태그 등록
    if message.content.startswith('!tag') and not message.content.startswith('!tag-list') and not message.content.startswith('!tag-remove'):
        tags = re.findall(r'#\w+', message.content)
        all_tags.extend(tags)
        all_tags[:] = sorted(list(set(all_tags)))

        if tags:
            tag_text = ', '.join(tags)
            await message.channel.send(f"등록된 태그: {tag_text}")
        else:
            await message.channel.send("태그가 없습니다. 예시: '!tag #공부 #감성'")

    # 태그 리스트 출력
    if message.content == '!tag-list':
        if all_tags:
            await message.channel.send(f"현재 태그 목록: {', '.join(all_tags)}")
        else:
            await message.channel.send("등록된 태그가 없습니다.")

    # 태그 삭제
    if message.content.startswith('!tag-remove'):
        tags_remove = re.findall(r'#\w+', message.content)
        if tags_remove:
            removed = []
            for tag in tags_remove:
                if tag in all_tags:
                    all_tags.remove(tag)
                    removed.append(tag)
            if removed:
                await message.channel.send(f"삭제된 태그: {', '.join(removed)}")
            else:
                await message.channel.send("입력한 태그는 등록된 태그 목록에 없습니다.")
        else:
            await message.channel.send("삭제할 태그를 입력해주세요. 예시: '!tag-remove #감성'")
```

---

## 📚 배운 점 요약
- `re.findall(r'#\w+', message.content)` → 태그 추출
- `all_tags.extend()` → 태그 추가
- `list(set(all_tags))` → 중복 제거
- `sorted()` → 정렬
- `message.content.startswith()` → 명령어 분기 처리

---

## 🔜 다음 단계 추천
- `!tag-search` 기능 추가
- 함수 분리 리팩토링
- MySQL 연동 연습
