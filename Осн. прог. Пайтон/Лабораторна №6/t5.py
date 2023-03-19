def f(ch):
    ch = ch.lstrip('https://www.')
    idx = ch.find('.')
    return ch[:idx]

ch  = 'https://cnet.com'
print(f(ch))
ch  = 'http://github.com/carbonfive/raygun'
print(f(ch))
ch  = 'http://www.zombie-bites.com'
print(f(ch))
ch  = 'www.codewars.com/kata/514a024011ea4fb54200004b'
print(f(ch))