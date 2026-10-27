# 2주차 · 1일차: 리스트, 값 여러 개를 한 번에 다루기

**배울 내용:** 값 여러 개를 순서대로 담는 **리스트**를 만들고, 값을 꺼내고, 바꾸고, 추가하는 방법을 배웁니다. 반복문으로 리스트의 값을 하나씩 살펴보는 방법도 배웁니다.

**로봇을 다룰 때 필요한 이유:** ROS의 라이다(LiDAR) 메시지 `LaserScan`에는 거리 값 수백 개가 `ranges`라는 리스트로 들어 있습니다. 로봇은 이 리스트에서 가장 가까운 물체를 찾고, 너무 가까운 값이 몇 개인지 셉니다. 오늘 연습 문제가 바로 이 일입니다.

---

## 1. 리스트 만들기

리스트는 대괄호 `[ ]` 안에 값을 쉼표로 구분해서 씁니다.

```python
readings = [2.5, 0.8, 3.1, 1.2]     # 라이다 거리 값(미터)
names = ["rail", "drone", "wire"]
empty = []                          # 빈 리스트

print(readings)                     # [2.5, 0.8, 3.1, 1.2]
print(len(readings))                # 4   (값의 개수)
print(len(empty))                   # 0
```

리스트 안의 값 하나하나를 **요소**라고 합니다. `len()`은 문자열에서처럼 개수를 알려 줍니다.

---

## 2. 인덱싱과 슬라이싱: 문자열과 같습니다

1주차 5일차에 문자열에서 배운 방법이 리스트에도 그대로 통합니다. 인덱스는 **0**부터 시작합니다.

```
 readings:   2.5   0.8   3.1   1.2
 index:       0     1     2     3
 from end:   -4    -3    -2    -1
```

```python
readings = [2.5, 0.8, 3.1, 1.2]
print(readings[0])      # 2.5        첫 번째 요소
print(readings[-1])     # 1.2        마지막 요소
print(readings[1:3])    # [0.8, 3.1] 인덱스 1부터 3 직전까지(새 리스트)
print(readings[:2])     # [2.5, 0.8]
```

`readings[4]`는 `IndexError: list index out of range`를 일으킵니다. 마지막 인덱스는 `len(readings) - 1`입니다.

---

## 3. 리스트는 바꿀 수 있습니다

문자열은 바꿀 수 없었습니다. 리스트는 **바꿀 수 있습니다**.

```python
readings = [2.5, 0.8, 3.1]
readings[0] = 2.6           # 인덱스 0의 값을 바꿉니다
readings.append(1.9)        # 끝에 값을 하나 추가합니다
print(readings)             # [2.6, 0.8, 3.1, 1.9]
```

⚠️ `.append()`는 리스트 **자체**를 바꾸고 `None`을 돌려줍니다. 결과를 다시 저장하지 마세요.

```python
readings = readings.append(1.9)    # ❌ readings가 None이 됩니다!
readings.append(1.9)               # ✅
```

문자열 메서드(`text = text.strip()`)와 반대이니 주의하세요.

### 직접 해 보기

VS Code 터미널에 `python3`를 입력하세요. 파이썬 `>>>` 프롬프트에서 아래 순서대로 입력하세요.

1. `battery = [100, 95, 90]`
2. `.append()`로 `85`를 추가하세요.
3. 인덱스를 사용해서 첫 번째 값을 `99`로 바꾸세요.
4. `battery`를 입력하세요. `[99, 95, 90, 85]`가 나와야 합니다.

마지막으로 `>>>`에 `exit()`을 입력하세요.

---

## 4. `in`과 `for`: 리스트 살펴보기

`in`은 리스트에 어떤 값이 있는지 확인합니다.

```python
names = ["rail", "drone", "wire"]
print("drone" in names)     # True
print("boat" in names)      # False
```

`for` 문은 리스트의 요소를 **처음부터 하나씩** 꺼냅니다. 문자열에서 글자를 하나씩 꺼낸 것과 같습니다.

