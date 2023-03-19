def f(ch):
    if ch.isalpha() == False:
        print("ERROR")
        exit()
    sum = 0
    for i in ch:
        if i in 'eyuioaEYUIOA':
            sum += 1
    return sum

ch = "sdfghjkyea    ".strip()
f(ch)
print("Number of vowel letters: " + str(f(ch)))
assert f(ch) == 3
ch = "HELLO".strip()
f(ch)
print("Number of vowel letters: " + str(f(ch)))
assert f(ch) == 2
ch = "Python".strip()
f(ch)
print("Number of vowel letters: " + str(f(ch)))
assert f(ch) == 2
ch = "aOYaEya".strip()
f(ch)
print("Number of vowel letters: " + str(f(ch)))
assert f(ch) == 7
print("SUCCESS")