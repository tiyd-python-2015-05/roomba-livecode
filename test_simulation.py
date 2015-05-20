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