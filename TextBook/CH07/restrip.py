import re


def custom_strip(text, chars=None):
    # charsがNoneの場合は、デフォルトで空白文字を除去する正規表現を使用
    if chars is None:
        pattern = r'^\s+|\s+$'
    else:
        # charsに指定された文字列を正規表現の一部として使用する
        pattern = f'^[{re.escape(chars)}]+|[{re.escape(chars)}]+$'

    # 正規表現で文字列を置換して空白を除去
    return re.sub(pattern, '', text)


# テスト
text = "  Hello, World!  "
chars_to_remove = " !"
print(custom_strip(text))  # "Hello, World!"
print(custom_strip(text, chars_to_remove))  # "Hello, World"

