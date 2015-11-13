"""add current capacity to shelter

Revision ID: e54766eec5b
Revises: 2533fb8e21f1
Create Date: 2015-11-13 07:53:55.042000

"""

# revision identifiers, used by Alembic.
revision = 'e54766eec5b'
down_revision = '2533fb8e21f1'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('shelter', sa.Column('current_occupancy', sa.Integer))


def downgrade():
    op.drop_column('shelter', 'current_occupancy')
