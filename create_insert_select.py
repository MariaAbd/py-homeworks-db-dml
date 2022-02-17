import sqlalchemy
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, MetaData, Table, Sequence, select, func

engine = sqlalchemy.create_engine('postgresql://postgres:Artem_Arya0315SQL@localhost:5432/py_48')
connection = engine.connect()
meta = MetaData()

# Создаем таблицы

musician = Table(
    'musician', meta,
    Column('id', Sequence('user_id_seq'), primary_key=True),
    Column('name', String(60), nullable=False)
)

genre = Table(
    'genre', meta,
    Column('id', Sequence('user_id_seq'), primary_key=True),
    Column('name', String(60), nullable=False)
)

genremusician = Table(
    'genremusician', meta,
    Column('id_genre', Integer, ForeignKey('genre.id'), nullable=False),
    Column('id_musician', Integer, ForeignKey('musician.id'), nullable=False)
)

album = Table(
    'album', meta,
    Column('id', Sequence('user_id_seq'), primary_key=True),
    Column('name', String(60), nullable=False),
    Column('release_year', Integer, nullable=False)
)

albummusician = Table(
    'albummusician', meta,
    Column('id_musician', Integer, ForeignKey('musician.id'), nullable=False),
    Column('id_album', Integer, ForeignKey('album.id'), nullable=False)
)

treck = Table(
    'treck', meta,
    Column('id', Sequence('user_id_seq'), primary_key=True),
    Column('name', String(60), nullable=False),
    Column('id_album', Integer, ForeignKey('album.id'), nullable=False),
    Column('duration', Numeric(3, 2), nullable=False)
)

collection = Table(
    'collection', meta,
    Column('id', Sequence('user_id_seq'), primary_key=True),
    Column('name', String(60), nullable=False),
    Column('id_treck', Integer, nullable=False),
    Column('release_year', Integer, nullable=False)
)


treckcollection = Table(
    'treckcollection', meta,
    Column('id_collection', Integer, ForeignKey('collection.id'), nullable=False),
    Column('id_treck', Integer, ForeignKey('treck.id'), nullable=False)
)

# Заполняем их

# connection.execute(musician.insert(), [
#     {'id': 1, 'name': 'Muse'},
#     {'id': 2, 'name': 'Wardruna'},
#     {'id': 3, 'name': 'Bring me the horizon'},
#     {'id': 4, 'name': 'Nothing but thieves'},
#     {'id': 5, 'name': 'Oomph!'},
#     {'id': 6, 'name': 'BB Brunes'},
#     {'id': 7, 'name': 'Calogero'},
#     {'id': 8, 'name': 'Hurts'}
# ])

# connection.execute(genre.insert(),[
#     {'id': 1, 'name': 'classic rock'},
#     {'id': 2, 'name': 'punk rock'},
#     {'id': 3, 'name': 'synth-pop'},
#     {'id': 4, 'name': 'alternative rock'},
#     {'id': 5, 'name': 'indie rock!'}
# ])


# connection.execute(genremusician.insert(), [
#     {'id_musician': 1, 'id_genre': 4},
#     {'id_musician': 1, 'id_genre': 2},
#     {'id_musician': 2, 'id_genre': 1},
#     {'id_musician': 3, 'id_genre': 2},
#     {'id_musician': 4, 'id_genre': 5},
#     {'id_musician': 5, 'id_genre': 1},
#     {'id_musician': 5, 'id_genre': 4},
#     {'id_musician': 6, 'id_genre': 5},
#     {'id_musician': 7, 'id_genre': 2},
#     {'id_musician': 8, 'id_genre': 1}
# ])

# connection.execute(album.insert(), [
#     {'id': 1, 'name': 'Showbiz', 'release_year': 1999},
#     {'id': 2, 'name': 'Absolution', 'release_year': 2003},
#     {'id': 3, 'name': 'Ritual', 'release_year': 2019},
#     {'id': 4, 'name': 'Defekt ', 'release_year': 1995},
#     {'id': 5, 'name': "That's the Spirit", 'release_year': 2015},
#     {'id': 6, 'name': 'Kvitravn', 'release_year': 2021},
#     {'id': 7, 'name': 'Desire ', 'release_year': 2017},
#     {'id': 8, 'name': 'Moral Panic', 'release_year': 2020},
#     {'id': 9, 'name': 'Visage', 'release_year': 2019}
# ])

