import mysql.connector 

from tkinter import * 

import random 

import datetime 

from datetime import datetime 

import time 

import sys 

import os 

az= datetime.today().strftime('%Y-%m-%d') 

 

mydb = mysql.connector.connect( 

  host="localhost", 

  user="root", 

  password="kshitij2803", 

  database="foodshop" 

) 

root =Tk() 

root.geometry("14000x800+0+0") 

root.title("All time food shop") 

root.configure(background='Blue') 

 

initial = Frame(root,bg='aqua',bd=20,pady=5,relief=RIDGE) 

initial.pack(side=TOP) 

 

lblTitle=Label(initial,font=('georgia',40,'bold'),text='All time Food shop',bd=21,bg='black', 

               fg='aqua',justify=CENTER) 

lblTitle.grid(row=0) 

 

 

BillCal_F = Frame(root,bg='lime',bd=10,relief=RIDGE) 

BillCal_F.pack(side=RIGHT) 

 

Buttons_F=Frame(BillCal_F,bg='lime',bd=3,relief=RIDGE) 

Buttons_F.pack(side=BOTTOM) 

 

 

 

BillF=Frame(BillCal_F,bg='lime',bd=4,relief=RIDGE) 

BillF.pack(side=BOTTOM) 

 

MenuFrame = Frame(root,bg='lime',bd=10,relief=RIDGE) 

MenuFrame.pack(side=LEFT) 

Cost_F=Frame(MenuFrame,bg='lime',bd=4) 

Cost_F.pack(side=BOTTOM) 

Drinks_F=Frame(MenuFrame,bg='lime',bd=4) 

Drinks_F.pack(side=TOP) 

 

 

Drinks_F=Frame(MenuFrame,bg='lime',bd=4,relief=RIDGE) 

Drinks_F.pack(side=LEFT) 

Food_F=Frame(MenuFrame,bg='lime',bd=4,relief=RIDGE) 

Food_F.pack(side=RIGHT)  

 

var1=IntVar() 

var2=IntVar() 

var3=IntVar() 

var4=IntVar() 

var5=IntVar() 

var6=IntVar() 

var7=IntVar() 

var8=IntVar() 

var9=IntVar() 

var10=IntVar() 

var11=IntVar() 

var12=IntVar() 

var13=IntVar() 

var14=IntVar() 

var15=IntVar() 

var16=IntVar() 

 

e=0 

f=1 

g=0 

h=0 

 

aa=0 

ab=0 

ac=0 

ad=0 

ae=0 

af=0 

ag=0 

ah=0 

ai=0 

aj=0 

ak=0 

al=0 

am=0 

an=0 

ao=0 

ap=0 

aq=0 

ar=0 

DateofOrder = StringVar() 

Bill_Ref = StringVar() 

PaidTax = StringVar() 

SubTotal = StringVar() 

TotalCost = StringVar() 

CostofFood = StringVar() 

CostofDrinks = StringVar() 

ServiceCharge = StringVar() 

 

text_Input = StringVar() 

operator = "" 

 

E_Sprite = StringVar() 

E_Pepsi = StringVar() 

E_DietCoke = StringVar() 

E_Mojito = StringVar() 

E_Cappuccino = StringVar() 

E_Fanta = StringVar() 

E_CocaCola = StringVar() 

E_ColdCoffee = StringVar() 

 

E_Nachos = StringVar() 

E_VegBurger = StringVar() 

E_Pasta = StringVar() 

E_HamBurger = StringVar() 

E_Sandwich = StringVar() 

E_Fires = StringVar() 

E_Spagetti = StringVar() 

E_Fazitas = StringVar() 

 

E_Sprite.set("0") 

E_Pepsi.set("0") 

E_DietCoke.set("0") 

E_Mojito.set("0") 

E_Cappuccino.set("0") 

E_Fanta.set("0") 

E_CocaCola.set("0") 

E_ColdCoffee.set("0") 

 

E_Nachos.set("0") 

E_VegBurger.set("0") 

E_Pasta.set("0") 

E_HamBurger.set("0") 

E_Sandwich.set("0") 

E_Fires.set("0") 

E_Spagetti.set("0") 

E_Fazitas.set("0") 

 

DateofOrder.set(time.strftime("%d/%m/%y")) 

  

