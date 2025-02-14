from pydantic_settings import BaseSettings 


class Settings(BaseSettings):
    database_port: int
    database_host:str
    database_name: str
    database_password: str
    database_username: str 
    secret_key: str 
    algorithm: str
    access_token_expire_minutes: int

class config:
    env_file = ".env"

settings = Settings()
print(settings.database_username)  