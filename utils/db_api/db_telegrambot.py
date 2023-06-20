import sqlalchemy as db

engine = db.create_engine("postgresql+psycopg2://postgres:admin@localhost/Telebot")

connection = engine.connect()

metadata = db.MetaData()

users = db.Table('Users', metadata,
                 db.Column('user_id', db.Integer, primary_key=True),
                 db.Column('name', db.Text),
                 db.Column('birthdate', db.Text),
                 db.Column('phone_number', db.Text),
                 db.Column('text', db.Text),
                 db.Column('telegram_id', db.Integer)
                 )

metadata.create_all(engine)

insertion_query = users.insert().values([
    {'telegram_id': '1231234512', 'name': 'Timur', 'birthdate': '13.10.1999', 'text': " grgsdbgsdgsgsegser"},
    {'telegram_id': '213412', 'name': 'Timur', 'birthdate': '13.10.1999', 'text': " grgsgweghswehgswdbgsdgsgsegser"},
    {'telegram_id': '5236236', 'name': 'Timur', 'birthdate': '13.10.1999', 'text': " fwefwefwe"},
])
connection.execute(insertion_query)
select_all_query = db.select([users])
select_all_result = connection.execute(select_all_query)
print(select_all_result.fetchall())
