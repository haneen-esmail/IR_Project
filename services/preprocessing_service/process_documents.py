import sqlite3

from cleaner import light_clean, heavy_clean

DB_PATH = "database/ir.db"
BATCH_SIZE = 1000

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

total_processed = 0

while True:

    cursor.execute("""
        SELECT doc_id, text
        FROM documents
        WHERE processed_text IS NULL
        LIMIT ?
    """, (BATCH_SIZE,))

    rows = cursor.fetchall()

    if not rows:
        break

    updates = []

    for doc_id, text in rows:

        updates.append(
            (
                heavy_clean(text),
                light_clean(text),
                doc_id
            )
        )

    cursor.executemany("""
        UPDATE documents
        SET processed_text = ?,
            light_clean_text = ?
        WHERE doc_id = ?
    """, updates)

    conn.commit()

    total_processed += len(rows)

    print(f"Processed: {total_processed}")

conn.close()

print("Finished Successfully")