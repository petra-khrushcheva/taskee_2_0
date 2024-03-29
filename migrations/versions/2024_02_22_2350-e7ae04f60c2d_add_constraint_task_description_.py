"""add constraint task description nullable true

Revision ID: e7ae04f60c2d
Revises: 778a1e686300
Create Date: 2024-02-22 23:50:14.803670

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "e7ae04f60c2d"
down_revision: Union[str, None] = "778a1e686300"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "tasks", "description", existing_type=sa.TEXT(), nullable=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "tasks", "description", existing_type=sa.TEXT(), nullable=False
    )
    # ### end Alembic commands ###
