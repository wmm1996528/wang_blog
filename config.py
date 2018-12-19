from peewee import *
from pathlib import *
data_path = Path.joinpath(Path(__file__).parent, 'data/')

SqliteData = SqliteDatabase(str(Path.joinpath(data_path, 'blogs.db')))