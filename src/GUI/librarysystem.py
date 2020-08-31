"""
@author Daniel Burrell
"""

from GUI.Views import Login
from GUI.Views import SignIn
from GUI.Views import NewAccount
from GUI.Views import Dashboard
from GUI.Views import HomeScreen
from GUI.Views import RentScreen
from GUI.Views import AddBook
from GUI.Views import ReturnScreen
from PyQt5.QtWidgets import QButtonGroup
from PyQt5 import QtWidgets
from GUI import database
import random
import string




class WelcomeScreen(Login.Ui_MainWindow):
    """ Launches the Welcome Screen that prompts the user to declare whether they are a regular user 
        or an administrator.
    """

    _welcomescreen = None
    _root = None

    def __init__(self, MainWindow: QtWidgets.QMainWindow)->None:
        if WelcomeScreen._welcomescreen is None:
            self.screen = MainWindow
            self.setupUi(self.screen)
            self._buttonGroup = QButtonGroup()
            self._buttonGroup.setExclusive(True)
            self._buttonGroup.addButton(self.adminButton)
            self._buttonGroup.addButton(self.userButton)
            self._buttonGroup.buttonClicked.connect(self._showLogin)
            WelcomeScreen._welcomescreen = self

        else:
            raise Exception("Unable to create another instance.")


    
    @classmethod
    def getWelcomeScreen(cls,MainWindow: QtWidgets.QMainWindow):
        """Returns the welcome screen.
           :param MainWindow (QMainWindow): A mainwindow.

        """

        if not cls._welcomescreen:
            cls(MainWindow)

        return cls._welcomescreen


    def _showLogin(self, clickedButton: QtWidgets.QPushButton)->None:
        """Shows the login screen.
           :param clickedButton (QPushButton): Either the User or Administrator button clicked.
        
        """

        if clickedButton == self.adminButton:
            WelcomeScreen._welcomescreen.screen.destroy()
            MainWindow = QtWidgets.QMainWindow()
            self._login = SignInScreen.getSignInScreen(MainWindow, "Administrator")
            self._login.screen.show()
        else:
            WelcomeScreen._welcomescreen.screen.destroy()
            MainWindow = QtWidgets.QMainWindow()
            self._login = SignInScreen.getSignInScreen(MainWindow, "User")
            self._login.screen.show()







class SignInScreen(SignIn.Ui_SignIn):
    """Defines the screen for a user to sign in."""

    _signInScreen = None

    def __init__(self, MainWindow: QtWidgets.QMainWindow, userType: str)->None:
        self.screen = MainWindow
        self.setupUi(self.screen)
        self.loginButton.clicked.connect(self._login)
        self.backButton.clicked.connect(self._back)
        self.createButton.clicked.connect(self._createAccount)
        self._userType = userType
        SignInScreen._signInScreen = self


    @classmethod
    def getSignInScreen(cls,MainWindow, userType=" "):
        """Returns the sign in screen.

           :param MainWindow (QMainWindow): A mainwindow.
           :param userType (str): The type of user currently on the system.
        """

        if not cls._signInScreen:
            cls(MainWindow, userType)
        
        return cls._signInScreen


    @staticmethod
    def clearInstance():
        """Clears the instance of the sign in screen"""

        if not SignInScreen._signInScreen is None:
            SignInScreen._signInScreen = None
        


    def _back(self):
        """Goes to the Login screen back from the sign in screen."""

        MainWindow = QtWidgets.QMainWindow()
        welcomeScreen = WelcomeScreen.getWelcomeScreen(MainWindow)
        welcomeScreen.screen.show()
        SignInScreen._signInScreen.screen.destroy()
        SignInScreen.clearInstance()


    def _login(self):
        """Validates a user's login credentials."""

        username = self.usernameField.text()
        password = self.passwordField.text()

        if username and password:
            if self._userType is "User":
                if database.validateUser(username,password):
                    dashboard = DashboardScreen.getDashboardScreen(QtWidgets.QMainWindow(),username)
                    SignInScreen._signInScreen.screen.destroy()
                    dashboard.screen.show()
                else:
                    self.error = QtWidgets.QErrorMessage()
                    self.error.setWindowTitle("Login Error")
                    self.error.showMessage("Incorrect User Credentials.")
            
            else:
                if database.validateAdmin(username,password):
                    adminScreen = BookEntry.getAddBookScreen(QtWidgets.QMainWindow(),username)
                    SignInScreen._signInScreen.screen.destroy()
                    adminScreen.screen.show()

                else:
                    self.error = QtWidgets.QErrorMessage()
                    self.error.setWindowTitle("Login Error")
                    self.error.showMessage("Incorrect Admin Credentials.")

        else:
            self.error = QtWidgets.QErrorMessage()
            self.error.setWindowTitle("Input Error")
            self.error.showMessage("Please enter all fields.")


    def _createAccount(self):
        """Shows the register screen."""

        MainWindow = QtWidgets.QMainWindow()
        registerScreen = RegisterScreen.getRegisterScreen(MainWindow,self._userType)
        registerScreen.screen.show()
        SignInScreen._signInScreen.screen.destroy()






