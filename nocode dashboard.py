import customtkinter
customtkinter.set_appearance_mode("light")
from PIL import Image,ImageTk
customtkinter.set_default_color_theme("dark-blue")

main = customtkinter.CTk()

main.geometry("2134x2845")
main.title("Main Page")
bg = ImageTk.PhotoImage(Image.open("NoCode.jpeg").resize((1910,1050),Image.ANTIALIAS))
icon = ImageTk.PhotoImage(Image.open("NoCode.jpeg"))
le = customtkinter.CTkLabel(main,image=bg)
le.pack()
start = ImageTk.PhotoImage(Image.open("home.png").resize((150,150),Image.ANTIALIAS))



main.geometry("2134x2845")
main.title("DASHBOARD")




main.iconphoto(True,icon)
n = customtkinter.CTkLabel(master=main, text="N",fg_color="black",text_color="red",font=("Arial", 120,"bold"))

n.place(x=625, y=5.32)
o = customtkinter.CTkLabel(master=main, text="o",fg_color="black", text_color="aqua",font=("Arial", 120,"bold"))

o.place(x=745, y=5.32)
c = customtkinter.CTkLabel(master=main, text="C",fg_color="black", text_color="gold",font=("Calligraffitti", 120,"bold"))

c.place(x=865, y=5.32)
o = customtkinter.CTkLabel(master=main, text="o",fg_color="black", text_color="aqua",font=("Arial", 120,"bold"))

o.place(x=985, y=5.32)

d = customtkinter.CTkLabel(master=main, text="d",fg_color="black", text_color="blue",font=("Arial", 120,"bold"))

d.place(x=1105, y=5.32)
e = customtkinter.CTkLabel(master=main, text="e",fg_color="black", text_color="green",font=("Arial", 120,"bold"))

