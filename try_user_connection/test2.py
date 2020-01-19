from sqlalchemy import create_engine

db_string = 'postgresql://postgres:NatashaNyasha@192.168.0.103:5432/Sanatorium2'
# db_string = 'postgresql://postgres:NatashaNyasha@172.20.10.7:5432/Sanatorium2'
# '172.20.10.7:5432//postgres:NatashaNyasha@nata_host/Sanatorium2'
db = create_engine(db_string)

# Read
result_set = db.execute("SELECT * FROM living_room")
result_resident = db.execute("SELECT * FROM resident WHERE name = 'Anton'")
for r in result_resident:
    print(r)

import os
print(os.environ['DATABASE_URL'])