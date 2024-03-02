import tkinter as tk
root = tk.Tk()  ## root of the box instance
root.title('simple calculator') ## box name
root.geometry('415x400+100+100')## box layout

root.attributes("-alpha", 0.9)## layout color and transparency
root["background"] = "#ffffff" ## background color = white


result_num = tk.StringVar() ## define result number, which is gonna be a Variable
result_num.set (0) ## set default number of result to 0

font = ('Arial', 20) ##define a font for further use
tk.Label(root,
         textvariable=result_num, font = font, height =2, width=20, justify=tk.LEFT, anchor = tk.SE, bg = "#ffffff").grid(row = 1, column = 1, columnspan= 4)
## set the lable (layout)
## grid result's lable, which is across 4 column to the rightest
## justify the location of result var

## define the function buttons of first row
button_clear = tk.Button(root, text = 'C', width = 5, font = font, relief=tk. FLAT, bg = '#808080')
button_back = tk.Button(root, text = '←', width = 5, font = font, relief=tk. FLAT, bg = '#808080')
button_div  = tk.Button(root, text = '/', width = 5, font = font, relief=tk. FLAT, bg = '#808080')
button_mul = tk.Button(root, text = '×', width = 5, font = font, relief=tk. FLAT, bg = '#808080')
## define the layout the above bottons
## use row/column to define where the button is, use padx/pady to add gaps bewteen the buttons
button_clear.grid(row = 2, column = 1, padx = 4, pady = 2) 
button_back.grid(row = 2, column = 2, padx = 4, pady = 2)
button_div.grid(row = 2, column = 3, padx = 4, pady = 2)
button_mul.grid(row = 2, column = 4, padx = 4, pady = 2)

## define the function buttons of second row
button_7= tk.Button(root, text = '7', width = 5, font = font, relief=tk. FLAT, bg = '#f0cf9e')
button_8 = tk.Button(root, text = '8', width = 5, font = font, relief=tk. FLAT, bg = '#f0cf9e')
button_9  = tk.Button(root, text = '9', width = 5, font = font, relief=tk. FLAT, bg = '#f0cf9e')
button_mi = tk.Button(root, text = '－', width = 5, font = font, relief=tk. FLAT, bg = '#808080')
## define the layout the second row bottons
## use row/column to define where the button is, use padx/pady to add gaps bewteen the buttons
button_7.grid(row = 3, column = 1, padx = 4, pady = 2) 
button_8.grid(row = 3, column = 2, padx = 4, pady = 2)
button_9.grid(row = 3, column = 3, padx = 4, pady = 2)
button_mi.grid(row = 3, column = 4, padx = 4, pady = 2)

## define the function buttons of third row
button_4= tk.Button(root, text = '4', width = 5, font = font, relief=tk. FLAT, bg = '#f0cf9e')
button_5 = tk.Button(root, text = '5', width = 5, font = font, relief=tk. FLAT, bg = '#f0cf9e')
button_6  = tk.Button(root, text = '6', width = 5, font = font, relief=tk. FLAT, bg = '#f0cf9e')
button_add = tk.Button(root, text = '＋', width = 5, font = font, relief=tk. FLAT, bg = '#808080')
## define the layout the second row bottons
## use row/column to define where the button is, use padx/pady to add gaps bewteen the buttons
button_4.grid(row = 4, column = 1, padx = 4, pady = 2) 
button_5.grid(row = 4, column = 2, padx = 4, pady = 2)
button_6.grid(row = 4, column = 3, padx = 4, pady = 2)
button_add.grid(row = 4, column = 4, padx = 4, pady = 2)

## define the function buttons of forth row
button_1= tk.Button(root, text = '1', width = 5, font = font, relief=tk. FLAT, bg = '#f0cf9e')
button_2 = tk.Button(root, text = '2', width = 5, font = font, relief=tk. FLAT, bg = '#f0cf9e')
button_3  = tk.Button(root, text = '3', width = 5, font = font, relief=tk. FLAT, bg = '#f0cf9e')
button_eq = tk.Button(root, text = '=', width = 5, height = 3, font = font, relief=tk. FLAT, bg = '#808080')
## define the layout the second row bottons
## use row/column to define where the button is, use padx/pady to add gaps bewteen the buttons
button_1.grid(row = 5, column = 1, padx = 4, pady = 2) 
button_2.grid(row = 5, column = 2, padx = 4, pady = 2)
button_3.grid(row = 5, column = 3, padx = 4, pady = 2)
button_eq.grid(row = 5, column = 4, padx = 4, pady = 2)

## define layout of last row
##问题出现了，此时最后一行只有0，小数点，及一个从第五行延展下来的=，那怎么做呢
button_0= tk.Button(root, text = '0', width = 12, font = font, relief=tk. FLAT, bg = '#f0cf9e')
button_dot = tk.Button(root, text = '.', width = 5, font = font, relief=tk. FLAT, bg = '#f0cf9e')
##首先固定好0和dot的位置
button_0.grid(row = 6, column = 1, padx = 4, pady = 2) 
button_dot.grid(row = 6, column = 3, padx = 4, pady = 2)
## 然后扩展=的这个框的大小,让他横跨两行，rowspan负责让他横跨上下两行，height这个属性让他显示的框也增大到3,因为height属于他的自身属性，所以必须补充填写到定义它的代码中，grid属于操作方法，可以后期添加
button_eq.grid(rowspan = 2)
button_0.grid(columnspan = 2)


## now we are going to make the calculation logic
## Logic: 1.when the button clicked,the number and formula will be shown and added onto the result box
## 2. when the equal button is clicked, the result will be shown

## so first, define what a function call click button, to define what will go on when the button is clicked
def click_button(temp):
    print('temp:\t', temp) ## formulate the input, show input in the command area
    result_num.set(result_num.get()+temp)  ## everytime the number is put in, get it self and make the following number behind

##define click event, when the button clicked, run click_button function
button_1.config(command=lambda : click_button('1')) ## when button_1 is clicked, return 1
button_2.config(command=lambda : click_button('2'))
button_3.config(command=lambda : click_button('3'))
button_4.config(command=lambda : click_button('4'))
button_5.config(command=lambda : click_button('5'))
button_6.config(command=lambda : click_button('6'))
button_7.config(command=lambda : click_button('7'))
button_8.config(command=lambda : click_button('8'))
button_9.config(command=lambda : click_button('9'))
button_0.config(command=lambda : click_button('0'))
button_add.config(command=lambda : click_button('+'))
button_mi.config(command=lambda : click_button('-'))
button_div.config(command=lambda : click_button('/'))
button_mul.config(command=lambda : click_button('*'))

##most important part, the equal. make a math run with it
def calculation():
    formula = result_num.get() ## combine everything input as a formula
    new_formula = formula[1:] ##只取第二个字符串开始的数据，不要0
    result = eval(new_formula) ## use eval() to calculate formula
    result_num.set(str(result)) ## use str() to formulate the result
button_eq.config(command=calculation)

root.mainloop()