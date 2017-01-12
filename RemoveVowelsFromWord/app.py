import sys

def disemvowel(word):
    word_list = list(word)
    for letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        while True:
			try:
				word_list.remove(letter)
			except ValueError:
				break
			else:
				continue
    word = "".join(word_list)
    return word

def main():
	f = open('output.txt', 'w')
	while True:
		f.write(disemvowel(str(sys.stdin.readline())))


main()
