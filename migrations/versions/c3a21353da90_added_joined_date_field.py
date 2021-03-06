"""added joined date field

Revision ID: c3a21353da90
Revises: 61795c91def9
Create Date: 2018-04-15 21:01:08.715225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3a21353da90'
down_revision = '61795c91def9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('joined', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'joined')
    # ### end Alembic commands ###