# connection.execute(albummusician.insert(), [
#     {'id_musician': 1, 'id_album': 1},
#     {'id_musician': 1, 'id_album': 2},
#     {'id_musician': 5, 'id_album': 3},
#     {'id_musician': 5, 'id_album': 4},
#     {'id_musician': 3, 'id_album': 5},
#     {'id_musician': 2, 'id_album': 6},
#     {'id_musician': 8, 'id_album': 7},
#     {'id_musician': 4, 'id_album': 8},
#     {'id_musician': 6, 'id_album': 9}
# ])

# connection.execute(treck.insert(), [
#     {'id': 1, 'name': 'Habibi', 'id_album': 9, 'duration': 2.37},
#     {'id': 2, 'name': 'Jungle', 'id_album': 9, 'duration': 2.31},
#     {'id': 3, 'name': 'Ice-Coffin', 'id_album': 4, 'duration': 4.55},
#     {'id': 4, 'name': 'Europa', 'id_album': 4, 'duration': 4.25},
#     {'id': 5, 'name': 'Unperson', 'id_album': 8, 'duration': 3.24},
#     {'id': 6, 'name': 'Impossible', 'id_album': 8, 'duration': 4.01},
#     {'id': 7, 'name': 'Endlessly', 'id_album': 2, 'duration': 3.49},
#     {'id': 8, 'name': 'Unintended ', 'id_album': 1, 'duration': 3.57},
#     {'id': 9, 'name': 'Falling Down', 'id_album': 1, 'duration': 4.33},
#     {'id': 10, 'name': 'Beautiful Ones', 'id_album': 7, 'duration': 3.01},
#     {'id': 11, 'name': 'Hold on to Me', 'id_album': 7, 'duration': 3.02},
#     {'id': 12, 'name': 'Boyfriend', 'id_album': 7, 'duration': 2.49},
#     {'id': 13, 'name': 'Synkverv', 'id_album': 6, 'duration': 4.52},
#     {'id': 14, 'name': 'Grá', 'id_album': 6, 'duration': 3.33},
#     {'id': 15, 'name': 'Follow You', 'id_album': 5, 'duration': 3.54}
# ])

# connection.execute(collection.insert(), [
#     {'id': 1, 'name': 'REBEL ROCK BOX NOVEMBER SONGS', 'id_treck': 1, 'release_year': 2021},
#     {'id': 2, 'name': 'REBEL ROCK BOX OCTOBER SONGS', 'id_treck': 5, 'release_year': 2021},
#     {'id': 3, 'name': 'REBEL ROCK BOX MAY SONGS', 'id_treck': 6, 'release_year': 2021},
#     {'id': 4, 'name': 'COUNTRY HEAT', 'id_treck': 5, 'release_year': 2021},
#     {'id': 5, 'name': "ROCK 'N' ROLL REMASTERS", 'id_treck': 1, 'release_year': 2020},
#     {'id': 6, 'name': 'ROCK HALLOWEEN', 'id_treck': 9, 'release_year': 2019},
#     {'id': 7, 'name': 'NEW ROCK 4', 'id_treck': 11, 'release_year': 2017},
#     {'id': 8, 'name': 'ROCK DRIVE', 'id_treck': 15, 'release_year': 2013}
# ])

# connection.execute(treckcollection.insert(), [
#     {'id_collection': 1, 'id_treck': 12},
#     {'id_collection': 2, 'id_treck': 4},
#     {'id_collection': 3, 'id_treck': 3},
#     {'id_collection': 4, 'id_treck': 4},
#     {'id_collection': 5, 'id_treck': 7},
#     {'id_collection': 6, 'id_treck': 6},
#     {'id_collection': 3, 'id_treck': 7},
#     {'id_collection': 6, 'id_treck': 14},
#     {'id_collection': 8, 'id_treck': 9}
# ])

connection.execute(album.update().where(album.c.id == 7).values(release_year=2018))
connection.execute((treck.update().where(treck.c.id == 1).values(name='My habibi')))

# select-запросы

s_1 = select([album.c.name, album.c.release_year]).where(album.c.release_year == 2018)
s_2 = select([func.max(treck.c.duration)])
s_3 = select([treck.c.name]).where(treck.c.duration >= 3.5)
s_4 = select([collection.c.name]).\
    where(collection.c.release_year.between(2018, 2020))
s_5 = select([musician.c.name]).where(musician.c.name.notlike("% %"))
s_6 = select([treck.c.name]).where(treck.c.name.ilike('%my%' or '%мой%'))
# print(connection.execute(s_1).fetchall())
# print(connection.execute(s_2).fetchall())
# print(connection.execute(s_3).fetchall())
# print(connection.execute(s_4).fetchall())
# print(connection.execute(s_5).fetchall())
# print(connection.execute(s_6).fetchall())
