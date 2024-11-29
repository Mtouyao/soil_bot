"""first revision

迁移 ID: ce7ee9d4e359
父迁移:
创建时间: 2024-08-21 13:01:53.113592

"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "ce7ee9d4e359"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = ("nonebot_plugin_lxns_maimai",)
depends_on: str | Sequence[str] | None = None


def upgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "nonebot_plugin_lxns_maimai_user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("friend_code", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_nonebot_plugin_lxns_maimai_user")),
        info={"bind_key": "nonebot_plugin_lxns_maimai"},
    )
    # ### end Alembic commands ###


def downgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("nonebot_plugin_lxns_maimai_user")
    # ### end Alembic commands ###