def Reset(): 

 

    PaidTax.set("") 

    SubTotal.set("") 

    TotalCost.set("") 

    CostofFood.set("") 

    CostofDrinks.set("") 

    ServiceCharge.set("") 

    txtBill.delete("1.0",END) 

 

 

    E_Sprite.set("0") 

    E_Pepsi.set("0") 

    E_DietCoke.set("0") 

    E_Mojito.set("0") 

    E_Cappuccino.set("0") 

    E_Fanta.set("0") 

    E_CocaCola.set("0") 

    E_ColdCoffee.set("0") 

 

    E_Nachos.set("0") 

    E_VegBurger.set("0") 

    E_Pasta.set("0") 

    E_HamBurger.set("0") 

    E_Sandwich.set("0") 

    E_Fires.set("0") 

    E_Spagetti.set("0") 

    E_Fazitas.set("0") 

 

    var1.set(0) 

    var2.set(0) 

    var3.set(0) 

    var4.set(0) 

    var5.set(0) 

    var6.set(0) 

    var7.set(0) 

    var8.set(0) 

    var9.set(0) 

    var10.set(0) 

    var11.set(0) 

    var12.set(0) 

    var13.set(0) 

    var14.set(0) 

    var15.set(0) 

    var16.set(0) 

 

 

    txtSprite.configure() 

    txtPepsi.configure(state=DISABLED) 

    txtDietCoke.configure(state=DISABLED) 

    txtMojito.configure(state=DISABLED) 

    txtCappuccino.configure(state=DISABLED) 

    txtFanta.configure(state=DISABLED) 

    txtCocaCola.configure(state=DISABLED) 

    txtColdCoffee.configure(state=DISABLED) 

    txtNachos.configure(state=DISABLED) 

    txtVegBurger.configure(state=DISABLED) 

    txtPasta.configure(state=DISABLED) 

    txtHamBurger.configure(state=DISABLED) 

    txtSandwich.configure(state=DISABLED) 

    txtFires.configure(state=DISABLED) 

    txtSpagetti.configure(state=DISABLED) 

    txtFazitas.configure(state=DISABLED) 

 

def CostofItem(): 

    global e 

    global f 

    global g 

    global h 

    global aa 

    global ab 

    global ac 

    global ad 

    global ae 

    global af 

    global ag 

    global ah 

    global ai 

    global aj 

    global ak 

    global al 

    global am 

    global an 

    global ao 

    global ap 

     

     

 

    Item1=int(E_Sprite.get()) 

    Item2=int(E_Pepsi.get()) 

    Item3=int(E_DietCoke.get()) 

    Item4=int(E_Mojito.get()) 

    Item5=int(E_Cappuccino.get()) 

    Item6=int(E_Fanta.get()) 

    Item7=int(E_CocaCola.get()) 

    Item8=int(E_ColdCoffee.get()) 

 

    Item9=int(E_Nachos.get()) 

    Item10=int(E_VegBurger.get()) 

    Item11=int(E_Pasta.get()) 

    Item12=int(E_HamBurger.get()) 

    Item13=int(E_Sandwich.get()) 

    Item14=int(E_Fires.get()) 

    Item15=int(E_Spagetti.get()) 

    Item16=int(E_Fazitas.get()) 

    PriceofDrinks =(Item1 * 65) + (Item2 * 75) + (Item3 * 99) + (Item4 * 130) + (Item5 * 180) + (Item6 * 75) + (Item7 * 75) + (Item8 * 89) 

    e= int(PriceofDrinks) 

    PriceofFood =(Item9 * 260) + (Item10 * 175) + (Item11 * 255) + (Item12 * 480) + (Item13 * 240) + (Item14 * 110) + (Item15 * 340) + (Item16 * 213) 

    f=int(PriceofFood) 

   

 

    DrinksPrice = "Rs",str('%.2f'%(PriceofDrinks)) 

    FoodPrice =  "Rs",str('%.2f'%(PriceofFood)) 

    CostofFood.set(FoodPrice) 

    CostofDrinks.set(DrinksPrice) 

    SC = "Rs",str('%.2f'%(15)) 

    ServiceCharge.set(SC) 

 

    SubTotalofITEMS = "Rs",str('%.2f'%(PriceofDrinks + PriceofFood + 15)) 

    SubTotal.set(SubTotalofITEMS) 

     

    Tax = "Rs",str('%.2f'%((PriceofDrinks + PriceofFood + 15) * 0.18)) 

    PaidTax.set(Tax) 

    g=(int(PriceofDrinks + PriceofFood + 15) * 0.18) 

    TT=((PriceofDrinks + PriceofFood + 15) * 0.18) 

    TC="Rs",str('%.2f'%(PriceofDrinks + PriceofFood + 15 + TT)) 

    TotalCost.set(TC) 

    h=int((PriceofDrinks + PriceofFood + 15 + TT)) 

         

    aa=Item1  

    ab=Item2  

    ac=Item3  

    ad=Item4  

    ae=Item5  

    af=Item6  

    ag=Item7  

    ah=Item8  

 

    ai=Item9  

    aj=Item10  

    ak=Item1  

    al=Item12  

    am=Item13  

    an=Item14  

    ao=Item15  

    ap=Item16  

     

 

 

