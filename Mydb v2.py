from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title('Enter Credentials')
root.geometry("400x400")

def update():
                #create database
                conn=sqlite3.connect('address_book.db')

                #ceate cursor
                c=conn.cursor()

                record_id=delete_box.get()

                c.execute("""UPDATE addresses SET
                          first_name= :first,
                          last_name= :last,
                          address= :address,
                          city= :city,
                          state= :state,
                          zipcode= :zipcode

                          WHERE oid= :oid""",
                          {
                                          'first':f_name.get(),
                                          'last':l_name.get(),
                                          'address':address.get(),
                                          'city':city.get(),
                                          'state':state.get(),
                                          'zipcode':zipcode.get(),
                                          'oid': record_id
                                          })
                          
                #commit
                conn.commit()

                #close connection
                conn.close()

                editor.destroy()

def edit():
                global editor
                editor=Tk()
                editor.title('Update a Record')
                editor.geometry("400x600")

                #create database
                conn=sqlite3.connect('address_book.db')

                #ceate cursor
                c=conn.cursor()

                #query the database
                record_id=delete_box.get()
                c.execute("SELECT * FROM addresses WHERE oid = "+ record_id)
                records=c.fetchall()

                
                global f_name
                global l_name
                global city
                global state
                global address
                global zipcode
                
                f_name=Entry(editor,width=30)
                f_name.grid(row=0,column=1,padx=20, pady=(10,0))

                l_name=Entry(editor,width=30)
                l_name.grid(row=1,column=1)

                address=Entry(editor,width=30)
                address.grid(row=2,column=1)

                city=Entry(editor,width=30)
                city.grid(row=3,column=1)

                state=Entry(editor,width=30)
                state.grid(row=4,column=1)

                zipcode=Entry(editor,width=30)
                zipcode.grid(row=5,column=1)

                

                #create textbox label
                f_name_label=Label(editor,text="First Name")
                f_name_label.grid(row=0,column=0,pady=(10,0))

                l_name_label=Label(editor,text="Last Name")
                l_name_label.grid(row=1,column=0)

                address_label=Label(editor,text="Address")
                address_label.grid(row=2,column=0)

                city_label=Label(editor,text="City")
                city_label.grid(row=3,column=0)

                state_label=Label(editor,text="State")
                state_label.grid(row=4,column=0)

                zipcode_label=Label(editor,text="Zipcode")
                zipcode_label.grid(row=5,column=0)

                #print(records)
                for record in records:
                                f_name.insert(0,record[0])
                                l_name.insert(0,record[1])
                                address.insert(0,record[2])
                                city.insert(0,record[3])
                                state.insert(0,record[4])
                                zipcode.insert(0,record[5])


                edit_btn=Button(editor,text="Save Record", command=update)
                edit_btn.grid(row=11,column=0, columnspan=2 ,pady=10, padx=10, ipadx=145)


                

def delete():
                conn=sqlite3.connect('address_book.db')
                c=conn.cursor()

                c.execute("DELETE FROM addresses WHERE oid="+delete_box.get())
                #commit
                conn.commit()

                #close connection
                conn.close()


#create submit function
def submit():
                #create database
                conn=sqlite3.connect('address_book.db')

                #ceate cursor
                c=conn.cursor()

                #Insert Into Table
                c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                          {
                                          'f_name' : f_name.get(),
                                          'l_name' : l_name.get(),
                                          'address' : address.get(),
                                          'city' : city.get(),
                                          'state' : state.get(),
                                          'zipcode' : zipcode.get()
                                }



                          )

                #commit
                conn.commit()

                #close connection
                conn.close()


                #clear the text boxes
                f_name.delete(0,END)
                l_name.delete(0,END)
                address.delete(0,END)
                city.delete(0,END)
                state.delete(0,END)
                zipcode.delete(0,END)

def query():
                #create database
                conn=sqlite3.connect('address_book.db')

                #ceate cursor
                c=conn.cursor()

                #query the database
                c.execute("SELECT *, oid FROM addresses")
                records=c.fetchall()
                #print(records)

                print_records=''
                for record in records:
                                print_records+= str(record[0]) +" "+str(record[1])+" "+str(record[6])+"\n"
                query_label=Label(root,text=print_records)
                query_label.grid(row=12, column=0, columnspan=2)

                #commit
                conn.commit()

                #close connection
                conn.close()
                
#create text boxes
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20, pady=(10,0))

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)

address=Entry(root,width=30)
address.grid(row=2,column=1)

city=Entry(root,width=30)
city.grid(row=3,column=1)

state=Entry(root,width=30)
state.grid(row=4,column=1)

zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1)

delete_box=Entry(root,width=30)
delete_box.grid(row=9,column=1, pady=5)

#create textbox label
f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0,pady=(10,0))

l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)

address_label=Label(root,text="Address")
address_label.grid(row=2,column=0)

city_label=Label(root,text="City")
city_label.grid(row=3,column=0)

state_label=Label(root,text="State")
state_label.grid(row=4,column=0)

zipcode_label=Label(root,text="Zipcode")
zipcode_label.grid(row=5,column=0)

delete_box_label=Label(root,text="Select ID")
delete_box_label.grid(row=9,column=0 ,pady=5)


#create Submit button
submit_btn=Button(root, text="Add record to Database", command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#Create Query Button
query_btn=Button(root,text="Show Records", command=query)
query_btn.grid(row=7,column=0, columnspan=2 ,pady=10, padx=10, ipadx=137)

#CREATE DELETE BUTTON
delete_btn=Button(root,text="Delete Record", command=delete)
delete_btn.grid(row=10,column=0, columnspan=2 ,pady=10, padx=10, ipadx=136)

edit_btn=Button(root,text="Edit Record", command=edit)
edit_btn.grid(row=11,column=0, columnspan=2 ,pady=10, padx=10, ipadx=143)



root.mainloop()
