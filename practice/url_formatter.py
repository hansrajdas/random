def format_url(s):
    spaces = 0
    for c in s:
        if c == ' ':
            spaces += 1
    res = list(s) + ['' for _ in range(spaces * 2)]
    res_idx = len(res) - 1
    idx = len(s) - 1
    while idx:
        if res[idx] == ' ':
            res[res_idx] = '0'
            res[res_idx - 1] = '2'
            res[res_idx - 2] = '%'
            res_idx -= 2
        else:
            res[res_idx] = res[idx]
        idx -= 1
        res_idx -= 1
    return ''.join(res)


assert format_url("https://hello world") == "https://hello%20world"
assert format_url("name-1") == "name-1"