e.place(x=1225, y=5.32)

   
       
             
def home():  
        main.destroy()  
        import customtkinter
        from PIL import Image,ImageTk
        import tkinter as tk

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        sim = customtkinter.CTk()

        sim.geometry("2134x2845")
        sim.title("DASHBOARD")
        bg = ImageTk.PhotoImage(Image.open("NoCode.jpeg"))
        icon = ImageTk.PhotoImage(Image.open("NoCode.jpeg"))
        li = customtkinter.CTkLabel(master=sim,)

        sim.geometry("2134x2845")
        sim.title("DASHBOARD")

        sim.iconphoto(True,icon)
        pic = ImageTk.PhotoImage(Image.open("profile.png"))
        wav = customtkinter.CTkImage(Image.open("a.gif"))

        frm = customtkinter.CTkFrame(master=sim, width=200,height=900 )
        frm.place(x=0, y=250)
        lili = customtkinter.CTkLabel(master=frm,image=wav ,width=200,height=900 )



        frm1 = customtkinter.CTkFrame(master=sim, width=200,height=249, bg_color="aliceblue", fg_color="blue")
        frm1.place(x=0, y=0)
        li = customtkinter.CTkLabel(master=frm1,image=pic,width=195,height=239,text="profile",text_color="black")
        li.pack()
        bb = customtkinter.CTkButton(master=frm,text="LOGIN",text_color="blue",fg_color="blue",hover_color="aqua")
        bb.place(x=1149, y=548)

        frm2 = customtkinter.CTkFrame(master=sim, width=1750,height=449, bg_color="aliceblue", fg_color="grey")
        frm2.place(x=201, y=0)

        n = customtkinter.CTkLabel(master=frm2, text="N", text_color="red",font=("Arial", 75,"bold"))

        n.place(x=625, y=5.32)
        o = customtkinter.CTkLabel(master=frm2, text="o", text_color="aqua",font=("Arial", 75,"bold"))

        o.place(x=700, y=5.32)
        c = customtkinter.CTkLabel(master=frm2, text="C", text_color="gold",font=("Calligraffitti", 75,"bold"))

        c.place(x=775, y=5.32)
        o = customtkinter.CTkLabel(master=frm2, text="o", text_color="aqua",font=("Arial", 75,"bold"))

        o.place(x=850, y=5.32)

        d = customtkinter.CTkLabel(master=frm2, text="d", text_color="blue",font=("Arial", 75,"bold"))

        d.place(x=925, y=5.32)
        e = customtkinter.CTkLabel(master=frm2, text="e", text_color="green",font=("Arial", 75,"bold"))

        e.place(x=1000, y=5.32)


        frm3 = customtkinter.CTkFrame(master=sim, width=1750,height=549, fg_color="white" )

        frm3.place(x=201,y=550)











        def login():
                sim.destroy()
                import customtkinter
                import tkinter 
                from PIL import Image,ImageTk


                customtkinter.set_appearance_mode("dark")
                customtkinter.set_default_color_theme('blue')


                root = customtkinter.CTk()


                root.geometry("2134x2845")
                root.title("NoCode")
                icon = ImageTk.PhotoImage(Image.open("NoCode.jpeg"))
                root.iconphoto(True,icon)
                img = ImageTk.PhotoImage(Image.open("bg2.jpg"))



                li = customtkinter.CTkLabel(root,image=img)
                li.pack()

                frm =customtkinter.CTkFrame(master=li,width=400, height=400,fg_color="#F0F8FF")
                frm. place(relx=0.5, rely=0.5, anchor="center")
                login =ImageTk.PhotoImage(Image.open("NoCode.jpeg").resize((400,400), Image.ANTIALIAS))


                n = customtkinter.CTkLabel(master=frm, text="N", text_color="red",font=("Arial", 25,"bold"))

                n.place(x=200, y=5.32)
                o = customtkinter.CTkLabel(master=frm, text="o", text_color="aqua",font=("Arial", 25,"bold"))

                o.place(x=215, y=5.32)
                c = customtkinter.CTkLabel(master=frm, text="C", text_color="gold",font=("Calligraffitti", 25,"bold"))

                c.place(x=230, y=5.32)
                o = customtkinter.CTkLabel(master=frm, text="o", text_color="aqua",font=("Arial", 25,"bold"))

                o.place(x=245, y=5.32)

                d = customtkinter.CTkLabel(master=frm, text="d", text_color="blue",font=("Arial", 25,"bold"))

                d.place(x=260, y=5.32)
                e = customtkinter.CTkLabel(master=frm, text="e", text_color="green",font=("Arial", 25,"bold"))

                e.place(x=275, y=5.32)


                logo =ImageTk.PhotoImage(Image.open("NoCode.jpeg").resize((40,40), Image.ANTIALIAS))

                #lebo = customtkinter.CTkLabel(master=frm, image=login)
                #lebo.pack()

                #leb = customtkinter.CTkLabel(master=lebo,image=logo)
                #leb.pack()

                entry1 = customtkinter.CTkEntry(master=frm, width=275,placeholder_text="Username",placeholder_text_color="black",corner_radius=4.532, fg_color="aliceblue")
                entry1.place(x=5.2, y=170.1, )
                entry2 = customtkinter.CTkEntry(master=frm, width=275,placeholder_text="Password",placeholder_text_color="black",corner_radius=4.532,fg_color="aliceblue")
                entry2.place(x=5.2, y=240.1, )

                logo1 = ImageTk.PhotoImage(Image.open("index.png").resize((20,20),Image.ANTIALIAS))
                logo2 = ImageTk.PhotoImage(Image.open("iG.jpeg").resize((20,20),Image.ANTIALIAS))
                logo3 = ImageTk.PhotoImage(Image.open("Facebook-logo.png").resize((20,20),Image.ANTIALIAS))
                logo4 = ImageTk.PhotoImage(Image.open("NoCode.jpeg").resize((100,100),Image.ANTIALIAS))

                button0 = customtkinter.CTkButton(master=frm, image=logo4, fg_color="white",text=" " ,width=100, height=100,corner_radius=3.5,compound="left", text_color="black",command=home)
                button0.place(x=125, y=40)

                button1 = customtkinter.CTkButton(master=frm, image=logo1, text="Google", fg_color="#F0F8FF", width=110, height=20,corner_radius=3.5,compound="left", text_color="black", hover_color="aqua")
                button1.place(x=12, y=345)
                button2 = customtkinter.CTkButton(master=frm, image=logo2, text="Instagram", width=110,fg_color="#F0F8FF", height=20,corner_radius=3.5,compound="left", text_color="black", hover_color="aqua")
                button2.place(x=130, y=345)
                button3 = customtkinter.CTkButton(master=frm, image=logo3, text="Facebook", width=110,fg_color="#F0F8FF", height=20,corner_radius=3.5,compound="left", text_color="black", hover_color="blue")
        
                button3.place(x=245, y=345)
        
                
                
                
                def forgot():
                        root.destroy()
                        import customtkinter
                        from PIL import Image,ImageTk
                        import tkinter as tk

                        customtkinter.set_appearance_mode("light")
                        customtkinter.set_default_color_theme("dark-blue")

                        window = customtkinter.CTk()
                        window.geometry("2134x2845")
                        
                        window.title("Reset Password")
                        

                        icon = ImageTk.PhotoImage(Image.open("NoCode.jpeg"))
                        bg = ImageTk.PhotoImage(Image.open("NoCode.jpeg").resize((450,450),Image.ANTIALIAS))

                        window.iconphoto(True,icon)
                        window.iconname("Reset Password")

                        img1 = ImageTk.PhotoImage(Image.open("bg2.jpg"))

                        li = customtkinter.CTkLabel(window,image=img1, height=1250, width=1800)
                        li.pack()

                        frm = customtkinter.CTkFrame(master=li, width=450, height=450, corner_radius=6.34567)
                        frm.place(relx=0.5, rely=0.5,anchor="center")


                        libi = customtkinter.CTkLabel(master=frm,image=bg, height=450, width=450)
                        libi.pack()
                        n = customtkinter.CTkLabel(master=frm, text="N", text_color="red",font=("Arial", 25,"bold"),fg_color="black")

                        n.place(x=200, y=5.32)
                        o = customtkinter.CTkLabel(master=libi, text="o", text_color="aqua",font=("Arial", 25,"bold"),fg_color="black")

                        o.place(x=215, y=5.32)
                        c = customtkinter.CTkLabel(master=libi, text="C", text_color="gold",font=("Calligraffitti", 25,"bold"),fg_color="black")

                        c.place(x=230, y=5.32)
                        o = customtkinter.CTkLabel(master=libi, text="o", text_color="aqua",font=("Arial", 25,"bold"),fg_color="black")

                        o.place(x=245, y=5.32)

                        d = customtkinter.CTkLabel(master=libi, text="d", text_color="blue",font=("Arial", 25,"bold"),fg_color="black")

                        d.place(x=260, y=5.32)
                        e = customtkinter.CTkLabel(master=libi, text="e", text_color="green",font=("Arial", 25,"bold"),fg_color="black")

                        e.place(x=275, y=5.32)

                        libi1 = customtkinter.CTkLabel(master=frm, text="RESET PASSWORD", font=("Arial",22,"bold"),fg_color="black",text_color="white")
                        libi1.place(x=130,y=35)

                        gmail = customtkinter.CTkEntry(master=libi,width=345,height=35, text_color="black", placeholder_text="Enter active gmail")
                        gmail.place(x=75, y=112)
                        
                        reset = customtkinter.CTkButton(master=libi,width=75,height=23,text_color="gold",text="RESET PASSWORD",fg_color="green")
                        reset.place(x=125, y=295)
                        window.mainloop()  
                button5 = customtkinter.CTkButton(master=frm,text="Forgot Password?",fg_color="white",text_color="black",hover_color="white",command=forgot)
                button5.place(x=145, y=305)
                root.mainloop()
                
        def register():
                sim.destroy()
                import customtkinter
                from PIL import Image,ImageTk
                customtkinter.set_appearance_mode("light")
                customtkinter.set_default_color_theme("dark-blue")
                
                zuu = customtkinter.CTk()

                zuu.geometry("2134x2845")
                zuu.title("NoCode Registration")
                icon = ImageTk.PhotoImage(Image.open("NoCode.jpeg"))
                zuu.iconphoto(True,icon)
                pic = ImageTk.PhotoImage(Image.open("bg2.jpg").resize((1415,800),Image.ANTIALIAS))

                lii = customtkinter.CTkLabel(zuu,image=pic)
                lii.pack()
                fremu = customtkinter.CTkFrame(master=lii,width=500, height=600,fg_color="#F0F8FF") 
                fremu.place(relx=0.5, rely=0.5, anchor="center")
                loo = customtkinter.CTkLabel(master=fremu,text="REGISTRATION",text_color="black")
                loo.place(x=52,y=65)
                n = customtkinter.CTkLabel(master=fremu, text="N", text_color="red",font=("Arial", 25,"bold"))

                n.place(x=200, y=5.32)
                o = customtkinter.CTkLabel(master=fremu, text="o", text_color="aqua",font=("Arial", 25,"bold"))

                o.place(x=215, y=5.32)
                c = customtkinter.CTkLabel(master=fremu, text="C", text_color="gold",font=("Calligraffitti", 25,"bold"))

                c.place(x=230, y=5.32)
                o = customtkinter.CTkLabel(master=fremu, text="o", text_color="aqua",font=("Arial", 25,"bold"))

                o.place(x=245, y=5.32)

                d = customtkinter.CTkLabel(master=fremu, text="d", text_color="blue",font=("Arial", 25,"bold"))

                d.place(x=260, y=5.32)
                e = customtkinter.CTkLabel(master=fremu, text="e", text_color="green",font=("Arial", 25,"bold"))

                e.place(x=275, y=5.32)
                
                ome = ImageTk.PhotoImage(Image.open("home.png"))
                cc = customtkinter.CTkButton(master=zuu,image=ome,command=home)
                cc.place(x=115,y=123)
                h1 = customtkinter.CTkEntry(master=fremu,width=345,height=35, text_color="black", placeholder_text="first name")
                h1.place(x=75, y=112)
                h2 = customtkinter.CTkEntry(master=fremu,width=345,height=35, text_color="black", placeholder_text="second name")
                h2.place(x=75, y=182)

                h3 = customtkinter.CTkEntry(master=fremu,width=345,height=35, text_color="black", placeholder_text="last name")
                h3.place(x=75, y=252)
                h4 = customtkinter.CTkEntry(master=fremu,width=345,height=35, text_color="black", placeholder_text="DD/MM/YYY")
                h4.place(x=75, y=322)

                h5 = customtkinter.CTkEntry(master=fremu,width=345,height=35, text_color="black", placeholder_text="password")
                h5.place(x=75, y=392)
                h6 = customtkinter.CTkEntry(master=fremu,width=345,height=35, text_color="black", placeholder_text="password")
                h6.place(x=75, y=462)
                def display():
                        zuu.destroy()
                        import customtkinter
                        from PIL import Image,ImageTk
                        customtkinter.set_appearance_mode("light")
                        customtkinter.set_default_color_theme("dark-blue")
                        
                        ksi = customtkinter.CTk()

                        ksi.geometry("2134x2845")
                        ksi.title("successful registration")
                        icon = ImageTk.PhotoImage(Image.open("NoCode.jpeg"))
                        ksi.iconphoto(True,icon)
                        foto = ImageTk.PhotoImage(Image.open("bg2.jpg"))
                        lia = customtkinter.CTkLabel(ksi,image=foto)
                        lia.pack()
                        fr = customtkinter.CTkFrame(master=ksi,width=540,height=654)
                        fr.place(relx=0.5, rely=0.5, anchor="center")
                        
                        
                        
                        
                        
                        
                        ksi.mainloop()

                submit = customtkinter.CTkButton(master=fremu,text="submit",text_color="brown",fg_color="grey",hover_color="black",command=display)
                submit.place(x=98, y=500)

                zuu.mainloop()

                
        login = customtkinter.CTkButton(master=sim,text="Login",fg_color="black",text_color="white" ,command=login)
        login.place(x=200,y=1000)
        register = customtkinter.CTkButton(master=sim,text="register",fg_color="black",text_color="white",command=register)
        register.place(x=395,y=1000)

        sim.mainloop()
starter = customtkinter.CTkButton(master=le,image=start,width=20,height=20,fg_color="black",text="get started",text_color="white",command=home,hover_color="black")
starter.place(x=250,y=12)
main.mainloop() 