import os
import re

def find_missing_numbers(directory, prefix):
    # ファイル名の正規表現パターンを定義
    pattern = re.compile(rf'{prefix}(\d{{3}})\.txt')
    
    # 指定されたディレクトリ内のファイルを取得
    try:
        files = os.listdir(directory)
    except FileNotFoundError:
        print(f"The directory {directory} does not exist.")
        return []
    
    # 見つかった番号を格納するリスト
    numbers = []
    
    for file in files:
        match = pattern.match(file)
        if match:
            number = int(match.group(1))
            numbers.append(number)
    
    # 見つかった番号をソート
    if numbers:
        numbers.sort()
    else:
        print("No matching files found.")
        return []
    
    # 欠けている番号を見つける
    missing_numbers = []
    for i in range(numbers[0], numbers[-1]):
        if i not in numbers:
            missing_numbers.append(i)
    
    return missing_numbers

# 現在のディレクトリを取得
current_directory = os.path.dirname(os.path.abspath(__file__))

# 使用例
directory_to_search = current_directory  # 現在のスクリプトのディレクトリを指定
file_prefix = 'spam'
missing_numbers = find_missing_numbers(directory_to_search, file_prefix)

if missing_numbers:
    print(f'Missing numbers: {missing_numbers}')
else:
    print('No missing numbers found.')
