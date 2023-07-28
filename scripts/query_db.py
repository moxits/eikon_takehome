import psycopg2

def connect_to_db():
    connection = psycopg2.connect(user = "postgres",
                               password = "postgres",
                               host = "localhost",
                               port = "5432",
                               database = "test_db")
    return connection

def query_db():
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM results")
    records = cur.fetchall()
    print("user_id, total_experiments,average_time,most_common_compound")
    for record in records:
        print(record)

if __name__ == "__main__":
    query_db()