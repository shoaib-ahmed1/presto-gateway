from trino.dbapi import connect
import sys

def runDummyQueries(argv):

    try:
        conn = connect(
            host=str(argv[0]),
            port=argv[1],
            user="adhoc"
        )
        cur = conn.cursor()

        list = []
        queries = [
            "select count(1) from(select * from tpch.tiny.part limit 1)",
            "select count(1) from(select * from tpch.tiny.orders limit 1)",
            # "select count(*) from tpch.tiny.supplier limit 1",
            # "select count(*) from tpch.tiny.orders limit 1",
        ]

        for query in queries:
            cur.execute(query)
            rows = cur.fetchone()
            # print(rows)
            # print(cur.rowcount)
            list.append(rows[0])

        cur.close()
        conn.close()
        #print(list)
        return (0 in list)
    except :
        #print("Unknown error occurred")
        return True


if __name__ == "__main__":
    sys.stdout.write(str(runDummyQueries(sys.argv[1:])))
