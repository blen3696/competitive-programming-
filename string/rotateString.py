def rotateString( s, goal):
    r = len(s) -1
    l = 0
    while r>= l:
        if s == goal:
            return True
        else:
            s = s[1:] +s[0]
            r -=1
    return False

print(rotateString("abcde", "cdeab"))