```python
readings = [2.5, 0.8, 3.1]
for r in readings:
    print("Distance:", r)
```

```
Distance: 2.5
Distance: 0.8
Distance: 3.1
```

반복할 때마다 `r`에 다음 요소가 들어갑니다. `range()`가 필요 없습니다.

---

## 5. 리스트와 누적 방법

1주차 4일차에 배운 누적 방법(반복문 **앞에서** 시작하고, **안에서** 갱신하고, **뒤에서** 사용하기)을 리스트에 그대로 사용합니다.

**합계:**

```python
readings = [2.5, 0.8, 3.1]
total = 0
for r in readings:
    total = total + r
print(total)                # 6.4
```

**개수 세기:** 조건에 맞는 요소만 셉니다.

```python
readings = [2.5, 0.8, 3.1, 0.4]
count = 0
for r in readings:
    if r > 2.0:
        count = count + 1
print(count)                # 2
```

**지금까지 가장 큰 값 기억하기:** 첫 번째 요소로 시작하고, 더 큰 값을 만나면 바꿉니다.

```python
readings = [2.5, 0.8, 3.1, 1.2]
biggest = readings[0]       # 첫 번째 요소로 시작합니다
for r in readings:
    if r > biggest:
        biggest = r
print(biggest)              # 3.1
```

| 반복 회차 | `r` | `r > biggest`? | 계산 후 `biggest` |
|---|---|---|---|
| 시작 | | | 2.5 |
| 1 | 2.5 | False | 2.5 |
| 2 | 0.8 | False | 2.5 |
| 3 | 3.1 | True | 3.1 |
| 4 | 1.2 | False | 3.1 |

`biggest = 0`으로 시작하면 안 되는 이유를 생각해 보세요. 값이 모두 음수이면 0이 답이 되어 버립니다. 그래서 **리스트의 첫 번째 요소**로 시작합니다.

### 파이썬의 기본 함수

파이썬에는 이 일을 대신하는 함수도 있습니다.

| 함수 | 결과 | `[2.5, 0.8, 3.1]`의 예 |
|---|---|---|
| `len(x)` | 요소의 개수 | `3` |
| `sum(x)` | 합계 | `6.4` |
| `max(x)` | 가장 큰 값 | `3.1` |
| `min(x)` | 가장 작은 값 | `0.8` |

오늘 연습 문제 1번에서는 `sum()`과 `len()`을 써도 됩니다. 연습 문제 3번은 반복문을 연습하는 문제이므로 `min()`을 쓰지 말고 반복문으로 푸세요.

⚠️ `sum([])`은 `0`이지만 `max([])`와 `min([])`은 `ValueError`를 일으킵니다. 빈 리스트로 나누면 `ZeroDivisionError`가 납니다. 빈 리스트가 들어올 수 있으면 먼저 `if len(readings) == 0:`으로 확인하세요.

---

## 6. 자주 하는 실수

| 실수 | 해결 방법 |
|---|---|
| `IndexError: list index out of range`가 나옵니다 | 마지막 인덱스는 `len(x) - 1`입니다. 빈 리스트에는 `x[0]`도 없습니다 |
| 리스트가 `None`이 됩니다 | `x = x.append(...)`로 쓰지 말고 `x.append(...)`만 쓰세요 |
| `ZeroDivisionError: division by zero`가 나옵니다 | 빈 리스트의 `len()`은 0입니다. 나누기 전에 빈 리스트인지 확인하세요 |
| `TypeError: 'list' object is not callable`이 나옵니다 | 인덱스에는 대괄호를 씁니다: `readings[0]` (`readings(0)`이 아닙니다) |
| 결과가 0이거나 틀립니다 | 시작값이 반복문 안에 있으면 매번 초기화됩니다. 반복문 **앞으로** 옮기세요 |

---

## 7. 연습 문제

