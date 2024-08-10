import psycopg2
import sys
import os

try:
    database = sys.argv[1]
    connection = psycopg2.connect(user=os.environ.get('PGUSER'),
                                  password=os.environ.get('PGPASSWORD'),
                                  database = database,
                                  host=os.environ.get('PGHOST'),
                                  port=os.environ.get('PGPORT'))
    
    cursor = connection.cursor()
    
    def datee():
        with open("date.txt") as f:
            data = f.read()
            new = data.split(" ")
            return str(new[0])
    
    query = f"select name from referees where referee_id = (select mr.referee from matches m, match_referees mr where m.match_num = mr.match_num and m.match_date = '{datee()}')"
    
    cursor.execute(query)
    
    for i in cursor.fetchall():
        name = i[0].split(" ")
        if len(name) == 1:
            print(i[0])
        elif len(name) == 2:
            print(f"{name[0]} {name[1][0]}.")
        elif len(name) == 3:
            print(f"{name[0]} {name[1][0]}. {name[2][0]}.")
        
    
    cursor.close()
    connection.close()


except (Exception, psycopg2.DatabaseError) as e:
    print(e)
        
