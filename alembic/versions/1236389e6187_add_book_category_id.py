"""add book category_id

Revision ID: 1236389e6187
Revises: 02eb16c0a742
Create Date: 2026-08-13 13:15:49.602832

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1236389e6187'
down_revision: Union[str, Sequence[str], None] = '02eb16c0a742'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("books", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("category_id", sa.Integer(), nullable=True)
        )
        batch_op.create_foreign_key(
            "fk_books_category_id_categories",
            "categories",
            ["category_id"],
            ["id"],
        )


def downgrade() -> None:
    with op.batch_alter_table("books", schema=None) as batch_op:
        batch_op.drop_constraint(
            "fk_books_category_id_categories",
            type_="foreignkey",
        )
        batch_op.drop_column("category_id")