**연습 문제 진행 방법:** 한 번에 하나씩 **순서대로** 푸세요. 아래의 각 연습 문제에는 번호가 붙은 진행 순서가 있습니다. 1번부터 끝까지 따라 한 뒤 다음 연습 문제로 넘어가세요. 잘되지 않는 단계가 있으면 [연습 문제 진행 방법 5부](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 참고하세요.

세 함수는 모두 [`exercises/week2/w2d1_lists.py`](../../exercises/week2/w2d1_lists.py)에 있습니다. 아래에서 각 함수의 번호가 붙은 진행 순서를 따르세요.

### 연습 문제 1/3: `average(readings)`

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [4부: 함수 연습 문제](../../docs/02-how-exercises-work.md#4부-함수-연습-문제-따라-하기-35일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** 센서 값 리스트의 평균을 반환하세요. 리스트가 비어 있으면 `0.0`을 반환하세요.

```python
>>> average([2.0, 4.0])
3.0
>>> average([])
0.0
```

**따라 해 볼 예제:** 비슷한 문제입니다(이 연습 문제의 정답은 아닙니다).

이 함수는 배터리 기록 리스트에서 처음 값과 마지막 값의 차이(사용한 배터리)를 반환합니다. 빈 리스트이면 `levels[0]`이 없으므로 **먼저** 확인하고 `0`을 반환합니다.

```python
def battery_used(levels):
    if len(levels) == 0:
        return 0
    return levels[0] - levels[-1]
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 -i playground.py`를 실행하세요.

**파이썬 `>>>` 프롬프트**에 아래 호출을 입력하세요. `>>>`가 없는 줄은 나와야 할 결과입니다.

```python
$ python3 -i playground.py
>>> battery_used([100, 90, 75])
25
>>> battery_used([])
0
>>> exit()
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 위쪽에 나타난 입력 칸에 [`exercises/week2/w2d1_lists.py`](../../exercises/week2/w2d1_lists.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열립니다. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week2`](../../exercises/week2/) → [`w2d1_lists.py`](../../exercises/week2/w2d1_lists.py)를 클릭하세요.
2. VS Code 편집기에서 `w2d1_lists.py`의 `average` 안에 있는 `pass`를 코드로 바꾸세요. 먼저 빈 리스트인지 확인해서 `0.0`을 반환하세요. 그다음 합계를 개수로 나눈 값을 반환하세요(5절의 `sum()`과 `len()`).
3. VS Code 편집기에서 **Ctrl + S**로 `w2d1_lists.py`를 저장하세요. 파일 탭의 **●**가 사라집니다.

   VS Code 터미널에서 `python3 -i exercises/week2/w2d1_lists.py`를 실행하세요.
   **파이썬 `>>>` 프롬프트**에 위의 **할 일** 아래에 나온 `average(...)` 호출을 입력하고 결과를 비교하세요.

   `>>>`에 `exit()`을 입력해서 VS Code 터미널로 돌아오세요.
4. VS Code 터미널에서 [`test_w2d1.py`](../../exercises/week2/tests/test_w2d1.py)로 `average`를 테스트하세요.
   ```bash
   pytest exercises/week2/tests/test_w2d1.py -k average
   ```
   ✔ `4 passed, 8 deselected`가 나와야 합니다.
5. VS Code 터미널에서 `python3 next.py`를 실행하세요. 테스트가 통과했으면 다음 단계가 나타납니다.

> `deselected`는 이 파일에 있는 **다른** 연습 문제의 테스트는 실행하지 않았다는 뜻입니다. `-k`를 사용하면 이렇게 되니 괜찮습니다.

### 연습 문제 2/3: `count_below(readings, limit)`

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [4부: 함수 연습 문제](../../docs/02-how-exercises-work.md#4부-함수-연습-문제-따라-하기-35일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** 라이다 거리 값 중에서 `limit`보다 **작은** 값(너무 가까운 물체)이 몇 개인지 반환하세요. `limit`과 같은 값은 세지 않습니다.

```python
>>> count_below([0.5, 2.0, 0.3, 5.0], 1.0)
2
>>> count_below([], 1.0)
0
```

**따라 해 볼 예제:** 비슷한 문제입니다(이 연습 문제의 정답은 아닙니다).

이 함수는 `limit`보다 **큰** 값의 개수를 셉니다. 연습 문제에서는 비교 기호를 어떻게 바꿔야 할지 생각하세요.

```python
def count_above(readings, limit):
    count = 0
    for r in readings:
        if r > limit:
            count = count + 1
    return count
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 -i playground.py`를 실행하세요.

**파이썬 `>>>` 프롬프트**에 아래 호출을 입력하세요. `>>>`가 없는 줄은 나와야 할 결과입니다.

```python
$ python3 -i playground.py
>>> count_above([0.5, 2.0, 0.3, 5.0], 1.0)
2
>>> count_above([1.0, 1.0], 1.0)
0
>>> exit()
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 위쪽에 나타난 입력 칸에 [`exercises/week2/w2d1_lists.py`](../../exercises/week2/w2d1_lists.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열립니다. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week2`](../../exercises/week2/) → [`w2d1_lists.py`](../../exercises/week2/w2d1_lists.py)를 클릭하세요.
2. VS Code 편집기에서 `w2d1_lists.py`의 `count_below` 안에 있는 `pass`를 코드로 바꾸세요. 5절의 "개수 세기" 방법을 사용하세요. `count = 0`은 반복문 **앞에**, `return`은 반복문이 끝난 **뒤에** 두세요.
3. VS Code 편집기에서 **Ctrl + S**로 `w2d1_lists.py`를 저장하세요. 파일 탭의 **●**가 사라집니다.

   VS Code 터미널에서 `python3 -i exercises/week2/w2d1_lists.py`를 실행하세요.
   **파이썬 `>>>` 프롬프트**에 위의 **할 일** 아래에 나온 `count_below(...)` 호출을 입력하고 결과를 비교하세요.

   `>>>`에 `exit()`을 입력해서 VS Code 터미널로 돌아오세요.
4. VS Code 터미널에서 [`test_w2d1.py`](../../exercises/week2/tests/test_w2d1.py)로 `count_below`를 테스트하세요.
   ```bash
   pytest exercises/week2/tests/test_w2d1.py -k count_below
   ```
   ✔ `4 passed, 8 deselected`가 나와야 합니다.
5. VS Code 터미널에서 `python3 next.py`를 실행하세요. 테스트가 통과했으면 다음 단계가 나타납니다.

### 연습 문제 3/3: `closest(readings)`

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [4부: 함수 연습 문제](../../docs/02-how-exercises-work.md#4부-함수-연습-문제-따라-하기-35일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** 라이다 거리 값 중에서 가장 **작은** 값(가장 가까운 물체까지의 거리)을 반환하세요. `min()`을 쓰지 말고 반복문으로 찾으세요. 리스트에는 값이 항상 하나 이상 있습니다.

```python
>>> closest([2.5, 0.8, 3.1])
0.8
>>> closest([250.0, 300.0])
250.0
```

**따라 해 볼 예제:** 비슷한 문제입니다(이 연습 문제의 정답은 아닙니다).

이 함수는 가장 **큰** 값(가장 먼 물체)을 찾습니다. 5절의 "지금까지 가장 큰 값 기억하기"와 같습니다. 연습 문제에서는 무엇을 바꿔야 할지 생각하세요.

```python
def farthest(readings):
    best = readings[0]
    for r in readings:
        if r > best:
            best = r
    return best
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 -i playground.py`를 실행하세요.

**파이썬 `>>>` 프롬프트**에 아래 호출을 입력하세요. `>>>`가 없는 줄은 나와야 할 결과입니다.

```python
$ python3 -i playground.py
>>> farthest([2.5, 0.8, 3.1])
3.1
>>> farthest([4.0])
4.0
>>> exit()
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 위쪽에 나타난 입력 칸에 [`exercises/week2/w2d1_lists.py`](../../exercises/week2/w2d1_lists.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열립니다. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week2`](../../exercises/week2/) → [`w2d1_lists.py`](../../exercises/week2/w2d1_lists.py)를 클릭하세요.
2. **먼저 종이에** `closest([2.5, 0.8, 3.1])`의 표를 5절처럼 그리세요. 열 이름은 *반복 회차*, *`r`*, *계산 후 가장 작은 값*으로 하세요. 첫 행은 '시작, (빈칸), 2.5'입니다.
3. VS Code 편집기에서 `w2d1_lists.py`의 `closest` 안에 있는 `pass`를 코드로 바꾸세요. 첫 번째 요소(`readings[0]`)로 시작하세요. `0`이나 `100` 같은 숫자로 시작하면 안 됩니다. 반복문 안에서 더 **작은** 값을 만나면 바꾸세요.
4. VS Code 편집기에서 **Ctrl + S**로 `w2d1_lists.py`를 저장하세요. 파일 탭의 **●**가 사라집니다.

   VS Code 터미널에서 `python3 -i exercises/week2/w2d1_lists.py`를 실행하세요.
   **파이썬 `>>>` 프롬프트**에 위의 **할 일** 아래에 나온 `closest(...)` 호출을 입력하고 결과를 비교하세요.

   `>>>`에 `exit()`을 입력해서 VS Code 터미널로 돌아오세요.
5. VS Code 터미널에서 [`test_w2d1.py`](../../exercises/week2/tests/test_w2d1.py)로 `closest`를 테스트하세요.
   ```bash
   pytest exercises/week2/tests/test_w2d1.py -k closest
   ```
   ✔ `4 passed, 8 deselected`가 나와야 합니다.
6. 아직 `python3 next.py`를 실행하지 마세요. 아래 **마지막으로: 오늘의 테스트 전체**로 가세요. 추가 도전은 선택입니다. `python3 next.py`는 그 절의 테스트를 실행한 다음에 실행합니다.

### 추가 도전(선택): `count_in_range(readings, low, high)`

시간이 남을 때만 하세요. 테스트하지 않으며 `python3 next.py`의 단계에도 없습니다.

`playground.py`의 내용을 지우고, `low` 이상 `high` 이하인 값의 개수를 반환하는 `count_in_range(readings, low, high)` 함수를 작성하세요. 연습 문제 2번과 같은 방법에 조건만 바뀝니다(`and`).

VS Code 터미널에서 `python3 -i playground.py`를 실행하고 `>>>`에 `count_in_range([0.5, 2.0, 3.5, 9.0], 1.0, 4.0)`을 입력하세요. `2`가 나와야 합니다. 마치면 `exit()`을 입력하세요.

### 마지막으로: 오늘의 테스트 전체

VS Code 터미널에서 [`test_w2d1.py`](../../exercises/week2/tests/test_w2d1.py)의 오늘 테스트를 실행하세요.

```bash
pytest exercises/week2/tests/test_w2d1.py
```

✔ **`12 passed`**가 나와야 합니다. VS Code 터미널에서 `python3 next.py`를 실행하세요.

---

## 8. 오늘 마치기 전에

VS Code 터미널에서 `python3 next.py`를 실행하세요. 오늘 남은 단계를 하나씩 안내합니다.

- 수업 내용을 설명할 수 있는지 묻는 질문에 답하세요.
- 실습 일지를 **직접** 쓰세요. `python3 next.py`는 일지를 대신 써 주지 않고, 썼는지만 확인합니다. 제목의 날짜, 오늘 수업, 배운 내용, 겪은 문제, 질문, 공부한 시간을 **모두** 채우세요. 일지 양식에서 ✏️ 표시가 있는 곳이 채울 곳입니다.
- 멘토와 점검하세요. 멘토가 확인하면 점검 질문에 `y`로 답하세요.
- **마지막으로** 커밋하고 푸시하세요. 오늘의 코드, 실습 일지, 진도가 모두 GitHub로 갑니다. 푸시했는지는 다음에 `python3 next.py`를 실행할 때 자동으로 확인합니다.

푸시까지 마치면 오늘 공부는 끝입니다. `python3 next.py`에 **2일차**가 나타나도 오늘은 시작하지 마세요.
