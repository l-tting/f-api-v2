"""update user model

Revision ID: cbc318a71f52
Revises: 46e13fab3584
Create Date: 2025-01-17 16:18:22.866678

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cbc318a71f52'
down_revision: Union[str, None] = '46e13fab3584'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('full_name', sa.String(), nullable=False))
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('users', 'full_name')
    # ### end Alembic commands ###
