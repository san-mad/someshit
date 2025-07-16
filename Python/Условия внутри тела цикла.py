def count_chars_ignore_case(text, char):
    text = text.lower()
    char = char.lower()
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count
    print(count_chars_ignore_case('Abracadabra', 'a')) 
print(count_chars_ignore_case('Abracadabra', 'A'))