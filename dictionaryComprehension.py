from string import ascii_lowercase
lettermap=dict((c,k) for k,c in enumerate(ascii_lowercase,1))
print(lettermap)
#lettermap={c:k for k,c in enumerate(ascii_lowercasse,1)}