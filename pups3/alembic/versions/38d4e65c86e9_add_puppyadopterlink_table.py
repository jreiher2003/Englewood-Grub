"""add puppyadopterlink table

Revision ID: 38d4e65c86e9
Revises: 803b1aa60c5
Create Date: 2015-11-12 10:24:11.607000

"""

# revision identifiers, used by Alembic.
revision = '38d4e65c86e9'
down_revision = '803b1aa60c5'
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
