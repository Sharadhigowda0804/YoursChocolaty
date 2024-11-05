import sqlite3

def connect_db():
    conn = sqlite3.connect('YoursChocolaty.db')
    conn.row_factory = sqlite3.Row  
    return conn

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Create table for seasonal flavors
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS flavors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        seasonal BOOLEAN NOT NULL,
        description TEXT
    )
    ''')

    # Create table for ingredients
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
    ''')

    # Create table for customer suggestions
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS suggestions (
        id INTEGER PRIMARY KEY,
        flavor_id INTEGER,
        customer_name TEXT NOT NULL,
        allergies TEXT,
        FOREIGN KEY (flavor_id) REFERENCES flavors (id)
    )
    ''')
    
    conn.commit()
    conn.close()

create_tables()
