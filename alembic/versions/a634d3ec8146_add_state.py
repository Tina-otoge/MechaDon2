"""Add state

Revision ID: a634d3ec8146
Revises: efcef62ef92a
Create Date: 2024-05-15 10:45:04.711956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a634d3ec8146'
down_revision = 'efcef62ef92a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('states',
    sa.Column('server_id', sa.Integer(), nullable=False),
    sa.Column('react', sa.String(), nullable=False),
    sa.Column('react_message_id', sa.Integer(), nullable=True),
    sa.Column('icon', sa.String(), nullable=True),
    sa.Column('channel_id', sa.Integer(), nullable=True),
    sa.Column('channel_text', sa.String(), nullable=True),
    sa.Column('message_id', sa.Integer(), nullable=True),
    sa.Column('message_text', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('server_id', 'react', name=op.f('pk_states'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('states')
    # ### end Alembic commands ###
