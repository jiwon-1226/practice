import tkinter as tk

root = tk.Tk()
root.title("회원가입")
root.geometry("500x200")

id_label = tk.Label(root, text="아이디:")
id_label.grid(row=0, column=0, pady=10)

id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=5)

#entry 옆에 버튼 하나 만들고 해당 버튼 클릭시 아아디 출력
#아이디 밑에 비밀번호도 똑같이

def re_button_click():
    print(id_entry.get())

re_button = tk.Button(root, text="중복확인", command=re_button_click)
re_button.grid(row=0, column=2)

pw_label = tk.Label(root, text="비밀번호:")
pw_label.grid(row=1, column=0, pady=10)

pw_entry = tk.Entry(root)
pw_entry.grid(row=1, column=1, padx=5)


root.mainloop()