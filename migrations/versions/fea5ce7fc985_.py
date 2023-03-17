"""empty message

Revision ID: fea5ce7fc985
Revises: 369ea7370828
Create Date: 2023-03-16 21:37:59.129581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fea5ce7fc985'
down_revision = '369ea7370828'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('gender', sa.String(length=80), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('race', sa.String(length=80), nullable=True),
    sa.Column('hair_color', sa.String(length=80), nullable=True),
    sa.Column('eye_color', sa.String(length=80), nullable=True),
    sa.Column('favorite_people', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['favorite_people'], ['favorites.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('gravity', sa.Integer(), nullable=True),
    sa.Column('orbital_period', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(length=80), nullable=True),
    sa.Column('terrain', sa.String(length=80), nullable=True),
    sa.Column('favorite_planets', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['favorite_planets'], ['favorites.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    op.drop_table('people')
    op.drop_table('favorites')
    # ### end Alembic commands ###
