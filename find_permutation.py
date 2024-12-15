


def find_p(s):
    if len(s) == 1: return [s]
    permutations=[]
    for i in range(len(s)):
        current_ch = s[i]
        remaining_ch = s[:i] + s[i+1:]
        print (remaining_ch)
        perms = find_p(remaining_ch)
        print (perms)  
       # for p in perms:
        #    permutations.append(current_ch + p)


if __name__ == "__main__":
    find_p('abc')
