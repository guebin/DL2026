#!/bin/bash
# Quiz2의 모든 짧은 답안에 구분선 추가

perl -i -pe 's{(<details>\n<summary>답안 보기</summary>\n)(②|③|①|④)(\n</details>)}{$1\n---\n\n$2\n\n---\n$3}g' Quiz2.qmd
perl -i -pe 's{(<details>\n<summary>답안 보기</summary>\n)(\*\*[OX]\*\*[^\n]+)(\n</details>)}{$1\n---\n\n$2\n\n---\n$3}g' Quiz2.qmd
