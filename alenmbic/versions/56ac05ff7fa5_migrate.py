"""migrate

Revision ID: 56ac05ff7fa5
Revises: 650b950b879f
Create Date: 2024-04-14 21:44:58.606601

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56ac05ff7fa5'
down_revision: Union[str, None] = '650b950b879f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
