import tkinter as tk

root = tk.Tk()
root.title("bomb")
root.geometry("600x700")
root.resizable(True, True)

by_num_c = 16
by_num_r = 24
btn_list = []

def ground():
    for c in range(by_num_c):   # 열 0~17
        for r in range(by_num_r):  # 행 0~17
            btn_list.append(("", r, c))  # 빈 텍스트

ground()
print(btn_list)

# 버튼 생성
for (text, row, col) in btn_list:
    btn = tk.Button(root, text=text, width=3, height=1)
    btn.grid(row=row, column=col, ipadx=2)

root.mainloop()

