import pytest
from geocoding.models import Task, Point, Link
from uuid import UUID


@pytest.mark.django_db
def test_task_created():
	task = Task.objects.create(
		task_id="d2c46e5b-0d40-455d-a5d2-9b18dfaecb0c"
	)
	qs = Task.objects.last()
	assert qs.task_id == UUID('d2c46e5b-0d40-455d-a5d2-9b18dfaecb0c')


@pytest.mark.django_db
def test_point_created():
	task = Task.objects.create(
		task_id="d2c46e5b-0d40-455d-a5d2-9b18dfaecb0c"
	)
	point = Point.objects.create(
		task_id=task,
		name='Kyiv',
		address='2а, Лисенка вулиця, Старий Київ, Центр,'
				' Шевченківський район, Київ, 01034, Україна'
	)
	qs = Point.objects.last()
	assert qs.name == 'Kyiv'


@pytest.mark.django_db
def test_link_created():
	task = Task.objects.create(
			task_id="d2c46e5b-0d40-455d-a5d2-9b18dfaecb0c"
	)	
	link = Link.objects.create(
		task_id=task,
		name='AB',
		distance=324.3
	)
	qs = Link.objects.last()
	assert qs.distance == 324.3
