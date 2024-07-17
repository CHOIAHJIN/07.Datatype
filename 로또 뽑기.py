# 예제
import random
i = 0
list = [ ]
while i < 6 :
    i = i + 1
    new_num = random.randint(1, 45)
    if new_num in list :
        print("A에 값이 있습니다.")
    print(list)

