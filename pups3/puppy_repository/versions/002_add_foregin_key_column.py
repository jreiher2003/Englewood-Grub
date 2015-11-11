from sqlalchemy import Table, MetaData, String, Column, ForeignKey, Integer


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    puppy = Table('puppy', meta, autoload=True)
    shelter_id = Column('shelter_id', Integer)
    shelter_id.create(puppy)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    puppy = Table('puppy', meta, autoload=True)
    puppy.c.shelter_id.drop()
