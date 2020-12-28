import sqlite3

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

def compare(psswrd):
    create_table()
    pin = '0810'
    if pin == psswrd:
        return True
    else:
        return False

def create_table():
    c.execute(f"""CREATE TABLE IF NOT EXISTS accounts (
        platform TEXT,
        email TEXT,
        password TEXT)""")

def registerAccount(platform, email, psswrd):
    c.execute(f"""INSERT INTO accounts (platform, email, password) VALUES ('{str(platform)}', '{str(email)}', '{str(psswrd)}')""")
    conn.commit()
    return True

def removeAccount(platform, email, psswrd):
    c.execute(f"""DELETE FROM accounts WHERE platform='{str(platform)}' AND email='{str(email)}' AND password='{str(psswrd)}'""")
    conn.commit()
    return True

def consultAccounts(whereToSearch, whatToSearchFor):
    rows = c.execute(f"""SELECT * FROM accounts WHERE {whereToSearch}='{whatToSearchFor}'""").fetchall()
    return rows