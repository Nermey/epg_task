from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    DATABASE_PORT = os.getenv("DATABASE_PORT")
    DATABASE_HOST = os.getenv("DATABASE_HOST")
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/database"


settings = Settings()

