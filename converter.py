import struct

def filling_the_bit(result:str) -> str:
    bits = int(input(f'Give amount of bits\nFor calculus use 1 extra bit just to be sure\n---'))
    while len(result) < bits:
        result = "0"+result
    return result 

def dtb():
    decimal = int(input(f'Give decimal: '))
    conversion = bin(decimal)[2:]
    result = filling_the_bit(conversion)
    print(f'The converted result is {result}')

def btd():
    binary = input(f'Give binary')
    conversion = int(binary, 2)
    result = filling_the_bit(conversion)
    print(f'The converted result is {result}')

def tcompdtb():
    decimal = int(input(f'Give decimal number: '))
    bits = int(input(f'Give amount of bits: '))
    absolute = bin(abs(decimal))[2:]
    result_array = []
    i = 0
    while len(absolute) < bits:
        absolute = "0"+absolute
    while i < len(absolute):
        if absolute[i] == "0":
            result_array.append("1")
            i += 1
        else:
            result_array.append("0")
            i += 1
    result = "".join(result_array)
    result = bin(int(result, 2)+1)[2:]
    print(f'Two\'s component is {result}')
    

def tcompbtd():
    binary = input(f'Give binary number: ')
    bits = int(input(f'Give amount of bits: '))
    while len(binary)<bits :
        binary = '0'+binary
    if binary[0] == '0':
        print(f'Two\'s complement reversed is {int(binary, 2)}')
    else:
        print(f'Two\'s complement reversed is {-1 * (int("".join("1" if x == "0" else "0" for x in binary), 2) + 1)}')

def dth():
    decimal = int(input(f'Give decimal: '))
    result = hex(decimal)[2:].upper()
    print(f'The converted result is {result}')

def htd():
    hexadecimal = input(f'Give hexadecimal: ')
    result = int(hexadecimal, 16)
    print(f'The converted result is {result}')

def binsum():
    num1 = int(input("First binary number: "), 2)
    num2 = int(input("Second binary number: "), 2)
    sum = bin(num1+num2)[2:]
    result = filling_the_bit(sum)
    print(f'The sum is {result}')

def binmul():
    print(f'For \"two times\" use the binary value of \'2\' => 10')
    num1 = int(input(f'Give first binary number: '), 2)
    num2 = int(input(f'Give second binary number: '), 2)
    mul = bin(num1*num2)[2:]
    result = filling_the_bit(mul)
    print(f'The result is {result}')

def binsub():
    num1 = int(input(f'Give first binary number: '), 2)
    num2 = int(input(f'Give second binary number: '), 2)
    sub = bin(num1-num2)[2:]
    result = filling_the_bit(sub)
    print(f'The result is {result}')

def hexsum():
    num1 = int(input(f'Give first hexadecimal number: '), 16)
    num2 = int(input(f'Give second hexadecimal number: '), 16)
    result = hex(num1+num2)[2:].upper()
    print(f'The sum is {result}')

def ftd():
    binary = input(f'Give binary: ')
    while len(binary) < 32:
        binary += '0'
    result = struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]
    print(f'The result is {result}')

def dtf():
    decimal = float(input(f'Give decimal: '))
    bits, = struct.unpack('!I', struct.pack('!f', decimal))
    print(f'The result is {"{:032b}".format(bits)}')

def convert() -> None:
    choice = input(f'''Choose between \n
    -Decimal to binary => type dtb\n
    -Binary to decimal => type btd\n
    -Two's complement (decimal to binary) => type tcompdtb\n
    -Two's complenemt (binary to decimal) => tcompbtd\n
    -Decimal to hexadecimal => type dth\n
    -Hexadecimal to deciaml => type htd\n
    -Binary sum => binsum\n
    -Binary subtraction => type binsub\n
    -Binary multiplication => binmul\n
    -Hexadecimal sum => hexsum\n
    -Floating point to decimal => type ftd\n
    -Decimal to floating point => type dtf\n
    ---''')
    if choice == 'dtb':
        dtb()
    elif choice == 'btd':
        btd()
    elif choice == 'tcompdtb':
        tcompdtb()
    elif choice == 'tcompbtd':
        tcompbtd()
    elif choice == 'dth':
        dth()
    elif choice == 'htd':
        htd()
    elif choice == 'binsum':
        binsum()
    elif choice == 'binsub':
        binsub()
    elif choice == 'binmul':
        binmul()
    elif choice == 'hexsum':
        hexsum()
    elif choice == 'dtf':
        dtf()
    elif choice == 'ftd':
        ftd()

def main() -> None:
    convert()
    running = True
    while running:
        choice = input(f'To end the program => type end\nElse press enter\n')
        if choice == 'end':
            running = False
        else:
            convert()

main()