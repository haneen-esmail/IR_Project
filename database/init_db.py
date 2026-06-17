import sqlite3

# إنشاء الاتصال بقاعدة البيانات
conn = sqlite3.connect("database/ir.db")
cursor = conn.cursor()

# إنشاء جدول المستندات مع الحقول المطلوبة لمستويات المعالجة
cursor.execute("""
CREATE TABLE IF NOT EXISTS documents(
    doc_id TEXT PRIMARY KEY,
    text TEXT,
    processed_text TEXT,
    light_clean_text TEXT
)
""")

# إنشاء جدول الاستعلامات
cursor.execute("""
CREATE TABLE IF NOT EXISTS queries(
    query_id TEXT PRIMARY KEY,
    text TEXT
)
""")

# إنشاء جدول التقييمات (qrels)
cursor.execute("""
CREATE TABLE IF NOT EXISTS qrels(
    query_id TEXT,
    doc_id TEXT,
    relevance INTEGER
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")