names=['Victor Omondi', 'Ann Wanjiku', 'Miriam Muthoni', 'Peter Mutisya']
campus=['MMU', 'KU', None, 'PU']
info=list(zip(names,campus))
print(info)
info2=list(map(lambda *a: a,names,campus))
print(info2)