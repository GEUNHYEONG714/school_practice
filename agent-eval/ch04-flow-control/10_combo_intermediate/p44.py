"""
TITLE: 암호 해독 (시저 암호)
DIFFICULTY: hard
TAGS: string, cipher, while
EVAL: stdio

DESCRIPTION:
시저 암호를 구현하시오. 3개의 입력을 순서대로 받습니다.
1) 모드 (1: 인코딩, 2: 디코딩)
2) 이동 칸수 N
3) 문장

규칙:
- 소문자 a~z, 대문자 A~Z는 각각 N만큼 순환 이동
- 알파벳 외 문자는 그대로 유지
- 디코딩 모드는 반대 방향으로 이동

결과 출력: `결과: 변환결과` (콤마 뒤 공백 — `print("결과:", result)` 그대로)

예시:
- 입력: `1\\n3\\nHello World!` → `결과: Khoor Zruog!`
- 입력: `2\\n3\\nKhoor Zruog!` → `결과: Hello World!`
"""
# META_TESTS:
# - stdin: "1\n3\nHello World!"
#   expected_stdout: "결과: Khoor Zruog!"
# - stdin: "2\n3\nKhoor Zruog!"
#   expected_stdout: "결과: Hello World!"
# - stdin: "1\n1\nabcXYZ"
#   expected_stdout: "결과: bcdYZA"

# ord(), chr() 사용. 소문자/대문자/기타 분기 처리
mode = int(input())
shift = int(input())
text = input()
result = ""
# TODO
print("결과:", result)
