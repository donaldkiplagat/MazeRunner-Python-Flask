"""Anime added

Revision ID: 52b1be69762e
Revises: c8c9a62894cd
Create Date: 2018-10-25 09:47:50.151414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52b1be69762e'
down_revision = 'c8c9a62894cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=255), nullable=True),
    sa.Column('choice1', sa.String(), nullable=True),
    sa.Column('choice2', sa.String(), nullable=True),
    sa.Column('button1', sa.String(), nullable=True),
    sa.Column('button2', sa.String(), nullable=True),
    sa.Column('div', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_animes_question'), 'animes', ['question'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_animes_question'), table_name='animes')
    op.drop_table('animes')
    # ### end Alembic commands ###
