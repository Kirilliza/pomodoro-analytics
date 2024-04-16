from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    GOOGLE_TOKEN_ID:str = 'sfbyuabbaoub274ybjhabs82'
    sqlite_db_name:str = 'pomodoro.sqlite'
