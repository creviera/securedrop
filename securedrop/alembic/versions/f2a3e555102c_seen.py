"""test

Revision ID: f2a3e555102c
Revises: 35513370ba0d
Create Date: 2020-09-15 00:14:24.334986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2a3e555102c'
down_revision = '35513370ba0d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "seen_files",
        sa.Column("file_uuid", sa.String(length=36), nullable=False),
        sa.Column("journalist_uuid", sa.String(length=36), nullable=False),
        sa.Column("file_id", sa.Integer(), nullable=True),
        sa.Column("journalist_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["file_id"], ["submissions.id"]),
        sa.ForeignKeyConstraint(["journalist_id"], ["journalists.id"]),
    )

def downgrade():
    op.drop_table("seen_files")
