def comma(list):
    result = ''
    length = len(list)
    if length == 0:
        result = 'You gave me nothing.'
    elif length == 1:
        result = list[0]
    else:
        for i in range(length - 1):
            result += list[i] + ', '
        result += 'and ' + list[-1]
    return result

spam = ['apples', 'bananas', 'tofu', 'cats']

print(comma(spam))
