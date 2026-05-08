import os

def restore_my_termux():
    print("--- بدأ عملية استعادة أدوات خالد ---")

    # 1. تثبيت الأدوات من ملف my_tools.txt
    if os.path.exists("my_tools.txt"):
        with open("my_tools.txt", "r") as file:
            tools = file.readlines()
            for tool in tools:
                tool_name = tool.strip()
                if tool_name:
                    print(f"جاري تثبيت: {tool_name}...")
                    os.system(f"pkg install {tool_name} -y")
    else:
        print("⚠️ تنبيه: ملف my_tools.txt غير موجود")

    # 2. فحص العناصر بالمنطق الذي طلبته
    print("\n--- فحص المجلدات والملفات الاحتياطية ---")
    if os.path.exists("folders_list.txt"):
        with open("folders_list.txt", "r") as file:
            items = file.readlines()
            for item in items:
                name = item.strip()
                if not name: continue
                
                # إذا كان مجلداً (وعادة المجلد يحتوي ملفات)
                if os.path.isdir(name):
                    print(f"✅ مجلد موجود: {name}")
                # إذا كان ملفاً وليس مجلدًا
                elif os.path.isfile(name):
                    print(f"🥸 ملف موجود: {name}")
                # إذا لم يجد شيئاً
                else:
                    print(f"❌ مفقود: {name}")
    
    print("\n--- تمت العملية بنجاح! ---")

if __name__ == "__main__":
    restore_my_termux()

