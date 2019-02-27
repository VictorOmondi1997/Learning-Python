#Chain map is provided for quicky linking a number of mappings so they can be treated as a single unit
from collections import ChainMap
default_connection={'host': 'localhost', 'port': 4567}
connection = {'port': 5678}
conn = ChainMap(connection, default_connection)
print(conn['port'])
print(conn['host'])
print(conn.maps)
conn['host']= 'victoromondi.ml' # Add host
print(conn.maps)


#Remove the port information
del conn['port']
print(conn.maps)

#Port will be fetched from the second deictionary
print(conn['port'])
print(dict(conn))

