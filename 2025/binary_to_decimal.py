def binary_to_decimal(binary_str):
    decimal = 0
    length = len(binary_str)
    print(f"Converting binary {binary_str} to decimal:")
    for i in range(length):
        bit = int(binary_str[length - 1 - i])  # start from rightmost bit
        value = bit * (2 ** i)
        print(f"Bit {bit} at position {length - 1 - i} contributes {bit} * 2^{i} = {value}")
        decimal += value
    return decimal

binary_input = input("Enter a binary number (only 0s and 1s): ")
decimal_output = binary_to_decimal(binary_input)
print(f"The decimal value of binary {binary_input} is: {decimal_output}")
