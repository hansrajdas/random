
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

def test():
  for s in ("''", "'", '"', "'hello'", '"my name is..."', 'hans', """'ab"d"c'""", '''"ab'd'c"'''):
    _find_quote_char_in_part(s)


if __name__ == '__main__':
    import dis
    dis.dis(_find_quote_char_in_part)
    # print(timeit.timeit('test()', setup='from __main__ import test'))
