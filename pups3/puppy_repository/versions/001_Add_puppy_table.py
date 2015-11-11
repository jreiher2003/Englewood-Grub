from sqlalchemy import Table, Column, Integer, String, Date, MetaData, ForeignKey, Numeric
from sqlalchemy.orm import relationship

meta = MetaData()

puppy = Table(
    'puppy', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(250), nullable=False),
    Column('gender', String(6), nullable=False),
    Column('dateOfBirth', Date),
    Column('picture', String),
    Column('weight', Numeric(10))
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    puppy.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    puppy.drop()
