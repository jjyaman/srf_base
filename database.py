from mysql.connector import connect

conx = connect(
    host = "monorail.proxy.rlwy.net",
    port = "26134",
    user = "root",
    password = "i0_fmiifnztx8kydltn9sy$vyyvv1zm4",
    db = "railway"
)

def select_sql():
    try:
        with conx as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM register")
            conn.commit
            data = cursor.fetchall()
            cursor.close()
        return data
    except Exception as e:
        return e
    

def insert_sql(a, b, c):

    try:
        with conx as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO register (id, vector, name) VALUES ('{a}', '{b}', '{c}')")
            conn.commit
            cursor.close()
        print("Insercción en la BD")
    except Exception as e:
        return e
    
#print(insert_sql(2, [1,2,3,4,5], 'jjyg'))

# data = [ i for i in ['juan', [1,2,3,4,5,6], '18']]