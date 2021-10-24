from decouple import config

DB_HOST = config("DB_HOST", default="", cast=str)
DB_PORT = config("DB_PORT", default="", cast=str)
DB_USER = config("DB_USER", default="", cast=str)
DB_PASS = config("DB_PASS", default="", cast=str)
