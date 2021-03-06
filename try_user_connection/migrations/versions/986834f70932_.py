"""empty message

Revision ID: 986834f70932
Revises: 
Create Date: 2019-12-30 01:59:23.851815

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '986834f70932'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item_rent')
    op.drop_table('car')
    op.drop_table('expenses')
    op.drop_table('parking')
    op.drop_table('sport_membership')
    op.drop_table('staff')
    op.drop_table('place_rent')
    op.drop_table('timetable')
    op.drop_table('medical_procedure')
    op.drop_table('canteen_place')
    op.drop_table('sport_group')
    op.drop_table('consultation')
    op.drop_table('warehouse')
    op.drop_table('living_room')
    op.drop_table('income')
    op.drop_table('item')
    op.drop_table('infrastructure')
    op.drop_table('appointment')
    op.drop_table('resident')
    op.drop_table('diet')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('diet',
    sa.Column('id_diet', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('diet_name', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_diet', name='diet_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('resident',
    sa.Column('id_resident', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('gender', sa.VARCHAR(length=8), autoincrement=False, nullable=True),
    sa.Column('surname', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('patronymic', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('room_number', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('birthday', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('place_number', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('start_day', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('final_day', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['place_number'], ['canteen_place.canteen_number'], name='place_number'),
    sa.ForeignKeyConstraint(['room_number'], ['living_room.room_number'], name='resident_room_number_fkey'),
    sa.PrimaryKeyConstraint('id_resident', name='resident_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('appointment',
    sa.Column('id_resident', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id_procedure', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_procedure'], ['medical_procedure.id_procedure'], name='appointment_id_procedure_fkey'),
    sa.ForeignKeyConstraint(['id_resident'], ['resident.id_resident'], name='appointment_id_resident_fkey')
    )
    op.create_table('infrastructure',
    sa.Column('rent_number', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('rent_number', name='infrastructure_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('item',
    sa.Column('id_item', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('item_name', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_item', name='item_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('income',
    sa.Column('operation_number', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('operation_time', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('sum', postgresql.MONEY(), autoincrement=False, nullable=True),
    sa.Column('id_resident', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_resident'], ['resident.id_resident'], name='id_resident'),
    sa.PrimaryKeyConstraint('operation_number', name='income_pkey')
    )
    op.create_table('living_room',
    sa.Column('room_number', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('floor', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('room_class', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('room_number', name='living_room_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('warehouse',
    sa.Column('id_warehouse', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('number', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id_item', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_item'], ['item.id_item'], name='warehouse_id_item_fkey'),
    sa.PrimaryKeyConstraint('id_warehouse', name='warehouse_pkey')
    )
    op.create_table('consultation',
    sa.Column('id_consultation', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('consultation_name', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('id_resident', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_resident'], ['resident.id_resident'], name='consultation_id_resident_fkey'),
    sa.PrimaryKeyConstraint('id_consultation', name='consultation_pkey')
    )
    op.create_table('sport_group',
    sa.Column('id_group', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('group_name', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_group', name='sport_group_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('canteen_place',
    sa.Column('canteen_number', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id_diet', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_diet'], ['diet.id_diet'], name='canteen_place_id_diet_fkey'),
    sa.PrimaryKeyConstraint('canteen_number', name='canteen_place_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('medical_procedure',
    sa.Column('id_procedure', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('procedure_name', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_procedure', name='medical_procedure_pkey')
    )
    op.create_table('timetable',
    sa.Column('week_day', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('start_time', postgresql.TIME(), autoincrement=False, nullable=True),
    sa.Column('finish_time', postgresql.TIME(), autoincrement=False, nullable=True),
    sa.Column('staff_cadr', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['staff_cadr'], ['staff.staff_cadr'], name='staff_cadr'),
    sa.PrimaryKeyConstraint('week_day', name='timetable_pkey')
    )
    op.create_table('place_rent',
    sa.Column('id_resident', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rent_number', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_resident'], ['resident.id_resident'], name='id_resident'),
    sa.ForeignKeyConstraint(['rent_number'], ['infrastructure.rent_number'], name='rent_number')
    )
    op.create_table('staff',
    sa.Column('staff_cadr', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('surname', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('patronymic', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('position', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('hours', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('salary', postgresql.MONEY(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('staff_cadr', name='staff_pkey')
    )
    op.create_table('sport_membership',
    sa.Column('id_resident', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id_group', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_group'], ['sport_group.id_group'], name='sport_membership_id_group_fkey'),
    sa.ForeignKeyConstraint(['id_resident'], ['resident.id_resident'], name='sport_membership_id_resident_fkey')
    )
    op.create_table('parking',
    sa.Column('id_place', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('car_number', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['car_number'], ['car.car_number'], name='parking_car_number_fkey'),
    sa.PrimaryKeyConstraint('id_place', name='parking_pkey')
    )
    op.create_table('expenses',
    sa.Column('operation_num', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('operation_data', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('operation_sum', postgresql.MONEY(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('operation_num', name='expenses_pkey')
    )
    op.create_table('car',
    sa.Column('car_number', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('id_resident', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('model', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('color', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_resident'], ['resident.id_resident'], name='car_id_resident_fkey'),
    sa.PrimaryKeyConstraint('car_number', name='car_pkey')
    )
    op.create_table('item_rent',
    sa.Column('id_resident', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id_item', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_item'], ['item.id_item'], name='item_rent_id_item_fkey'),
    sa.ForeignKeyConstraint(['id_resident'], ['resident.id_resident'], name='item_rent_id_resident_fkey')
    )
    # ### end Alembic commands ###
