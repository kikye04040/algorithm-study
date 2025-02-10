def is_vps(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                return "NO"
    if stack:
        return "NO"
    else:
        return "YES"
    
T = int(input())

for _ in range(T):
    s = input().strip()
    print(is_vps(s))
