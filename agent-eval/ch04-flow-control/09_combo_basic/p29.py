"""
TITLE: FizzBuzz
DIFFICULTY: medium
TAGS: for, if, elif, modulo

DESCRIPTION:
1부터 50까지 출력하되 3의 배수이면 `Fizz`, 5의 배수이면 `Buzz`,
3과 5의 공배수(15의 배수)이면 `FizzBuzz`, 나머지는 숫자를 그대로 출력하시오.

예시:
- 출력: `1`, `2`, `Fizz`, `4`, `Buzz`, `Fizz`, ... `FizzBuzz` (15), ...
"""
# META_TESTS:
# - stdin: ""
#   expected_stdout: "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz"

# 15의 배수를 먼저 검사해야 함
# TODO
