# ============================================================
# ОЮУТНЫ УДИРДЛАГЫН СИСТЕМ
# Tkinter ашигласан GUI програм
# ============================================================

# tkinter санг tk нэрээр ашиглаж байна
# GUI буюу цонхтой програм хийхэд хэрэглэгдэнэ
import tkinter as tk

# popup message (алдаа, мэдээлэл) гаргах messagebox
from tkinter import messagebox

# JSON файлтай ажиллах сан
# өгөгдлийг файлд хадгалах / унших
import json

# файл байгаа эсэх шалгах
import os


# ============================================================
# ТОГТМОЛ ХУВЬСАГЧУУД
# ============================================================

# оюутны мэдээлэл хадгалах файл
FILE_NAME = "students.json"

# багшийн нууц үг
TEACHER_PASSWORD = "admin123"

# бүх оюутны мэдээлэл хадгалах dictionary
students = {}

# шинэ оюутанд өгөх дараагийн ID
current_id = 1


# ============================================================
# ФАЙЛААС ӨГӨГДӨЛ УНШИХ
# ============================================================

def load_data():
    # global ашигласнаар function дотор
    # гаднах хувьсагчийг өөрчлөх боломжтой
    global students
    global current_id

    # файл байгаа эсэхийг шалгана
    if os.path.exists(FILE_NAME):

        # файлыг унших горимоор нээнэ
        with open(FILE_NAME, "r", encoding="utf-8") as file:

            # JSON өгөгдлийг Python dictionary болгоно
            students = json.load(file)

        # хэрвээ students хоосон биш бол
        if students:

            # хамгийн их ID-г олж дараагийн ID-г тооцоолно
            current_id = max(int(i) for i in students.keys()) + 1


# ============================================================
# ФАЙЛД ХАДГАЛАХ
# ============================================================

def save_data():

    # файлыг бичих горимоор нээнэ
    with open(FILE_NAME, "w", encoding="utf-8") as file:

        # dictionary-г JSON формат руу хөрвүүлж файлд хадгална
        json.dump(students, file, ensure_ascii=False, indent=4)


# ============================================================
# ДЭЛГЭЦ ЦЭВЭРЛЭХ
# ============================================================

def clear_screen():

    # root цонхон дээр байгаа бүх widget-ийг авна
    for widget in root.winfo_children():

        # widget бүрийг устгана
        widget.destroy()


# ============================================================
# ROLE СОНГОХ ДЭЛГЭЦ
# ============================================================

def show_role_screen():

    # өмнөх дэлгэцийг цэвэрлэнэ
    clear_screen()

    # гарчиг текст
    tk.Label(
        root,
        text="Та аль хэрэглэгч вэ?",
        font=("Arial", 16)
    ).pack(pady=20)

    # багш сонгох товч
    tk.Button(
        root,
        text="Багш",
        width=20,
        command=show_teacher_login
    ).pack(pady=10)

    # оюутан сонгох товч
    tk.Button(
        root,
        text="Оюутан",
        width=20,
        command=show_student_screen
    ).pack(pady=10)


# ============================================================
# БАГШ НЭВТРЭХ
# ============================================================

def show_teacher_login():

    # дэлгэц цэвэрлэх
    clear_screen()

    # нууц үг оруулах текст
    tk.Label(root, text="Багшийн нууц үг:").pack(pady=10)

    global password_entry

    # Entry widget
    # show="*" гэвэл нууц үг одоор харагдана
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    # нэвтрэх товч
    tk.Button(
        root,
        text="Нэвтрэх",
        command=check_password
    ).pack(pady=5)

    # буцах товч
    tk.Button(
        root,
        text="Буцах",
        command=show_role_screen
    ).pack(pady=5)


# ============================================================
# НУУЦ ҮГ ШАЛГАХ
# ============================================================

def check_password():

    # entry доторх текстийг авна
    if password_entry.get() == TEACHER_PASSWORD:

        # зөв бол багшийн хэсэг рүү орно
        show_teacher_screen()

    else:
        # буруу бол popup алдаа
        messagebox.showerror("Алдаа", "Нууц үг буруу!")


# ============================================================
# БАГШИЙН ХЭСЭГ
# ============================================================

def show_teacher_screen():

    clear_screen()

    tk.Label(root, text="Багшийн хэсэг",
             font=("Arial", 14)).pack(pady=10)

    # -------- ОЮУТАН НЭМЭХ --------

    tk.Label(root, text="Оюутны нэр:").pack()

    global name_entry
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Button(
        root,
        text="Оюутан нэмэх",
        command=add_student
    ).pack(pady=5)

    # -------- ОНОО НЭМЭХ --------

    tk.Label(root, text="Оюутны ID:").pack()

    global id_entry
    id_entry = tk.Entry(root)
    id_entry.pack()

    # хичээлийн нэр оруулах
    tk.Label(root, text="Хичээлийн нэр:").pack()

    global subject_entry
    subject_entry = tk.Entry(root)
    subject_entry.pack()

    # оноо оруулах
    tk.Label(root, text="Оноо (0-100):").pack()

    global grade_entry
    grade_entry = tk.Entry(root)
    grade_entry.pack()

    # оноо нэмэх товч
    tk.Button(
        root,
        text="Оноо нэмэх",
        command=add_grade
    ).pack(pady=5)

    # -------- ОЮУТАН УСТГАХ --------

    tk.Label(root, text="Хасах оюутны ID:").pack()

    global delete_entry
    delete_entry = tk.Entry(root)
    delete_entry.pack()

    tk.Button(
        root,
        text="Оюутан хасах",
        command=delete_student
    ).pack(pady=5)

    # -------- СТАТИСТИК ХАЙХ --------

    tk.Label(root, text="Статистик харах оюутны нэр:").pack()

    global search_entry
    search_entry = tk.Entry(root)
    search_entry.pack()

    tk.Button(
        root,
        text="Статистик",
        command=show_statistics
    ).pack(pady=10)

    tk.Button(
        root,
        text="Буцах",
        command=show_role_screen
    ).pack(pady=10)


