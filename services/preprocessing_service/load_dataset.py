import sqlite3
import ir_datasets

DB_PATH = "database/ir.db"

dataset = ir_datasets.load("beir/quora/test")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("Loading documents...")

count = 0

for doc in dataset.docs_iter():
    cursor.execute("""
        INSERT OR IGNORE INTO documents
        (doc_id, text)
        VALUES (?, ?)
    """, (
        doc.doc_id,
        doc.text
    ))

    count += 1

    if count % 10000 == 0:
        print(f"{count} docs loaded")

conn.commit()

print("Loading queries...")

for query in dataset.queries_iter():

    cursor.execute("""
        INSERT OR IGNORE INTO queries
        (query_id, text)
        VALUES (?, ?)
    """, (
        query.query_id,
        query.text
    ))

conn.commit()

print("Loading qrels...")

for qrel in dataset.qrels_iter():

    cursor.execute("""
        INSERT INTO qrels
        (query_id, doc_id, relevance)
        VALUES (?, ?, ?)
    """, (
        qrel.query_id,
        qrel.doc_id,
        qrel.relevance
    ))

conn.commit()
conn.close()

print("Dataset Loaded Successfully")