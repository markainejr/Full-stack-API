"""add user table

Revision ID: d8a2d5bb5113
Revises: 26afca35b785
Create Date: 2025-02-21 23:34:01.469166

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8a2d5bb5113'
down_revision: Union[str, None] = '26afca35b785'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None: 
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable = False),
    sa.Column('email', sa.String(), nullable = False),    
    sa.Column('password', sa.String(), nullable = False),     
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default =sa.text('now()'), nullable = False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
