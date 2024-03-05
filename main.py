import os
import shutil
import csv

# CSV 파일에서 문제 이름과 순서를 읽어옵니다.
with open('problems_adv.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    problems = [row[2:5] for row in reader]  # 문제 순서와 문제 이름만 가져옵니다.
    print(problems)

# 기존 백준 문제 폴더 경로
base_paths = ['./백준/Bronze/', './백준/Silver/', './백준/Gold/']

# 새로운 폴더 경로
new_base_path = './Week_1/adv/'

for i, problem in enumerate(problems[1:], start=1):  # 첫 번째 행(헤더)를 제외하고 시작합니다.
    # 기존 폴더 경로에서 문제 폴더를 찾습니다.
    old_path = None
    for base_path in base_paths:
        for dir_name in os.listdir(base_path):
            if problem[2] in dir_name:  # 문제 이름을 포함하는 폴더를 찾습니다.
                print(problem)
                old_path = os.path.join(base_path, dir_name)
                break
        if old_path is not None:  # 문제 폴더를 찾았을 경우, 더 이상 검색하지 않습니다.
            break

    if old_path is None:  # 문제 폴더를 찾지 못했을 경우, 다음 문제로 넘어갑니다.
        # print(f"Could not find folder for problem: {problem[1]}")
        continue

    new_path = os.path.join(new_base_path, f"{problem[0].zfill(3)}.{problem[1]}")

    # 새로운 경로에 디렉토리를 생성합니다.
    os.makedirs(new_path, exist_ok=True)

    # 파일을 복사합니다.
    for file_name in os.listdir(old_path):
        shutil.copy(os.path.join(old_path, file_name), new_path)
