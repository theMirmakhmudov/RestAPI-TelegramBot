import psycopg2

conn = psycopg2.connect(database="a10",
                        user="postgres",
                        password="mirmakhmudov16",
                        host="localhost",
                        port=5432)

cursor = conn.cursor()  # creating a cursor
cursor.execute("""
CREATE TABLE IF NOT EXISTS new
(
    id serial PRIMARY KEY NOT NULL,
    fullname VARCHAR(255)  NOT NULL,
    username VARCHAR(255) NOT NULL,
    user_id BIGINT NOT NULL
)
""")
conn.commit()
conn.close()