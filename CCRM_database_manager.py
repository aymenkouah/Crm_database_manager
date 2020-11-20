#packages and modules
from tkinter import *
import sqlite3
import csv


#main window
root = Tk()
root.title("CRM database manager")
root.geometry("490x1000")

#Setting up the database
mydb = sqlite3.connect("database")
mycursor = mydb.cursor()

	#create the database table if first use
mycursor.execute("""CREATE TABLE IF NOT EXISTS customers (
			first_name text(255),
			last_name text(255),
			postal_code text(20),
			price_paid real(10, 2),
			user_id integer AUTO_INCREMENT PRIMARY KEY,
			email text(255), 
			adress_1 text(255),
			adress_2 text(255),
			city text(55),
			state text(50),
			country text(255),
			phone text(20),
			payment_method text(255),
			discount_code text(50)
			) 
			""")




#Functions
def clear():
	global first_name, last_name, postal_code, price_paid, user_id, email, adress_1, adress_2, city, state, country, phone, payment_method, discount_code
	first_name.delete(0, END)
	last_name.delete(0, END)
	postal_code.delete(0, END)
	price_paid.delete(0, END)
	user_id.delete(0, END)
	email.delete(0, END)
	adress_1.delete(0, END)
	adress_2.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	country.delete(0, END)
	phone.delete(0, END)
	payment_method.delete(0, END)
	discount_code.delete(0, END)


def add_to_database():
	global first_name, last_name, postal_code, price_paid, user_id, email, adress_1, adress_2, city, state, country, phone, payment_method, discount_code
	sql_command = "INSERT INTO customers (first_name, last_name, postal_code, price_paid, user_id, email, adress_1, adress_2, city, state, country, phone, payment_method, discount_code) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )"
	sql_values = (first_name.get(), last_name.get(), postal_code.get(), price_paid.get(), user_id.get(), email.get(), adress_1.get(), adress_2.get(), city.get(), state.get(), country.get(), phone.get(), payment_method.get(), discount_code.get())

	mydb = sqlite3.connect("database")
	mycursor = mydb.cursor()

	mycursor.execute(sql_command, sql_values)

	mydb.commit()
	mydb.close()
	clear()


def show_all_customers():
	global first_name, last_name, postal_code, price_paid, user_id, email, adress_1, adress_2, city, state, country, phone, payment_method, discount_code
	show_customers_window = Toplevel()
	show_customers_window.title("Customers list")
	show_customers_window.geometry("1469x800")

	mydb = sqlite3.connect("database")
	mycursor = mydb.cursor()

	mycursor.execute("""SELECT name FROM PRAGMA_TABLE_INFO("customers")
		""")
	field_names = mycursor.fetchall()
	col = 0
	pad = 10
	for field in field_names:
		Label(show_customers_window, text=field, fg="red", font=(15) ).grid(row=0, column=col, sticky="w", padx=xpad)
		col += 1

	mycursor.execute("SELECT * FROM customers")
	customers_query_result = mycursor.fetchall()
	row = 1
	for customer in customers_query_result:
		col = 0
		for field_info in customer:
			field_info = "N/A" if field_info=="" else field_info
			Label(show_customers_window, text=field_info).grid(row=row, column=col, sticky=W, padx=xpad) 
			col += 1
		row +=1

	mydb.commit()
	mydb.close()

	      ###save to csv button###
	csv_button = Button(show_customers_window, text="Save to excel records", command=lambda: write_to_csv(customers_query_result))
	csv_button.grid(row=row, column=0, columnspan=col, sticky=W+E)

def write_to_csv(customers_query_result):
	with open('customers.csv', 'a', newline="") as f:
		writer = csv.writer(f, dialect='excel')
		writer.writerow("")
		for record in result:
			writer.writerow(record)


def search_customers():
	search_window = Toplevel()
	search_window.title("Search")
	search_window.geometry("800x1000")
	
	search_entry = Entry(search_window, width=100)

	mydb = sqlite3.connect("database")
	mycursor = mydb.cursor()

	mycursor.execute("""SELECT name FROM PRAGMA_TABLE_INFO("customers")
		""")
	options_list = mycursor.fetchall()

	mydb.commit()
	mydb.close()
	options = []
	for option in options_list:
		options.append(option[0])

	criteria_value = StringVar()
	search_criteria = OptionMenu(search_window, criteria_value, *options)

	search_btn = Button(search_window, text="Search", command=lambda: search(search_entry.get(), criteria_value.get()))

	search_entry.grid(row=0,column=0, columnspan=3)
	search_criteria.grid(row=0, column=3)
	search_btn.grid(row=0, column=4)


def search(search_text, search_criteria):
	pass
#creating the Gui main window components
	#The title
title_lbl = Label(root, text="CRM for my company", font=("odibee sans", 50), fg='green', relief=FLAT)
title_lbl.grid(row=0, column=0, columnspan=3)

	#The entry boxes
