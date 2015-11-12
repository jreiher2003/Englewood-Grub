"""create profile table

Revision ID: b68ba34f5ee
Revises: 4a9614abefca
Create Date: 2015-11-12 09:47:24.006000

"""

# revision identifiers, used by Alembic.
revision = 'b68ba34f5ee'
down_revision = '4a9614abefca'
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
