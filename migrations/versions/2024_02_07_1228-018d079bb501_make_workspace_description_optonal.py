"""make workspace description optonal

Revision ID: 018d079bb501
Revises: a2efb925de75
Create Date: 2024-02-07 12:28:20.841062

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "018d079bb501"
down_revision: Union[str, None] = "a2efb925de75"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "workspaces", "description", existing_type=sa.TEXT(), nullable=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "workspaces", "description", existing_type=sa.TEXT(), nullable=False
    )
    # ### end Alembic commands ###
