"""create puppy_adopter_link table

Revision ID: 2aaaf94c6f3e
Revises: 39a9fd97cff5
Create Date: 2015-11-13 07:34:44.604000

"""

# revision identifiers, used by Alembic.
revision = '2aaaf94c6f3e'
down_revision = '39a9fd97cff5'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
    	'puppyadopterlink',
    	sa.Column('puppy_id', sa.Integer, sa.ForeignKey('puppy.id'), primary_key=True),
    	sa.Column('adopter_id', sa.Integer, sa.ForeignKey('adopter.id'), primary_key=True)
	)


def downgrade():
    op.drop_table('puppyadopterlink')
