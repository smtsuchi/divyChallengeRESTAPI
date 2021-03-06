"""empty message

Revision ID: fcd77813355d
Revises: 
Create Date: 2021-04-09 15:56:00.544981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcd77813355d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('divvy',
    sa.Column('trip_id', sa.Integer(), nullable=False),
    sa.Column('starttime', sa.DateTime(), nullable=False),
    sa.Column('stoptime', sa.DateTime(), nullable=False),
    sa.Column('bikeid', sa.Integer(), nullable=False),
    sa.Column('from_station_id', sa.Integer(), nullable=False),
    sa.Column('from_station_name', sa.String(), nullable=False),
    sa.Column('to_station_id', sa.Integer(), nullable=False),
    sa.Column('to_station_name', sa.String(), nullable=False),
    sa.Column('usetype', sa.String(), nullable=False),
    sa.Column('gender', sa.String(length=150), nullable=True),
    sa.Column('birthday', sa.String(length=150), nullable=True),
    sa.Column('trip_duration', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('trip_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('divvy')
    # ### end Alembic commands ###
