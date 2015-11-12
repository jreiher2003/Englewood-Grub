"""add maxiumn and current to shelter

Revision ID: 3f2bacf0a02c
Revises: 38d4e65c86e9
Create Date: 2015-11-12 11:38:37.814000

"""

# revision identifiers, used by Alembic.
revision = '3f2bacf0a02c'
down_revision = '38d4e65c86e9'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('shelter', sa.Column('maximum_capacity', sa.Integer))
    op.add_column('shelter', sa.Column('current_occupancy', sa.Integer))


def downgrade():
    op.drop_column('shelter', 'maximum_capacity')
    op.dropt_column('shelter', 'current_occupancy')
