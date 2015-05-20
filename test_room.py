from simulation import Room
import pytest

@pytest.fixture
def room():
    return Room(length=10, width=20)

def test_room_knows_its_length_and_width(room):
    assert room.length == 10
    assert room.width == 20

def test_room_knows_its_area(room):
    assert room.area == 200

def test_room_is_not_clean_on_init(room):
    assert room.clean_percentage() == 0.0

def test_squares_can_be_cleaned(room):
    room.clean(1.8, 10.2)
    assert room.is_clean(1, 10)
    assert room.clean_percentage() == 0.005

def test_room_knows_its_bounds(room):
    assert room.in_bounds(10, 6)
    assert not room.in_bounds(21, 5)
    assert not room.in_bounds(10, 11)
    assert not room.in_bounds(21, 11)
    assert not room.in_bounds(-1, 5)
    assert not room.in_bounds(20, 10)

