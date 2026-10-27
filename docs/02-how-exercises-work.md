# 연습 문제 진행 방법

**첫 연습 문제를 풀기 전**(1주차 1일차)에 이 안내를 읽으세요. 연습 문제가 함수로 바뀌는 3일차 전에는 4부를 다시 읽으세요.

화면에 실제로 보이는 예제를 통해 전체 과정을 단계별로 안내합니다.
명령을 입력하기 전에 [어디에 입력합니까?](01-how-to-study.md#어디에-입력합니까)를 확인하세요.

---

## 1부: 연습 문제란 무엇입니까?

모든 연습 문제에는 **파일 두 개**가 있습니다.

| 파일 | 예 | 역할 | 수정합니까? |
|---|---|---|---|
| **연습 문제 파일** | [`exercises/week1/w1d3_conditions.py`](../exercises/week1/w1d3_conditions.py) | 맨 위에 안내가 있고, 코드를 작성할 곳에 `TODO`가 있습니다 | ✅ **네**, 직접 작성하는 파일입니다 |
| **테스트 파일** | [`exercises/week1/tests/test_w1d3.py`](../exercises/week1/tests/test_w1d3.py) | 연습 문제 파일을 자동으로 확인하는 프로그램입니다 | ❌ **절대 수정하지 마세요** |

파일 이름을 보면 어느 수업의 연습 문제인지 알 수 있습니다.

```
w1d3_conditions.py
│ │  └── 주제
│ └───── 3일차
└─────── 1주차
```

`w1d3_...`에 해당하는 테스트 파일은 항상 `tests/test_w1d3.py`입니다.

### 테스트가 하는 일

테스트는 결과물을 확인하는 로봇과 같습니다. 다음 일을 합니다.

1. 코드를 실행합니다. 입력을 받는 연습 문제는 **다양한 입력값**으로 실행합니다.
2. 결과를 **정답**과 비교합니다.
3. **통과** ✅ 또는 **실패** ❌를 알려 주고, 실패했다면 **무엇이 잘못됐는지** 알려 줍니다.

**해당 연습 문제의 테스트가 모두 통과하면** 연습 문제를 마친 것입니다.

---

## 2부: 매번 따라 하는 8단계

**모든** 연습 문제를 다음 순서대로 진행하세요.

**1단계: VS Code 편집기에서 연습 문제 파일을 여세요.**
VS Code 왼쪽 파일 목록에서 [`exercises`](../exercises/) → [`week1`](../exercises/week1/) → 파일(예: [`w1d1_hello.py`](../exercises/week1/w1d1_hello.py))을 클릭하세요. 또는 **Ctrl + P**를 누르고 파일 이름을 입력한 뒤 Enter를 누르세요. 편집기에서 파일을 열어야 코드를 작성할 수 있습니다.

**2단계: VS Code 편집기에서 연습 문제 파일(예: `w1d1_hello.py`) 맨 위의 안내를 모두 읽으세요.**
`#`으로 시작하는 줄(또는 함수 안의 `"""` 사이에 있는 글)에서 다음 내용을 알려 줍니다.
- 프로그램이 해야 할 일
- 출력하거나 반환해야 할 **정확한** 문구
- 하나 이상의 **예제**
- 무엇을 사용하면 좋을지 알려 주는 **힌트**

파일의 안내를 두 번 읽으세요. 대부분의 실수는 너무 빨리 읽어서 생깁니다.

**3단계: VS Code 편집기에서 연습 문제 파일(예: `w1d1_hello.py`)의 `TODO` 위치에 코드를 작성하세요.**
- **스크립트** 연습 문제(1–2일차): `# TODO: 이 줄 아래에 코드를 작성하세요` 아래에 작성하세요.
- **함수** 연습 문제(3–5일차): `pass`를 코드로 바꾸세요. `def ...` 줄은 **그대로** 두세요.

**4단계: VS Code 편집기에서 Ctrl + S로 연습 문제 파일(예: `w1d1_hello.py`)을 저장하세요.** 파일 탭의 흰 점 ●는 **저장하지 않았다**는 뜻입니다. 테스트는 항상 **저장된** 파일을 확인합니다.

**5단계: VS Code 터미널에서 저장한 연습 문제 파일(예: `w1d1_hello.py`)을 실행하세요.** 수업의 번호가 붙은 진행 순서에 나온 명령을 사용하세요.
스크립트는 `python3` 명령으로 실행하세요. 프로그램이 입력을 요청하면 예제 입력값을 입력하세요.
함수는 `python3 -i` 명령으로 실행하세요. 같은 VS Code 터미널 안의 **파이썬 `>>>` 프롬프트**에 불러온 연습 문제 파일의 함수 호출을 입력하세요.

결과를 수업 내용과 비교하세요. `>>>`가 보이면 `exit()`을 입력해서 VS Code 터미널로 돌아오세요. 스크립트가 끝나고 터미널 프롬프트가 다시 나타났다면 바로 다음 명령을 입력하면 됩니다.
3부와 4부에 예제가 있습니다.

**6단계: VS Code 터미널에서 연습 문제 파일(예: `w1d1_hello.py`)의 테스트를 실행하세요.** 수업의 해당 연습 문제에 나온 `pytest` 명령을 입력하세요.
이 명령에는 `-k`가 붙어 있어서 **지금 푸는 문제의 테스트만** 실행합니다. 예를 들어 다음 명령은 [`exercises/week1/tests/test_w1d1.py`](../exercises/week1/tests/test_w1d1.py)에서 `w1d1_hello.py`의 테스트만 실행합니다.
문제를 풀었다면 `1 passed, 1 deselected`가 나와야 합니다.

```bash
pytest exercises/week1/tests/test_w1d1.py -k hello
```

`-k`가 없는 하루 전체 명령(`pytest exercises/week1/tests/test_w1d1.py`)은 그날의 연습 문제를 **모두** 푼 뒤 수업 끝의 "마지막으로" 단계에서 실행하세요. 그 전에 실행하면 아직 풀지 않은 문제 때문에 `failed`가 나옵니다.

**7단계: 테스트가 실패하면 VS Code 터미널에 나온 오류 메시지를 읽으세요.**
VS Code 편집기에서 메시지에 나온 연습 문제 파일을 고치고 4단계로 돌아가세요.
5부에서 메시지를 설명합니다. 지금 푸는 문제의 테스트가 모두 통과할 때까지 반복하세요.

**8단계: VS Code 터미널에서 연습 문제 파일(예: `w1d1_hello.py`)을 GitHub에 저장하세요.** 다음 명령을 순서대로 입력하세요.
`git push` 후에 브라우저에서 포크의 **Code** 탭을 여세요. 저장한 변경 사항이 보여야 합니다.

```bash
git add .
git commit -m "Week 1 Day 1: hello exercise"
git push
```

---

## 3부: 스크립트 연습 문제 따라 하기 (1–2일차)

이 부분은 **연습용 예제**입니다. VS Code나 브라우저에서 아래 코드와 출력을 읽으세요. `w1d0` 파일은 설명용입니다. 이 파일을 만들거나 명령을 입력하지 마세요.

### 연습 문제 파일: `w1d0_ready.py`

```python
# 로봇 이름을 입력받으세요:   Robot name:
# 그런 다음 출력하세요:      <name> is ready
#
# 예: 사용자가 RR-01을 입력하면 "RR-01 is ready"를 출력하세요.

# TODO: 이 줄 아래에 코드를 작성하세요
```

### 코드를 작성하기 전에 테스트 실행하기: 스크립트

```bash
pytest exercises/week1/tests/test_w1d0.py
```

```
E       AssertionError: 프로그램이 출력한 내용: ''
E       assert 'RR-01 is ready' in ''
```

다음처럼 읽으면 됩니다.
- `프로그램이 출력한 내용: ''`: `''`는 **빈 문자열**입니다. 아무것도 출력하지 않았다는 뜻입니다. 아직 코드가 없으니 이 상태가 맞습니다.
- `assert 'RR-01 is ready' in ''`: 테스트가 출력에서 `RR-01 is ready`를 찾았지만 없었습니다.

### 첫 번째 시도: 오류로 중단됩니다

```python
name = input("Robot name: ")
print(name + " is ready" + 1)
```

```
스크립트를 실행하다가 오류가 났습니다. 오류 메시지:
Traceback (most recent call last):
  File ".../exercises/week1/w1d0_ready.py", line 2, in <module>
    print(name + " is ready" + 1)
          ~~~~~~~~~~~~~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

다음처럼 읽으면 됩니다.
- `스크립트를 실행하다가 오류가 났습니다. 오류 메시지:`: 프로그램이 끝나기 전에 오류로 멈췄습니다.
- `line 2`: 2번째 줄에 문제가 있습니다.
- **마지막 줄**은 무엇이 잘못됐는지 알려 줍니다. 문자열에 숫자(`1`)를 더할 수 없습니다.

### 두 번째 시도: 올바르게 동작합니다

```python
name = input("Robot name: ")
print(name + " is ready")
```

```
1 passed in 0.12s
```

완료했습니다. ✅

### 직접 스크립트 실행하기 (5단계)

VS Code 터미널에서 `w1d0_ready.py`를 실행하는 예입니다. 실제로 없는 파일이니 명령을 입력하지 마세요.
사용자가 `Robot name:`에 `RR-01`을 입력하면 프로그램이 `RR-01 is ready`를 출력합니다.

```bash
python3 exercises/week1/w1d0_ready.py
```

```
Robot name: RR-01
RR-01 is ready
```

### 테스트는 어떻게 대신 입력합니까?

스크립트 연습 문제에서는 테스트가 프로그램을 실행하고 입력값을 자동으로 입력합니다. 예를 들어 `RR-01`을 입력하고 Enter를 누릅니다. 그런 다음 프로그램이 출력한 내용을 읽습니다.

따라서 입력을 받는 연습 문제에서 `print("RR-01 is ready")`처럼 **고정된 답만 출력해서 통과하려고 하면 안 됩니다**. 1일차처럼 정해진 문구를 출력하는 문제는 안내한 문구를 그대로 출력하면 됩니다. 실제 테스트는 **여러 입력값**을 사용합니다. 예를 들어 이름 대신 `RR-01`, `DR-07`처럼 서로 다른 이름을 입력해서 확인합니다. 2일차 배터리 문제에서도 용량과 전류 값을 바꿔 가며 같은 방법으로 확인합니다. 고정된 답은 이 테스트를 통과하지 못합니다.

---

## 4부: 함수 연습 문제 따라 하기 (3–5일차)

3일차부터 연습 문제는 **함수**입니다. 테스트는 파일을 프로그램으로 실행하지 않습니다. 대신 다양한 값으로 **함수를 호출**하고 **반환하는 값**을 확인합니다.

### 연습 문제 파일: `w1d0_speed.py`

읽기만 하는 설명용 예제입니다. `w1d0_speed.py`를 만들거나 테스트 명령을 입력하지 마세요.

```python
def speed_status(speed):
    """로봇 속도(m/s)에 맞는 상태 단어를 반환하세요.

    - 정확히 0          -> "STOPPED"
    - 2.0 초과          -> "TOO FAST"
    - 그 밖의 값        -> "MOVING"

    예: speed_status(1.0)은 "MOVING"을 반환합니다
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    pass
```

### 코드를 작성하기 전에 테스트 실행하기: 함수

```
E       AssertionError: assert None == 'STOPPED'
E        +  where None = speed_status(0)
...
5 failed in 0.15s
```

다음처럼 읽으면 됩니다.
- `speed_status(0)`: 테스트가 `speed = 0`으로 함수를 호출했습니다.
- `assert None == 'STOPPED'`: `'STOPPED'`를 기대했는데 `None`이 나왔습니다.
- `None`은 "값이 없음"을 뜻합니다. 함수가 아무것도 **반환(return)**하지 않았습니다. `pass`만 있으니 이 상태가 맞습니다.

> **VS Code 터미널에 `None`이 나오면 VS Code 편집기에서 메시지에 나온 함수를 확인하세요. `return`이 빠졌거나 `print`를 잘못 사용했는지 확인하세요.**

### 첫 번째 시도: 거의 맞았습니다

```python
def speed_status(speed):
    if speed == 0:
        return "STOPPED"
    elif speed >= 2.0:
        return "TOO FAST"
    else:
        return "MOVING"
```

```
...F.
FAILED exercises/week1/tests/test_w1d0.py::test_speed_status[2.0-MOVING]
E       AssertionError: assert 'TOO FAST' == 'MOVING'
1 failed, 4 passed in 0.14s
```

다음처럼 읽으면 됩니다.
- `...F.`: 테스트 하나를 문자 하나로 표시합니다. `.`은 통과, `F`는 실패입니다. 5개 중 4개가 통과했습니다.
- `test_speed_status[2.0-MOVING]`: 실패한 테스트는 `speed = 2.0`을 사용했고 `"MOVING"`을 기대했습니다.
- `assert 'TOO FAST' == 'MOVING'`: **작성한** 함수는 `'TOO FAST'`(왼쪽)를 반환했고 정답은 `'MOVING'`(오른쪽)입니다.

위의 읽기 전용 `speed_status` 예제에서 규칙을 다시 읽으세요. *"2.0 **초과** → TOO FAST"*입니다. 정확히 2.0이면 2.0을 **초과하지 않습니다**. `>=`가 잘못됐으므로 `>`로 바꿔야 합니다.

> 💡 **테스트는 경계값을 자주 확인합니다.** 정확히 `2.0`, `0`, `90`, `15` 같은 값입니다. 테스트 하나만 실패할 때는 보통 `>`와 `>=` 또는 `<`와 `<=`가 원인입니다.

### 두 번째 시도: 이제 맞았습니다

```python
    elif speed > 2.0:
```

```
5 passed in 0.12s
```

완료했습니다. ✅

### 직접 함수 실행하기 (5단계)

아래 명령으로 [`exercises/week1/w1d3_conditions.py`](../exercises/week1/w1d3_conditions.py)를 불러오세요.
파이썬 `>>>` 프롬프트에 아래 호출을 입력한 뒤 `exit()`을 입력하세요.
`battery_status`를 풀었다면 `>>>`가 없는 줄에 나온 결과가 나와야 합니다.

```bash
python3 -i exercises/week1/w1d3_conditions.py
```

```python
>>> battery_status(55)
'OK'
>>> battery_status(90)
'FULL'
>>> exit()
```

파일을 바꾼 뒤에는 **Ctrl + S**로 저장하세요. 파이썬이 아직 열려 있으면 `>>>`에 `exit()`을 입력하세요. 그런 다음 VS Code 터미널에 `python3 -i exercises/week1/w1d3_conditions.py`를 입력해서 저장한 변경 사항을 불러오세요.

### 함수 연습 문제 규칙

- 함수나 매개변수 **이름을 바꾸지 마세요**. 테스트는 그 이름 그대로 호출합니다. 바꾸면 `ImportError: cannot import name 'battery_status'`가 나옵니다.
- 답은 **`print`가 아니라 `return`으로 반환하세요**.
- 함수 파일 맨 아래에 **`input()`이나 시험 삼아 실행한 코드를 남기지 마세요**. 테스트가 파일을 불러올 때 `input()`이 있으면 다음 오류가 납니다.
  ```
  OSError: pytest: reading from stdin while output is captured!
  ```
  위의 [직접 함수 실행하기](#직접-함수-실행하기-5단계)에 나온 불러오기 명령과 함수 호출을 사용하세요.

---

## 5부: 테스트 결과 읽기

### 요약 줄(항상 맨 아래에 있습니다)

| 화면에 나온 내용 | 의미 |
|---|---|
| `5 passed` | 모두 통과했습니다 ✅ |
| `1 failed, 4 passed` | 거의 다 되었습니다. 실패한 하나를 고치세요 |
| `5 failed` | 아직 모두 실패합니다. 시작 전에는 정상입니다. 이미 풀었다면 실행 중 오류나 빠진 `return`을 찾아보세요 |
| `1 error` | 테스트가 파일을 **불러오지도** 못했습니다. `SyntaxError`, `IndentationError`, `ImportError`, `OSError ... reading from stdin`을 찾아보세요 |
| `6 deselected`만 나오고 `passed`나 `failed`가 없습니다 | 실행한 테스트가 없습니다. `-k` 뒤의 이름에 오타가 있습니다. 수업에 나온 명령을 그대로 다시 입력하세요 |

### 실패한 테스트 이름

```
FAILED exercises/week1/tests/test_w1d3.py::test_battery_status[89-OK]
       │                                   │                   └ 입력값과 기대한 답
       │                                   └ 확인할 대상
       └ 테스트 파일
```

`[89-OK]`는 테스트가 `89`를 사용했고 `OK`를 기대했다는 뜻입니다.

### `E`로 시작하는 줄

`E`로 시작하는 줄은 **오류**입니다. 보통 가장 중요한 줄은 다음과 같습니다.

```
E       assert 'FULL' == 'OK'
               │         └ 기대한 값
               └ 작성한 코드의 값
```

**왼쪽은 작성한 코드가 내놓은 값이고, 오른쪽은 기대한 값입니다.**

### 자주 나오는 메시지와 해결 방법

| 메시지 | 원인 | 해결 방법 |
|---|---|---|
| `assert None == ...` | `return`이 없거나 `return` 대신 `print`를 사용했습니다 | VS Code 편집기에서 오류 메시지에 나온 함수 안에 `return`을 추가하세요 |
| `프로그램이 출력한 내용: ''` | 스크립트가 아무것도 출력하지 않습니다 | 저장했습니까? `TODO` 아래에 코드를 작성했습니까? |
| 스크립트를 실행해도 **아무것도 나타나지 않습니다** | 파일에 코드가 없고 주석만 있거나 저장하지 않았습니다. 또는 함수를 호출만 하고 반환값을 출력하지 않았습니다 | VS Code 편집기에서 해당 파일을 열고 `TODO` 아래에 코드를 작성하세요. **Ctrl + S**를 누르면 탭의 **●**가 사라집니다. 함수 호출만 적으면 반환값이 화면에 나오지 않습니다. `playground.py`에서는 `print(battery_status(55))`처럼 호출을 `print()`로 감싸세요. 연습 문제 함수 안에서는 답을 `return`으로 반환하세요 |
| `스크립트를 실행하다가 오류가 났습니다. 오류 메시지:` | 스크립트에 오류가 있습니다 | VS Code 터미널에서 오류 메시지의 **마지막 줄**을 읽으세요 |
| `스크립트가 10초 안에 끝나지 않았습니다.` / `끝나지 않는 반복문이나 필요 없는 input()이 있는지 확인하세요.` | 끝나지 않는 반복문이나 필요 없는 `input()`이 있습니다 | VS Code 편집기에서 해당 연습 문제 파일을 열고 `while` 조건과 `input()` 호출 개수를 확인하세요 |
| 함수 테스트가 끝나지 않고 아무것도 나오지 않습니다 | 함수 안의 반복문이 끝나지 않습니다. 함수 테스트에는 시간 제한이 없습니다 | VS Code 터미널에서 **Ctrl + C**를 누르세요. 마지막 줄의 파일 이름과 줄 번호(예: `w1d4_loops.py:48: KeyboardInterrupt`)가 멈춘 반복문입니다. 그 반복문 안에서 조건에 쓰는 변수가 바뀌도록 고치세요 |
| `sum_to must add the numbers in a for or while loop` | 공식이나 `sum()`으로 계산했습니다 | 4일차 수업 2절처럼 `for` 문 안에서 합계에 숫자를 하나씩 더하세요 |
| `closest must find the smallest value with a for or while loop` | `min()`, `sorted()`, `.sort()`로 찾았습니다 | 2주차 1일차 수업 5절처럼 첫 번째 요소로 시작하고, 반복문 안에서 더 작은 값을 만나면 바꾸세요 |
| `ImportError: cannot import name ...` | 함수 이름을 바꾸거나 함수를 지웠습니다 | VS Code 편집기에서 오류 메시지에 나온 연습 문제 파일의 함수 이름을 원래대로 되돌리세요 |
| `ModuleNotFoundError: No module named 'playground'` | 코드를 입력할 때 VS Code가 `from playground import …` 줄을 연습 문제 파일 맨 위에 저절로 추가했습니다 | VS Code 편집기에서 해당 연습 문제 파일 맨 위의 `from playground import …` 줄을 지우고 **Ctrl + S**로 저장하세요. 연습 문제 파일에는 `import` 줄이 필요 없습니다 |
| `SyntaxError` / `IndentationError` | `:` `)` `"`가 빠졌거나 공백이 잘못되었습니다 | VS Code 편집기에서 오류 메시지에 나온 연습 문제 파일을 열고 표시된 줄 번호로 이동하세요 |
| `SyntaxError: invalid character '（' (U+FF08)` | 비슷하게 보이지만 파이썬이 사용할 수 없는 문자입니다. 전각 괄호 `（ ）`, 전각 콜론 `：`, 둥근 따옴표 `‘ ’ “ ”`는 문서나 메신저에서 코드를 복사하면 자주 생깁니다 | VS Code 편집기에서 표시된 줄로 이동하세요. 그 문자를 지우고 키보드로 `(` `)` `:` `'` `"`를 다시 입력하세요. **Ctrl + S**로 저장하고 다시 실행하세요 |
| `OSError: pytest: reading from stdin...` | 함수 파일에 `input()`을 남겨 두었습니다 | 해당 연습 문제 파일에서 필요 없는 `input()`을 지우고 **Ctrl + S**로 저장하세요. 수업의 `python3 -i` 진행 순서를 따르세요 |
| `프로그램이 예상보다 더 많이 입력을 요청했습니다. (반복문이 제대로 멈춥니까?)` | 주간 과제의 반복문이 멈추지 않습니다 | VS Code 편집기에서 오류 메시지에 나온 주간 과제 파일의 `main()` 안에 있는 `break`를 확인하세요 |

### 유용한 옵션

VS Code 터미널에서 다음 명령으로 [3일차 테스트](../exercises/week1/tests/test_w1d3.py) 또는 [1주차 연습 문제 전체](../exercises/week1/)를 실행합니다.
각 명령이 어떤 결과를 보여 주는지는 주석에 나와 있습니다.

```bash
pytest exercises/week1/tests/test_w1d3.py -x          # 처음 실패하면 중단합니다(읽을 내용이 줄어듭니다)
pytest exercises/week1/tests/test_w1d3.py -k status   # 이름에 "status"가 들어간 테스트만 실행합니다
pytest exercises/week1/tests/test_w1d3.py --tb=line   # 실패 하나를 한 줄로 보여 줍니다
pytest exercises/week1                                # 이번 주 모든 연습 문제
```

출력이 너무 길면 지금 푸는 문제의 테스트 명령 끝에 `-x`를 붙여서 처음 실패한 테스트만 확인하세요.
VS Code 편집기에서 해당 연습 문제를 고치고 **Ctrl + S**로 저장하세요.
테스트가 통과할 때까지 같은 명령을 반복한 뒤 수업으로 돌아가세요. 다른 날짜의 파일은 아직 수정하지 마세요.

---

## 6부: 주간 과제(매주 마지막에 진행합니다)

주간 과제(체크포인트)는 메뉴와 반복문이 있는 조금 더 큰 프로그램입니다. 테스트가 **사용자 역할**을 합니다. 프로그램의 각 `input()`에 정해진 답을 하나씩 입력하고 프로그램이 출력한 내용을 확인합니다.

예를 들어 1주차 게임 테스트는 `50`, `abc`, `25`, `42`를 입력하고 `Too high`, `Please enter a number.`, `Too low`, `Correct!`, `You got it in 3 tries!`가 나오는지 확인합니다.

따라서 다음을 지켜야 합니다.
- [주간 과제 안내](../checkpoints/week1/README.md)에 나온 메시지를 **정확히** 출력하세요.
- 안내한 것과 **같은 순서로** 입력을 요청하세요.
- 반복문이 테스트에서 준비한 입력보다 더 많이 요청하면 `프로그램이 예상보다 더 많이 입력을 요청했습니다. (반복문이 제대로 멈춥니까?)`가 나옵니다.

VS Code 편집기에서 주간 과제 파일을 저장하세요. `python3 checkpoints/week1/converter.py`로 [`checkpoints/week1/converter.py`](../checkpoints/week1/converter.py)를 실행하세요.
[`checkpoints/week1/README.md`](../checkpoints/week1/README.md)의 예제 입력값을 입력하세요. `Choose:`에 `q`를 입력해서 끝내고 VS Code 터미널로 돌아오세요.

그런 다음 `python3 checkpoints/week1/guess.py`로 [`checkpoints/week1/guess.py`](../checkpoints/week1/guess.py)를 실행하세요.
게임을 해 보고 출력을 주간 과제 안내와 비교하세요.
정답은 무작위이므로 추측한 숫자는 예제와 달라도 됩니다. 두 프로그램을 멘토에게 보여 주세요.

---

## 7부: 규칙

1. **[`tests/`](../exercises/week1/tests/) 폴더 안의 파일은 절대 수정하지 마세요.** 멘토는 GitHub에서 모든 변경 사항을 볼 수 있습니다.
2. 연습 문제 파일이나 함수 **이름을 바꾸지 마세요**.
3. 맨 위에서부터 **실패한 테스트를 하나씩 고치세요**.
4. **20분 동안 막혀 있습니까?** 정확한 오류 메시지와 시도한 방법을 적고 멘토에게 물어보세요.
5. 모든 테스트가 통과하지 않았어도 **매일 마칠 때 푸시하세요**. GitHub의 자동 테스트는 시작한 일차의 테스트만 실행합니다. 오늘까지의 연습 문제를 모두 풀었으면 ✅가 나오고, 아직 풀지 못한 문제가 있으면 ❌가 나옵니다. ❌이면 멘토에게 알리세요.
