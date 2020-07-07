from cassandra.cluster import Cluster
clstr=Cluster()
session=clstr.connect('cms')
session.execute("insert into students (studentID, name, age, marks) values (1, 'Juhi',20, 200);")
