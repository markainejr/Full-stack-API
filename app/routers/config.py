from pydantic_settings import BaseSettings 







class Settings(BaseSettings):
    path = int
    database_username: str = "postgres"
    secret_key: str = "234758dfg56789"

settings = Settings()
print(settings.database_username)  