def chkSprite(): 

    if(var1.get() == 1): 

        txtSprite.configure(state = NORMAL) 

        txtSprite.focus() 

        txtSprite.delete('0',END) 

        E_Sprite.set("") 

    elif(var1.get() == 0): 

        txtSprite.configure(state = DISABLED) 

        E_Sprite.set("0") 

 

def chkPepsi(): 

    if(var2.get() == 1): 

        txtPepsi.configure(state = NORMAL) 

        txtPepsi.focus() 

        txtPepsi.delete('0',END) 

        E_Pepsi.set("") 

    elif(var2.get() == 0): 

        txtPepsi.configure(state = DISABLED) 

        E_Pepsi.set("0") 

 

def chk_DietCoke(): 

    if(var3.get() == 1): 

        txtDietCoke.configure(state = NORMAL) 

        txtDietCoke.delete('0',END) 

        txtDietCoke.focus() 

    elif(var3.get() == 0): 

        txtDietCoke.configure(state = DISABLED) 

        E_DietCoke.set("0") 

 

def chk_Mojito(): 

    if(var4.get() == 1): 

        txtMojito.configure(state = NORMAL) 

        txtMojito.delete('0',END) 

        txtMojito.focus() 

    elif(var4.get() == 0): 

        txtMojito.configure(state = DISABLED) 

        E_Mojito.set("0") 

 

def chk_Cappuccino(): 

    if(var5.get() == 1): 

        txtCappuccino.configure(state = NORMAL) 

        txtCappuccino.delete('0',END) 

        txtCappuccino.focus() 

    elif(var5.get() == 0): 

        txtCappuccino.configure(state = DISABLED) 

        E_Cappuccino.set("0") 

 

def chk_Fanta(): 

    if(var6.get() == 1): 

        txtFanta.configure(state = NORMAL) 

        txtFanta.delete('0',END) 

        txtFanta.focus() 

    elif(var6.get() == 0): 

        txtFanta.configure(state = DISABLED) 

        E_Fanta.set("0") 

 

def chk_CocaCola(): 

    if(var7.get() == 1): 

        txtCocaCola.configure(state = NORMAL) 

        txtCocaCola.delete('0',END) 

        txtCocaCola.focus() 

    elif(var7.get() == 0): 

        txtCocaCola.configure(state = DISABLED) 

        E_CocaCola.set("0") 

 

def chk_ColdCoffee(): 

    if(var8.get() == 1): 

        txtColdCoffee.configure(state = NORMAL) 

        txtColdCoffee.delete('0',END) 

        txtColdCoffee.focus() 

    elif(var8.get() == 0): 

        txtColdCoffee.configure(state = DISABLED) 

        E_ColdCoffee.set("0") 

 

def chk_Nachos(): 

    if(var9.get() == 1): 

        txtNachos.configure(state = NORMAL) 

        txtNachos.delete('0',END) 

        txtNachos.focus() 

    elif(var9.get() == 0): 

        txtNachos.configure(state = DISABLED) 

        E_Nachos.set("0") 

 

def chk_VegBurger(): 

    if(var10.get() == 1): 

        txtVegBurger.configure(state = NORMAL) 

        txtVegBurger.delete('0',END) 

        txtVegBurger.focus() 

    elif(var10.get() == 0): 

        txtVegBurger.configure(state = DISABLED) 

        E_VegBurger.set("0") 

 

def chk_Pasta(): 

    if(var11.get() == 1): 

        txtPasta.configure(state = NORMAL) 

        txtPasta.delete('0',END) 

        txtPasta.focus() 

    elif(var11.get() == 0): 

        txtPasta.configure(state = DISABLED) 

        E_Pasta.set("0") 

 

