from modules.resident import Patient, RH
from modules.administration import Archive
from database import get_db_config, db_connect, db_close

# CONSTANTS
VERBOSE = True
CONFIG_FILE_PATH = 'config.json'
CONFIG = get_db_config(CONFIG_FILE_PATH)


if __name__ == "__main__":

    # Database connection
    bdd = db_connect(CONFIG, VERBOSE)

    if bdd.is_connected():
        print('DB is connected')



    # Close BDD
    db_close(bdd, VERBOSE)