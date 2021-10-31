import pytest
from mock import Mock
from geocoding.models import Task, Point, Link
from uuid import UUID


def test_task_creation():
	task = Mock(spec=Task)
	task.task_id = "d2c46e5b-0d40-455d-a5d2-9b18dfaecb0c"
	assert task.task_id == "d2c46e5b-0d40-455d-a5d2-9b18dfaecb0c"


def test_point_creation():
	task = Mock(spec=Task)
	point = Mock(spec=Point)
	point.task_id = task
	point.name = 'Kyiv',
	point.address = '2а, Лисенка вулиця, Старий Київ, Центр'
	assert point.address == '2а, Лисенка вулиця, Старий Київ, Центр'


def test_point_creation():
	task = Mock(spec=Task)
	link = Mock(spec=Link)
	link.task_id = task
	link.name = 'AB',
	link.distance = 234.9
	assert link.distance == 234.9


@pytest.mark.django_db
def test_task_created():
	Task.objects.create(
		task_id="d2c46e5b-0d40-455d-a5d2-9b18dfaecb0c"
	)
	qs = Task.objects.last()
	assert qs.task_id == UUID('d2c46e5b-0d40-455d-a5d2-9b18dfaecb0c')


@pytest.mark.django_db
def test_point_created():
	task = Task.objects.create(
		task_id="d2c46e5b-0d40-455d-a5d2-9b18dfaecb0c"
	)
	Point.objects.create(
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
	Link.objects.create(
		task_id=task,
		name='AB',
		distance=324.3
	)
	qs = Link.objects.last()
	assert qs.distance == 324.3
