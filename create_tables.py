from sqlalchemy import create_engine
from models import Base
import config

# Create the database engine
engine = create_engine(f"mysql+mysqlconnector://{config.DATABASE_CONFIG['user']}:{config.DATABASE_CONFIG['password']}@{config.DATABASE_CONFIG['host']}/{config.DATABASE_CONFIG['database']}")

# Create all tables
Base.metadata.create_all(engine)

print("Tables created successfully!")

