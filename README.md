# INFSCI_2710_Project
*MySQL setup instructions
**create schema using the file app/ddl_statements.sql
**edit line 10 in config.py to have the name of your mySQL username, password and schema name (SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:5Qf*6*oD@localhost/SmartPharm')
**make sure the mysql server is running
*Application Run Instructions
**install python3.6 or higher
**install poetry (pip3 install poetry)
**from the base project folder: poetry shell
**inside the shell: flask run
