#!/usr/bin/env python3
import re

with open('posts/Quiz2.qmd', 'r', encoding='utf-8') as f:
    content = f.read()

# 패턴 1: <details>로 시작하는 짧은 답안 (①②③④ 등)
pattern1 = r'<details>\s*\n<summary>답안 보기</summary>\s*\n([①②③④])\s*\n</details>'
replacement1 = r'::: {.callout-note collapse="true"}\n## 답안\n\n\1\n:::'

# 패턴 2: <details>로 시작하는 O/X 답안
pattern2 = r'<details>\s*\n<summary>답안 보기</summary>\s*\n(\*\*[OX]\*\*[^\n]+)\s*\n</details>'
replacement2 = r'::: {.callout-note collapse="true"}\n## 답안\n\n\1\n:::'

# 패턴 3: 구분선이 있는 답안
pattern3 = r'<details>\s*\n<summary>답안 보기</summary>\s*\n\n---\n\n(.+?)\n\n---\n\n</details>'
replacement3 = r'::: {.callout-note collapse="true"}\n## 답안\n\n\1\n:::'

content = re.sub(pattern3, replacement3, content, flags=re.DOTALL)
content = re.sub(pattern1, replacement1, content)
content = re.sub(pattern2, replacement2, content)

with open('posts/Quiz2.qmd', 'w', encoding='utf-8') as f:
    f.write(content)

print("Quiz2 converted to Quarto callout format!")
