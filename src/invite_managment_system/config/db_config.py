from sqlmodel import SQLModel, create_engine , Session
from .env_config import DATABASE_URL

connection_string = str(DATABASE_URL).replace("postgresql" , "postgresql+psycopg2")

engine = create_engine(DATABASE_URL, echo=True)


def connect_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session