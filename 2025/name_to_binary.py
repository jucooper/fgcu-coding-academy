def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_emojis(binary_str):
    return binary_str.replace('1', '🔵').replace('0', '⚪')

def name_to_binary_emojis(name):
    print(f"Hello, {name}!")
    binary = text_to_binary(name)
    emoji_version = binary_to_emojis(binary)
    print("\nYour name in binary:")
    print(binary)
    print("\nYour name in binary emojis:")
    print(emoji_version)

name = input("Enter your name: ")
name_to_binary_emojis(name)