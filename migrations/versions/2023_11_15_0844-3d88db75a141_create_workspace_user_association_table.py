"""create workspace user association table

Revision ID: 3d88db75a141
Revises: 531e446eb4f5
Create Date: 2023-11-15 08:44:50.257221

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '3d88db75a141'
down_revision: Union[str, None] = '531e446eb4f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workspaces',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default='TRUE', nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workspace_user_association',
    sa.Column('workspace_id', sa.Uuid(), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.Column('role', sa.Enum('admin', 'user', 'reader', name='grouprole'), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default='TRUE', nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'workspace_id', name='unique_workspace_user')
    )
    op.alter_column('tasks', 'executor_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.drop_constraint('tasks_creator_id_fkey', 'tasks', type_='foreignkey')
    op.drop_constraint('tasks_executor_id_fkey', 'tasks', type_='foreignkey')
    op.create_foreign_key(None, 'tasks', 'users', ['executor_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'tasks', 'users', ['creator_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.create_foreign_key('tasks_executor_id_fkey', 'tasks', 'users', ['executor_id'], ['id'])
    op.create_foreign_key('tasks_creator_id_fkey', 'tasks', 'users', ['creator_id'], ['id'])
    op.alter_column('tasks', 'executor_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_table('workspace_user_association')
    op.drop_table('workspaces')
    # ### end Alembic commands ###