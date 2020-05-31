from global_vars import *

class Room:
    def __init__(self, name, building, floor, capacity):
        self._name = name
        self._building = building
        self._floor = floor
        self._capacity = capacity
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name
    @property
    def building(self):
        return self._building
    @building.setter
    def building(self,building):
        self._building=building
    @property
    def floor(self):
        return self._floor
    @floor.setter
    def floor(self,floor):
        self._floor=floor
    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity
    @property
    def group(self):
        return self._group
    @group.setter
    def group(self, group):
        self._group = group
    def getRoomInfo(self):
        return self

class RoomList:
    def __init__(self, room_list):
        self._room_list = room_list
    def __init__(self, room_list,organization):
        self.room_list = room_list
        self.__organization=organization
    @property
    def room_list(self):
        return self._room_list
    @room_list.setter
    def room_list(self,room_list):
        self._room_list = room_list
    def createRoomList(self,file):
        return self
    def convertToCSV(self):
        return self