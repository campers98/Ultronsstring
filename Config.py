import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 24853835))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', "bdd57a7f24d7d1f59b82f937289e4abb")
    BOT_TOKEN = os.environ.get('BOT_TOKEN', "6998449442:AAGIrcg6vJyp0e-bJES3VtErA38Wlyr2hlM")
    DATABASE_URL = os.environ.get('DATABASE_URL', "mongodb+srv://Singlecell94:Single_1122334455@cluster234.n2vmnn3.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_URL = DATABASE_URL.replace("MONGO_DB_URL", "mongodb")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', "https://t.me/SVD_Squad_Gamerz")
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 0
    API_HASH = ""
    BOT_TOKEN = ""
    DATABASE_URL = ""
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = ""
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
