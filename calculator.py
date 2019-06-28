import tkinter
window  = tkinter.Tk()
window.title("CASS calculator")

x = 390
y = 280

numbers = {"0":tkinter.PhotoImage(file = r"images/10.gif"),
           "1":tkinter.PhotoImage(file = r"images/1.gif"),
           "2":tkinter.PhotoImage(file = r"images/2.gif"),
           "3":tkinter.PhotoImage(file = r"images/3.gif"),
           "4":tkinter.PhotoImage(file = r"images/4.gif"),
           "5":tkinter.PhotoImage(file = r"images/5.gif"),
           "6":tkinter.PhotoImage(file = r"images/6.gif"),
           "7":tkinter.PhotoImage(file = r"images/7.gif"),
           "8":tkinter.PhotoImage(file = r"images/8.gif"),
           "9":tkinter.PhotoImage(file = r"images/9.gif"),
           "10":tkinter.PhotoImage(file = r"images/empty.gif"),
           ".":tkinter.PhotoImage(file = r"images/dot.gif"),
           "-":tkinter.PhotoImage(file = r"images/minus.gif"),
           "gallons":tkinter.PhotoImage(file = r"images/gallons.gif"),
           "miles":tkinter.PhotoImage(file = r"images/miles.gif"),
           "celsius":tkinter.PhotoImage(file = r"images/celsius.gif"),
           "pounds":tkinter.PhotoImage(file = r"images/pounds.gif")}

mini_numbers = {"0":tkinter.PhotoImage(file = r"images/m0.gif"),
           "1":tkinter.PhotoImage(file = r"images/m1.gif"),
           "2":tkinter.PhotoImage(file = r"images/m2.gif"),
           "3":tkinter.PhotoImage(file = r"images/m3.gif"),
           "4":tkinter.PhotoImage(file = r"images/m4.gif"),
           "5":tkinter.PhotoImage(file = r"images/m5.gif"),
           "6":tkinter.PhotoImage(file = r"images/m6.gif"),
           "7":tkinter.PhotoImage(file = r"images/m7.gif"),
           "8":tkinter.PhotoImage(file = r"images/m8.gif"),
           "9":tkinter.PhotoImage(file = r"images/m9.gif"),
           "mini_empty":tkinter.PhotoImage(file = r"images/mini_empty.gif"),
           "+":tkinter.PhotoImage(file = r"images/mini_plus.gif"),
           "-":tkinter.PhotoImage(file = r"images/mini_minus.gif"),
           "*":tkinter.PhotoImage(file = r"images/mini_x.gif"),
           "/":tkinter.PhotoImage(file = r"images/mini_divide.gif"),
           ".":tkinter.PhotoImage(file = r"images/mini_dot.gif")}

memory = {"first_slot":"","second_slot":"",
        "third_slot":"", "total":"","result":""}

def button_of_number(num):
    if memory["second_slot"] == "":
        memory["first_slot"]+= num
        screen(memory["first_slot"],photo = numbers[num])
    else:
        memory["third_slot"]+= num
        screen(memory["third_slot"],photo = numbers[num])

def check_button_opt():
    if memory["result"] != "" and memory["first_slot"] == "":
        memory["first_slot"] = memory["result"]

def operation(opt):
    empty_screen()
    if memory["second_slot"] == "" and memory["third_slot"] == "":
        memory["second_slot"] = opt
        empty_screen()
    #if user press operation after equal
    elif memory["third_slot"] != "":
        first_zero()

def first_zero():    
    memory["first_slot"],memory["second_slot"],memory["third_slot"],memory["total"] = "","","",""
    empty_screen()
    mini_empty()
    canvas.create_image(120,y, image=numbers["0"]) #zero on a screen

def equal():
    memory["total"] = memory["first_slot"] + memory["second_slot"] + memory["third_slot"]
    if memory["second_slot"] == "%":
        memory["total"] = memory["first_slot"]+"/100"+"*"+memory["third_slot"]
    elif memory["second_slot"] == "Volume":
        memory["total"] = memory["first_slot"]+"/"+"3.785411784"      
    elif memory["second_slot"] == "Temperature":
        memory["total"] = memory["first_slot"]+"*1.8"+"+32"    
    elif memory["second_slot"] == "Pounds":
        memory["total"] = memory["first_slot"]+"*2.2046" 
    elif memory["second_slot"] == "Length":
        memory["total"] = memory["first_slot"]+"*0.62137" 
    elif memory["second_slot"] == "Root":
        counter = 1
        root = 0
        while root <= int(memory["first_slot"]):
            counter+= 0.1
            root = counter * counter
        memory["total"] = str(counter) 

    empty_screen()
    mini_empty()
    memory["result"] = str(eval(memory["total"])) 
    photo = ""
    #first_zero()
    screen(memory["result"],photo)  
    mini() 

def mini():
    mini_empty()
    if memory["second_slot"] == "+" or memory["second_slot"] == "-" or memory["second_slot"] == "*" or memory["second_slot"] == "/":
        x = 125
        znak = memory["first_slot"]+memory["second_slot"]+memory["third_slot"]
        print(znak)
        print(memory)
        for i in znak[:19]:
            canvas.create_image(x,198, image=mini_numbers[str(i)])
            x+=15  
    if memory["second_slot"] == "Volume":
        canvas.create_image(220,198, image=numbers["gallons"])
    elif memory["second_slot"] == "Length":
        canvas.create_image(180,198, image=numbers["miles"])
    elif memory["second_slot"] == "Temperature":
        canvas.create_image(260,198, image=numbers["celsius"])  
    elif memory["second_slot"] == "Pounds":
        canvas.create_image(270,198, image=numbers["pounds"])   