def chk_HamBurger(): 

    if(var12.get() == 1): 

        txtHamBurger.configure(state = NORMAL) 

        txtHamBurger.delete('0',END) 

        txtHamBurger.focus() 

    elif(var12.get() == 0): 

        txtHamBurger.configure(state = DISABLED) 

        E_HamBurger.set("0") 

 

def chk_Sandwich(): 

    if(var13.get() == 1): 

        txtSandwich.configure(state = NORMAL) 

        txtSandwich.delete('0',END) 

        txtSandwich.focus() 

    elif(var13.get() == 0): 

        txtSandwich.configure(state = DISABLED) 

        E_Sandwich.set("0") 

 

def chk_Fires(): 

    if(var14.get() == 1): 

        txtFires.configure(state = NORMAL) 

        txtFires.delete('0',END) 

        txtFires.focus() 

    elif(var14.get() == 0): 

        txtFires.configure(state = DISABLED) 

        E_Fires.set("0") 

 

def chk_Spagetti(): 

    if(var15.get() == 1): 

        txtSpagetti.configure(state = NORMAL) 

        txtSpagetti.delete('0',END) 

        txtSpagetti.focus() 

    elif(var15.get() == 0): 

        txtSpagetti.configure(state = DISABLED) 

        E_Spagetti.set("0") 

 

def chk_Fazitas(): 

     

    if(var16.get() == 1): 

         

        txtFazitas.configure(state = NORMAL) 

        txtFazitas.delete('0',END) 

        txtFazitas.focus() 

    elif(var16.get() == 0): 

        txtFazitas.configure(state = DISABLED) 

        E_Fazitas.set("0") 

j=random.randint(1,999999999) 

