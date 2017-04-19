from string import ascii_lowercase
LEGAL_CHARS = set(ascii_lowercase)


def answer(chunk, word):
    ''' Return the shortest, lexicographically earliest string that can be
        formed from *chunk* by removing *word* repeatedly.

        Traverse a tree of removal paths, then sort the leaves.
    '''
    assert len(chunk) <= 20
    assert 1 <= len(word) <= len(chunk)
    assert set(chunk).issubset(LEGAL_CHARS)
    assert set(word).issubset(LEGAL_CHARS)

    chunks = {chunk} # set for type stability with subchunks
    leaves = []
    while chunks:
        subchunks = set()
        for chunk in chunks:
            if word in chunk:
                for subchunk in remove_once(chunk, word):
                    subchunks.add(subchunk) # uniquify
            else:
                leaves.append(chunk)
        chunks = subchunks

    leaves.sort()
    return leaves[0]

def remove_once(chunk, word):
    ''' Generate all strings that can result from a removal of word from chunk.

    '''

    start = 0
    length = len(word)
    while True:
        pos = chunk.find(word, start)
        if pos == -1: # word not found code
            return
        else:
            # cut out word and rejoin
            yield chunk[:pos] + chunk[pos+length:]
            start = pos + 1 # only look for word after the previous occurrence


ans = answer('lololololo','lol')
print ans
print ans == 'looo'
ans = answer('goodgooogoogfogoood','goo')
print ans
print ans == 'dogfood'
