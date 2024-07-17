def 문자요금(x) :
    l = len(x)
    result = 0
    if l <= 20 :
        result = ("50원입니다.")
        print(result)
    elif l > 20 :
        result = ("100원입니다.")
        print(result)
        return result


문자요금("문자 요금이 얼마니")

# 교수님 풀이
# def find_len(x) :
#     result = 0
#     if len(x) <= 20 :
#         result = 50
#     elif len(x) > 20 :
#         result = 100
#         return result
#
# text = input("문자를 입력해주세요. : ")
# var = find_len(text)
# print(var)
#
# find_len("000000000")
