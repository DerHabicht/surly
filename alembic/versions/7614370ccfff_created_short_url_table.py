"""Created short URL table

Revision ID: 7614370ccfff
Revises: 
Create Date: 2021-02-01 20:11:52.498141

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7614370ccfff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('short_urls',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('short_url', sa.String(), nullable=False),
                    sa.Column('full_url', sa.String(), nullable=False),
                    sa.Column('created', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('full_url'),
                    sa.UniqueConstraint('short_url')
                    )


def downgrade():
    op.drop_table('short_urls')
