
def _find_quote_char_in_part(part):
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

def test():
  for s in ("''", "'", '"', "'hello'", '"my name is..."', 'hans', """'ab"d"c'""", '''"ab'd'c"'''):
    _find_quote_char_in_part(s)


if __name__ == '__main__':
    import dis
    dis.dis(_find_quote_char_in_part)
    # print(timeit.timeit('test()', setup='from __main__ import test'))
