"""empty message

Revision ID: d8c229fba653
Revises: 55c225aa3e19
Create Date: 2022-03-29 15:16:08.609078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8c229fba653'
down_revision = '55c225aa3e19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('homeplanet', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'people', 'planet', ['homeplanet'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'people', type_='foreignkey')
    op.drop_column('people', 'homeplanet')
    # ### end Alembic commands ###
