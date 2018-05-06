Guys i need you to write all your file names and what they do in here. We will remove the text that says “manager” , “Employee” and “Customer” but that’s so that everyone can write without it getting mixed up


Manager:  
To run this the user must make sure that their HTML files are in a templates folder called templates. 
The python files and database files must be outside the templates folder but the python and the templates folder must all be in the same folder. 
User must have python downloaded on laptop/desktop computer and added to path environment variable.  
The user will also need flask, numpy, and SQLite downloaded on their system as well.
When the user wants to run it, the user will need to go into terminal/command prompt and make sure that the user is in the folder where the python code is and making  sure that folder has a subfolder named templates which will contain the html files that will be run.
The user must type into the command prompt/terminal window: python thing.py  and a url would come up such as http://localhost:8000 
Go to that link and you will be directed to the application.


addItemForm.html  - webpage used in adding an item to the inventory
added.html - determines whether adding a new item to the menu was successful or not
addtoMenu.html - used in adding an item to the menu                
deleteItemForm.html        - delete an item from the inventory 
deleted.html - prints whether deleting an item from menu was a success or not
deletefromMenu.html        - form that takes in user input specifying what menu item to remove
financemenu1.html - finances submenu after going into finances menu
inventoryPage.html - list of all items in the inventory database
inventorymenu1.html        - gives user options after entering inventory menu
mainmenu1.html - displays the main menu when user(manager) initially logs in         
menuPage.html - displays the menu database
menuoptions1.htm - displays the menu submenu         
transactionsTable.html - page displaying all the transactions of restaurant        
updateMenuItem.html        - form which takes in user input which updates a menu item price 
updatedMenu.html - result of updating a menu item
addEmployee1.html - add an employee to the system
deleteEmployee1.html - delete an employee from the system        
employeePortal1.html - page that displays employee submenu
profProjForm.html - form asking length of time to take in as input to project future profits        
profitMenu.html - page displaying  profit submenu
restaurantTraffic1.html - page displaying amount of traffic in the restuarant        
result.html - determines whether adding item to inventory was successful or not
result2.html- displays whether deleting an item from the inventory worked or gave an error
result3.html - result of adding an employee
result4.html - result of deleting an employee from the system
result5.html - page displaying result of profit projections
result6.html - form obtaining values of length of time to calculate profit projections
searchInventory.html - search through the inventory items
updateResult.html - result of updating an item in the inventory
wagesPage.html - amount of pay for the employees
weeklyProfits.html - profits for each week
initializeInventory.py - initializes the inventory database
initializeMenu.py - initializes the menu database
initializeTransactionHistory.py - connecting the frontend and backend that deal with transactions
menu.db - database file of menu items
inventory.db - database file of inventory items
trafficmonitoring.db - database for amount of traffic in the restaurant
transactionHistory.db - database of transactions of the restaurant






Employee:     
addshifts.html - webpage for employee to add shift
changeshifts.html - webpage for employee shift changes
employeelogin.html - webpage for employee login
employeemainpage.html - webpage for viewing employee home screen
empviewshift.HTML - webpage for viewing shifts
viewpayrate.html - webpage to view employee pay rate
viewprofile.html - webpage for employee to view their own profile
viewshifts.html         - webpage to view all scheduled shifts
wagesPage.html - webpage of the employee wages
mainlog.html - webpage of main login screen
bgvp.jpg - background photo to view employee profile
chat.jpg - background for the chat page
cheflogo.png - chef’s logo icon
clock.jpg  - clock icon
emp.jpg - employee background photo
employeelogin.css - employee login code
employeemainpage.css  - employee main page code
empviewshift4.css  - employee view shift code
hello.js - login page code
images.jpg - background photo
loginbg.jpg - log in background
main.css - main file for employee side
mainlogdemo2.css - main file for employee side updated
or.jpg - icon photo
pay.jpg - pay rate photo icon
payet.jpg - pay rate background
profile.jpg - employee profile photo icon
re.jpg - background image
res.jpg - background image
restaurant.jpg - background image for restaurant
restaurant1.png - background image for restaurant updated
shiftsimg.gif - shift schedule background image
t.jpg - background image
viewprofile.jpg - employee view profile background
vp.css - view employee profile file
vp.png - view employee profile icon photo
addshiftsbusser.html - webpage for busser to add shifts
addshiftschef.html - webpage for chef to add shifts
addshiftswaiter.html - webpage for waiter to add shifts
busserlogin.html - webpage for busser login        
bussermainpage.html - webpage for busser’s home page
changeshiftsbusser.html - webpage for busser to change shifts
changeshiftschef.html - webpage for chef to change shifts
changeshiftswaiter.html - webpage for waiter to change shifts
chatapp.html - employee chat application webpage
cheflogin.html - webpage for chef login
chefmainpage.html - webpage for chef home page
clientwaiter.html - webpage for waiter homepage
deleteshiftsbusser.html - webpage for busser to delete shifts
deleteshiftschef.html - webpage for chef to delete shifts
deleteshiftswaiter.html - webpage for waiter to delete shifts        
empviewshiftbusser.html - webpage for busser to view shifts
empviewshiftchef.html - webpage for chef to view shifts
empviewshiftwaiter.html - webpage for waiter to view shifts        
mainlogdemo2.html - webpage for updated login file
orderinterfacechef.html - webpage for chef interface
serverchef.html - webpage for chef’s server
socket.html - webpage for chat system
sync.html - webpage to chat system
trafficmonitoring.html - webpage for traffic monitoring
trafficmonitoringb.html - webpage for traffic monitoring
viewpayratebusser.html - webpage to view busser pay rate
viewpayratechef.html - webpage to view chef pay rate
viewpayratewaiter.html - webpage to view waiter pay rate
viewprofilebusser.html - webpage to view busser profile rate
viewprofilechef.html - webpage to view busser profile rate
viewprofilewaiter.html - webpage to view busser profile rate
waiterlogin.html - webpage to waiter login
waitermainpage.html        - webpage for waiter home page
busserSchedule.db - database for busser schedule
chefSchedule.db - database for chef schedule
orderStatus.db - database from order status
orderStatus1.db - database from order status
staffProfile.db - database for all staff profile
waiterSchedule.db - database for waiter schedule
busserprofile.db - database for busser profile
chatapp.py - database for chat system
chefprofile.db - database for chef profile
Mainlogdemo2.py - main python file
mainlogdemo2busser.pyc - busser login python file
mainlogdemo2chef.pyc - chef login python file
mainlogdemo2waiter.pyc - waiter login python file
waiterprofile.db - database for waiter profile




