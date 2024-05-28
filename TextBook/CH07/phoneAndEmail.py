import pyperclip, re

# 電話番号の正規表現パターンを定義
phone_regex = re.compile(r"""(
    (0\d{1,3}|\(0\d{1,3}\))  # 市外局番
    (\s|-|\.)?               # 区切り文字（省略可能）
    (\d{1,4})                # 市内局番
    (\s|-|\.)                # 区切り文字
    (\d{3,4})                # 加入者番号
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # 内線番号（省略可能）
    )""", re.VERBOSE)

# メールアドレスの正規表現パターンを定義
email_regex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+  # ユーザー名
    @
    [a-zA-Z0-9.-]+     # ドメイン名
    (\.[a-zA-Z]{2,4})  # ドメインのトップレベル
    )""", re.VERBOSE)

# クリップボードからテキストを取得
text = str(pyperclip.paste())
matches = []

# テキストから電話番号を抽出
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[7] != '':
        phone_num += ' x' + groups[7]
    matches.append(phone_num)

# テキストからメールアドレスを抽出
for groups in email_regex.findall(text):
    matches.append(groups[0])

# 抽出された情報をクリップボードにコピーし、出力する
if len(matches) > 0:
    s = '\n'.join(matches)
    pyperclip.copy(s)
    print('クリップボードにコピーしました:')
    print(s)
else:
    print('電話番号やメールアドレスは見つかりませんでした。')

