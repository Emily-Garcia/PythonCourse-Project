import sqlite3

# creando base de datos
def create_or_get_database():
    conex = sqlite3.connect('restaurante.db')
    print("--- BASE DE DATOS CONECTADO CORRECTAMENTE ---")
    return conex

# metodo para crear tabla del usuario
def create_table_user(conex):
    sql = '''
        CREATE TABLE IF NOT EXISTS user (
            first_name VARCHAR NOT NULL,
            last_name VARCHAR NOT NULL,
            email TEXT NOT NULL,
            phone INT NOT NULL,
            password TEXT NOT NULL,
            is_logged INT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    '''
    conex.execute(sql)
    print("- tabla USER creada correctamente -")

# metodo para crear tabla del platillo
def create_table_dish(conex):
    sql = '''
        CREATE TABLE IF NOT EXISTS dish (
            name VARCHAR NOT NULL,
            description TEXT NOT NULL,
            price DOUBLE NOT NULL,
            ingredients TEXT NOT NULL,
            preparation_time INT NOT NULL,
            is_available INT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    '''
    conex.execute(sql)
    print("- tabla DISH creada correctamente -")

# metodo para crear tabla de la orden
def create_table_order(conex):
    # Usamos llave foranea
    sql = '''
        CREATE TABLE IF NOT EXISTS ordeer (
            notes TEXT NOT NULL,
            preparation_time INT NOT NULL,
            total DOUBLE NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES user(rowid)
        )
    '''
    conex.execute(sql)
    print("- tabla ORDER creada correctamente -")

def main():
    conex = create_or_get_database()
    create_table_user(conex)
    create_table_dish(conex)
    create_table_order(conex)


main()

