import re

# findall search sub
# compile

string = "este e um teste de expressoes teste regulares"

print(re.search(r"teste",string))
print(re.findall(r"teste",string))
print(re.sub(r"teste","abcd",string))

print()

regexp = re.compile(r"teste")
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub("abc",string))