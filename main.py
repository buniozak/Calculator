from tkinter import *
import tkinter
import re
import customtkinter

root = customtkinter.CTk()
root.geometry("430x720")

customtkinter.set_appearance_mode("dark")

def validate_input(value):
    allowed_chars = set('0123456789+-*/()%.—')
    return set(value).issubset(allowed_chars)



validate_cmd = (root.register(validate_input), '%P')

def clear_text():
   entry.delete(0, END)

def delete_last():
    entry.delete(END, END)

def print_x(number):
    if number=="-":
        number="—"

    entry.insert(END, number)








def insert_result(sonuc):
    sonuc = str(sonuc)
    print(sonuc)
    entry.insert(customtkinter.END, sonuc)






def calculate():
    soru = entry.get()
    result = re.split(r'[\+|\*|\—|\/|\/|\-|\%|]', soru)

    if result[0]=='':
        print(result)
        result[1]=f"-{result[1]}"
        del result[0]

    print(f"result önce :  {result}")

    index_sayac=0

    for say in result:
        if say == '':
            del result[index_sayac]
            index_sayac += 1
        else:
            index_sayac += 1

    print(f"result :  {result}")
    print(f"soru :  {soru}")

    result_idx = 0
    operator = "+"
    total = 0

    for i in range(len(soru)):
        if soru[i] in ["+", "—", "*", "/","%"]:
            if operator == "+":
                if result_idx < len(result):
                    total += float(result[result_idx])
                    result_idx += 1
            elif operator == "—":
                if result_idx < len(result):
                    total -= float(result[result_idx])
                    result_idx += 1
            elif operator == "*":
                if result_idx < len(result):
                    total *= float(result[result_idx])
                    result_idx += 1
            elif operator == "/":
                if result_idx < len(result):
                    total /= float(result[result_idx])
                    result_idx += 1
            elif operator == "%":
                if result_idx < len(result):
                    total *= float(result[result_idx])/100
                    result_idx += 1

            operator = soru[i]

        if i == len(soru) - 1:
            if operator == "+":
                if result_idx < len(result):
                    total += float(result[result_idx])
            elif operator == "—":
                if result_idx < len(result):
                    total -= float(result[result_idx])
            elif operator == "*":
                if result_idx < len(result):
                    total *= float(result[result_idx])
            elif operator == "/":
                if result_idx < len(result):
                    total /= float(result[result_idx])
            elif operator == "%":
                if result_idx < len(result):
                    total *= float(result[result_idx])/100

    clear_text()
    insert_result(sonuc="%.2f" % total)


                # devam ettir - or * or /   print(result)





canvas=Canvas(background="#2C3639")
canvas.configure(width=450,height=222,)
canvas.place(x=-20,y=-30)

calculator_label=customtkinter.CTkLabel(master=root,text="Calculator !",font=("family",35))
calculator_label.place(anchor=tkinter.CENTER,relx=0.5,rely=0.03)


entry = customtkinter.CTkEntry(root,width=405,height=100,corner_radius=10,fg_color="#F5E9CF",font=("Monospace",50),text_color="black",validate = 'key', validatecommand = validate_cmd,placeholder_text="calculate")
entry.place(x=12,y=55)




#-------------İLK SATIR------------

button_parantez_sol=customtkinter.CTkButton(root,text="C",command=clear_text,width=105,height=100,corner_radius=15,border_width=4,border_color="#03001C",font=("Monospace",35),fg_color="#BDCDD6",text_color="black",hover_color="#A0C3D2")
button_parantez_sol.place(x=0,y=620)

button_parantez_sol=customtkinter.CTkButton(root,text="%",command=lambda: print_x("%"),width=105,height=100,corner_radius=15,border_width=4,fg_color="#443C68",border_color="#18122B",font=("Monospace",35))
button_parantez_sol.place(x=330,y=200)

button_parantez_sol=customtkinter.CTkButton(root,text="/",command=lambda: print_x("/"),width=105,height=100,corner_radius=15,border_width=4,fg_color="#443C68",border_color="#18122B",font=("Monospace",35))
button_parantez_sol.place(x=330,y=305)
#-----------'2. SATIR'--------------



