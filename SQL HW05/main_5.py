import psycopg2

def create_db(conn):
    print('create tables:')
    with conn.cursor() as cur:
        try:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS clients(id SERIAL PRIMARY KEY, name VARCHAR(500), surname VARCHAR(500), email VARCHAR(100) UNIQUE);"
                "CREATE TABLE IF NOT EXISTS phones(id SERIAL PRIMARY KEY, client_id INT REFERENCES clients(id), phone VARCHAR(50) UNIQUE);")
            conn.commit()
            print('OK')
        except Exception as e:
            conn.rollback()
            print(e)

def add_client(conn, first_name, last_name, email, phones=None):
    print('add client:')
    with conn.cursor() as cur:
        try:
            cur.execute(
                "INSERT INTO clients (name, surname, email) VALUES (%s, %s, %s) RETURNING id;", (first_name,last_name,email))
            client_id = cur.fetchone()[0]
            print(f'add client is OK: id = {client_id}')

            if not (phones is None):
                print('add phones:')
                for phone in phones:
                    add_phone(conn, client_id, phone)
        except Exception as e:
            conn.rollback()
            print(e)

def add_phone(conn, client_id, phone):
    print(f'add phone of client {client_id}:')
    with conn.cursor() as cur:
        try:
            cur.execute(
                "INSERT INTO phones (client_id, phone) VALUES (%s, %s);", (client_id, phone))
            conn.commit()
            print('add phone is OK')
        except Exception as e:
            conn.rollback()
            print(e)

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    print(f'add phone of client {client_id}:')
    if first_name or last_name or email:
        with conn.cursor() as cur:
            try:
                cur.execute('UPDATE clients SET name = COALESCE(%s, name),surname = COALESCE(%s, surname), email = COALESCE(%s, email) WHERE id=%s;', (first_name, last_name, email, client_id))
                conn.commit()
                print('change client is OK')
            except Exception as e:
                conn.rollback()
                print(e)

    if not (phones is None):
        print('update phone list: delete all phones first')
        delete_all_phones(conn, client_id)

        print('update phone list: add phone')
        for phone in phones:
            add_phone(conn, client_id, phone)

def delete_all_phones(conn, client_id):
    print(f'delete all phones of client {client_id}:')
    with conn.cursor() as cur:
        try:
           cur.execute('DELETE FROM phones WHERE client_id=%s;', (client_id, ))
           conn.commit()
           print('delete phones is OK')
        except Exception as e:
           conn.rollback()
           print(e)

def delete_phone(conn, client_id, phone):
    print(f'delete phone {phone} of client {client_id}:')
    with conn.cursor() as cur:
        try:
            cur.execute('DELETE FROM phones WHERE client_id=%s AND phone = %s;', (client_id,phone))
            conn.commit()
            print('delete phone is OK')
        except Exception as e:
            conn.rollback()
            print(e)


def delete_client(conn, client_id):
    print(f'delete all phones of client {client_id}:')
    delete_all_phones(conn, client_id)
    print(f'delete client {client_id}:')
    with conn.cursor() as cur:
        try:
           cur.execute('DELETE FROM clients WHERE clients.id=%s;', (client_id, ))
           conn.commit()
           print('delete client is OK')
        except Exception as e:
           conn.rollback()
           print(e)

def get_client_id(conn, email):
    print(f'get client id by email: {email}')
    with conn.cursor() as cur:
        try:
            cur.execute("SELECT clients.id from clients where clients.email = %s;", (email, ))
            result = cur.fetchone()
            if result:
                return result
            else:
                return None
        except Exception as e:
            conn.rollback()
            print(e)

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    print(f'find client: {first_name} {last_name} {email} {phone}')
    clients_id = []
    with conn.cursor() as cur:
        try:
            query = "SELECT DISTINCT clients.id, clients.name, clients.email from clients LEFT JOIN phones ON phones.client_id = clients.id where 1=1 "
            params = []
            if first_name:
                query += " AND clients.name = %s"
                params.append(first_name)
            if last_name:
                query += " AND clients.surname = %s"
                params.append(last_name)
            if email:
                query += " AND clients.email = %s"
                params.append(email)
            if phone:
                query += " AND phones.phone = %s"
                params.append(phone)
            query +=';'

            cur.execute(query, tuple(params))

            clients_id = cur.fetchall()
        except Exception as e:
            conn.rollback()
            print(e)

    return clients_id


with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
    print('Database is connected')
    create_db(conn)

    add_client(conn, "name1", "surname1", "email1")
    add_client(conn, "name2", "surname2", "email2")
    add_client(conn, "name3", "surname3", "email3")

    phones = []
    phones.append("phone41")
    phones.append("phone42")
    add_client(conn, "name4", "surname4", "email4", phones)

    add_client(conn, "name4", "surname42", "email42")


    result = find_client(conn,'name4')
    for line in result:
        print(f'{line[0]}: {line[1]}    {line[2]}')

    phones.clear()
    phones.append("phone43")
    phones.append("phone44")
    phones.append("phone45")
    phones.append("phone46")
    client_id = get_client_id(conn, 'email4')
    change_client(conn, client_id, first_name="name4_", phones = phones)

    result = find_client(conn,'name4_')
    for line in result:
        print(f'{line[0]}: {line[1]}    {line[2]}')

    client_id = get_client_id(conn, 'email4')
    delete_phone(conn, client_id, 'phone46')

    client_id = get_client_id(conn, 'email4')
    delete_client(conn, client_id)
conn.close()