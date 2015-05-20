from simulation import Roomba
import math

def test_roomba_should_know_its_position():
    roomba = Roomba(x=5, y=5)
    assert roomba.position == (5, 5)

def test_roomba_should_know_its_angle():
    roomba = Roomba(angle=90)
    assert roomba.angle == 90

def test_roomba_should_have_a_speed():
    roomba = Roomba()
    assert roomba.speed == 1

def test_roomba_should_know_next_position():
    roomba = Roomba(x=10, y=10, angle=45)
    assert roomba.next_position == (10 + math.sqrt(0.5), 10 + math.sqrt(0.5))

def test_roomba_should_turn_45_degrees_on_collision():
    roomba = Roomba(angle=280)
    roomba.collide()
    assert roomba.angle == 325

    roomba.collide()
    assert roomba.angle == 10

def test_roomba_can_move():
    roomba = Roomba(x=10, y=10, angle=45)
    roomba.move()
    assert roomba.position == (10 + math.sqrt(0.5), 10 + math.sqrt(0.5))

def test_roomba_can_be_placed():
    roomba = Roomba()
    roomba.place(4, 5)
    assert roomba.position == (4, 5)
