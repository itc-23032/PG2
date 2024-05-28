import re


def is_strong_password(password):
    # 正規表現パターン：8文字以上、大文字と小文字を含み、1つ以上の数字を含む
    password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'

    # 正規表現でパスワードの妥当性をチェック
    if re.match(password_pattern, password):
        return True
    else:
        return False


# テスト
password1 = "Secure123"
password2 = "weakpass"
password3 = "1pass12"
password4 = "VeryStrongPass12"

print(is_strong_password(password1))  # True
print(is_strong_password(password2))  # False
print(is_strong_password(password3))  # False
print(is_strong_password(password4))  # True

