"""added tags table

Revision ID: 0e10354a8fd4
Revises: bd1633663515
Create Date: 2024-11-11 08:47:11.261030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0e10354a8fd4'
down_revision: Union[str, None] = 'bd1633663515'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('uid', sa.UUID(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('booktag',
    sa.Column('book_id', sa.Uuid(), nullable=False),
    sa.Column('tag_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.uid'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.uid'], ),
    sa.PrimaryKeyConstraint('book_id', 'tag_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('booktag')
    op.drop_table('tags')
    # ### end Alembic commands ###
