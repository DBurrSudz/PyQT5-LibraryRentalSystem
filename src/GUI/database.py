from peewee import *
import os
import datetime


libraryDB = MySQLDatabase("library_rental", host= "localhost", port= 3306, user= "root", passwd= os.environ.get('libraryDBPassword'))


class Table(Model):
    """Base class that represents a table in the database. Inherits from peewee.Model and 
       defines an inner class Meta which specifies the database.

    """

    class Meta:
        database = libraryDB



class User(Table):
    """Model that represents the User table in the database."""

    _username = CharField(primary_key= True, column_name= "Username")
    _password = CharField(column_name= "Password")
    _firstname = CharField(column_name= "Firstname")
    _lastname = CharField(column_name= "Lastname")




class Administrator(Table):
    """Model that represents the Administrator table in the database."""

    _username = CharField(primary_key= True, column_name= "Username")
    _password = CharField(column_name= "Password")
    _firstname = CharField(column_name= "Firstname")
    _lastname = CharField(column_name= "Lastname")



class Collection(Table):
    """Model that represents the Collection table in the database."""

    _collectionID = CharField(primary_key= True, column_name= "Collection ID")
    _title = CharField(column_name= "Title")
    _publisher = CharField(column_name= "Publisher")
    _author = CharField(column_name= "Author")
    _genre = CharField(column_name= "Genre")
    _amount = IntegerField(column_name= "Amount In Stock")
    _publicationDate = DateField(column_name= "Publication Date")




class Book(Table):
    """Model that represents the Book table in the database."""

    _bookID = CharField(primary_key= True, column_name= "Book ID")
    _collectionID = ForeignKeyField(Collection, column_name= "Collection ID", backref="books")
    _adminID = ForeignKeyField(Administrator, column_name= "Admin ID", backref="books")




class Rental(Table):
    """Model that represents the Rental table in the database."""

    _rentalID = CharField(primary_key= True, column_name= "Rental ID")
    _username = ForeignKeyField(User, column_name= "User", backref= "rentals")
    _bookID = ForeignKeyField(Book, column_name= "Book ID", backref= "rentals")
    _dateRented = DateField(column_name= "Date Rented")
    _returnDate = DateField(column_name= "Return Date")









def addCollection(collectionid: str, title: str, publisher: str, author: list, genre: list, amount: int, publicationDate: datetime.datetime)-> bool:
    """Adds a new Book record to the database. Unpacks the lists containing the authors and genres into a str delimited by a ','.

       :param collectionid (str): The id of the collection.
       :param title (str): The title of the books in that collection.
       :param publisher (str): The publisher of the books in that collection.
       :param author (list): The author(s) of the books in that collection.
       :param genre (list): The genre(s) of the books in that collection.
       :param amount (int): The amount of the books in stock for that collection.
       :param publicationDate (datetime): The date that the books of the collection was published.
       :rtype (bool): If the creation of the record was successful.
       :raises IntegrityError: The collection id submitted already exists in the Collection table.

    """
    try:
        libraryDB.connect(reuse_if_open=True)
        if Collection.insert(_collectionID= collectionid.strip(), _title= title.strip(), _publisher= publisher.strip(), _author= ",".join(author), _genre= ",".join(genre), _amount= amount, _publicationDate= publicationDate).execute() == 0:
            print(f"The Collection ID {collectionid.strip()} is available.")
            return True

    except IntegrityError:
        print(f"The Collection ID {collectionid.strip()} is already being used.")
        return False

    finally:
        libraryDB.close()