first_name_lbl = Label(root, text="First Name", font=('Helvetica, 15'))
last_name_lbl = Label(root, text="Last Name", font=('Helvetica, 15'))
postal_code_lbl = Label(root, text="Postal Code", font=('Helvetica, 15'))
price_paid_lbl = Label(root, text="Price Paid", font=('Helvetica, 15'))
user_id_lbl = Label(root, text="User ID", font=('Helvetica, 15'))
email_lbl = Label(root, text="E-mail", font=('Helvetica, 15'))
adress_1_lbl = Label(root, text="Adress 1", font=('Helvetica, 15'))
adress_2_lbl = Label(root, text="Adress 2", font=('Helvetica, 15'))
city_lbl = Label(root, text="City", font=('Helvetica, 15'))
state_lbl = Label(root, text="State", font=('Helvetica, 15'))
country_lbl = Label(root, text="Country", font=('Helvetica, 15'))
phone_lbl = Label(root, text="Phone number", font=('Helvetica, 15'))
payment_method_lbl = Label(root, text="Payment Method", font=('Helvetica, 15'))
discount_code_lbl = Label(root, text="Discount Code", font=('Helvetica, 15'))


xpad = 10
ypad = 5

first_name_lbl.grid(row=1, column=0, sticky="w", padx=xpad, pady=ypad)
last_name_lbl.grid(row=2, column=0, sticky="w", padx=xpad, pady=ypad)
postal_code_lbl.grid(row=3, column=0, sticky="w", padx=xpad, pady=ypad)
price_paid_lbl.grid(row=4, column=0, sticky="w", padx=xpad, pady=ypad)
user_id_lbl.grid(row=5, column=0, sticky="w", padx=xpad, pady=ypad)
email_lbl.grid(row=6, column=0, sticky="w", padx=xpad, pady=ypad)
adress_1_lbl.grid(row=7, column=0, sticky="w", padx=xpad, pady=ypad)
adress_2_lbl.grid(row=8, column=0, sticky="w", padx=xpad, pady=ypad)
city_lbl.grid(row=9, column=0, sticky="w", padx=xpad, pady=ypad)
state_lbl.grid(row=10, column=0, sticky="w", padx=xpad, pady=ypad)
country_lbl.grid(row=11, column=0, sticky="w", padx=xpad, pady=ypad)
phone_lbl.grid(row=12, column=0, sticky="w", padx=xpad, pady=ypad)
payment_method_lbl.grid(row=13, column=0, sticky="w", padx=xpad, pady=ypad)
discount_code_lbl.grid(row=14, column=0, sticky="w", padx=xpad, pady=ypad)


first_name = Entry(root, width=50)
last_name = Entry(root, width=50)
postal_code = Entry(root, width=50)
price_paid = Entry(root, width=50)
user_id = Entry(root, width=50)
email = Entry(root, width=50)
adress_1 = Entry(root, width=50)
adress_2 = Entry(root, width=50)
city = Entry(root, width=50)
state = Entry(root, width=50)
country = Entry(root, width=50)
phone = Entry(root, width=50)
payment_method = Entry(root, width=50)
discount_code = Entry(root, width=50)

first_name.grid(row=1, column=1, columnspan=2, sticky="w", pady=ypad)
last_name.grid(row=2, column=1, columnspan=2, sticky="w", pady=ypad)
postal_code.grid(row=3, column=1, columnspan=2, sticky="w", pady=ypad)
price_paid.grid(row=4, column=1, columnspan=2, sticky="w", pady=ypad)
user_id.grid(row=5, column=1, columnspan=2, sticky="w", pady=ypad)
email.grid(row=6, column=1, columnspan=2, sticky="w", pady=ypad)
adress_1.grid(row=7, column=1, columnspan=2, sticky="w", pady=ypad)
adress_2.grid(row=8, column=1, columnspan=2, sticky="w", pady=ypad)
city.grid(row=9, column=1, columnspan=2, sticky="w", pady=ypad)
state.grid(row=10, column=1, columnspan=2, sticky="w", pady=ypad)
country.grid(row=11, column=1, columnspan=2, sticky="w", pady=ypad)
phone.grid(row=12, column=1, columnspan=2, sticky="w", pady=ypad)
payment_method.grid(row=13, column=1, columnspan=2, sticky="w", pady=ypad)
discount_code.grid(row=14, column=1, columnspan=2, sticky="w", pady=ypad)


	#Add to data base button
add_to_db_btn = Button(root, text="Add to database", font=('helvetica', 15), command=add_to_database, bg='pink')
add_to_db_btn.grid(row=15, column=0, columnspan=3, sticky="we", pady=ypad, padx=(xpad,0))


	#clear button
cls_btn = Button(root, text="Clear", font=('helvetica', 15), command=clear, bg='pink')
cls_btn.grid(row=16, column=0, columnspan=3, sticky="we", pady=ypad, padx=(xpad,0))

	#show all customers
show_customers_btn = Button(root, text="Show all customers", font=('helvetica', 15), command=show_all_customers, bg='pink')
show_customers_btn.grid(row=17, column=0, columnspan=3, sticky="we", pady=ypad, padx=(xpad,0))

	#Search
search_btn = Button(root, text="search", command=search_customers, font=('helvetica', 15), bg="pink")
search_btn.grid(row=18, column=0, columnspan=3, sticky="we", pady=ypad, padx=(xpad,0))


mycursor.execute("SELECT * FROM  customers")
result = mycursor.fetchall()
for x in result:
	print(x)


mydb.commit()
mydb.close()

#the main loop
root.mainloop()

