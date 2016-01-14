"""add table puppy

Revision ID: 4a9614abefca
Revises: 154bfbe229a6
Create Date: 2015-11-11 14:07:49.839000

"""

# revision identifiers, used by Alembic.
revision = '4a9614abefca'
down_revision = '154bfbe229a6'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('puppy',
    	sa.Column('id',sa.Integer,primary_key=True),
    	sa.Column('name',sa.String(250), nullable=False),
    	sa.Column('gender',sa.String(6), nullable=False),
    	sa.Column('dateOfBirth',sa.Date),
    	sa.Column('picture',sa.String),
    	sa.Column('weight',sa.Integer),
    	sa.Column('shelter_id',sa.Integer, sa.ForeignKey('shelter.id'))
    	)


def downgrade():
    op.drop_table('puppy')