def screen(result,photo):
    #prevent 10 digits (limitaion of a screen)
    cut = result[:9]
    empty_screen()  
    x = 110
    for i in cut:
        canvas.create_image(x,y, image=numbers[str(i)])
        x+=35 
          
def empty_screen():
    canvas.create_image(252,280, image=numbers["10"])  

def mini_empty():
    canvas.create_image(252,198, image=mini_numbers["mini_empty"])     

def left_click(event):

    print(str(event.x) + "," + str(event.y))
        
    if event.x > 45 and event.x < 124 and event.y > 706 and event.y < 760:
        button_of_number(num = "1")        
    if event.x > 155 and event.x < 236 and event.y > 706 and event.y < 760:
        button_of_number(num = "2")      
    if event.x > 267 and event.x < 347 and event.y > 706 and event.y < 760:
        button_of_number(num = "3")
    if event.x > 46 and event.x < 121 and event.y > 628 and event.y < 680:
        button_of_number(num = "4")
    if event.x > 155 and event.x < 236 and event.y > 628 and event.y < 680:
        button_of_number(num = "5")
    if event.x > 267 and event.x < 347 and event.y > 628 and event.y < 680:
        button_of_number(num = "6")
    if event.x > 46 and event.x < 121 and event.y > 549 and event.y < 600:
        button_of_number(num = "7")
    if event.x > 155 and event.x < 236 and event.y > 549 and event.y < 600:
        button_of_number(num = "8")
    if event.x > 267 and event.x < 347 and event.y > 549 and event.y < 600:
        button_of_number(num = "9")
    if event.x > 45 and event.x < 124 and event.y > 788 and event.y < 834:
        button_of_number(num = "0")
    
    #Dot
    if event.x > 160 and event.x < 232 and event.y > 788 and event.y < 834:
        if memory["second_slot"] == "":
            if "." in memory["first_slot"][:2]:
                pass
            else:
                memory["first_slot"]+= "."    
                screen(memory["first_slot"],photo = numbers["."])
        else:
            if "." in memory["third_slot"][:2]:
                pass
            else:
                memory["third_slot"]+= "."
                screen(memory["third_slot"],photo = numbers["."])
    
    #negative number
    if event.x > 156 and event.x < 233 and event.y > 468 and event.y < 519:
        if memory["second_slot"] == "":
            if "-" in memory["first_slot"]:
                pass
            else:
                memory["first_slot"] = "-"+ memory["first_slot"]    
                screen(memory["first_slot"],photo = numbers["-"])
        else:
            if "-" in memory["third_slot"]:
                pass
            else:
                memory["third_slot"] = "-" + memory["third_slot"]
                screen(memory["third_slot"],photo = numbers["-"])

    if event.x > 267 and event.x < 347 and event.y > 786 and event.y < 839:       
        check_button_opt()
        operation(opt="+")    
        mini()     
    if event.x > 379 and event.x < 454 and event.y > 627 and event.y < 678:
        mini()
        check_button_opt()
        operation(opt="-")
        mini() 
    if event.x > 379 and event.x < 454 and event.y > 549 and event.y < 600:
        mini()
        check_button_opt()
        operation(opt="*")
        mini() 
    if event.x > 379 and event.x < 454 and event.y > 469 and event.y < 525:
        check_button_opt()
        operation(opt="/")   
        mini() 

    #percent
    if event.x > 271 and event.x < 345 and event.y > 469 and event.y < 525:
        memory["second_slot"] = "%"
        equal()

    #Volume
    if event.x > 400 and event.x < 456 and event.y > 400 and event.y < 435:
        memory["second_slot"] = "Volume"
        equal()

    #Temperature
    if event.x > 222 and event.x < 273 and event.y > 400 and event.y < 435:
        memory["second_slot"] = "Temperature"
        equal()

    #Weight
    if event.x > 136 and event.x < 189 and event.y > 400 and event.y < 435:
        memory["second_slot"] = "Pounds"
        equal()

    #Length
    if event.x > 47 and event.x < 100 and event.y > 400 and event.y < 435:
        memory["second_slot"] = "Length"
        equal()

    #root
    if event.x > 313 and event.x < 369 and event.y > 400 and event.y < 435:
        memory["second_slot"] = "Root"
        equal()

    #equal button    
    if event.x > 379 and event.x < 454 and event.y > 707 and event.y < 839:
        equal()

    #ac/c button
    if event.x > 54 and event.x < 118 and event.y > 471 and event.y < 524:
        first_zero()
    
canvas = tkinter.Canvas(window , height=900, width=502)
canvas.grid(row = 0, column = 0)

calculator_background = tkinter.PhotoImage(file = 'images/bg.gif')
canvas.create_image(253,450, image=calculator_background)
first_zero()


window.bind("<Button-1>", left_click)

canvas.pack()
window.mainloop()