class RegisterScreen(NewAccount.Ui_NewAccount):
    """Defines the screen for a user to create a new account."""

    _registerPage = None

    def __init__(self, MainWindow: QtWidgets.QMainWindow, userType: str)->None:
        if RegisterScreen._registerPage is None:
            self.screen = MainWindow
            self._userType = userType
            self.setupUi(self.screen)
            self.createButton.clicked.connect(self._createAccount)
            self.pushButton_2.clicked.connect(self._back)
            RegisterScreen._registerPage = self

        else:
            raise Exception("An instance of this class already exists.")


    
    @classmethod
    def getRegisterScreen(cls,MainWindow: QtWidgets.QMainWindow, userType: str):
        """Returns the register screen.
           :param MainWindow(QMainWindow): A mainwindow
           :param userType (str): The type of user
        
        """

        if not cls._registerPage:
            cls(MainWindow, userType)

        return cls._registerPage


    
    def _createAccount(self):
        """Validates credentials and creates an account in the database."""

        username = self.username.text()
        firstname = self.firstname.text()
        lastname = self.lastname.text()
        password = self.password.text()
        confirmPass = self.confirm.text()

        if username and firstname and lastname and password and confirmPass:
            if password == confirmPass:
                if self._userType is "User":
                    if database.addUser(username,password,firstname,lastname):
                        print("User account was created.")
                    
                    else:
                        self.error = QtWidgets.QErrorMessage()
                        self.error.setWindowTitle("Creation Error")
                        self.error.showMessage("Unable to create User account.")

                else:
                    if database.addAdmin(username,password,firstname,lastname):
                        print("Admin account was created.")

                    else:
                        self.error = QtWidgets.QErrorMessage()
                        self.error.setWindowTitle("Creation Error")
                        self.error.showMessage("Unable to create Admin account.")
            
            else:
                self.error = QtWidgets.QErrorMessage()
                self.error.setWindowTitle("Input Error")
                self.error.showMessage("Make sure Password and Confirm Password are the same.")

        else:
            self.error = QtWidgets.QErrorMessage()
            self.error.setWindowTitle("Input Error")
            self.error.showMessage("Please enter all fields.")

    
    def _back(self):
        """Returns to the sign in screen from the register screen."""

        MainWindow = QtWidgets.QMainWindow()
        signInScreen = SignInScreen.getSignInScreen(MainWindow, self._userType)
        signInScreen.screen.show()
        RegisterScreen._registerPage.screen.destroy()
        RegisterScreen._registerPage = None







