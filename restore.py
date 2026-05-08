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
        print("خطأ: لم يتم العثور على ملف my_tools.txt")

    # 2. التأكد من وجود المجلدات من ملف folders_list.txt
    print("\n--- فحص المجلدات والمشاريع ---")
    if os.path.exists("folders_list.txt"):
        with open("folders_list.txt", "r") as file:
            folders = file.readlines()
            for folder in folders:
                folder_name = folder.strip()
                if os.path.isdir(folder_name):
                    print(f"✅ المجلد موجود: {folder_name}")
                else:
                    print(f"❌ المجلد مفقود: {folder_name} (قد تحتاج لتحميله مرة أخرى)")
    
    print("\n--- تمت العملية بنجاح! ---")

if __name__ == "__main__":
    restore_my_termux()

