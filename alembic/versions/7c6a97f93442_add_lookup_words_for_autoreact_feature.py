"""add lookup words for autoreact feature

Revision ID: 7c6a97f93442
Revises: 0b579352511c
Create Date: 2024-12-25 01:39:38.978841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c6a97f93442'
down_revision = '0b579352511c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('autoreacts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('lookup', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('autoreacts', schema=None) as batch_op:
        batch_op.drop_column('lookup')

    # ### end Alembic commands ###