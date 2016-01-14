"""create adopter table

Revision ID: 39a9fd97cff5
Revises: 41ab9f841d48
Create Date: 2015-11-13 07:32:54.717000

"""

# revision identifiers, used by Alembic.
revision = '39a9fd97cff5'
down_revision = '41ab9f841d48'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
    	'adopter',
    	sa.Column('id', sa.Integer, primary_key=True),
    	sa.Column('name', sa.String, nullable=False)
	)


def downgrade():
    op.drop_table('adopter')
