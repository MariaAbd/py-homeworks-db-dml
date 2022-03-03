import sqlalchemy as sq
from sqlalchemy import MetaData, Table, func, Column, String, Integer, ForeignKey, Numeric, select, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

engine = sq.create_engine('postgresql://postgres:Artem_Arya0315SQL@localhost:5432/py_48')
Session = sessionmaker(bind=engine)
session = Session()
meta = MetaData(bind=engine)

# Создаем таблицы и классы

genremusician = sq.Table(
    'genremusician', Base.metadata,
    sq.Column('id_genre', sq.Integer, sq.ForeignKey('genre.id'), nullable=False),
    sq.Column('id_musician', sq.Integer, sq.ForeignKey('musician.id'), nullable=False)
)


albummusician = sq.Table(
    'albummusician', Base.metadata,
    sq.Column('id_musician', sq.Integer, sq.ForeignKey('musician.id'), nullable=False),
    sq.Column('id_album', sq.Integer, sq.ForeignKey('album.id'), nullable=False)
)

trackcollection = sq.Table(
    'trackcollection', Base.metadata,
    sq.Column('id_collection', sq.Integer, sq.ForeignKey('collection.id'), nullable=False),
    sq.Column('id_track', sq.Integer, sq.ForeignKey('track.id'), nullable=False)
)

class Musician(Base):
    __tablename__ = 'musician'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(60), nullable=False)
    albums = relationship('Album', secondary=albummusician, back_populates='musicians', cascade='all,delete')
    genres = relationship('Genre', secondary=genremusician, back_populates='musicians', cascade='all,delete')


class Genre(Base):
    __tablename__ = 'genre'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(60), nullable=False)
    musicians = relationship(Musician, secondary=genremusician, back_populates='genres', cascade='all,delete')


class Album(Base):
    __tablename__ = 'album'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(60), nullable=False)
    release_year = sq.Column(sq.Integer, nullable=False)
    musicians = relationship(Musician, secondary=albummusician, back_populates='albums', cascade='all,delete')


class Track(Base):
    __tablename__ = 'track'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(60), nullable=False)
    id_album = sq.Column(sq.Integer, sq.ForeignKey('album.id'), nullable=False)
    duration = sq.Column(sq.Numeric(3, 2), nullable=False)
    collections = relationship('Collection', secondary='trackcollection', back_populates='tracks', cascade='all,delete')


class Collection(Base):
    __tablename__ = 'collection'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(60), nullable=False)
    id_track = sq.Column(sq.Integer, nullable=False)
    release_year = sq.Column(sq.Integer, nullable=False)
    tracks = relationship(Track, secondary='trackcollection', back_populates='collections', cascade='all,delete')


Base.metadata.create_all(engine)


# Наполнение таблиц (из предыдущего дз)

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

# connection.execute(track.insert(), [
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
#     {'id': 1, 'name': 'REBEL ROCK BOX NOVEMBER SONGS', 'id_track': 1, 'release_year': 2021},
#     {'id': 2, 'name': 'REBEL ROCK BOX OCTOBER SONGS', 'id_track': 5, 'release_year': 2021},
#     {'id': 3, 'name': 'REBEL ROCK BOX MAY SONGS', 'id_track': 6, 'release_year': 2021},
#     {'id': 4, 'name': 'COUNTRY HEAT', 'id_track': 5, 'release_year': 2021},
#     {'id': 5, 'name': "ROCK 'N' ROLL REMASTERS", 'id_track': 1, 'release_year': 2020},
#     {'id': 6, 'name': 'ROCK HALLOWEEN', 'id_track': 9, 'release_year': 2019},
#     {'id': 7, 'name': 'NEW ROCK 4', 'id_track': 11, 'release_year': 2017},
#     {'id': 8, 'name': 'ROCK DRIVE', 'id_track': 15, 'release_year': 2013}
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

# connection.execute(album.update().where(album.c.id == 7).values(release_year=2018))
# connection.execute((track.update().where(track.c.id == 1).values(name='My habibi')))

# Запросы

def get_query_1():
    i = int()
    for genres in session.query(Genre.name).all():
        gen = session.query(func.count(genremusician.c.id_musician)).\
            where(genremusician.c.id_genre == i).scalar()
        print(f'В жанре {genres} - {gen} исполнителей(я)')
        i += 1


def get_query_2():
    tracks = (
        session.query(
            func.count(Track.id)
        )
        .join(Album)
        .filter(Album.release_year.between(2018, 2020))
        .all()
    )
    print(tracks)


def get_query_3():
    i = int()
    for album_mid_duration in session.query(Album).join(Track).all():
        i += 1
        album_mid_duration = session.query(func.avg(Track.duration)).\
            where(Track.id_album == i).scalar()
        print(f'{session.query(Album.name).where(Album.id == i).all()}{album_mid_duration}')


# Одного музыканта не выводит, так как у него вообще нет ни одного альбома, а соотвественно и в связующей таблице нет.
# Не понимаю, как это исправить
def get_query_4():
    musicians = (
        session.query(
            Musician.name
        )
        .join(albummusician, Album)
        .filter(Album.release_year != 2020)
        .distinct()
        .all()
    )
    print(musicians)


def get_query_5():
    musician_collections = (
        session.query(
            Collection.name
        )
        .join(trackcollection, Track, Album, albummusician, Musician)
        .filter(Musician.name == 'Muse')
        .all()
    )
    print(musician_collections)


def get_query_6():
    gen_musicians = (
        session.query(
            Album.name,
            func.count(genremusician.c.id_musician).label('total_genres')
        )
        .join(albummusician, Musician, genremusician)
        .group_by(Album.name)
        .order_by(desc('total_genres'))
        .all()
    )

    for albums in gen_musicians:
        if albums[1] != 1:
            print(albums[0])
        else:
            break


def get_query_7():
    not_collection_tracks = (
        session.query(
            Track.name
        )
        .join(trackcollection, Collection)
        .filter(Track.id != Collection.id_track)
        .distinct()
        .all()
    )
    print(not_collection_tracks)


def get_query_8():
    min_track = session.query(func.min(Track.duration)).scalar()
    musician_min_track = (
        session.query(
            Musician.name
        )
        .join(albummusician, Album, Track)
        .filter(Track.duration == min_track)
        .all()
    )
    print(musician_min_track)


def get_query_9():
    track_number = (
        session.query(
            Album.name,
            func.count(Track.id_album).label('track_total')
        )
        .join(Track)
        .group_by(Album.name)
        .order_by('track_total')
        .all()
    )
    min_album = track_number[0][1]
    for min_albums in track_number:
        if min_albums[1] == min_album:
            print(min_albums[0])
        else:
            break
