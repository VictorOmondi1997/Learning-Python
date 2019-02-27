sname = 'Omondi'
letters1 = set(c for c in sname)
letters2 = {c for c in sname} # same as letters1
print(letters1)
print(letters1==letters2)