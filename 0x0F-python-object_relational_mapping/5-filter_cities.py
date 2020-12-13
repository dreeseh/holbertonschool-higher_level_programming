#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa"""


def connectToDB():
    """connect to database"""
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset='utf8')
    cur = conn.cursor()

    cur.execute("SELECT cities.name \
                 FROM cities INNER JOIN states ON cities.state_id=states.id \
                 WHERE states.name=%s \
                 ORDER BY cities.id ASC", (sys.argv[4],))

    query_rows = cur.fetchall()

    items = []
    for row in query_rows:
        items.append(row[0])

    print(', '.join(items))

    cur.close()
    conn.close()

if __name__ == '__main__':
    import MySQLdb
    import sys
    connectToDB()
