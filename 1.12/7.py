# https://stepik.org/lesson/5047/step/7?unit=1086


s = str(input())
sum1 = int(s[0]) + int(s[1]) + int(s[2])
sum2 = int(s[3]) + int(s[4]) + int(s[5])
if sum1 == sum2:
    print('Счастливый')
else:
    print('Обычный')
