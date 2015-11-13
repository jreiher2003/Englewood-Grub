"""create profile table

Revision ID: 41ab9f841d48
Revises: 
Create Date: 2015-11-13 07:26:26.074000

"""

# revision identifiers, used by Alembic.
revision = '41ab9f841d48'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
    	'profile',
    	sa.Column('id', sa.Integer, primary_key=True),
    	sa.Column('photo', sa.String),
    	sa.Column('description', sa.String),
    	sa.Column('specialNeeds', sa.String),
    	sa.Column('puppy_id', sa.Integer, sa.ForeignKey('puppy.id'))
	)


def downgrade():
    op.drop_table('profile')
