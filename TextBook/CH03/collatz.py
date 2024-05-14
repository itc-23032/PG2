def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return int(3 * number + 1)


print('整数を入力してください。')
try:
    input_number = int(input())
except ValueError:
    print('整数でないので終了します。')
    
while input_number != 1:    
    input_number = collatz(input_number)
    print(input_number)
    if input_number == 1:
        break
    else:
        continue

