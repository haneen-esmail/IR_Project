import sqlite3

conn = sqlite3.connect("database/ir.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM documents")
print("documents:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM queries")
print("queries:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM qrels")
print("qrels:", cursor.fetchone()[0])

conn.close()