

def removeOuterParentheses_1(data):
    """双指针"""
    indexs = []
    left, count = 0, 0

    for i in range(len(data)):
        count += 1 if data[i] == '(' else -1
        if count == 0:
            indexs.append((left, i))
            left = i + 1
    return ''.join([data[m+1,n] for m,n in indexs])


def removeOuterParentheses_2(data):
    """单指针"""
    res, count = [], 0
    for s in data:
        if s == '(' and count > 0:
            res.append(s)
        elif s == ')' and count > 1:
            res.append(s)

        count += 1 if s == '(' else -1

    return ''.join(res)

def removeOuterParentheses_3(data):
    """栈"""
    res, stack = '', []
    for s in data:
        if s == '(':
            if stack:
                res += s
            stack.append(s)
        elif s == ')':
            stack.pop()
            if stack:
                res += s
    return res
