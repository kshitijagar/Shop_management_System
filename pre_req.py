# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 21:54:42 2023

@author: DELL
"""

import mysql.connector 

mydb = mysql.connector.connect( 

  host="localhost", 

  user="root", 

  password="kshitij2803" 

) 

mycursor1 = mydb.cursor() 
mycursor1.execute("CREATE DATABASE foodshop")

mycursor2 = mydb.cursor() 
mycursor2.execute("CREATE TABLE salesrecords (Billno VARCHAR(10), date date, Sprite VARCHAR(10), Pepsi VARCHAR(10), Dietcoke VARCHAR(10), Mojito VARCHAR(10), Cappuccino VARCHAR(10), Fanta varchar(10), Cocacola varchar(10), Coldcoffee VARCHAR(10), Nachos VARCHAR(10), Vegburger VARCHAR(10), Pasta VARCHAR(10), Hamburger VARCHAR(10), Sandwhich VARCHAR(10), Fries VARCHAR(10), Spegetti VARCHAR(10), Fazitas VARCHAR(10), drinkscost varchar(20), foodcost varchar(10), tax varchar(10), Totalcost varchar(10))")