def Bill(): 

    txtBill.delete("1.0",END) 

    global j 

    billno= str(j) 

    Bill_Ref.set("Billing number"+ billno) 

     

     

 

    txtBill.insert(END,'Bill Ref:\t\t\t'+Bill_Ref.get() +'\t'+ DateofOrder.get() +'\n') 

    txtBill.insert(END,'Items\t\t\t\t'+"Number of items \n") 

    txtBill.insert(END,'Sprite:\t\t\t\t75 x ' + E_Sprite.get() +'\n') 

    txtBill.insert(END,'Pepsi:\t\t\t\t75 x '+ E_Pepsi.get()+'\n') 

    txtBill.insert(END,'DietCoke:\t\t\t\t100 x '+ E_DietCoke.get()+'\n') 

    txtBill.insert(END,'Mojito:\t\t\t\t130 x '+ E_Mojito.get()+'\n') 

    txtBill.insert(END,'Cappuccino:\t\t\t\t180 x '+ E_Cappuccino.get()+'\n') 

    txtBill.insert(END,'Fanta:\t\t\t\t75 x '+ E_Fanta.get()+'\n') 

    txtBill.insert(END,'CocaCola:\t\t\t\t75 x'+ E_CocaCola.get()+'\n') 

    txtBill.insert(END,'ColdCoffee:\t\t\t\t89 x '+ E_ColdCoffee.get()+'\n') 

    txtBill.insert(END,'Nachos:\t\t\t\t260 x '+ E_Nachos.get()+'\n') 

    txtBill.insert(END,'VegBurger:\t\t\t\t175 x '+ E_VegBurger.get()+'\n') 

    txtBill.insert(END,'Pasta:\t\t\t\t255 x '+ E_Pasta.get()+'\n') 

    txtBill.insert(END,'HamBurger:\t\t\t\t480 x '+ E_HamBurger.get()+'\n') 

    txtBill.insert(END,'Sandwich:\t\t\t\t240 x '+ E_Sandwich.get()+'\n') 

    txtBill.insert(END,'fries:\t\t\t\t110 x '+ E_Fires.get()+'\n') 

    txtBill.insert(END,'Spagetti:\t\t\t\t350 x '+ E_Spagetti.get()+'\n') 

    txtBill.insert(END,'Fazitas:\t\t\t\t250 x '+ E_Fazitas.get()+'\n') 

    txtBill.insert(END,'Cost of Drinks:\t\t\t\t'+CostofDrinks.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n") 

    txtBill.insert(END,'Cost of Foods:\t\t\t\t'+ CostofFood.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n") 

    txtBill.insert(END,'Service Charge:\t\t\t\t'+ ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n") 

     

    file=open(billno ,'w') 

    file.write("\t\t\t  All Time Food Shop\n\n\n") 

    file.write('Bill Ref:\t\t\t'+Bill_Ref.get() +'\t'+ DateofOrder.get() +'\n') 

    file.write('Items\t\t\t\t'+"Number of items \n") 

    file.write('Sprite:\t\t\t\t75 x ' + E_Sprite.get() +'\n') 

    file.write('Pepsi:\t\t\t\t75 x '+ E_Pepsi.get()+'\n') 

    file.write('DietCoke:\t\t\t100 x '+ E_DietCoke.get()+'\n') 

    file.write('Mojito:\t\t\t\t130 x '+ E_Mojito.get()+'\n') 

    file.write('Cappuccino:\t\t\t180 x '+ E_Cappuccino.get()+'\n') 

    file.write('Fanta:\t\t\t\t75 x '+ E_Fanta.get()+'\n') 

    file.write('CocaCola:\t\t\t75 x'+ E_CocaCola.get()+'\n') 

    file.write('ColdCoffee:\t\t\t89 x '+ E_ColdCoffee.get()+'\n') 

    file.write('Nachos:\t\t\t\t260 x '+ E_Nachos.get()+'\n') 

    file.write('VegBurger:\t\t\t175 x '+ E_VegBurger.get()+'\n') 

    file.write('Pasta:\t\t\t\t255 x '+ E_Pasta.get()+'\n') 

    file.write('HamBurger:\t\t\t480 x '+ E_HamBurger.get()+'\n') 

    file.write('Sandwich:\t\t\t240 x '+ E_Sandwich.get()+'\n') 

    file.write('Fries:\t\t\t\t110 x '+ E_Fires.get()+'\n') 

    file.write('Spagetti:\t\t\t350 x '+ E_Spagetti.get()+'\n') 

    file.write('Fazitas:\t\t\t250 x '+ E_Fazitas.get()+'\n') 

    file.write('Cost of Drinks:\t\t\t'+CostofDrinks.get()+'\nTax Paid:\t\t\t'+PaidTax.get()+"\n") 

    file.write('Cost of Foods:\t\t\t'+ CostofFood.get()+'\nSubTotal:\t\t\t'+str(SubTotal.get())+"\n") 

    file.write('Service Charge:\t\t\t'+ ServiceCharge.get()+'\nTotal Cost:\t\t\t'+str(TotalCost.get())+"\n") 

    file.write("\n\n\t\t\t  Thank you for shopping with us \n\t\t\t\t hope to see you again") 

    file.close() 

     

     

def mysql(): 

    mycursor = mydb.cursor() 

    sql = "INSERT INTO salesrecords (Billno,date, Sprite , Pepsi  , Dietcoke ,Mojito, Cappuccino,Fanta, Cocacola, Coldcoffee , Nachos , Vegburger , Pasta , Hamburger , Sandwhich, Fries , Spegetti , Fazitas , drinkscost, foodcost ,tax , Totalcost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" 

    val = (j , az,aa,ab,ac, ad,ae, af,ag,ah,ai,aj,ak,al,am,an,ao,ao,e,f,g,h) 

    mycursor.execute(sql, val) 

    mydb.commit()    

     

Sprite=Checkbutton(Drinks_F,text='Sprite',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'), 

                    bg='lime',command=chkSprite).grid(row=0,sticky=W) 

Pepsi=Checkbutton(Drinks_F,text='Pepsi',variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'), 

                    bg='lime',command=chkPepsi).grid(row=1,sticky=W) 

DietCoke=Checkbutton(Drinks_F,text='DietCoke',variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'), 

                    bg='lime',command=chk_DietCoke).grid(row=2,sticky=W) 

Mojito=Checkbutton(Drinks_F,text='Mojito',variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'), 

                    bg='lime',command=chk_Mojito).grid(row=3,sticky=W) 

Cappuccino=Checkbutton(Drinks_F,text='Cappuccino',variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'), 

                    bg='lime',command=chk_Cappuccino).grid(row=4,sticky=W) 

Fanta=Checkbutton(Drinks_F,text='Fanta',variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'), 

                    bg='lime',command=chk_Fanta).grid(row=5,sticky=W) 

CocaCola=Checkbutton(Drinks_F,text='CocaCola',variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'), 

                    bg='lime',command=chk_CocaCola).grid(row=6,sticky=W) 

ColdCoffee=Checkbutton(Drinks_F,text='ColdCoffee',variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'), 

                    bg='lime',command=chk_ColdCoffee).grid(row=7,sticky=W) 

  

txtSprite = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED 

                        ,textvariable=E_Sprite) 

txtSprite.grid(row=0,column=1) 

 

txtPepsi = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED 

                        ,textvariable=E_Pepsi) 

txtPepsi.grid(row=1,column=1) 

 

txtDietCoke = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED 

                        ,textvariable=E_DietCoke) 

