import tkinter as tk
from PIL import Image,ImageTk
import requests
import re
import webbrowser

#创建一个窗口
mainwin=tk.Tk()
#设置窗口大小
mainwin.geometry('800x580+200+200')
#固定窗口大小
mainwin.resizable(False, False)
#窗口的标题
mainwin.title('我们不需要VIP! VIP不属于无产阶级!!')
def show():
    num=num_int_var.get()#获取选择的窗口
    words=input_val.get()#获取输入的链接
    
    if num==1:
        link="https://okjx.cc/?url="+words
        html_data=requests.get(url=link).text
        video_url= re.findall('<iframe width="100%" height="100%" allowTransparency="true" frameborder="0" scrolling="no" allowfullscreen="true" src="(.*?)"',html_data)[0]
        webbrowser.open(video_url)

    elif num==2:
        link="https://jiexi.pengdouw.com/jiexi1/?url="+words
        html_data=requests.get(url=link).text
        video_url= re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"',html_data)[0]
        webbrowser.open(video_url)
    elif num==3:
        link="https://jiexi.pengdouw.com/jiexi2/?url="+words
        html_data=requests.get(url=link).text
        video_url= re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"',html_data)[0]
        webbrowser.open(video_url)

#窗口添加封面
img=Image.open("cover.jpg")
photo=ImageTk.PhotoImage(img)
'''
mainwin.PhotoImage(file='cover.jpg')#
# 此条代码应该已经被更新掉了，PhotoImage函数没有在窗口实例中找到
# 网上找了个替代容纳多种图片格式的实现方式
'''
#布局图片
tk.Label(master=mainwin,image=photo).pack()
#设置标签框
choose_frame=tk.LabelFrame(master=mainwin)
choose_frame.pack(pady=10,fill='both')
tk.Label(master=choose_frame,text='选择接口:',font=('仿宋',20,'bold')).pack(side=tk.LEFT)
#设置接口
#设置可变变量
num_int_var=tk.IntVar()
#设置默认value=1
num_int_var.set(1)
#设置选项按钮
tk.Radiobutton(master=choose_frame,text='1号通用VIP引擎',font=('仿宋',18),variable=num_int_var,value=1).pack(side=tk.LEFT,padx=5)
tk.Radiobutton(master=choose_frame,text='2号通用VIP引擎',font=('仿宋',18),variable=num_int_var,value=2).pack(side=tk.LEFT,padx=5)
tk.Radiobutton(master=choose_frame,text='3号通用VIP引擎',font=('仿宋',18),variable=num_int_var,value=3).pack(side=tk.LEFT,padx=5)

#设置一个接收输入链接的可变变量
input_val=tk.StringVar()
###设置输入标签框
input_frame=tk.LabelFrame(master=mainwin)
input_frame.pack(pady=10,fill='both')
tk.Label(master=input_frame,text='播放地址:',font=('仿宋',20,'bold')).pack(side=tk.LEFT)
tk.Entry(master=input_frame,width=100,borderwidth=5,font=('宋体',12,),relief='flat',textvariable=input_val).pack(side=tk.LEFT,fill='both')
#创建一个按钮
botton=tk.Button(master=mainwin,text='点击此处粉碎万恶VIP',font=('仿宋',28,'bold'),relief='flat',fg='red',bg='yellow',command=show).pack(fill='both',pady=10)
#让窗口持续出现
mainwin.mainloop()
