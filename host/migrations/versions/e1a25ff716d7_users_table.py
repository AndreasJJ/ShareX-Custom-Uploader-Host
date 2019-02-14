"""users table

Revision ID: e1a25ff716d7
Revises: 40660b4c7550
Create Date: 2019-02-13 22:16:24.307327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1a25ff716d7'
down_revision = '40660b4c7550'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('link', sa.Column('size', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('link', 'size')
    # ### end Alembic commands ###