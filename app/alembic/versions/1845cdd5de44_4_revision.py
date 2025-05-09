"""4 revision

Revision ID: 1845cdd5de44
Revises: f9b9e2dc3b5e
Create Date: 2025-04-13 19:17:48.887587

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1845cdd5de44'
down_revision: Union[str, None] = 'f9b9e2dc3b5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_place_assoc',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('place_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['place_id'], ['places.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('userplaceassocs')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userplaceassocs',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('place_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['place_id'], ['places.id'], name='userplaceassocs_place_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='userplaceassocs_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='userplaceassocs_pkey')
    )
    op.drop_table('user_place_assoc')
    # ### end Alembic commands ###
