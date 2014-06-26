

def scan(sentence):
	words = [convert_number(('error', word)) for word in sentence.split()]
	return [get_token(word) for word in words]

def get_token(word):
	tokenized = word
	for token in lex:
		if str(word[1]).lower() in lex[token]:
			tokenized = (token, word[1])
	return tokenized

def shaw_split(words):
	return words.split(', ')

def convert_number(i):
	try:
		return ('number', int(i[1]))
	except ValueError:
		return (i[0], i[1])

direction = shaw_split('north, south, east, west, down, up, left, right, back')
verb = shaw_split('go, stop, kill, eat')
stop = shaw_split('the, in, of, from, at, it')
noun = shaw_split('door, bear, princess, cabinet')

lex = {'direction': direction,
			'verb': verb,
			'stop': stop,
			'noun': noun,
			}

