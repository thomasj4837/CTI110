import sqlite3

# Connect to SQLite database file (creates file if it doesn't exist)
conn = sqlite3.connect("signup_hw.db")
cursor = conn.cursor()

# Drop table so script can be re-run cleanly in class
cursor.execute("DROP TABLE IF EXISTS users")

# STUDENT CODE GOES IN THIS SECTION ONLY!!!
#--------------------------------------------------------------------------------------
# STEP 1: Create users table
# TO DO: Create a table called users with fields
# user_id, first_name, last_name, email, username, password_hash, signup_date, country, age
# I have started the table for you with the primary key 'user_id'
# NOTE: SQLite assigns user_id for you. You do not insert a value for it.
# NOTE: Do not put a comma after the LAST column in the table. A trailing comma is a syntax error.
cursor.execute("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    username TEXT,
    password_hash TEXT,
    signup_date DATE,
    country TEXT,
    age INTEGER
)""")

# STEP 2: Insert sample fake users
# TO DO: Create a list called users that will store all 10 of your fake users information.
# I have started it for you
# Each user has 8 values, in this order (user_id is NOT included):
# first_name, last_name, email, username, password_hash, signup_date, country, age

users = [('Naruto', 'Uzamaki', 'ramen@example.com', 'naruto_u', 'LoveRamen1', '2026-06-01', 'JAPAN', 16),
         ('Sakura', 'Haruno', 'sakura@example.com', 'sakura_h', 'CherryBlossom2', '2026-06-03', 'JAPAN', 17),
         ('Sasuke', 'Uchiha', 'sasuke@example.com', 'sasuke_u', 'Sharingan3', '2026-06-05', 'JAPAN', 17),
         ('Kakashi', 'Hatake', 'kakashi@example.com', 'kakashi_h', 'HiddenLeaf4', '2026-06-08', 'JAPAN', 29),
         ('Hinata', 'Hyuga', 'hinata@example.com', 'hinata_h', 'Byakugan5', '2026-06-10', 'JAPAN', 16),
         ('Goku', 'Son', 'goku@example.com', 'goku_s', 'SaiyanPower6', '2026-06-12', 'USA', 35),
         ('Vegeta', 'Prince', 'vegeta@example.com', 'vegeta_p', 'PrinceOfSaiyans7', '2026-06-15', 'USA', 38),
         ('Ash', 'Ketchum', 'ash@example.com', 'ash_k', 'Pikachu8', '2026-06-18', 'USA', 14),
         ('Misty', 'Waterflower', 'misty@example.com', 'misty_w', 'Cerulean9', '2026-06-20', 'USA', 15),
         ('Bulbasaur', 'Kanto', 'bulbasaur@example.com', 'bulbasaur_k', 'VineWhip10', '2026-06-22', 'USA', 10)]



#------------------------------------------------------------------------------------
# DO NOT CODE PASS HERE!!!
# STEP 3: Run the python script! Once your done creating your table and adding in the user information
# You should run the program and it will create your database called signup_hw.db.
# You can then view it in your terminal and you can upload the .db file to a database viewer thats provided on Canvas.

cursor.executemany("""
INSERT INTO users (
    first_name, last_name, email, username, password_hash,
    signup_date, country, age
) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", users)

conn.commit()
conn.close()

print("✅ signup_hw.db created with users table and sample data.")

print()

conn = sqlite3.connect("signup_hw.db")
cur = conn.cursor()
for row in cur.execute("SELECT * FROM users LIMIT 10"):
    print(row)
conn.close()