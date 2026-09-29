from prettytable import PrettyTable,TableStyle
'''
Each element of dictionary has this structure --->
Bookstore = { book_no : [book_title,author,publication,pub_year,price,stock] }
'''

Bookstore = {
    101: ["The Alchemist", "Paulo Coelho", "HarperCollins", 1988, 399, 25],
    102: ["Wings of Fire", "A.P.J. Abdul Kalam", "Universities Press", 1999, 350, 18],
    103: ["Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Bloomsbury", 1997, 499, 30],
    104: ["The Guide", "R.K. Narayan", "Indian Thought Publications", 1958, 275, 12],
    105: ["To Kill a Mockingbird", "Harper Lee", "J.B. Lippincott & Co.", 1960, 450, 20],
    106: ["The Hobbit", "J.R.R. Tolkien", "George Allen & Unwin", 1937, 550, 15],
    107: ["1984", "George Orwell", "Secker & Warburg", 1949, 399, 22],
    108: ["Pride and Prejudice", "Jane Austen", "T. Egerton", 1813, 299, 10],
    109: ["The Secret", "Rhonda Byrne", "Atria Books", 2006, 425, 17],
    110: ["Rich Dad Poor Dad", "Robert Kiyosaki", "Warner Books", 1997, 375, 28]
}

orders=dict()

