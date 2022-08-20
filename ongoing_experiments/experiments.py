from ast import Str
import json
from turtle import bgcolor
import requests
import os
from colorama import Fore, Back, Style

app_id = "c7421794"
app_key = "4bd934700afdd3bab496f650ab649bd4"

base_url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/"
language = "en-gb"

no_value_error_text = "Не удалось найти."


url = base_url + language + "/" + "definition"
response = requests.get(url, headers={"app_id": app_id, "app_key": app_key}).json()

def parse_response(response):
    if type(response) == type({}):
        for key, value in dict(response).items():
            if type(value) == type('string'):
                print(f"{key}: {value}")
            else:
                print('-------')
                print(key)
                parse_response(value)
    elif type(response) == type([]):
        for item in response:
            parse_response(item)

print(parse_response(response))

exit()

print(json.dumps(response, indent=4, sort_keys=True, check_circular=False))

print(Fore.GREEN)
print('Level 0'.upper())
print(Fore.WHITE)
print(f"word_id = {response['id']}\n")
print(f"metadata = {response['metadata']}\n")
print(f"word = {response['word']}\n")

for results_item in response['results']:
    print(Fore.GREEN)
    print('Level 1'.upper())
    print(Fore.WHITE)
    print(f"results_id = {results_item['id']}\n")
    print(f"results_language = {results_item['language']}\n")
    print(f"type = {results_item['type']}\n")
    print(f"word = {results_item['word']}\n")
    print(Fore.GREEN)
    print('Level 2'.upper())
    print(Fore.WHITE)
    for entry in results_item['lexicalEntries']:
        print(f"language = {entry['language']}\n\n")
        print(f"lexicalCategory = {entry['lexicalCategory']}\n\n")
        print(f"phrases = {entry['phrases']}\n\n")
        print(f"text = {entry['text']}\n\n")
        print(Fore.GREEN)
        print('Level 3'.upper())
        print(Fore.WHITE)
        for item in entry['entries']:
            print(f"etymologies = {item['etymologies']}\n\n")
            print(f"pronunciations = {item['pronunciations']}\n\n")
            print(Fore.GREEN)
            print('Level 4'.upper())
            print(Fore.WHITE)
            for sense in item['senses']:
                print(f"definitions = {sense['definitions']}\n")
                print(f"examples = {sense['examples']}\n")
                print(f"shortDefinitions = {sense['shortDefinitions']}\n")
                print(f"subsenses = {sense['subsenses']}\n")
                synonyms_str = ""
                for synonim in sense['synonyms']:
                    synonyms_str += synonim['text'] + ', '
                print(f"synonyms = {synonyms_str[:-2]}\n")
                print('\n')

exit()

string = "This is a string"

paragraph = "This is a string \
that was split into two \
substrings in the code."

triple_quotes_paragraph = """This is a string \
that was split into two \
substrings in the code."""

print(paragraph)
print(triple_quotes_paragraph)
string_type = type(string)
print(string_type)

# Sorting a dictionary by value
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
reversed = sorted(xs.items(), key=lambda x: x[1])
print(reversed)
# Another way to sort a dictionary by value
import operator
reversed = sorted(xs.items(), key=operator.itemgetter(1))
print(reversed)

string = "sdhfsdjhfabcefjwewkeabcwejfkwe12435abcwejwejfabcerjeabc"
print(len(string))
result = string.split("abc")
result_str = ""
for element in result:
    result_str += element

print(result_str)
print(len(result_str))

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

