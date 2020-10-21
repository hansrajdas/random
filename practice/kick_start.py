def check_string(s, sub):
    res = []
    for idx in range(len(s)):
        if s[idx:idx + len(sub)] == sub:
            res.append(idx)
    return res

def solve(S):
    if not S:
        return 0
    count = 0
    kick = check_string(S, 'KICK')
    start = check_string(S, 'START')
    for k in kick:
        for i in range(len(start)):
            if k < start[i]:
                count += len(start) - i
                break
    return count

def main():
    tc = int(input())
    ctr = 1
    while tc:
        s = input()
        tc -= 1
        c = solve(s.strip())
        print('Case #%d: %d' % (ctr, c))
        ctr += 1
        
if __name__ == '__main__':
    main()
