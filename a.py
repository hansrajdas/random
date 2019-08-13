def _find_quote_char_in_part(part):
    if '"' not in part and "'" not in part:
        return
    quote_char = None
    double_quote = part.find('"')
    single_quote = part.find("'")
    if double_quote >= 0 and single_quote == -1:
        quote_char = '"'
    elif single_quote >= 0 and double_quote == -1:
        quote_char = "'"
    elif double_quote < single_quote:
        quote_char = '"'
    elif single_quote < double_quote:
        quote_char = "'"
    return quote_char

def myfun(part):
    """
    Returns single or double quote character whichever appears first in given
    string. None is returned if given string don't have single or double quote
    character.
    """
    quote_char = None
    for ch in part:
        if ch in ('"', "'"):
            quote_char = ch
            break
    return quote_char


assert _find_quote_char_in_part("''") == myfun("''")
assert _find_quote_char_in_part("'") == myfun("'")
assert _find_quote_char_in_part('"') == myfun('"')
assert _find_quote_char_in_part("'hello'") == myfun("'hello'")
assert _find_quote_char_in_part('"my name.."') == myfun('"my name is..."')
assert _find_quote_char_in_part('hans') == myfun('hans')
assert _find_quote_char_in_part("""'ab"d"c'""") == myfun("""'ab"d"c'""")
assert _find_quote_char_in_part('''"ab'd'c"''') == myfun('''"ab'd'c"''')
