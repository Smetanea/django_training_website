def arabic_to_roman(number):
    if number < 1 or number > 100:
        return print("not supported number")
    one = 'I'
    five = 'V'
    ten = 'X'
    fifty = 'L'
    one_hundred = 'C'
    result = ''
    i = number
    while i > 0:
        if i // 100 > 0:
            return print('100 = ' + one_hundred)
        elif i // 50 > 0:
            result = result + fifty
            i = i % 50
        elif i // 10 > 0:
            result = result + (i // 10 * ten)
            i = i % 10
        elif i // 5 > 0:
            result = result + (i // 5 * five)
            i = i % 5
        elif i > 0:
            result = result + (i * one)
            i = 0
    result = result.replace('VIIII', 'IX')
    result = result.replace('IIII', 'IV')
    result = result.replace('LXXXX', 'XC')
    result = result.replace('XXXX', 'XL')
    return print(str(number) + ' = ' + result)


arabic_to_roman(44)
arabic_to_roman(55)
arabic_to_roman(66)
arabic_to_roman(73)
arabic_to_roman(82)
arabic_to_roman(99)
arabic_to_roman(100)
arabic_to_roman(108)
