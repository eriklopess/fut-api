from sqlalchemy import create_engine
import os

conn = os.getenv('POSTGRES_PRISMA_URL')

def get_connection():
    engine = create_engine(conn)
    connection = engine.connect()
    return connection