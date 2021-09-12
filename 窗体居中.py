# 2021年8月 Python 自学
import tkinter as tk
import tkinter.font as font
root = tk.Tk()
fc = font.Font(size=20, family='华文行楷')#设定字体参数，必须建立在窗体循环内部
root.title('学校信息管理')#设置窗口标题
root_w=800
root_h=600 #分别设置窗体的宽高值
scr_w=root.winfo_screenwidth()
scr_h=root.winfo_screenheight()#分别获取当前屏幕的分别率宽高值
x=(scr_w-root_w)/2
y=(scr_h-root_h)/2#计算窗体的起点坐标值x,y
root.geometry('%dx%d+%d+%d' %(root_w,root_h/2,x,y))#初始化窗体尺寸与位置
lab1=tk.Label(root, text=f'起始坐标为x={x},y={y}', font=fc)#实例化标签，调用字体设置
lab1.pack(fill='x',side='bottom')#布局标签
root.mainloop()