string_to_truncate = 'I have a beautiful cat!'
i = len(string_to_truncate)
while i:
    i -= 1
    print(string_to_truncate[:i])
    if i == 0:
        print("Nothing's left here")