txtDietCoke.grid(row=2,column=1) 

 

txtMojito= Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED 

                        ,textvariable=E_Mojito) 

txtMojito.grid(row=3,column=1) 

 

txtCappuccino = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED 

                        ,textvariable=E_Cappuccino) 

txtCappuccino.grid(row=4,column=1) 

 

txtFanta = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED 

                        ,textvariable=E_Fanta) 

txtFanta.grid(row=5,column=1) 

 

txtCocaCola = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED 

                        ,textvariable=E_CocaCola) 

txtCocaCola.grid(row=6,column=1) 

 

txtColdCoffee = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED 

                        ,textvariable=E_ColdCoffee) 

txtColdCoffee.grid(row=7,column=1) 

 

#Foods 

 

Nachos = Checkbutton(Food_F,text="Nachos\t\t\t ",variable=var9,onvalue = 1, offvalue=0, 

                        font=('arial',16,'bold'),bg='lime',command=chk_Nachos).grid(row=0,sticky=W) 

VegBurger = Checkbutton(Food_F,text="VegBurger",variable=var10,onvalue = 1, offvalue=0, 

                        font=('arial',16,'bold'),bg='lime',command=chk_VegBurger).grid(row=1,sticky=W) 

Pasta = Checkbutton(Food_F,text="Pasta ",variable=var11,onvalue = 1, offvalue=0, 

                        font=('arial',16,'bold'),bg='lime',command=chk_Pasta).grid(row=2,sticky=W) 

HamBurger = Checkbutton(Food_F,text="Rice Plate ",variable=var12,onvalue = 1, offvalue=0, 

                        font=('arial',16,'bold'),bg='lime',command=chk_HamBurger).grid(row=3,sticky=W) 

Sandwich = Checkbutton(Food_F,text="Sandwich ",variable=var13,onvalue = 1, offvalue=0, 

                        font=('arial',16,'bold'),bg='lime',command=chk_Sandwich).grid(row=4,sticky=W) 

Fires = Checkbutton(Food_F,text="Fires ",variable=var14,onvalue = 1, offvalue=0, 

                        font=('arial',16,'bold'),bg='lime',command=chk_Fires).grid(row=5,sticky=W) 

Spagetti = Checkbutton(Food_F,text="Spagetti ",variable=var15,onvalue = 1, offvalue=0, 

                        font=('arial',16,'bold'),bg='lime',command=chk_Spagetti).grid(row=6,sticky=W) 

Fazitas = Checkbutton(Food_F,text="Fazitas ",variable=var16,onvalue = 1, offvalue=0, 

                        font=('arial',16,'bold'),bg='lime',command=chk_Fazitas).grid(row=7,sticky=W) 

  

txtNachos=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED, 

                 textvariable=E_Nachos) 

txtNachos.grid(row=0,column=1) 

 

txtVegBurger=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED, 

                        textvariable=E_VegBurger) 

txtVegBurger.grid(row=1,column=1) 

 

txtPasta=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED, 

                        textvariable=E_Pasta) 

txtPasta.grid(row=2,column=1) 

 

txtHamBurger=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED, 

                        textvariable=E_HamBurger) 

txtHamBurger.grid(row=3,column=1) 

 

txtSandwich=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED, 

                        textvariable=E_Sandwich) 

txtSandwich.grid(row=4,column=1) 

 

txtFires=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED, 

                        textvariable=E_Fires) 

txtFires.grid(row=5,column=1) 

 

txtSpagetti=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED, 

                        textvariable=E_Spagetti) 

txtSpagetti.grid(row=6,column=1) 

 

txtFazitas=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED, 

                        textvariable=E_Fazitas) 

txtFazitas.grid(row=7,column=1) 

  

lblCostofDrinks=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Drinks\t',bg='lime', 

                fg='black',justify=CENTER) 

lblCostofDrinks.grid(row=0,column=0,sticky=W) 

