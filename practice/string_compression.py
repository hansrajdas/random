def string_compression(s):
    if not s:
        return s
    comp = []
    last_char = s[0]
    char_count = 1
    for c in s[1:]:
        if last_char == c:
            char_count += 1
        else:
            comp.append(f'{last_char}{char_count}')
            last_char = c
            char_count = 1
    comp.append(f'{last_char}{char_count}')
    new = ''.join(comp)
    return new if len(new) < len(s) else s

assert string_compression('aabbbcddd') == 'a2b3c1d3'
assert string_compression('abcd') == 'abcd'
assert string_compression('abbcd') == 'abbcd'
assert string_compression('aaaaa') == 'a5'
