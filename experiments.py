from ast import Str


string = "sdhfsdjhfabcefjwewkeabcwejfkwe12435abcwejwejfabcerjeabc"
print(len(string))
result = string.split("abc")
result_str = ""
for element in result:
    result_str += element

print(result_str)
print(len(result_str))
exit()

#Unpacking data
#requires checking for mismatches in number of elements
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
name, shares, price, (year, mon, day) = data
_, shares, price, _ = data
#print(year)

#Unpacking iterables of arbitrary length
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
#print(phone_numbers)

#Unpacking example
records = [('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4)]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

