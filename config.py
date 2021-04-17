# DB access
with open('C:\\Users\\micha\\OneDrive\\Pulpit\\keys\\db_access_local.txt') as file:
    credentials = (file.read()).split(',')
    user = credentials[0]
    password = credentials[1]
    host = credentials[2]
    port = credentials[3]
    database = credentials[4]

db_address = 'postgresql://{}:{}@localhost:{}/{}'.format(user, password, port, database)
