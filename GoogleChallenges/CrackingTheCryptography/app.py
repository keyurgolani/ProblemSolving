import string

def CrackingTheCryptography(message):
	crypto_key = dict(zip(string.lowercase, string.lowercase[::-1]))
	return ''.join(map(lambda x: crypto_key[x] if x in crypto_key.keys() else x, message))


def main():
	print CrackingTheCryptography("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
	print CrackingTheCryptography("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")


main()

# did you see last night's episode?
# Yeah! I can't believe Lance lost his job at the colony!!
