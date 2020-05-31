class Tag:
    def __init__(self,name):
        self._name=name
        self._event_list= []
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name
    @property
    def event_list(self):
        return self._event_list
    @event_list.setter
    def event_list(self, event):
        self._event_list.append(event)

class TagList:
    def __init__(self,organization):
        self._tag_list = []
        self.__organization=organization
    @property
    def tag_list(self):
        return self._tag_list
    def addTag(self, name):
        #checks if the Tag is already on the list
        oldTag = next((x for x in self.tag_list if x.name == name), None)
        if(oldTag != None):
            #if already there it informs us
            print("Whoops, this tag is already in the tag list!")
            return oldTag
        else:
            #if new it is added to the list
            newTag = Tag(name)
            self._tag_list.append(newTag)
            return newTag