class DashboardScreen(Dashboard.Ui_MainWindow):
    """Defines the dashboard screen that will be shown to a regular user of the system."""

    _dashboardScreen = None

    def __init__(self, MainWindow: QtWidgets.QMainWindow, user: str)->None:
        if DashboardScreen._dashboardScreen is None:
            self.currentUser = user
            self.screen = MainWindow
            self.setupUi(self.screen)
            self._buttonGroup = QtWidgets.QButtonGroup()
            self._buttonGroup.addButton(self.borrow)
            self._buttonGroup.addButton(self.home)
            self.layout = QtWidgets.QHBoxLayout(self.displayFrame)
            self._buttonGroup.addButton(self.signout)
            self._buttonGroup.addButton(self.rent)
            self._buttonGroup.buttonClicked.connect(self._switchPage)
            self._showHome()
            DashboardScreen._dashboardScreen = self

        else:
            raise Exception("An instance already exists.")


    @classmethod
    def getDashboardScreen(cls,MainWindow: QtWidgets.QMainWindow, user: str):
        """Returns the dashboard screen
           
           :param MainWindow(QMainWindow): A mainwindow
           :param user (str): The current user of the system.
        
        """
        if not cls._dashboardScreen:
            cls(MainWindow,user)

        return cls._dashboardScreen

    

    def _switchPage(self, clickedButton: QtWidgets.QPushButton)->None:
        """Switch the pages on the dashboard.
           :param clickedButton (QPushButton): A button on the dashboard
        
        """

        if clickedButton == self.home:
            self._showHome()
        
        elif clickedButton == self.borrow:
            self._clearLayout()
            borrowScreen = Rent.getRentScreen(QtWidgets.QFrame(),self.currentUser)
            borrowScreen._rentscreen.populateTable()
            self.layout.addWidget(borrowScreen._rentscreen.frame)
            borrowScreen._rentscreen.frame.show()

        
        elif clickedButton == self.rent:
            self._clearLayout()
            returnScreen = BookReturn.getReturnScreen(QtWidgets.QFrame(),self.currentUser)
            returnScreen._returnscreen.populateTable()
            self.layout.addWidget(returnScreen._returnscreen.frame)
            returnScreen._returnscreen.frame.show()
            
        else:
            DashboardScreen._dashboardScreen.screen.destroy()
            signInScreen = SignInScreen.getSignInScreen(QtWidgets.QMainWindow)
            Home._homescreen = None
            Rent._rentscreen = None
            BookReturn._returnscreen = None
            DashboardScreen._dashboardScreen = None
            signInScreen.screen.show()



    
    def _showHome(self):
        """Shows the overdue book screen for a user."""
        
        self._clearLayout()
        homeScreen = Home.getHomeFrame(QtWidgets.QFrame(),self.currentUser)
        homeScreen._homescreen.populateTable()
        self.layout.addWidget(homeScreen._homescreen.frame)
        homeScreen._homescreen.frame.show()


    def _clearLayout(self):
        """Clears the layout in order to switch dashboard pages"""

        child = self.layout.itemAt(0)
        if child:
            child.widget().setParent(None)

        

class Home(HomeScreen.Ui_homeFrame):
    """Defines the homescreen where users see the books that are overdue for return."""

    _homescreen = None

    def __init__(self, Frame: QtWidgets.QFrame, user: str):
        if Home._homescreen is None:
            self.frame = Frame
            self.setupUi(self.frame)
            self._currentUser = user
            self.overdueBooksTable.setEnabled(False)
            self.overdueBooksTable.setColumnCount(3)
            self.overdueBooksTable.setHorizontalHeaderLabels(["Rental ID","Book ID","Return Date"])
            Home._homescreen = self
        
        else:
            raise Exception("An instance already exists.")



    @classmethod
    def getHomeFrame(cls,Frame: QtWidgets.QFrame, user: str):
        """Returns the home screen page of the dashboard
           
           :param Frame (QFrame): A frame
           :param user (str): The current user of the system

        """

        if not cls._homescreen:
            cls(Frame,user)

        return cls._homescreen


    
    def populateTable(self)->None:
        """Populates the overdue table."""

        self.overdueBooksTable.setRowCount(0)
        overduebooks = database.getOverdueRentals(self._currentUser)
        if not overduebooks is None:
            for rowNumber, rental in enumerate(overduebooks):
                self.overdueBooksTable.insertRow(rowNumber)
                for columnNumber, content in enumerate(rental):
                    self.overdueBooksTable.setColumnWidth(columnNumber,160)
                    self.overdueBooksTable.setItem(rowNumber,columnNumber,QtWidgets.QTableWidgetItem(str(content)))





