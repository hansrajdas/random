import re

text = 'With ADP newer ADJ form NOUN of ADP digital ADJ storage NOUN devices NOUN , PUNCT large ADJ screen NOUN readers NOUN and CCONJ'
# r2 = re.compile(r'(\w+ (ADJ|NOUN))* (\w+ NOUN)')
# r1 = r2.findall(text)
# print(r1)
# i = 0
# while i < len(r1):
#     match = [r1[i]]
#     j = i + 1
#     while j < len(r1) and not r1[j][0]:
#         match.append(r1[j])
#         j += 1
#     i = j
#     print(' '.join('%s %s' % (t[0], t[2]) for t in match))

pattern = re.compile(r'( *\w+ (ADJ|NOUN))* *\w+ NOUN')
p = pattern.search(text, 0)
if not p:
    print('No pattern found')
    exit(0)
while p:
    print (p.group())
    i = p.end()
    print(i)
    p = pattern.search(text, i)
