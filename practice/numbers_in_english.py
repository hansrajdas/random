static = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

def numbers_in_english(n):
    if n < 1:
        return 'Invalid'
    print(f'{n}:', end=' ')
    while n > 0:
        if n < 20:
            print(static[n])
            return
        if n >= 20 and n < 30:
            print('twenty', end=' ')
            n -= 20
        elif n >= 30 and n < 40:
            print('thirty', end=' ')
            n -= 30
        elif n >= 40 and n < 50:
            print('fourty', end=' ')
            n -= 40
        elif n >= 50 and n < 60:
            print('fifty', end=' ')
            n -= 50
        elif n >= 60 and n < 70:
            print('sixty', end=' ')
            n -= 60
        elif n >= 70 and n < 80:
            print('seventy', end=' ')
            n -= 70
        elif n >= 80 and n < 90:
            print('eighty', end=' ')
            n -= 80
        elif n >= 90 and n < 100:
            print('ninty', end=' ')
            n -= 90
        elif n >= 100 and n < 1000:
            x = n // 100
            print(static[x], end=' ')
            print('hundred', end=' ')
            n -= x * 100
        else:
            print('Too large, unsupported')
            return

numbers_in_english(10)
numbers_in_english(25)
numbers_in_english(59)
numbers_in_english(159)
numbers_in_english(999)
numbers_in_english(500)
numbers_in_english(650)
