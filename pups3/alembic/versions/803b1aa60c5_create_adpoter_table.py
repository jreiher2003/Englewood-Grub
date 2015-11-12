"""create adpoter table

Revision ID: 803b1aa60c5
Revises: b68ba34f5ee
Create Date: 2015-11-12 10:05:00.498000

"""

# revision identifiers, used by Alembic.
revision = '803b1aa60c5'
down_revision = 'b68ba34f5ee'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
    	'adpoter',
    	sa.Column('id', Integer, primary_key=True),
    	sa.Column('name', sa.Sting, nullable=False)
	)


def downgrade():
    op.drop_table('adpoter')
