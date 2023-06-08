import sqlalchemy as sa

engine = sa.create_engine("postgresql+psycopg2://postgres:admin@localhost/Telebot")

connection = engine.connect()

metadata = sa.MetaData()

users = sa.Table('Users', metadata,
                 sa.Column('user_id', sa.Integer, primary_key=True),
                 sa.Column('name', sa.Text),
                 sa.Column('birthdate', sa.Text)
                 )

metadata.create_all(engine)

insertion_query = users.insert().values([
    {'name': 'Timur', 'birthdate': '13.10.1999'},
    {'name': 'Anvar', 'birthdate': '12.10.1999'},
    {'name': 'Arthur', 'birthdate': '11.10.1999'}
])

select_all_query = sa.select([users])
select_all_result = connection.execute(select_all_query)
print(select_all_result.fetchall())
