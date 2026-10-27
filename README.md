# ROS를 위한 파이썬: 4주 집중 과정

반갑습니다! 이 과정에서는 프로그래밍을 처음 배우는 사람도 4주 동안 파이썬을 단계별로 익힐 수 있습니다. 과정을 마치면 **ROS 2**(로봇 운영 체제)로 실제 로봇을 프로그래밍할 준비가 됩니다.

**혼자서** 자기 속도에 맞춰 공부합니다. 멘토가 매일 진행 상황을 점검합니다. 모든 연습 문제에는 코드가 올바른지 알려 주는 **자동 테스트**가 있습니다.

---

## 여기서 시작하세요

👉 **지금 보고 있는 브라우저에서 파란색 링크 [docs/00-setup.md](docs/00-setup.md)를 클릭하고 설치 안내를 처음부터 따라 하세요.**

설치를 마친 뒤에는 VS Code 터미널에서 `python3 next.py`를 실행하면 **지금 할 일**을 알려 줍니다. 어디까지 했는지 기억하지 않아도 됩니다.
[어디에 입력합니까?](docs/01-how-to-study.md#어디에-입력합니까)를 참고하세요.

처음 할 일은 다음과 같습니다.

1. **컴퓨터 설치 및 준비:** 브라우저에서 [docs/00-setup.md](docs/00-setup.md)를 여세요(약 1–2시간).
2. **이 과정의 공부 방법:** 브라우저나 VS Code 편집기에서 [docs/01-how-to-study.md](docs/01-how-to-study.md)를 여세요(10분).
3. **연습 문제와 테스트 진행 방법:** 브라우저나 VS Code 편집기에서 [docs/02-how-exercises-work.md](docs/02-how-exercises-work.md)를 여세요(20분).
4. 그다음부터는 `python3 next.py`가 1주차 1일차부터 차례로 안내합니다.

---

## 일정

| 주차 | 날짜(2026년) | 주제 | ROS에서 필요한 이유 | 주간 과제(체크포인트) |
|---|---|---|---|---|
| **1** | 10월 19일 – 10월 26일 | 터미널과 파이썬 기초 | 터미널에서 ROS를 제어합니다 | 로봇 콘솔 도구(단위 변환기 + 숫자 맞히기 게임) |
| **2** | 10월 27일 – 11월 2일 | 데이터와 함수 | ROS 메시지는 구조가 있는 데이터입니다 | 센서 데이터 분석기 |
| **3** | 11월 3일 – 11월 9일 | 코드 정리: 클래스, 모듈, 오류 | 모든 ROS 노드는 클래스입니다 | 로봇 클래스 계층 |
| **4** | 11월 10일 – 11월 16일 | ROS 방식의 코드: 콜백, 타이머, 발행/구독 | 실제 ROS 2에서도 같은 개념을 사용합니다 | **mini-ROS**: 작은 ROS 직접 만들기 |

2–4주차 자료는 학습할 때가 되면 이 저장소에 올라옵니다. [새 수업 받기](docs/01-how-to-study.md#새-수업-받기)를 참고하세요.

### 1주차

| 일차 | 수업 | 연습 문제 |
|---|---|---|
| 1 | [터미널과 첫 프로그램](lessons/week1/day1-terminal-and-first-program.md) | [`exercises/week1/w1d1_*.py`](exercises/week1/) |
| 2 | [변수, 숫자, 입력](lessons/week1/day2-variables-numbers-input.md) | `exercises/week1/w1d2_*.py` |
| 3 | [조건에 따라 판단하기: 함수와 if 문](lessons/week1/day3-functions-and-decisions.md) | [`exercises/week1/w1d3_conditions.py`](exercises/week1/w1d3_conditions.py) |
| 4 | [반복하기: for 문과 while 문](lessons/week1/day4-loops.md) | [`exercises/week1/w1d4_loops.py`](exercises/week1/w1d4_loops.py) |
| 5 | [문자열 다루기 + 주간 과제](lessons/week1/day5-strings-and-checkpoint.md) | [`exercises/week1/w1d5_strings.py`](exercises/week1/w1d5_strings.py), [주간 과제](checkpoints/week1/README.md) |

### 2주차

| 일차 | 수업 | 연습 문제 |
|---|---|---|
| 1 | [리스트, 값 여러 개를 한 번에 다루기](lessons/week2/day1-lists.md) | [`exercises/week2/w2d1_lists.py`](exercises/week2/w2d1_lists.py) |

---

## 수업을 진행하는 방법

수업은 **하나의 경로**를 따라 진행합니다. 단계를 건너뛰지 말고 항상 바로 다음 단계를 진행하세요.

```
설치 및 준비 → 1일차 → 2일차 → 3일차 → 4일차 → 5일차 + 주간 과제 → 2주차 → ... → 4주차 → ROS 2
```

### `python3 next.py`: 지금 할 일 확인하기

과정을 진행하는 동안 VS Code 터미널에서 언제든지 다음 명령을 실행하세요.

```bash
python3 next.py
```

다음과 비슷한 내용이 나옵니다.

```
1주차  15 / 59 완료
  ✔ 시작 준비
  ✔ 1일차: 터미널과 첫 프로그램
  ▶ 2일차: 변수, 숫자, 입력
    3일차: 조건에 따라 판단하기, 함수와 if 문
    ...

▶ 지금 할 일 (2일차: 변수, 숫자, 입력): 연습 문제 w1d2_time_format.py
   열 파일: lessons/week1/day2-variables-numbers-input.md (연습 문제 2/2)
   열 파일: exercises/week1/w1d2_time_format.py
   테스트: pytest exercises/week1/tests/test_w1d2.py -k time_format
```

- **연습 문제와 주간 과제**는 테스트로 자동 확인합니다. 테스트가 통과하면 다음에 실행할 때 자동으로 다음 단계로 넘어갑니다.
- **실습 일지**는 직접 씁니다. `python3 next.py`는 일지를 썼는지만 확인합니다. **커밋/푸시**는 자동으로 확인합니다.
- **수업 읽기, "직접 해 보기", "설명할 수 있습니까?"** 같은 단계는 `(y/n)` 질문으로 묻습니다. 정말 마쳤을 때만 `y`를 입력하고 Enter를 누르세요. 아직 마치지 않았으면 `n`을 입력하세요.
- "설명할 수 있습니까?" 질문에는 수업을 보지 않고 해당 개념을 혼자 소리 내어 설명해 본 뒤 답하세요.

`열 파일`에 나온 경로는 VS Code 터미널에서 **Ctrl**을 누른 채 클릭하면 편집기에서 열립니다.

진도는 `progress/state.json`과 `PROGRESS.md`에 자동으로 저장됩니다. 이 두 파일은 직접 수정하지 마세요. 커밋하고 푸시하면 멘토가 GitHub에서 `PROGRESS.md`로 진도를 확인합니다.

### 매일 마칠 때

> 설치를 마친 뒤 매일 하는 일입니다. 지금은 명령을 실행하지 마세요. 설치 안내에서 차례로 연습합니다.
> - **포크**: GitHub에 만드는 나만의 과정 저장소 복사본입니다.
> - **커밋**: 지금까지 바꾼 파일을 내 컴퓨터에 하나의 기록으로 저장하는 것입니다.
> - **푸시**: 커밋한 기록을 GitHub의 포크로 보내는 것입니다.

하루의 마지막 단계는 실습 일지 작성, 멘토 점검, 커밋과 푸시입니다. 커밋과 푸시가 맨 마지막입니다. `python3 next.py`가 차례로 안내합니다. 코드와 실습 일지를 저장한 뒤 VS Code 터미널에 다음 명령을 순서대로 입력하세요.

```bash
git add .
git commit -m "Week 1 Day 1: finished exercises"
git push
```

멘토는 GitHub에서 포크를 열어 `PROGRESS.md`, 코드, 실습 일지, 테스트 통과 여부(✅ 또는 ❌)를 확인합니다.

### 다음 날로 넘어가기

다음 학습일이 되면 `python3 next.py`를 실행하고, **N + 1일차**가 지금 할 일로 나오면 그 수업을 시작하세요. 일찍 끝나면 "추가 도전"을 해 보거나 어려웠던 부분을 다시 읽으세요. 다음 날 수업을 미리 시작하지 마세요.

### 다음 주로 넘어가기

다음 조건을 모두 만족하면 한 주를 마친 것입니다.

1. `python3 next.py`에서 이번 주의 모든 단계가 ✔로 표시됩니다.
2. 이번 주 주간 과제가 테스트를 통과했습니다.
3. 멘토에게 주간 과제를 보여 주었습니다.

주간 과제를 금요일에 다 마치지 못해도 괜찮습니다. 멘토에게 알리고 다음 주 월요일 오전에 마치세요.

그런 다음 다음 주 자료를 받으세요.

1. 브라우저에서 GitHub의 포크를 열고 **Sync fork** → **Update branch**를 클릭하세요.
2. VS Code 터미널에 `git pull`을 입력하세요. VS Code 편집기에 새 주차 파일이 나타나야 합니다.
3. VS Code 터미널에서 `python3 next.py`를 실행하세요. 새 주차의 첫 단계가 나타납니다.

### 하루 일과 예시

```
오전        오늘 수업을 읽습니다. 모든 예제를 직접 입력합니다(복사해서 붙여 넣지 마세요).
오후        연습 문제를 풉니다. 통과할 때까지 테스트를 실행합니다.
마칠 때     실습 일지를 씁니다. python3 next.py로 확인합니다.
멘토 점검   멘토와 15분 동안 확인합니다. 결과물을 보여 주고 궁금한 점을 질문합니다.
푸시        마지막으로 커밋하고 푸시합니다. 그러면 오늘 공부는 끝입니다.
```

---

## 규칙

- **붙여 넣지 말고 직접 입력하세요.** 손으로 입력하는 것도 연습입니다.
- **20분 동안 시도한 뒤 질문하세요.** 20분 동안 막히는 건 자연스럽습니다. 하지만 2시간을 계속 쓰는 건 아깝습니다. 실습 일지에 질문을 적고, 멘토 점검 시간을 기다리지 말고 **바로** 멘토에게 직접 가서 묻거나 메신저로 보내세요.
- **AI 도구**(ChatGPT, Claude, Copilot 등)에는 **오류 메시지나 개념을 설명해 달라**고 물어봐도 됩니다. 연습 문제나 주간 과제 코드를 대신 작성해 달라고 하면 **안 됩니다**. 멘토가 코드를 한 줄씩 설명해 보라고 할 것입니다.
- **매일 푸시하세요.** 멘토가 GitHub에서 진도를 확인합니다.
- **[`tests/`](exercises/week1/tests/) 폴더는 절대 수정하지 마세요.** 테스트가 통과하도록 코드를 고치세요. 코드에 맞춰 테스트를 고치면 안 됩니다.

---

## 저장소 구성

```
README.md           ← 지금 읽고 있는 파일입니다
docs/               설치 및 준비, 공부 방법 안내
lessons/weekN/      수업 자료: 읽을 파일입니다
exercises/weekN/    연습 문제 파일: 여기에 코드를 작성합니다
exercises/weekN/tests/   자동 테스트(수정하지 마세요)
checkpoints/weekN/  주간 과제
logs/               실습 일지(TEMPLATE.md를 복사하세요)
next.py             지금 할 일을 알려 주는 도구(python3 next.py)
PROGRESS.md         내 진도표(next.py가 자동으로 만듭니다)
progress/           주차별 단계 목록과 내 진도 기록
```

## 유용한 명령

VS Code 터미널에서 다음 명령으로 [3일차 테스트](exercises/week1/tests/test_w1d3.py), [1주차 연습 문제](exercises/week1/), [주간 과제 테스트](checkpoints/week1/)를 실행합니다.
주석에는 각 명령이 실행하는 테스트가 나와 있습니다. 1주차를 마친 뒤에는 순서대로 `21 passed`, `56 passed`, `11 passed`, `67 passed`가 나와야 합니다.

```bash
pytest exercises/week1/tests/test_w1d3.py   # 하루치 테스트
pytest exercises/week1                      # 한 주 전체 테스트
pytest checkpoints/week1                    # 주간 과제 테스트
pytest                                      # 모든 테스트
```
