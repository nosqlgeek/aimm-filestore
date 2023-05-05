import os


CONFIG = {
    "data_folder": os.getenv("FS_DATA_FOLDER"),
    "access_key" : os.getenv("FS_ACCESS_KEY"),
    "access_secret": os.getenv("FS_ACCESS_SECRET")
}