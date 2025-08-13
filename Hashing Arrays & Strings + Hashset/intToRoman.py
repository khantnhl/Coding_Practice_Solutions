
def intToRoman(self, num: int) -> str:
    symbols = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
        (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    result = []

    # 3890
    # 3890 // 1000 -> 3 * M
    # 3 * 1000 -> 890
    for value, symbol in symbols:
        if(num == 0):
            break

        count = num // value
        result.append(symbol * count)
        num -= count * value
    return ''.join(result)