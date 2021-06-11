"""empty message

Revision ID: 430f1ae04974
Revises: d4d83f442abd
Create Date: 2021-05-30 17:23:45.630953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '430f1ae04974'
down_revision = 'd4d83f442abd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('player_coachId_key', 'player', type_='unique')
    op.drop_column('player', 'coachId')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('player', sa.Column('coachId', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_unique_constraint('player_coachId_key', 'player', ['coachId'])
    # ### end Alembic commands ###