def addUser(usrname: str, passw: str, fname: str, lname: str)-> bool:
    """Adds a new User record to the database.

       :param usrname (str): The username of the user.
       :param passw (str): The password of the user.
       :param fname (str): The first name of the user.
       :param lname (str): The last name of the user.
       :rtype (bool): If the creation of the record was successful.
       :raises IntegrityError: The username submitted already exists in the User table.

    """
    try:
        libraryDB.connect(reuse_if_open=True)
        if User.insert(_username= usrname.strip(), _password= passw.strip(), _firstname= fname.strip(), _lastname= lname.strip()).execute() == 0:
            print(f"The Username {usrname.strip()} is available.")
            return True

    except IntegrityError:
        print(f"The Username {usrname.strip()} has already been taken.")
        return False

    finally:
        print("The database connection has been closed.")
        libraryDB.close()




def validateUser(usrname: str, passw: str)-> bool:
    """ Checks if a user is valid in the database.

        :param usrname (str): The username of the user.
        :param passw (str): The password of the user.
        :rtype (bool): If the user is valid.
        :raises DoesNotExist: The user was not found in the User table.

    """

    try:
        libraryDB.connect(reuse_if_open=True)
        query = User.select().where((User._username == usrname.strip()) & (User._password == passw.strip())).get()
        if query:
            return True
    

    except DoesNotExist:
        return False


    finally:
        libraryDB.close()





def addBook(bookid: str, collectionid: str, adminid: str, **kwargs)-> bool:
    """Adds a new Book record to the database. Unpacks the lists containing the authors and genres into a str delimited by a ','.

       :param bookid (str): The id of the book.
       :param collectionid (str): The id of the collection that the book belongs to.
       :param adminid (str): The id of the administrator who is adding the book.
       :rtype (bool): If the creation of the record was successful.
       :raises IntegrityError: The book id submitted already exists in the Book table.

    """
    try:
        libraryDB.connect(reuse_if_open=True)
        if kwargs:
            if addCollection(collectionid,kwargs["title"],kwargs["publisher"],kwargs["author"],kwargs["genre"],kwargs["amount"],kwargs["publicationDate"]) and Book.insert(_bookID= bookid.strip(), _collectionID= collectionid.strip(), _adminID= adminid.strip()).execute() == 0: #Adds new collection and adds book
                return True

            else:
                return False

        else:
            if Book.insert(_bookID= bookid.strip(), _collectionID= collectionid.strip(), _adminID= adminid.strip()).execute() == 0: #adds book to existing collection
                print(f"The Book ID {bookid.strip()} is available.")
                return True

    except IntegrityError:
        print(f"The Book ID {bookid.strip()} is already being used.")
        return False

    finally:
        libraryDB.close()






def getOverdueRentals(currentUser: str):
    """Get the overdue books for a certain user.

       :param currentUser (str): The username of the current user of the system.
       :rtype (list): A list of tuples each containing the required information about an overdue rental.
       :raises DoesNotExist: There was no rental record satisfying the criteria.

    """

    try:
        libraryDB.connect(reuse_if_open=True)
        query = Rental.select(Rental._rentalID,Rental._bookID, Rental._returnDate).where((Rental._username == currentUser.strip()) & (Rental._returnDate <= datetime.datetime.now()))
        if query:
            return [(rental._rentalID,rental._bookID,rental._returnDate) for rental in query]

    except DoesNotExist:
        return None

    finally:
        libraryDB.close()




def getRentals(currentUser: str):
    """Gets all the rentals made for a particular user.
       
       :param currentUser (str): The username of the current user of the system.
       :rtype (list): A list of tuples each containing the required information about a rental.
       :raises DoesNotExist: There was no rental record satisfying the criteria.

    """

    try:
        libraryDB.connect(reuse_if_open=True)
        query = Rental.select().where(Rental._username == currentUser)
        if query:
            return [(rental._rentalID,rental._bookID,rental._dateRented,rental._returnDate) for rental in query]

    except DoesNotExist:
        return None

    finally:
        libraryDB.close()




def getBooks():
    """Gets all the books in the database

       :rtype (list): A list of tuples containing the required information for a book.
       :raises DoesNotExist: No record was retrieved.
    
    """

    try:
        libraryDB.connect(reuse_if_open=True)
        query = Collection.select(Book._bookID,Collection._title,Collection._author,Collection._genre,Collection._amount,Collection._publicationDate).join(Book).where(Collection._amount > 0).dicts()
        if query:
            li = []
            for record in query:
                li.append(tuple(record.values()))           
            return li

    except DoesNotExist:
        return None

    
    finally:
        libraryDB.close()



    

