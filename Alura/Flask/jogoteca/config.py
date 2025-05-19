import os


SECRET_KEY = 'python'

SQLALCHEMY_DATABASE_URI = \
            f'{'mysql+mysqlconnector'}://{'root'}:{'998674629Th.'}@{'127.0.0.1'}/{'jogoteca'}'

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads' 