while True:
          print("""-----------BOOKSTORE MANAGEMENT----------------
                 1. ADMIN PANEL
                 2. PURCHASE
                 3. INVOICE/BILLING
                 4. EXIT """)
          main_menu = int(input("Enter your choice:"))
          if main_menu == 1:  # 1. ADMIN PANEL
                    print("""-----------ADMIN PANEL------------
                  1. Insert new book
                  2. Display all books
                  3. Search for a book
                  4. Update a book
                  5. Delete a book
                  6. Back to main menu """)
                    admin = int(input("Enter your choice:"))
                    if admin == 1: # 1. Insert new book
                              new = [input('Book name:'),input('Author:'),input('Publisher:'),input('Year of publishing:'),input('Price:'),input('Stock:')]
                              Bookstore[max(Bookstore)+1]= new
                    elif admin == 2:# 2. Display all books
                        Dbooks = PrettyTable()
                        Dbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                        for a in Bookstore:
                            Dbooks.add_row([a,Bookstore[a][0],Bookstore[a][1],Bookstore[a][2],Bookstore[a][3],Bookstore[a][4],Bookstore[a][5]])
                        Dbooks.set_style(TableStyle.SINGLE_BORDER)
                        print(Dbooks)
                                  
                    elif admin == 3:  # 3. Search for a book
                              print("""-------SEARCH A BOOK--------
                                        1. BY BOOK TITLE
                                        2. BY BOOK ID
                                        3. BY PUBLISHER
                                        4. BY PUBLICATION YEAR
                                        5. BY PUBLISHED BETWEEN
                                        6. BY AUTHOR
                                        7. BACK""")
                              search = int(input("Enter your choice:"))
                              if search == 1: #1. BY BOOK TITLE
                                        btitle = input("Enter few consecutive characters of the book title:")
                                        found = False
                                        for bookno in Bookstore:
                                                  if Bookstore[bookno][0].lower().find(btitle.lower()) >= 0:
                                                            found = True
                                                            tbooks = PrettyTable()
                                                            tbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                                                            tbooks.add_row([bookno,Bookstore[bookno][0],Bookstore[bookno][1],Bookstore[bookno][2],Bookstore[bookno][3],Bookstore[bookno][4],Bookstore[bookno][5]])
                                                            tbooks.set_style(TableStyle.SINGLE_BORDER)
                                                            print(tbooks)
                                                            
                                        if not found:
                                                  print("No such book found!")
                                        

                                                                             
                              elif search == 2: #2 search by book no
                                        bookID = int(input('enter book id'))
                                        for bookno in Bookstore:
                                                  if bookID == bookno:
                                                      tbooks = PrettyTable()
                                                      tbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                                                      tbooks.add_row([bookno,Bookstore[bookno][0],Bookstore[bookno][1],Bookstore[bookno][2],Bookstore[bookno][3],Bookstore[bookno][4],Bookstore[bookno][5]])
                                                      tbooks.set_style(TableStyle.SINGLE_BORDER)
                                                      print(tbooks)
                                                      break
                                        else:
                                                  print('not Found')
                              elif search == 3: #3. BY PUBLISHER
                                        pub = input("Enter few consecutive characters of the publisher name:")
                                        found = False
                                        for bookno in Bookstore:
                                                  tbooks = PrettyTable()
                                                  tbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                                                  tbooks.set_style(TableStyle.SINGLE_BORDER)
                                                  if Bookstore[bookno][2].lower().find(pub.lower()) >= 0:
                                                            found = True
                                                            tbooks.add_row([bookno,Bookstore[bookno][0],Bookstore[bookno][1],Bookstore[bookno][2],Bookstore[bookno][3],Bookstore[bookno][4],Bookstore[bookno][5]])
                                                   
                                                  print(tbooks)
                                        if not found:
                                                  print("No such book found!")
                              elif search == 4: #4. BY YEAR
                                        found =False
                                        year = int(input('enter publication year:'))
                                        for bookno in Bookstore:
                                            tbooks = PrettyTable()
                                            tbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                                            if Bookstore[bookno][3] == year:
                                                      found = True
                                                      tbooks.add_row([bookno,Bookstore[bookno][0],Bookstore[bookno][1],Bookstore[bookno][2],Bookstore[bookno][3],Bookstore[bookno][4],Bookstore[bookno][5]])
                                                      tbooks.set_style(TableStyle.SINGLE_BORDER)
                                                      print(tbooks)
                                        if not found:
                                                  print('*'*50)
                                                  print('not found!')
                                                  print('='*50)
                              elif search == 5: #5. BY PUB. YEAR RANGE
                                        print('|ENTER PUBLICATION YEAR RANGE|')
                                        start = int(input('From:'))
                                        stop = int(input('Till:'))
                                        
                                        for bookno in Bookstore:
                                            if Bookstore[bookno][3] in range(start,stop+1):
                                                 tbooks = PrettyTable()
                                                 tbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                                                 tbooks.add_row([bookno,Bookstore[bookno][0],Bookstore[bookno][1],Bookstore[bookno][2],Bookstore[bookno][3],Bookstore[bookno][4],Bookstore[bookno][5]])
                                                 tbooks.set_style(TableStyle.SINGLE_BORDER)
                                                 print(tbooks)
                                               
                                        else:
                                            print('='*50)
                                            print('not found!')
                                            print('='*50)
                              elif search == 6: #6. BY AUTHOR
                                        found = False
                                        author = input('enter author:')
                                        print('='*50)
                                        for bookno in Bookstore:
                                            if Bookstore[bookno][1].lower() == author.lower():
                                                 found = True
                                                 tbooks = PrettyTable()
                                                 tbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                                                 tbooks.add_row([bookno,Bookstore[bookno][0],Bookstore[bookno][1],Bookstore[bookno][2],Bookstore[bookno][3],Bookstore[bookno][4],Bookstore[bookno][5]])
                                                 tbooks.set_style(TableStyle.SINGLE_BORDER)
                                                 print(tbooks)
                                        if not found:
                                                  print('not found!')
                                                  print('='*50)  
                              else:
                                        break #back to main search menu
                                    
                    elif admin == 4:  # 4. Update a book
                              # search for a book using bookno
                              
                              bookid = None
                              bookid = int(input('enter Book ID:'))
                              if bookid in Bookstore:
                                  
                                  tbooks = PrettyTable()
                                  tbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                                  tbooks.add_row([bookid,Bookstore[bookid][0],Bookstore[bookid][1],Bookstore[bookid][2],Bookstore[bookid][3],Bookstore[bookid][4],Bookstore[bookid][5]])
                                  tbooks.set_style(TableStyle.SINGLE_BORDER)
                                  print(tbooks)
                                  while True:
                                                  print("""-------------UPDATING BOOK RECORD----------------
Select the field one-by-one to update:
          1. BOOK TITLE
          2. AUTHOR
          3. PUBLICATION
          4. PUBLICATION YEAR
          5. PRICE
          6. STOCK
          7. BACK TO MAIN MENU>>""")
                                                  update = int(input("Enter your choice:"))
                                                  if update == 1:  # 1. BOOK TITLE
                                                            new = input('enter updated Book Title:')
                                                            Bookstore[bookid][0] = new
                                                            tbooks = PrettyTable()
                                                            tbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                                                            tbooks.add_row([bookid,Bookstore[bookid][0],Bookstore[bookid][1],Bookstore[bookid][2],Bookstore[bookid][3],Bookstore[bookid][4],Bookstore[bookid][5]])
                                                            tbooks.set_style(TableStyle.SINGLE_BORDER)
                                                            print(tbooks)
                                                  elif update == 2: # 2. AUTHOR
                                                            new = input('enter updated Author:')
                                                            Bookstore[bookid][1] = new
                                                            tbooks = PrettyTable()
                                                            tbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                                                            tbooks.add_row([bookid,Bookstore[bookid][0],Bookstore[bookid][1],Bookstore[bookid][2],Bookstore[bookid][3],Bookstore[bookid][4],Bookstore[bookid][5]])
                                                            tbooks.set_style(TableStyle.SINGLE_BORDER)
                                                            print(tbooks)
                                                  elif update == 3: # 3. PUBLICATION
                                                            new = input('enter updated Publication:')
                                                            Bookstore[bookid][2] = new
                                                            tbooks = PrettyTable()
                                                            tbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                                                            tbooks.add_row([bookid,Bookstore[bookid][0],Bookstore[bookid][1],Bookstore[bookid][2],Bookstore[bookid][3],Bookstore[bookid][4],Bookstore[bookid][5]])
                                                            tbooks.set_style(TableStyle.SINGLE_BORDER)
                                                            print(tbooks)
                                                  elif update == 4:  # 4. PUBLICATION YEAR
                                                            new = input('enter updated Publication Year:')
                                                            Bookstore[bookid][3] = new
                                                            tbooks = PrettyTable()
                                                            tbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                                                            tbooks.add_row([bookid,Bookstore[bookid][0],Bookstore[bookid][1],Bookstore[bookid][2],Bookstore[bookid][3],Bookstore[bookid][4],Bookstore[bookid][5]])
                                                            tbooks.set_style(TableStyle.SINGLE_BORDER)
                                                            print(tbooks)
                                                  elif update == 5:  # 5. PRICE
                                                            new = input('enter updated Price:')
                                                            Bookstore[bookid][4] = new
                                                            tbooks = PrettyTable()
                                                            tbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                                                            tbooks.add_row([bookid,Bookstore[bookid][0],Bookstore[bookid][1],Bookstore[bookid][2],Bookstore[bookid][3],Bookstore[bookid][4],Bookstore[bookid][5]])
                                                            tbooks.set_style(TableStyle.SINGLE_BORDER)
                                                            print(tbooks)
                                                  elif update == 6:  # 6. STOCK
                                                            new = input('enter updated Stock:')
                                                            Bookstore[bookid][5] = new
                                                            tbooks = PrettyTable()
                                                            tbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                                                            tbooks.add_row([bookid,Bookstore[bookid][0],Bookstore[bookid][1],Bookstore[bookid][2],Bookstore[bookid][3],Bookstore[bookid][4],Bookstore[bookid][5]])
                                                            tbooks.set_style(TableStyle.SINGLE_BORDER)
                                                            print(tbooks)
                                                  else:
                                                            break     # 7. BACK TO MAIN MENU>>
                              else:
                                        print("No book found!")
                              
                    elif admin == 5:  # 5. Delete a book
                              bookid = None
                              bookid = int(input('enter Book ID:'))
                              if bookid in Bookstore:
                                        tbooks = PrettyTable()
                                        tbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                                        tbooks.add_row([bookid,Bookstore[bookid][0],Bookstore[bookid][1],Bookstore[bookid][2],Bookstore[bookid][3],Bookstore[bookid][4],Bookstore[bookid][5]])
                                        tbooks.set_style(TableStyle.SINGLE_BORDER)
                                        print(tbooks)
                                        Bookstore.pop(bookid)
                                        print('book record deleted successfully')
                                        
                              else:
                                        print("No book found!")

                              
                    else:  # 6. Back to main menu
                        continue
                              
          elif main_menu == 2:  # 2. PURCHASE
                    ans = input('Do you want to purchase?[y/n]:')
                    new_order = list()
                    # --------auto-generate-orderid--------------
                    orderid = None
                    if not orders:
                              orderid = 1
                    else:
                              orderid = max(list(orders.keys())) + 1
                    # -------------------------------------------
                    cust_name = input('enter customer name:')
                    cust_add = input('enter customer address:')
                    cust_phone = input('enter customer phone number:')
                    cust_email = input('enter customer E-mail id:')
                    while ans in ('y','Y'):
                        #displaying all books
                              Dbooks = PrettyTable()
                              Dbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                              for a in Bookstore:
                                  Dbooks.add_row([a,Bookstore[a][0],Bookstore[a][1],Bookstore[a][2],Bookstore[a][3],Bookstore[a][4],Bookstore[a][5]])
                              Dbooks.set_style(TableStyle.SINGLE_BORDER)
                              print(Dbooks)
                        #purchase menu
                              bookid = None
                              bookid = int(input('\nenter Book ID:'))
                              if bookid in Bookstore:
                                        tbooks = PrettyTable()
                                        tbooks.field_names = ['BOOK ID','TITLE','AUTHOR','PUBLISHER','YEAR OF PUB.','PRICE','STOCK']
                                        tbooks.add_row([bookid,Bookstore[bookid][0],Bookstore[bookid][1],Bookstore[bookid][2],Bookstore[bookid][3],Bookstore[bookid][4],Bookstore[bookid][5]])
                                        tbooks.set_style(TableStyle.SINGLE_BORDER)
                                        print(tbooks)
                                        price = Bookstore[bookid][4]
                                        qty = int(input("Enter no.of copies to be purchased:"))
                                        stock = Bookstore[bookid][5]
                                        if qty >= stock:
                                                  print("Only "+str(stock)+" copies of the book remaining. Do you want to order? y/n")
                                                  order = input("enter y/n :")
                                                  if order == 'y':
                                                            qty = stock
                                                            Bookstore[bookid][5] = 0
                                                  else:
                                                          continue
                                        else:
                                                  Bookstore[bookid][5] -= qty
                                                  
                                        new_order.append([cust_name,cust_add,cust_phone,cust_email,bookid,Bookstore[bookid][0],Bookstore[bookid][4],qty,price*qty])                                
                                        
                              else:
                                        print('book no found')
                              
                              ans = input('continue purchasing?[y/n]:')
                    if new_order:
                              orders[orderid] = new_order
          elif main_menu == 3:  # 3. INVOICE/BILLING
                    # display a list of orderid,customer name
                    for ord_id in orders:
                              print('order id:',ord_id,' :- ','customer name:',orders[ord_id][0][0])
                    # ask from the user orderid
                    order_id = int(input('enter orderid:'))
                    tot_amt = 0
                    # display all details for that orderid
                    order_details = orders.get(order_id)
                    if order_details:
                              info = PrettyTable()
                              info.field_names = ["ORDER-ID","CUSTOMER NAME","ADDRESS","CONTACT NO.","EMAIL"]
                              info.add_row([order_id,order_details[0][0],order_details[0][1],order_details[0][2],order_details[0][3]])
                              info.set_style(TableStyle.SINGLE_BORDER)
                              print(info)

                              
                              x = PrettyTable()
                              x.field_names = ['BOOK ID','BOOK TITLE','PRICE','QTY','AMOUNT']
                              for orecord in order_details:
                                        x.add_row([orecord[4],orecord[5],orecord[6],orecord[7],orecord[8]])
                                        # [cust_name,cust_add,cust_phone,cust_email,bookid,Bookstore[bookid][0],Bookstore[bookid][4],qty,price*qty]
                                        tot_amt += orecord[8]
                              x.set_style(TableStyle.SINGLE_BORDER)
                              print(x)                              
                              # display the total amount payable in the end
                              print("TOTAL AMOUNT PAYABLE: \u20b9",tot_amt,'\n')
                    else:
                              print("NO SUCH ORDER PLACED!")
          else:
                    break   # exit
                    
          










