def 부과세(num) :
    result = []
    for n in num :


        VAT = n * 1.1
        result.append(int(VAT))
    return result

v = [100, 200, 300]
print(부과세(v))


