def check_string(s):
    current = None
    for i in s:
        print(i, end="")
        if i =="1":
            if current == None:
                current = 1
            elif current == 0:
                return False
        else:
            if current == 1:
                current = 0
        
    # return True
    return not('0' in s.strip('0'))

print(check_string("1001"))
