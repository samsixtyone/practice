def permutation(string, mutation=''):
    if len(string) == 0:
        print(mutation)
    for i in range(len(string)):
        newMutation = mutation + string[i]
        newString = string[0:i] + string[i+1:]
        permutation(newString, newMutation)

text = "SHABIR"
print("Permutations of \"" + text + "\" is as below,")
permutation(text)

