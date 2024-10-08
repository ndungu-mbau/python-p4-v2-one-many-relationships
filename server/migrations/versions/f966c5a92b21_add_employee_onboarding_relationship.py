"""add employee-onboarding relationship

Revision ID: f966c5a92b21
Revises: a2f891c3ba1d
Create Date: 2024-10-07 12:41:36.570548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f966c5a92b21'
down_revision = 'a2f891c3ba1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('onboardings', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_onboardings_employee_id_employees'), 'onboardings', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_onboardings_employee_id_employees'), 'onboardings', type_='foreignkey')
    op.drop_column('onboardings', 'employee_id')
    # ### end Alembic commands ###
