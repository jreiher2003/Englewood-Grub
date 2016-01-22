"""empty message

Revision ID: 98527a9c89d1
Revises: None
Create Date: 2016-01-22 17:06:25.439000

"""

# revision identifiers, used by Alembic.
revision = '98527a9c89d1'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('association',
    sa.Column('puppy_id', sa.Integer(), nullable=True),
    sa.Column('adopters_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['adopters_id'], ['adopters.id'], ),
    sa.ForeignKeyConstraint(['puppy_id'], ['puppy.id'], )
    )
    op.add_column(u'shelter', sa.Column('current_capacity', sa.Integer(), nullable=True))
    op.add_column(u'shelter', sa.Column('maximum_capacity', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'shelter', 'maximum_capacity')
    op.drop_column(u'shelter', 'current_capacity')
    op.drop_table('association')
    ### end Alembic commands ###
