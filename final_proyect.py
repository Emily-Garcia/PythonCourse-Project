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
            is_logged INT DEFAULT 0,
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
    email = input('Ingresa tu email: ')
    password = input('Ingresa una contraseña: ')

    try:
        sql = '''
            UPDATE user 
            SET
                is_logged = 1
            WHERE
                email = ?
            AND
                password = ?
        '''
        values = (email, password)
        cursor = conex.execute(sql, values)
        conex.commit()

        if cursor.rowcount < 1:
            #error
            print('- No se pudo iniciar sesion :(')
            user_while(conex)
        else:
            #success
            print('>>>Usuario ha iniciado sesion exitosamente!\n')
            menu_login(conex)
    except Exception as e:
        print('- Algo salio mal durante el inicio de sesion :(')
        print(e)
        print()

# funcion de menu ya que iniciaste sesion
def menu_login(conex):
    print('....................')
    print('Menu')
    print('1. Ver platillos')
    print('2. Crear platillo')
    print('3. Realizar pedido')
    print('4. Ver pedidos realizados')
    print('5. Ver perfil')
    print('6. Editar perfil')
    print('7. Cerrar sesión')
    print('....................')
    print()
    userlgin = int(input('Ingrese la opcion de lo que desea realizar: '))

# funcion para registrarse
def sign_in(conex):
    first_name = input('Ingresa tu nombre: ')
    last_name = input('Ingresa tu apellido: ')
    email = input('Ingresa tu email: ')
    phone = input('Ingresa numero de telefono: ')
    password = input('Ingresa una contraseña: ')
    print()

    sql = '''
        INSERT INTO
        user (first_name, last_name, email, phone, password)
        VALUES (?, ?, ?, ?, ?)
    '''
    values = (first_name, last_name, email, phone, password)
    
    conex.execute(sql, values)
    conex.commit()

    print('>>>>>Usuario creado correctamente!')
    user_while(conex)

# funcion para salir
def get_out(conex):
    pass

# funcion para saber si quiere seguir ocupando el programa
def user_while(conex):
    leave = input('¿Desea seguir utilizando la app? S/N: ')
    if leave != 'S' and leave != 'N':
            print('La opcion que ingresaste no es valida')
            leave = input('¿Deseas salir de la app? (S/N): ')
    else:
        principal_menu(conex)


def main():
    conex = create_or_get_database()
    create_table_user(conex)
    create_table_dish(conex)
    create_table_order(conex)
    principal_menu(conex)


main()

