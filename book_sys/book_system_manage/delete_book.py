from tkinter import *
import sqlite3
import time
import tkinter.messagebox as messagebox

#检查书号错误
def check_number(book_number):
	book_number = int(book_number)
	if len(str(book_number)) != 6:
		return False
	else:
		return True

def check_delete_book():
	while 1:
		conn = sqlite3.connect("D:/BookManagerSys.db")
		curs = conn.cursor()
		if len(number.get()) == 0:
			messagebox.showerror('错误', '请确认为书号信息不能为空！')
			break
		else:
			if check_number(number.get()) == False:  # 检查书号是否错误
				messagebox.showerror("图书添加失败", "请重新输入书号(6位数字)：")
				break
			else:
				query = 'delete from book where number = %s' % (number.get())
				sql_sel ='select number from  book  where number = %s'%(number.get())
				sql = curs.execute(sql_sel)
				def is_exit():
					for row in sql:
						return row[0]
				if is_exit() == number.get():
					curs.execute(query)
					conn.commit()
					messagebox.showinfo("成功", "图书删除成功！")
				else:
					messagebox.showerror("图书删除失败", "不存在")
				break
		conn.close()
#添加书目信息
def delete_book():
	win = Toplevel()
	win.geometry('520x166')
	win.title('图书库存管理系统')
	group = LabelFrame(win,text="修改图书修改信息",font=('华文新魏','16'))
	global number
	number = StringVar()
	txt6 = StringVar()
	txt6.set("请输入删除的图书信息")
	lab1 = Label(group, text="书号：", font=('华文新魏','16'))
	lab6 = Label(group,textvariable=txt6, relief='ridge', width=18, font=('华文新魏','16'))
	entry1 = Entry(group, textvariable=number, width=16, font=('宋体','16'))
	button = Button(group, text='提交', command=check_delete_book, font=('宋体','16'))
	#布局设置
	group.grid(row=0, column=0,padx=5,pady=5)
	lab1.grid(row=1, column=0)
	lab6.grid(row=2, column=0,columnspan=2)
	entry1.grid(row=1, column=1)
	button.grid(row=2, column=2)
	photo = PhotoImage(file="cat.gif")
	imgLabel = Label(win, image=photo)
	imgLabel.grid(row=0, column=3)
	mainloop()
