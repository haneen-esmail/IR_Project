import os

def check_database():
    db_path = "database/ir.db"
    
    # التأكد من وجود المجلد
    if not os.path.exists("database"):
        os.makedirs("database")
        
    # التأكد من وجود الملف
    if not os.path.exists(db_path):
        print("⚠️ تنبيه: قاعدة البيانات (ir.db) غير موجودة.")
        print("يرجى تحميلها من هذا الرابط: [ضعي رابط الدرايف الخاص بكِ هنا]")
        print("بعد التحميل، ضعِ الملف داخل مجلد 'database'.")
        return False
    return True

if __name__ == "__main__":
    if check_database():
        print("✅ قاعدة البيانات موجودة. جاري تشغيل النظام...")
        # هنا تكملين كود تشغيل النظام الخاص بكِ
    else:
        print("❌ تعذر التشغيل. يرجى إكمال الخطوات أعلاه.")