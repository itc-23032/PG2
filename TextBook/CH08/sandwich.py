import pyinputplus as pyip


def sandwich_maker():
    bread = pyip.inputMenu(['小麦', '白パン', '全粒粉', 'ライ麦'], prompt='パンを選んでください:\n', )
    protein = pyip.inputMenu(['チキン', 'ターキー', 'ハム', '豆腐'], prompt='タンパク質の種類を選んでください:\n', )
    cheese = pyip.inputYesNo(prompt='チーズを追加しますか？\n', yesVal='はい', noVal='いいえ',)
    if cheese == 'はい':
        cheese = pyip.inputMenu(['チェダー', 'スイス', 'モッツァレラ'], prompt='チーズを選んでください:\n', )
    else:
        cheese = 'なし'
    tomato = pyip.inputYesNo(prompt='トマトを追加しますか？\n', yesVal='はい', noVal='いいえ', )
    lettuce = pyip.inputYesNo(prompt='レタスを追加しますか？\n', yesVal='はい', noVal='いいえ', )
    mayo = pyip.inputYesNo(prompt='マヨネーズを追加しますか？\n', yesVal='はい', noVal='いいえ', )
    mustard = pyip.inputYesNo(prompt='マスタードを追加しますか？\n', yesVal='はい', noVal='いいえ', )

    count = pyip.inputInt(prompt='サンドイッチの数を入力してください:\n', min=1)

    print(f'注文内容は以下の通りです:\n'
          f'パン: {bread}\n'
          f'タンパク質: {protein}\n'
          f'チーズ: {cheese}\n'
          f'トマト: {tomato}\n'
          f'レタス: {lettuce}\n'
          f'マヨネーズ: {mayo}\n'
          f'マスタード: {mustard}\n'
          f'サンドイッチの数: {count}\n'
          f'ありがとうございました！')


if __name__ == '__main__':
    sandwich_maker()
