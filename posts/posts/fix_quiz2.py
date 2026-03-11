#!/usr/bin/env python3
import re

with open('Quiz2.qmd', 'r', encoding='utf-8') as f:
    content = f.read()

# 짧은 답안(한 줄)에 구분선 추가하는 패턴
# 패턴 1: 단일 문자 답안 (①, ②, ③, ④)
pattern1 = r'(<details>\n<summary>답안 보기</summary>\n)([①②③④])\n(</details>)'
replacement1 = r'\1\n---\n\n\2\n\n---\n\n\3'

# 패턴 2: O/X 답안
pattern2 = r'(<details>\n<summary>답안 보기</summary>\n)(\*\*[OX]\*\*[^\n]+)\n(</details>)'
replacement2 = r'\1\n---\n\n\2\n\n---\n\n\3'

content = re.sub(pattern1, replacement1, content)
content = re.sub(pattern2, replacement2, content)

with open('Quiz2.qmd', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
