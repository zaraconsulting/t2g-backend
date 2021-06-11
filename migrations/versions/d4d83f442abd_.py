"""empty message

Revision ID: d4d83f442abd
Revises: 89be32e94b6c
Create Date: 2021-05-30 17:20:09.681767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4d83f442abd'
down_revision = '89be32e94b6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('coachId', sa.Integer(), nullable=True, foreign_key=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('first_login', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.Column('team', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('coachId'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id')
    )
    op.create_unique_constraint(None, 'available__videos', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'available__videos', type_='unique')
    op.drop_table('player')
    # ### end Alembic commands ###
