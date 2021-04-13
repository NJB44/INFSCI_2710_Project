# INFSCI_2710_Project
* MySQL setup instructions

  * create schema using the files sqlDDL/ddl_statements.sql and sqlDDL/user_table_insert.sql

  * edit line 10 in config.py to have the name of your mySQL username, password and schema name (SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:5Qf*6*oD@localhost/SmartPharm')

  * make sure the mysql server is running

* Application Run Instructions

  * install python3.6 or higher

  * install poetry (follow instructions here and add to path: https://python-poetry.org/docs/ )

  * from the base project folder: poetry install 

  * from the base project folder: poetry shell 

  * inside the shell: flask run 

  * open the link created in a browser (set to http://127.0.0.1:5000/)

* Application Summary
 * The application models an end-to-end management for the delivery process of medication from pharmaceutical plant to patient. There are five implemented user types: admin, patient, doctor, pharmacy, and pharmaceutical plant. Admins can edit and remove any user account. Patients can create appointments with their doctors and check their appointments. Doctors can check appointments on their schedule and write prescriptions for medicine tied to a specific pharmacy. Pharmacies can browse their inventory, order from a production plant, check previous shipments, and see summary statistics about the store status. Production plants can browse their inventory, add new stock, confirm orders from pharmacies, and see previous shipments. A new account can be created freely for any user type from the home page  

* Database ER Diagram
![image](https://user-images.githubusercontent.com/46729414/114600661-95ddc800-9c62-11eb-936e-c0877472abd6.png)

* Database Relational Schema
![image](https://user-images.githubusercontent.com/46729414/114600880-da696380-9c62-11eb-91a2-af047c3cd808.png)
