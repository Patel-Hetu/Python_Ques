'''Question 10'''


def decimalToBinary(num):
    if num == 0:
        return '0'
    binary_version = ''
    while num > 0:
        binary_version += str(num % 2)
        num //= 2
    return binary_version[::-1]

for num in range(10):
    print(num,"in binary is",decimalToBinary(num))
