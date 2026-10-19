import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
with conn:
    c.execute("""CREATE TABLE List (
    purpose TEXT NOT NULL,
    price INTEGER,
    id INTEGER PRIMARY KEY,
    date TEXT  
    )    
    """)
class EXP():
    def __init__(self,purpose,price,date):
        self.purpose = purpose
        self.price = price
        self.date = date
    def __str__(self):
        return f"Price: {self.price} purpose: {self.purpose} date: {self.date}"

exp1 = EXP("food",150,'13-02-2026')
exp2 = EXP("travel",500,'23-02-2026')
exp3 = EXP("entertainment",200,'23-02-2026')
with conn:
    c.execute("INSERT INTO List (purpose,price,date) VALUES (?,?,?)",(exp1.purpose,exp1.price,exp1.date))
    c.execute("INSERT INTO List (purpose,price,date) VALUES (?,?,?)",(exp2.purpose,exp2.price,exp2.date))
    c.execute("INSERT INTO List (purpose,price,date) VALUES (?,?,?)",(exp3.purpose,exp3.price,exp3.date))

def add(exp):
    with conn:
            c.execute("INSERT INTO List(purpose,price,date) VALUES(?,?,?)",(exp.purpose,exp.price,exp.date))

def view():
    with conn:
        c.execute("SELECT * FROM List")
        return c.fetchall()
def total():
    with conn:
        c.execute("SELECT SUM(price) FROM List")
        return c.fetchone()
def delete(exp):
    with conn:
        c.execute("DELETE FROM List WHERE purpose = ?",(exp.purpose,))
def search(exp):
    with conn:
        c.execute("SELECT purpose,price FROM List WHERE purpose = ?",(exp.purpose,))
    return c.fetchone()

def mon_exp(mon,year):
    with conn:
        c.execute("SELECT SUM(price) FROM List WHERE date LIKE ?",("__-"+mon+"-"+year,))
    return c.fetchone()
def mon_sum(mon,year):
    with conn:
        c.execute("SELECT purpose,price,date FROM List WHERE date LIKE ?",("__-"+mon+"-"+year,))
        return c.fetchall()



exp4 = EXP("Book",200,"15-04-2026")
add(exp4)
# delete(exp1)
print(view())
# print(search(exp1))
# print(search(exp2))
mon = mon_exp('01','2026')
if mon[0]:
    print(mon)
else:
    print("You didn't purchase anything")

# for purpose,price,date in mon_sum('02','2026'):
#     print(f"Purpose: {purpose} Price: {price} Date: {date}")
