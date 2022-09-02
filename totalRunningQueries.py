import sys
from trino.dbapi import connect

def totalRunningQueries(argv):
    conn = connect(
        host=str(argv[0]),
        port=8080,
        user="adhoc"
    )
    cur = conn.cursor()
    #print(cur.stats)
    cur.execute("select count(1) from system.runtime.queries where state=\'RUNNING\'")
    rows = cur.fetchone()
    return rows[0]

if __name__ == "__main__":
    sys.stdout.write(str(totalRunningQueries(sys.argv[1:])))
