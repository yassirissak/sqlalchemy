"""add user_id to comment

Revision ID: a1f3e2c9d047
Revises: bbc569c641d5
Create Date: 2026-05-27 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1f3e2c9d047'
down_revision = 'bbc569c641d5'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_comment_user_id', 'user', ['user_id'], ['id'])


def downgrade():
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_constraint('fk_comment_user_id', type_='foreignkey')
        batch_op.drop_column('user_id')
