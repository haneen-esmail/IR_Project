import sqlite3

conn = sqlite3.connect("database/ir.db")
cursor = conn.cursor()

cursor.execute("""
SELECT text, light_clean_text, processed_text
FROM documents
LIMIT 3
""")

for row in cursor.fetchall():
    print(row)