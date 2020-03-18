import sys

class Mapper:
    def __init__(self, s1, s2):

        self.__s1, self.__s2 = s1, s2
        self.__mapping = {}
        self.__existsMapping = True
        self.validateMapping()

    def validateMapping(self):
        if len(self.__s1) > len(self.__s2):
            self.__existsMapping = False
        else:
            for i in range(len(self.__s1)):
                if self.__s1[i] in self.__mapping and self.__mapping[self.__s1[i]] != self.__s2[i]:
                    self.__existsMapping = False
                    break
                else:
                    self.__mapping[self.__s1[i]] = self.__s2[i]

mapper = Mapper(sys.argv[1], sys.argv[2])