"""empty message

Revision ID: 98dfa171a2a5
Revises: 
Create Date: 2020-03-10 20:30:27.306673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98dfa171a2a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    # ### end Alembic commands ###
