"""add content column to post table

Revision ID: 80b889aaf9f2
Revises: 4402619500c7
Create Date: 2025-04-08 00:07:06.671340

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80b889aaf9f2'
down_revision: Union[str, None] = '4402619500c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'posts',
        sa.Column('content', sa.String(), nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
