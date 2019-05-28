# Fractal Analytics
def longestEvenWord(sentence):
  sentence = sentence.split(' ')
  max_len_word = '00'
  for word in sentence:
    if not (len(word) % 2) and (len(max_len_word) < len(word) or max_len_word == '00'):
      max_len_word = word
  return max_len_word


print longestEvenWord('It is a pleasant day today')
print longestEvenWord('time to write great code')
print longestEvenWord('codes for man')
print longestEvenWord('co fo ma')
