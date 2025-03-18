# 디스코드 플레이리스트 봇 - 태그 기능 정리

## ✅ 목표
- 사용자의 `!tag #태그` 메시지를 감지하여 태그를 추출하고 출력하는 기능 구현

## 💻 코드 예시

```python
import re

message = "!tag #공부 #감성"
tags = re.findall(r'#\w+', message)

if tags:
    tag_text = ', '.join(tags)
    print(f"등록된 태그: {tag_text}")
else:
    print("태그가 없습니다.")
```

## 📌 배운 점
- 디스코드 봇 이벤트 감지 구조 (`on_message`)
- `startswith()`를 사용해 명령어 감지
- `re.findall()`로 정규표현식 태그 추출
- 추출된 태그 리스트를 문자열로 변환하여 출력

## 📂 앞으로 해볼 것
- 태그를 메모리에 저장해보기 (딕셔너리 등)
- 사용자별 태그 관리
- MySQL 연동 연습
