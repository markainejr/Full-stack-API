"""adding content column to posts

Revision ID: 26afca35b785
Revises: 13029d32543a
Create Date: 2025-02-21 16:10:59.520686

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26afca35b785'
down_revision: Union[str, None] = '13029d32543a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
