import psycopg2


def connect(psql_cfg: dict):
    """ Connect to the PostgreSQL database server """
    # TODO use logger instead of print
    try:
        # read connection parameters
        params = {k: v for k, v in psql_cfg}

        # connect to the PostgreSQL server
        print(f'Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        print(f'Successfully connected to {conn.dsn}')

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        return conn, cur
    except (Exception, psycopg2.DatabaseError) as error:
        # TODO proper error handling
        print(error)