# ============================================================
# ОЮУТНЫ ХЭСЭГ
# ============================================================

def show_student_screen():

    clear_screen()

    tk.Label(root,
             text="Оюутны жагсаалт",
             font=("Arial", 14)).pack(pady=10)

    # бүх оюутныг давталтаар харуулна
    for student_id, data in students.items():

        # хичээл + оноог нэг мөр текст болгоно
        grades_text = ", ".join(
            f"{g['subject']}:{g['grade']}" for g in data["grades"]
        )

        text = (
            f"ID: {student_id} | "
            f"{data['name']} | "
            f"Дүн: {grades_text}"
        )

        tk.Label(root, text=text).pack()

    tk.Button(
        root,
        text="Буцах",
        command=show_role_screen
    ).pack(pady=10)


# ============================================================
# ОЮУТАН НЭМЭХ
# ============================================================

def add_student():

    global current_id

    # нэрийг entry-ээс авна
    name = name_entry.get()

    # хоосон эсэхийг шалгана
    if name == "":
        messagebox.showerror("Алдаа", "Нэр хоосон!")
        return

    # шинэ ID
    student_id = str(current_id)

    # dictionary-д шинэ оюутан нэмнэ
    students[student_id] = {
        "name": name,
        "grades": []
    }

    # дараагийн ID
    current_id += 1

    # файлд хадгална
    save_data()

    messagebox.showinfo("Амжилттай",
                        f"ID {student_id} нэмэгдлээ!")


# ============================================================
# ОНОО НЭМЭХ
# ============================================================

def add_grade():

    # ID авна
    student_id = id_entry.get()

    # хичээлийн нэр авна
    subject = subject_entry.get()

    # оноог integer болгоно
    try:
        grade = int(grade_entry.get())
    except ValueError:
        messagebox.showerror("Алдаа", "Оноо тоо байх ёстой!")
        return

    # ID байгаа эсэх
    if student_id not in students:
        messagebox.showerror("Алдаа", "ID байхгүй!")
        return

    # онооны хязгаар
    if grade < 0 or grade > 100:
        messagebox.showerror("Алдаа", "0-100 хооронд!")
        return

    # хичээлийн нэр хоосон эсэх
    if subject == "":
        messagebox.showerror("Алдаа", "Хичээлийн нэр бич!")
        return

    # dictionary-д оноо нэмэх
    students[student_id]["grades"].append({
        "subject": subject,
        "grade": grade
    })

    # файлд хадгалах
    save_data()

    messagebox.showinfo("Амжилттай", "Оноо нэмэгдлээ!")


# ============================================================
# ОЮУТАН УСТГАХ
# ============================================================

def delete_student():

    student_id = delete_entry.get()

    if student_id not in students:
        messagebox.showerror("Алдаа", "ID байхгүй!")
        return

    # dictionary-с устгана
    del students[student_id]

    save_data()

    messagebox.showinfo("Амжилттай", "Устгагдлаа!")


# ============================================================
# СТАТИСТИК
# ============================================================

def show_statistics():

    # нэр авах
    name = search_entry.get()

    found = None

    # нэрээр хайх
    for student in students.values():
        if student["name"].lower() == name.lower():
            found = student
            break

    if found is None:
        messagebox.showerror("Алдаа", "Оюутан олдсонгүй!")
        return

    grades = found["grades"]

    if not grades:
        messagebox.showinfo("Статистик", "Оноо байхгүй!")
        return

    grades_text = ""
    grade_list = []

    # бүх хичээлийн оноо
    for g in grades:
        grades_text += f"{g['subject']} : {g['grade']}\n"
        grade_list.append(g["grade"])

    # хамгийн их
    maximum = max(grade_list)

    # хамгийн бага
    minimum = min(grade_list)

    messagebox.showinfo(
        "Статистик",
        f"Оюутан: {found['name']}\n\n"
        f"Хичээлүүд:\n{grades_text}\n"
        f"Хамгийн их оноо: {maximum}\n"
        f"Хамгийн бага оноо: {minimum}"
    )


# ============================================================
# ПРОГРАМ ЭХЛҮҮЛЭХ
# ============================================================

# үндсэн GUI цонх үүсгэнэ
root = tk.Tk()

# цонхны гарчиг
root.title("Оюутны удирдлагын систем")

# цонхны хэмжээ
root.geometry("450x550")

# файл уншина
load_data()

# эхний дэлгэц
show_role_screen()

# програмыг тасралтгүй ажиллуулна
root.mainloop()