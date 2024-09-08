import sqlite3

## Connecting sqlite
connection = sqlite3.connect("student.db")

## Creating cursor
cursor = connection.cursor()

# Creating table
table_info = """
Create table if not exists STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

# Insert records
students = [
    ('John Doe', '10th', 'A', 85),
    ('Jane Smith', '10th', 'B', 92),
    ('Alice Johnson', '9th', 'A', 78),
    ('Bob Brown', '9th', 'B', 88),
    ('Charlie Davis', '10th', 'A', 90),
    ('Diana White', '9th', 'C', 95),
    ('Ethan Green', '10th', 'B', 83)
]

cursor.executemany('INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?)', students)

# Commit the changes
connection.commit()

# Fetch and display the data
cursor.execute('SELECT * FROM STUDENT')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection

# cursor.execute('DELETE FROM STUDENT')
# # Commit the changes
# connection.commit()
connection.close()

