def connect(**options):
	connParams={
	'host': options.get('host','172.16.67.100'),
	'port': options.get('port', 24),
	'user': options.get('user', ''),
	'pwd': options.get('pwd','')
	}
	print(connParams)
connect()
connect(host='172.16.68.112', port=32)
connect(port=25,user='KK_Korea_04', pwd='Is@D0ra_9')
