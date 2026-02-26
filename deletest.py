import sqlite3

# เชื่อมต่อกับฐานข้อมูล
conn = sqlite3.connect("car_db.sqlite")
cursor = conn.cursor()

# ลบข้อมูลที่ id = 3
cursor.execute("DELETE FROM car WHERE id = 3")

# บันทึกการเปลี่ยนแปลง
conn.commit()

# ปิดการเชื่อมต่อ
conn.close()

print("ลบข้อมูล id=3 เรียบร้อยแล้ว")