class Rent(RentScreen.Ui_Frame):
    """Defines the screen where users are able to make rentals based on the books available."""

    _rentscreen = None
    
    def __init__(self, Frame: QtWidgets.QFrame, user: str):
        if Rent._rentscreen == None:
            self.frame = Frame
            self.setupUi(self.frame)
            self._currentUser = user
            self.rentButton.clicked.connect(self._rentBook)
            self.bookTable.setColumnCount(6)
            self.bookTable.setHorizontalHeaderLabels(["Book ID","Title","Author(s)","Genre(s)","Amount","Publication Date"])
            Rent._rentscreen = self


    @classmethod
    def getRentScreen(cls,Frame: QtWidgets.QFrame, user: str)->None:
        """Returns the book rent screen
           
           :param Frame (QFrame): A frame
           :param user (str): The current user of the system.

        """
        if not cls._rentscreen:
            cls(Frame,user)

        return cls._rentscreen


    def populateTable(self)->None:
        """Populates the book table"""

        self.bookTable.setRowCount(0)
        books = database.getBooks()
        if not books is None:
            for rowNumber, tuples in enumerate(books):
                self.bookTable.insertRow(rowNumber)
                for columnNumber, content in enumerate(tuples):
                    self.bookTable.setItem(rowNumber,columnNumber,QtWidgets.QTableWidgetItem(str(content)))




    def _rentBook(self):
        """Carries out the rental of a book."""

        if self.bookTable.currentColumn() == 0:
            bookID = self.bookTable.currentItem().text()
            letters = string.ascii_letters + string.digits
            if database.addRental(''.join(random.choice(letters) for _ in range(10)),self._currentUser,bookID):
                self.message = QtWidgets.QMessageBox()
                self.message.setIcon(QtWidgets.QMessageBox.Information)
                self.message.setWindowTitle("Rental Made")
                self.message.setFixedWidth(600)
                self.message.setInformativeText("Rental was successful.")
                self.message.show()
                self.populateTable()

            else:
                self.error = QtWidgets.QErrorMessage()
                self.error.setWindowTitle("Rental Error")
                self.error.showMessage("Rental was not successful.")

        else:
            self.error = QtWidgets.QErrorMessage()
            self.error.setWindowTitle("Selection Error")
            self.error.showMessage("Please select a Book ID")





class BookReturn(ReturnScreen.Ui_Frame):
    """Defines the screen where users are able to return a book they have rented."""

    _returnscreen = None
    
    def __init__(self, Frame: QtWidgets.QFrame, user: str):
        if BookReturn._returnscreen == None:
            self.frame = Frame
            self.setupUi(self.frame)
            self._currentUser = user
            self.returnButton.clicked.connect(self._returnBook)
            self.rentedBookTable.setColumnCount(4)
            self.rentedBookTable.setHorizontalHeaderLabels(["Rental ID","Book ID","Date Rented","Return Date"])
            BookReturn._returnscreen = self


    @classmethod
    def getReturnScreen(cls,Frame: QtWidgets.QFrame, user: str)->None:
        """Returns the book return screen."""

        if not cls._returnscreen:
            cls(Frame,user)

        return cls._returnscreen


    def populateTable(self)->None:
        """Populates the rental table"""

        self.rentedBookTable.setRowCount(0)
        rentalBooks = database.getRentals(self._currentUser)
        if not rentalBooks is None:
            for rowNumber, tuples in enumerate(rentalBooks):
                self.rentedBookTable.insertRow(rowNumber)
                for columnNumber, content in enumerate(tuples):
                    self.rentedBookTable.setColumnWidth(columnNumber,125)
                    self.rentedBookTable.setItem(rowNumber,columnNumber,QtWidgets.QTableWidgetItem(str(content)))


    
    def _returnBook(self):
        """Carries out a rental"""

        if self.rentedBookTable.currentColumn() == 0:
            rentalID = self.rentedBookTable.currentItem().text()
            bookID = self.rentedBookTable.item(self.rentedBookTable.currentRow(),1).text()
            if database.removeRental(rentalID,bookID):
                self.message = QtWidgets.QMessageBox()
                self.message.setIcon(QtWidgets.QMessageBox.Information)
                self.message.setWindowTitle("Return Made")
                self.message.setFixedWidth(600)
                self.message.setInformativeText("Return was successful.")
                self.message.show()
                self.populateTable()

            else:
                self.error = QtWidgets.QErrorMessage()
                self.error.setWindowTitle("Return Error")
                self.error.showMessage("Book was not returned successfully.")
            
        else:
            self.error = QtWidgets.QErrorMessage()
            self.error.setWindowTitle("Selection Error")
            self.error.showMessage("Please select a Rental ID")







