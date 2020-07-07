from cassandra.cluster import Cluster
clstr=Cluster()
session=clstr.connect('cms')
qry= '''
create table students (
   studentID int,
   name text,
   age int,
   marks int,
   primary key(studentID)
);'''
session.execute(qry)