txtCostofDrinks=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'), 

                        insertwidth=2,justify=RIGHT,textvariable=CostofDrinks) 

txtCostofDrinks.grid(row=0,column=1) 

 

lblCostofFood=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Foods  ',bg='lime', 

                fg='black',justify=CENTER) 

lblCostofFood.grid(row=1,column=0,sticky=W) 

txtCostofFood=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'), 

                        insertwidth=2,justify=RIGHT,textvariable=CostofFood) 

txtCostofFood.grid(row=1,column=1) 

 

lblServiceCharge=Label(Cost_F,font=('arial',14,'bold'),text='Service Charge',bg='lime', 

                fg='black',justify=CENTER) 

lblServiceCharge.grid(row=2,column=0,sticky=W) 

txtServiceCharge=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'), 

                        insertwidth=2,justify=RIGHT,textvariable=ServiceCharge) 

txtServiceCharge.grid(row=2,column=1) 

 

#Payment information 

  

lblPaidTax=Label(Cost_F,font=('arial',14,'bold'),text='\tPaid Tax',bg='lime',bd=7, 

                fg='black',justify=CENTER) 

lblPaidTax.grid(row=0,column=2,sticky=W) 

txtPaidTax=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'), 

                        insertwidth=2,justify=RIGHT,textvariable=PaidTax) 

txtPaidTax.grid(row=0,column=3) 

 

lblSubTotal=Label(Cost_F,font=('arial',14,'bold'),text='\tSub Total',bg='lime',bd=7, 

                fg='black',justify=CENTER) 

lblSubTotal.grid(row=1,column=2,sticky=W) 

txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'), 

                        insertwidth=2,justify=RIGHT,textvariable=SubTotal) 

txtSubTotal.grid(row=1,column=3) 

 

lblTotalCost=Label(Cost_F,font=('arial',14,'bold'),text='\tTotal',bg='lime',bd=7, 

                fg='black',justify=CENTER) 

lblTotalCost.grid(row=2,column=2,sticky=W) 

txtTotalCost=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'), 

                        insertwidth=2,justify=RIGHT,textvariable=TotalCost) 

txtTotalCost.grid(row=2,column=3) 

 

#Bill 

 

txtBill=Text(BillF,width=46,height=20,bg='aqua',bd=4,font=('arial',12,'bold')) 

txtBill.grid(row=0,column=0) 

 

 

#BUTTONS 

 

btnTotal=Button(Buttons_F,padx=15,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=8,text='Total Amount', 

                        bg='lime',command=CostofItem).grid(row=1,column=0) 

btnBill=Button(Buttons_F,padx=40,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Bill', 

                        bg='lime',command=Bill).grid(row=1,column=1) 

btnReset=Button(Buttons_F,padx=15,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Refresh', 

                        bg='lime',command=Reset).grid(row=1,column=2) 

btnot=Button(Buttons_F,padx=15,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=8,text='SQL entry', 

                        bg='lime', command=mysql ).grid(row=3,column=0  ) 

btanalyser=Button(Buttons_F,padx=40,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=8,text='Business Analyser', 

                        bg='lime', command=os.system("accessingsqldata.py" ) ).grid(row=3,column=1  )  

   

 

root.mainloop() 

 

#Accessing the Data 

 

key=input("Enter the secure key: ") 

if key=="kshitij2803": 

    import mysql.connector 

    import datetime 

    mydb = mysql.connector.connect( 

    host="localhost", 

    user="root", 

    password="kshitij2803", 

    database="foodshop") 

     

    print("Welcome to the all time food shop datbase ") 

    print("what do you want to do:") 

    print("a. check the total revenue generated") 

    print("b. Check the amount of tax to be paid") 

    print("c. Check the quantity of a particular item sold") 

    ad=input("Enter your choice: ") 

    if ad=="a": 

        d1=input("enter starting date") 

        f=d1.split(",") 

        r=int(f[0]) 

        o=int(f[1]) 

        y=int(f[2]) 

        x = datetime.datetime(r,o,y) 

        

        d2=input("enter ending date") 

        g=d2.split(",") 

        u=int(g[0]) 

        i=int(g[1]) 

        q=int(g[2]) 

        m = datetime.datetime(u,i,q) 

         

        mycursor = mydb.cursor() 

 

         

        mycursor.execute("SELECT sum(Totalcost) FROM salesrecords WHERE date between %s and %s", (x, m))

 