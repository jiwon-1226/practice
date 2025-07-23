import tkinter as tk

root = tk.Tk()
root.geometry("800x600")

# label1 = tk.Label(root, text="텍스트1")
# label1.place(x=0, y=0)
#
# label2 = tk.Label(root, text="텍스트2")
# label2.place(x=0, y=200)
#
# label3 = tk.Label(root, text="텍스트3")
# label3.place(x=300, y=300)
#
# label4 = tk.Label(root, text="텍스트4")
# label4.place(x=500, y=0)

label1 = tk.Label(root, text="텍스트1", bg="blue")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="텍스트2", bg="yellow")
label2.grid(row=1, column=0)

label3 = tk.Label(root, text="텍스트3", bg="red")
label3.grid(row=2, column=0, rowspan=2) #빈공간을 비워두지 않음 => rowspan 쓰기(근데 왜 안돼!?)

label4 = tk.Label(root, text="텍스트4", bg="pink")
label4.grid(row=4, column=0)

label5 = tk.Label(root, text="텍스트5", bg="pink")
label5.grid(row=0, column=1)

label6 = tk.Label(root, text="텍스트6", bg="pink")
label6.grid(row=0, column=2)

label7 = tk.Label(root, text="텍스트7", bg="pink")
label7.grid(row=2, column=1, columnspan=2)

label8 = tk.Label(root, text="텍스트8", bg="pink")
label8.grid(row=0, column=3)



root.mainloop()
