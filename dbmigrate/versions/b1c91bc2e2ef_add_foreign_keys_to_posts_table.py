"""add foreign keys to posts table

Revision ID: b1c91bc2e2ef
Revises: d8a2d5bb5113
Create Date: 2025-02-21 23:59:25.874979

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1c91bc2e2ef'
down_revision: Union[str, None] = 'd8a2d5bb5113'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False)),
    op.create_foreign_key('posts_users_fk', source_table = 'posts', referent_table= 'users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
