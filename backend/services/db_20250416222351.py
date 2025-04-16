from clickhouse_connect import get_client

def get_clickhouse_client():
    client = get_client(
        host='localhost',
        port=8123,
        username='default',
        password='',
        database='default',
        secure=False
    )
    return client
