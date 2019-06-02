"""empty message

Revision ID: 57cd5d69895a
Revises: e8c512e9e8b5
Create Date: 2019-05-31 02:25:20.955862

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '57cd5d69895a'
down_revision = 'e8c512e9e8b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cart_items', 'user_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True,
               existing_server_default=sa.text("'0'"))
    op.alter_column('order_items', 'order_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True,
               existing_server_default=sa.text("'0'"))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order_items', 'order_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False,
               existing_server_default=sa.text("'0'"))
    op.alter_column('cart_items', 'user_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False,
               existing_server_default=sa.text("'0'"))
    # ### end Alembic commands ###