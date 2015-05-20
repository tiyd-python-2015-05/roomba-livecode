from simulation import Room, Roomba, Simulation
import pytest


@pytest.fixture
def room():
    return Room(length=10, width=10)


def test_simulation_can_have_a_room_and_roombas(room):
    roomba = Roomba()
    sim = Simulation(room=room, roombas=[roomba])

    assert sim.room is room
    assert sim.roombas == [roomba]


def test_simulation_can_step_forward(room):
    """
    In one step, I expect:
    - All roombas to move forward
    - The roombas' ending square to be clean
    """
    roomba = Roomba(5, 5)
    start_position = roomba.position
    sim = Simulation(room=room, roombas=[roomba])
    sim.step()

    assert roomba.position != start_position
    assert room.is_clean(*roomba.position)


def test_simulation_alerts_colliding_roomba(room):
    roomba = Roomba(9.5, 9.5, angle=90)
    start_position = roomba.position
    sim = Simulation(room=room, roombas=[roomba])
    sim.step()

    assert roomba.position != start_position
    assert roomba.angle != 90

def test_simulation_runs():
    room = Room(3, 3)
    roomba = Roomba(1, 1, angle=90)
    sim = Simulation(room=room, roombas=[roomba])
    results = sim.run()
    assert sim.steps > 0
    assert 0.5 in results
    assert 0.9 in results
    assert 1.0 in results