Customer:
├─ config/ //folder that contains the database
├─── database.php
├─ dev/ //folder that contains the sql file for setting up the database
├─── shop_cart_sessions_1.sql
├─── readme.txt
├─ images/ 
├─ libs/ //folder that stores the custom css files
├─── css/
├────── bootstrap/ 
├─── js/
├────── jquery.js
├─ objects/ //folder that contains the main php files for the products displayed
├─── product_image.php 
├─── product.php
├─ uploads/ //folder contains all the images for the products
├─── images/
├─────bbqwings.jpg //Item image
├─────buffalowings.jpg        //Item image
├─────chickenpenne.jpg   //Item image
├─────chocice.jpg                //Item image
├─────cocacola.jpg                //Item image
├─────coffe.jpg                  //Item image
├─────frenchsoup.jpg        //Item image
├─────greensalad.jpg        //Item image
├─────hot-tea.jpg                  //Item image
├─────icedtea.jpg            //Item image
├─────lasagna.jpg                //Item image
├─────lavacake.jpg                //Item image
├─────maccheese.jpg        //Item image
├─────mozzsticks.jpg        //Item image
├─────nuggsandfries.jpg        //Item image
├─────panpizza.jpg        //Item image
├─────ravioli.jpg                //Item image
├─────spinachDip.jpg        //Item image
├─────sprite.jpg                //Item image
├─────tomatosoup.jpg        //Item image
├─────vanice.jpg                //Item image
├─────water.jpg                //Item image
├─Reservation
├───reservationmain.html- initializes the array that contains the status of the tables
reservation.html- customer interface for reserving tables
confused.html - tutorial for customers on how to reserve tables.
reservationEmp.html - for employee to change the status of the table from busy to available
empS.html - for employee to sign in to change the table status
Confused2- employee table status change tutorial
2.png - restaurant layout
Available.png - normal table available
Available-b.png - top booth available
Available-c.png - bottom booth available
Available-d.png - employee interface available table
booked.png - normal table booked
booked-b.png - top booth booked
booked-c.png - bottom booth booked
booked-d.png - employee interface booked table


selected.png - normal table selected
selected.png - top booth selected
selected.png - bottom booth selected
unavailable.png - normal table unavailable
unavailable.png - top booth unavailable
unavailable.png - bottom booth unavailable
unavailable.png - employee interface unavailable table
noSeat.png - transparent picture for when there are no tables
├─ .htaccess        
├─ add_to_cart.php        //file that adds items to the cart and updates it
├─ cart.php                 // file that displays the cart
├─ checkout.php        //files that displays the cart and payment option
├─ layout_footer.php                //footer template for the php files
├─ layout_header.php        //header template for the php file
├─ navigation.php                // php file that enable going through different item pages
├─ paging.php                // the pages 
├─ place_order.php                // php file that sends items to check out
├─ product.php                // the php file that displays each product
├─ products.php                // the php file that updates and organizes the products
├─ read_products_template.php        //Php file that reads the products from the database
├─ remove_from_cart.php                //php file that removes item from database
├─ update_quantity.php                // updates quantity of items on cart
├─games.php                                //displays available gaming options
├─piano.html                //one of the games
├─uno.html                //one of the games
├─thing.db                //sqlite3 database for the items ordered
├─pexels-photo-326279.jpeg //the backround picture
├─Tutorial.php                //the tutorial page


Students.db












How to run the code:
Please include here how to run your software
Customer: 
When a customer walks in, they first see the hostess table where they can make their reservation. 
1. To view this interface: go to reservationmain.html. Click on the table you’d like to reserve and from there, it’ self explanatory. 
They then do to their table where they can view the menu and place order then pay
b) to view this interface → write here


Employee:
#http://flask.pocoo.org/docs/0.12/testing/ 
#The code in the setUp() method creates a new test client and initializes a new database. This function is called before each individual test function is run
#This file was called and run for each function the mainlogdemo2.py
#The 'DATABaSE' corresponds to our multiple databses we used like "employeeshiftsdb.db", "orderstatus.db"
import os
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

   def setUp(self):
       self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
       flaskr.app.testing = True
       self.app = flaskr.app.test_client()
       with flaskr.app.app_context():
           flaskr.init_db()

   def tearDown(self):
       os.close(self.db_fd)
       os.unlink(flaskr.app.config['DATABASE'])

if __name__ == '__main__':
   unittest.main()
Manager: