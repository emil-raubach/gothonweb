from nose.tools import *
from gothonweb.planisphere import *

def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_central_corridor():
    start_room = load_room(START)
    assert_equal(start_room.go('shoot!'), shoot_death)
    assert_equal(start_room.go('dodge!'), dodge_death)

def test_laser_weapon_armory():
    shoot = Room('laser_weapon_armory', 'Laser Beams!')

    shoot.add_paths({'shoot!': shoot_death})
    assert_equal(shoot.go('shoot!'), shoot_death)

def test_load_room():
    my_room = Room('central_corridor', 'Stuff')
    my_room.add_paths({'central_corridor': central_corridor})
    assert_equal(load_room(my_room.name), central_corridor)
