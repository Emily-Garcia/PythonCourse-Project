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

# metodo del menu principal
def principal_menu(conex):
    print("\n************************")
    print("MENU PRINCIPAL")
    print('1. Iniciar sesión')
    print('2. Registrarse')
    print('3. Salir del programa')
    print("************************\n")
    opcion = int(input('Ingrese la opcion de lo que desea realizar: '))
    if validate_user_selection(opcion):
        menu_princ_selection(opcion, conex)
    else:
        print("El valor que ingresaste no es válido")
        principal_menu(conex)
    
# funcion para saber si la opcion es valida
def validate_user_selection(opcion):
    return isinstance(opcion, int) and opcion >0 and opcion < 4

# funcion para llevar a cada opcion del menu principal
def menu_princ_selection(opcion, conex):
    if opcion == 1:
        log_in(conex)
    elif opcion == 2:
        sign_in(conex)
    else:
        get_out(conex)

# funcion para iniciar sesion
def log_in(conex):
    pass

# funcion para registrarse
def sign_in(conex):
    pass

# funcion para salir
def get_out(conex):
    pass

def main():
    conex = create_or_get_database()
    create_table_user(conex)
    create_table_dish(conex)
    create_table_order(conex)
    principal_menu(conex)


main()

