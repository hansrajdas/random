# Fiedelity
def compressWord(word, k):
    old = word
    for c in range(97, 123):
        ch = chr(c)
        word = word.replace(ch * k, '')
    if old != word:
        return compressWord(word, k)
    return word

print(compressWord('aba', 2))
print(compressWord('baac', 2))
