"""create puppy table

Revision ID: 154bfbe229a6
Revises: 
Create Date: 2015-11-11 08:44:06.675000

"""

# revision identifiers, used by Alembic.
revision = '154bfbe229a6'
down_revision = None
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
    	sa.Column('weight',sa.Numeric(10)),
    	sa.Column('shelter_id',sa.Integer, sa.ForeignKey('shelter.id'))
    	)


def downgrade():
    op.drop_table('puppy')
