import sqlite3          # Has functions we need in order to interact with the sqlite.db file in php
import function

db_connection = sqlite3.connect("sqlite.db")    # Function will return a connection, but does not allow us to run queries yet
print(db_connection)

db_cursor = db_connection.cursor()              # Run cursor method on connection object, return cursor object
print(db_cursor)
                        # Cursor allows us to run queries and is also where we are able to read the result of those queries.
query1 = "SELECT * FROM demo"
db_cursor.execute(query1)                       # Execute method accepts a query as an argument

print("Reading one row")
row1 = db_cursor.fetchone()
print(row1)

print("Reading a specified number of rows")             # Returns a list of rows
#row3 = db_cursor.fetchmany(3)
#print(row2)
#for r in row2:
#    print(r)
function.query_responder(db_cursor, "fetchmany", 3)


print("Reading all (remaining) rows from demo table")   # If you read one row first then this only returns the remaining rows
                                                        # since cursor has already read line 1 and is currently at row 2
                                                        # The Cursors reads from where ever it is an until the end
#rows = db_cursor.fetchall()
#print(rows)
#for r in rows:
#    print(r)

function.query_responder(db_cursor, "fetchall") # Shortcut that exists in the functions file for what we did above


query2 = "INSERT INTO demo (Name, Hint) VALUES ('Penny', 'Ahlstrom')"
db_cursor.execute(query2)                               # Starts a transaction, changes needs to be rolled back or committed,
                                                        # Changes not committed are rolled back by default
db_connection.commit()

id = int(input("Enter an id: "))
query3 = "SELECT * FROM demo WHERE ID > ?" # WHERE ID > {id} would put us at risk for "sql injection" attack. DON'T.
# db_cursor.execute(query3, (id))
# function.query_responder(db_cursor, "fetchall")

#db_cursor.close()
#db_connection.close()


