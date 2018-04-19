"""added first_name and last_name to user

Revision ID: 61795c91def9
Revises: 93d30788fca9
Create Date: 2018-04-15 20:57:47.119354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61795c91def9'
down_revision = '93d30788fca9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_name', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    # ### end Alembic commands ###