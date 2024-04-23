def reverse_string(text):
    """
    Reverse a string
    """
    
    reversed_text = ''
    for ch in text:
        reversed_text = ch + reversed_text
    return reversed_text

print(reverse_string('hello')) # 'olleh'