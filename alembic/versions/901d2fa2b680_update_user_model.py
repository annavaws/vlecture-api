"""Update user model

Revision ID: 901d2fa2b680
Revises: 6f702f53e396
Create Date: 2024-02-26 21:08:21.468421

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '901d2fa2b680'
down_revision: Union[str, None] = '6f702f53e396'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=225), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=225), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=225), autoincrement=False, nullable=True),
    sa.Column('hashed_password', postgresql.BYTEA(), autoincrement=False, nullable=False),
    sa.Column('refresh_token', sa.VARCHAR(length=225), autoincrement=False, nullable=True),
    sa.Column('access_token', sa.VARCHAR(length=225), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key')
    )
    # ### end Alembic commands ###