class BookEntry(AddBook.Ui_MainWindow):
    """Defines the screen where an admin is able to add a new book and/or collection to the database."""

    _addbookscreen = None

    def __init__(self,MainWindow: QtWidgets.QMainWindow, currentAdmin: str):
        if BookEntry._addbookscreen is None:
            self.screen = MainWindow
            self.setupUi(self.screen)
            self._currentAdmin = currentAdmin
            self.addBook.clicked.connect(self._pushBook)
            self.back.clicked.connect(self._back)
            BookEntry._addbookscreen = self

        else:
            raise Exception("An instance already exists.")

    
    @classmethod
    def getAddBookScreen(cls,MainWindow: QtWidgets.QMainWindow, currentAdmin: str):
        """Returns the add book screen"""

        if not cls._addbookscreen:
            cls(MainWindow,currentAdmin)

        return cls._addbookscreen


    
    def _pushBook(self):
        """Pushes a new book and/or collection to the database."""

        bookid = self.bookID.text()
        author = self.author.text()
        genre = self.genre.text()
        collection = self.collectionID.text()
        title = self.title.text()
        amount = self.amount.value()
        publisher = self.publisher.text()
        publicationDate = self.publicationDate.dateTime()

        if bookid and author and genre and title and amount and publisher and publicationDate and collection: #Creating new collection and adding book to it
            genreList = genre.split(",")
            authorList = author.split(",")
            if database.addBook(bookid,collection,self._currentAdmin, author= authorList,genre= genreList, title= title, amount= amount, publisher= publisher, publicationDate= publicationDate.toPyDateTime()):
                self.message = QtWidgets.QMessageBox()
                self.message.setIcon(QtWidgets.QMessageBox.Information)
                self.message.setWindowTitle("Book Entry Made")
                self.message.setFixedWidth(600)
                self.message.setInformativeText("Book Entry was successful.")
                self.message.show()

            else:
                self.error = QtWidgets.QErrorMessage()
                self.error.setWindowTitle("Add Error")
                self.error.showMessage("Book was not pushed successfully.")

        elif bookid and collection: #Adding book to existing collection
            if database.addBook(bookid, collection, self._currentAdmin):
                self.message = QtWidgets.QMessageBox()
                self.message.setIcon(QtWidgets.QMessageBox.Information)
                self.message.setWindowTitle("Book Entry Made")
                self.message.setInformativeText("Book Entry was successfull.")
                self.message.show()

            else:
                self.error = QtWidgets.QErrorMessage()
                self.error.setWindowTitle("Add Error")
                self.error.showMessage("Book was not pushed successfully.")

        else: #Sufficient fields not provided
            self.error = QtWidgets.QErrorMessage()
            self.error.setWindowTitle("Input Error")
            self.error.showMessage("Please enter the required fields.")



    def _back(self):
        """Returns to the sign in screen"""

        BookEntry._addbookscreen.screen.destroy()
        signInScreen = SignInScreen.getSignInScreen(QtWidgets.QMainWindow)
        BookEntry._addbookscreen = None
        signInScreen.screen.show()


