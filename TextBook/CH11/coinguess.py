import random

def get_input():
    while True:
        print('コインの表裏を当ててください。表か裏を入力してください：')
        guess = input()
        ind = ('裏', '表').index(guess)
        if ind >= 0:
            return ind

toss = random.randint(0, 1) # 0は裏、1は表

guess = get_input()
if toss == guess:
    print('当たり！')
else:
    print('はずれ！もう一回当てて！')
    guess = get_input()
    if toss == guess:
        print('当たり！')
    else:
        print('はずれ。このゲームは苦手ですね。')
