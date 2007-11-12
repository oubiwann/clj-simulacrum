from math import sqrt

class Location(object):
    """

    """
    def __init__(self, x, y, z, *coords):
        if coords:
            x, y, z = coords
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if not isinstance(other, Location):
            return False
        if (self.x == other.x and self.y == other.y and self.z == other.z):
            return True
        return False

    def __sub__(self, other):
        assert(isinstance(other, Location))
        x = (self.x - other.x)**2
        y = (self.y - other.y)**2
        z = (self.z - other.z)**2
        return sqrt(abs(x + y + z))

    def __repr__(self):
        return "<%s: x=%s, y=%s, z=%s>" % (
            self.__class__.__name__, self.x, self.y, self.z)


class Place(object):
    """

    """
    def __init__(self, w=1, l=1, h=1):
        self.width = w
        self.length = l
        self.height = h
        self.area = w * l
        self.volume = w * l * h
        self.map = {}

    def addObject(self, obj, location):
        """

        """
        # update map
        if isinstance(location, tuple):
            location = Location(*location)
        self.map[location] = obj
        obj.location = location

    def getObjectAt(self, location):
        """

        """
        return self.map[location]

    def moveObject(self, obj, location):
        """

        """
        oldLoc = None
        if obj not in self.map.values():
            msg = "Cannot move something that's not there!"
            raise Exception, msg
        if location in self.map.keys():
            msg = "Something's already there!"
            raise Exception, msg
        for loc, o in self.map.items():
            if o == obj:
                oldLoc = loc
                break
        print "Leaving old location %s for %s..." % (oldLoc, location)
        self.map[oldLoc] = None
        self.map[location] = obj

    def __contains__(self, objOrLocation):
        """

        """
        if isinstance(objOrLocation, Location):
            if objOrLocation in self.map.keys():
                return True
            return False
        elif isinstance(objOrLocation, Object):
            if objOrLocation in self.map.values():
                return True
            return False
        else:
            msg = "A Place object can only check for locations or objects."
            raise Exception, msg


class Room(Place):
    pass


class Relationship(dict):
    """

    """
    def __init__(self, owner, obj, attraction):
        """

        """
        self.owner = owner
        self.object = obj
        self.attraction = attraction

    def getObjectDistance(self):
        return self.owner.location - self.object.location


    def getNearestLocation(self):
        """
        Examine all neighboring locations and find the one that is closest to
        the object in this relationship.
        """

class Object(object):
    pass


class Person(Object):
    """

    """
    def __init__(self, id, location=(), relationships={}):
        """

        """
        self.id = self.name = id
        if location and isinstance(location, tuple):
            location = Location(*location)
        self.location = location
        self.relationships = relationships

    def addRelationship(self, relationship):
        """

        """
        assert(relationship.owner == self)
        self.relationships[relationship.object] = relationship


def runTest():
    print "Unrequited love..."
    room = Room(w=10, l=20, h=2)
    alice = Person('alice')
    bob = Person('bob')
    room.addObject(alice, (1,1,1))
    room.addObject(bob, (10,20,1))
    # bob is interested in being closer to alice
    bobToAlice = Relationship(bob, alice, 1)
    bob.addRelationship(bobToAlice)
    print bob.relationships[alice].getObjectDistance()
    # alice is ambivalent to bob
    alliceToBob = Relationship(alice, bob, 0)
    alice.addRelationship(alliceToBob)
    print alice.relationships[bob].getObjectDistance()

