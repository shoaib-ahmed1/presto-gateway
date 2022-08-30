from trino.dbapi import connect

def totalRunningQueries():
    conn = connect(
        host="coordinator",
        port=8001,
        user="adhoc"
    )
    cur = conn.cursor()
    #print(cur.stats)
    cur.execute("select count(1) from system.runtime.queries where state=\'RUNNING\'")
    rows = cur.fetchone()
    return rows[0]

if __name__ == "__main__":
    totalRunningQueries()
