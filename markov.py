import pandas as pd

fr = open("./Mary Johnston/Mary - lewis rand.txt", "r", encoding="utf8")

text = fr.read()
fr.close()

# Some problems: The PG texts have some fluff at the beginning and end that have
# to do with legal stuff with PG. We don't want that, I think.

# How much of these texts do we want to include in the Markov matrix?
# Do we include prefaces?
# Tables of contents?
# Chapter headings?
# Titles?

# What letters do we consider?
# alphabet + period + comma + space?
# How do we handle whitespace? Condense it down to a single space?

rows, cols = (28, 28)
T = [[0 for r in range(cols)] for c in range(rows)]

text = text.lower()

def getIndex (c):
	if ord(c) >= ord('a') and ord(c) <= ord('z'):
		return ord(c) - ord('a')
	elif c == ' ' or c == '\n' or c == '\t':
		return 26
	else:
		return 27

for i in range(1, len(text)):
	next = getIndex(text[i])
	prev = getIndex(text[i - 1])
	T[prev][next] = T[prev][next] + 1

for row in range(len(T)):
	rowSum = sum(T[row])
	for col in range(len(T[row])):
		T[row][col] = T[row][col] / rowSum

print(T)

df = pd.DataFrame(data=T, columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "space", "symbol"])
df.to_csv('M_markov2.csv', index=False, encoding='utf8')
