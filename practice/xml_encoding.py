#!/usr/bin/python

# Date: 2020-mm-dd
#
# Description:
#
# Approach:
#
# Complexity:


def xml_encoding(xml, i, tag, codes, res):
    if i > len(xml) - 1:
        return
    elif xml[i] == '<':
        xml_encoding(xml, i + 1, tag, codes, res)
    elif xml[i] == '>':
        res.append(0)
        xml_encoding(xml, i + 1, tag, codes, res)
    elif xml[i] in (' ', '=', '"'):
        if tag in codes:
            res.append(codes[tag])
        else:
            if tag:
                res.append(tag)
        xml_encoding(xml, i + 1, "", codes, res)
    else:
        xml_encoding(xml, i + 1, tag + xml[i], codes, res)

def main():
    xml = ('<family lastName="McDowell" state="CA">'
           '  <person firstName="Gayle">Some message</person>'
           '</family>')
    codes = {
        'family': 1,
        'person': 2,
        'firstName': 3,
        'lastName': 4,
        'state': 5
    }
    res = []
    xml_encoding(xml, 0, "", codes, res)
    print(res)

main()