button_parantez_sol=customtkinter.CTkButton(root,text="1",command=lambda: print_x("1"),width=105,height=100,corner_radius=15,border_width=4,border_color="#03001C",font=("Monospace",35))
button_parantez_sol.place(x=0,y=305)


button_parantez_sol=customtkinter.CTkButton(root,text="2",command=lambda: print_x("2"),width=105,height=100,corner_radius=15,border_width=4,border_color="#03001C",font=("Monospace",35))
button_parantez_sol.place(x=110,y=305)

button_parantez_sol=customtkinter.CTkButton(root,text="3",command=lambda: print_x("3"),width=105,height=100,corner_radius=15,border_width=4,border_color="#03001C",font=("Monospace",35))
button_parantez_sol.place(x=220,y=305)

button_parantez_sol=customtkinter.CTkButton(root,text="X",command=lambda: print_x("*"),width=105,height=100,corner_radius=15,border_width=4,fg_color="#443C68",border_color="#18122B",font=("Monospace",35))
button_parantez_sol.place(x=330,y=410)

#------------------3 : SATIR----------------------


button_parantez_sol=customtkinter.CTkButton(root,text="4",command=lambda: print_x("4"),width=105,height=100,corner_radius=15,border_width=4,border_color="#03001C",font=("Monospace",35))
button_parantez_sol.place(x=0,y=410)


button_parantez_sol=customtkinter.CTkButton(root,text="5",command=lambda: print_x("5"),width=105,height=100,corner_radius=15,border_width=4,border_color="#03001C",font=("Monospace",35))
button_parantez_sol.place(x=110,y=410)

button_parantez_sol=customtkinter.CTkButton(root,text="6",command=lambda: print_x("6"),width=105,height=100,corner_radius=15,border_width=4,border_color="#03001C",font=("Monospace",35))
button_parantez_sol.place(x=220,y=410)

button_parantez_sol=customtkinter.CTkButton(root,text="-",command=lambda: print_x("—"),width=105,height=100,corner_radius=15,border_width=4,fg_color="#443C68",border_color="#18122B",font=("Monospace",35))
button_parantez_sol.place(x=330,y=515)



#--------------4 : SATIR-----------------

button_parantez_sol=customtkinter.CTkButton(root,text="7",command=lambda: print_x("7"),width=105,height=100,corner_radius=15,border_width=4,border_color="#03001C",font=("Monospace",35))
button_parantez_sol.place(x=0,y=515)


button_parantez_sol=customtkinter.CTkButton(root,text="8",command=lambda: print_x("8"),width=105,height=100,corner_radius=15,border_width=4,border_color="#03001C",font=("Monospace",35))
button_parantez_sol.place(x=110,y=515)

button_parantez_sol=customtkinter.CTkButton(root,text="9",command=lambda: print_x("8"),width=105,height=100,corner_radius=15,border_width=4,border_color="#03001C",font=("Monospace",35))
button_parantez_sol.place(x=220,y=515)

button_parantez_sol=customtkinter.CTkButton(root,text="+",command=lambda: print_x("+"),width=105,height=100,corner_radius=15,border_width=4,fg_color="#443C68",border_color="#18122B",font=("Monospace",35))
button_parantez_sol.place(x=330,y=620)






button_parantez_equal=customtkinter.CTkButton(root,text="=",command=calculate,width=315,height=100,corner_radius=15,border_width=4,border_color="#DEFCF9",font=("Monospace",35),fg_color="#ECF9FF",text_color="black",hover_color="#BDCDD6",)
button_parantez_equal.place(x=0,y=200)

button_parantez_sol=customtkinter.CTkButton(root,text="0",command=lambda: print_x("0"),width=105,height=100,corner_radius=15,border_width=4,border_color="#3C84AB",font=("Monospace",35))
button_parantez_sol.place(x=110,y=620)

button_parantez_sol=customtkinter.CTkButton(root,text=".",command=lambda: print_x("."),width=105,height=100,corner_radius=15,border_width=4,border_color="#3C84AB",font=("Monospace",35))
button_parantez_sol.place(x=220,y=620)












root.mainloop()