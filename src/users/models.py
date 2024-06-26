from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import String
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core import Base


class User(Base, SQLAlchemyBaseUserTableUUID):
    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))

    created_tasks: Mapped[list["Task"]] = relationship(  # noqa: F821
        back_populates="creator", foreign_keys="Task.creator_id"
    )
    appointed_tasks: Mapped[list["Task"]] = relationship(  # noqa: F821
        back_populates="executor",
        foreign_keys="Task.executor_id",
        order_by="desc(Task.created_at)",
    )

    workspaces: Mapped[list["WorkspaceUserAssociation"]] = (  # noqa: F821
        relationship(back_populates="user", cascade="all, delete")
    )
    user_role: AssociationProxy[list[str]] = association_proxy(
        "workspaces", "user_role"
    )

    @hybrid_property
    def full_name(self):
        return self.first_name + " " + self.last_name
