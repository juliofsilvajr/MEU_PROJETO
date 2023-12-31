"""db_criar_banco

Revision ID: 70da55bbe61b
Revises: 
Create Date: 2023-08-15 11:31:19.979311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70da55bbe61b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contato_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('telefone', sa.String(length=14), nullable=False),
    sa.Column('mensagem', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contato_model')
    # ### end Alembic commands ###
