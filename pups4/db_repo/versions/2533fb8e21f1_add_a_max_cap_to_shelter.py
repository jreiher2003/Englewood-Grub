"""add a max cap to shelter

Revision ID: 2533fb8e21f1
Revises: 2aaaf94c6f3e
Create Date: 2015-11-13 07:42:58.326000

"""

# revision identifiers, used by Alembic.
revision = '2533fb8e21f1'
down_revision = '2aaaf94c6f3e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('shelter', sa.Column('maximum_capacity', sa.Integer))


def downgrade():
    op.drop_column('shelter', 'maximum_capacity')
