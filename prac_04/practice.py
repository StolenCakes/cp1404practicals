"""
Write a function that takes a single "query string" (from a URL) and returns a list of tuples of name-value pairs.
Example:
    "?name=Bob&age=99&day=Wed"
should result in a return value of:
    [('name', 'Bob'), ('age', 99), ('day', 'Wed')]
For bonus marks* convert any numeric values to numbers.
"""
sentence = "?name=Bob&age=99&day=Wed"

part = sentence[1:].split("&")  # Remove the '?' and split them into pairs through '&'

result = []
for pair in part:
    key, value = pair.split("=")
    if value.isdigit():
        value = int(value)
    result.append((key, value))

print(result)
