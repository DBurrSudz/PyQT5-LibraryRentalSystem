# Library Rental System
This project emulates a miniature library rental system. This system allows a user to use it as a regular 'User' or an 'Admin'.
After validation, the User is taken to the dashboard where they can perform tasks such as making rentals and returning books. The Admin is taken to their screen where they are able to add books and collections to the database.


## Graphical User Interface
Built with the PyQT module and QT Designer. **DO NOT edit the .py files in the src/GUI/Views folder**.

## Database
This project uses the [**peewee**](http://docs.peewee-orm.com/en/latest/) Object Relational Mapping module to connect to a local database to create models and execute SQL commands.

## Running the Project
To run this project, run `python main.py` from the command line. You can change the database connection in `database.py` to connect to a preferred database provided in the [**peewee**](http://docs.peewee-orm.com/en/latest/) documentation. Set database credentials in local environment variables.