def addAdmin(usrname: str, passw: str, fname: str, lname: str)-> bool:
    """Adds a new Administrator record to the database.

       :param usrname (str): The username of the administrator.
       :param passw (str): The password of the administrator.
       :param fname (str): The first name of the administrator.
       :param lname (str): The last name of the administrator.
       :rtype (bool): If the creation of the record was successful.
       :raises IntegrityError: The username submitted already exists in the Administrator table.

    """
       
    try:
        libraryDB.connect(reuse_if_open=True)
        if Administrator.insert(_username= usrname.strip(), _password= passw.strip(), _firstname= fname.strip(), _lastname= lname.strip()).execute() == 0:
            return True
   
    except IntegrityError:
        return False

    finally:
        libraryDB.close()
  




def validateAdmin(usrname: str, passw: str)-> bool:
    """ Checks if an admin is valid in the database.

        :param usrname (str): The username of the admin.
        :param passw (str): The password of the admin.
        :rtype (bool): If the admin is valid.
        :raises DoesNotExist: The user was not found in the Administrator table.

    """

    try:
        libraryDB.connect(reuse_if_open=True)
        query = Administrator.select().where((Administrator._username == usrname.strip()) & (Administrator._password == passw.strip())).get()
        if query:
            return True
    

    except DoesNotExist:
        return False


    finally:
        libraryDB.close()




def addRental(rentalid: str, usrname: str, bookid: str)-> bool:
    """Adds a new Rental record to the database. The rental date of the book is inferred by the function
       upon call and the subsequent return date is also calculated using the inferred rental date. The rental date of the book
       will be the date of the function's call.
       
       :param rentalid (str): The rental id.
       :param usrname (str): The username of the person who made the rental.
       :param bookid (str): The id of the book that was rented.
       :rtype (bool): If the creation of the record was successful.
       :raises IntegrityError: The rental id submitted already exists in the Rental table.

    """
    try:
        libraryDB.connect(reuse_if_open=True)
        query = Collection.select(Collection._collectionID,Collection._amount).join(Book).where(Book._bookID == bookid)
        if query:
            for result in query:
                updateAmt = result._amount - 1
                if Collection.update(_amount = updateAmt).where(Collection._collectionID == result._collectionID).execute() == 1:
                    break

                else:
                    return False

            if Rental.insert(_rentalID= rentalid.strip(), _username= usrname.strip(), _bookID= bookid.strip(), _dateRented= datetime.datetime.now(), _returnDate= datetime.datetime.now() + datetime.timedelta(days= 30)).execute() == 0:
                return True

            else:
                return False
    
    except (IntegrityError,DoesNotExist):
        return False

    finally:
        libraryDB.close()



def removeRental(rentalid: str, bookid: str)->bool:
    """Removes a rental from the database and updates the Collection table.
       
       :param rentalid (str): The rental id for the record to be removed.
       :param bookid(str): The book id of the book being returned.
       :rtype (bool): If the operation was successful.
       :raises DoesNotExist: The record was not found.

    """

    try:
        libraryDB.connect(reuse_if_open=True)
        query = Collection.select(Collection._collectionID, Collection._amount).join(Book).where(Book._bookID == bookid.strip())
        if query:
            for result in query:
                updatedAmt = int(result._amount + 1)
                if Collection.update(_amount = updatedAmt).where(Collection._collectionID == result._collectionID).execute() == 1:
                    break

                else:
                    return False

            
            if Rental.delete().where(Rental._rentalID == rentalid.strip()).execute() == 1:
                return True

            else:
                return False
      
                
    except DoesNotExist:
        return False

    finally:
        libraryDB.close()
            
