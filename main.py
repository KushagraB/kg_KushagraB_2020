import sys

class Mapper:
    def __init__(self, s1, s2):

        self.__s1, self.__s2 = s1, s2
        self.__mapping = {}
        self.__existsMapping = True
        self.validateMapping()

    def validateMapping(self):
        # One-to-one mapping from s1 to s2 cannot exist if len(s1) > len(s2)
        if len(self.__s1) > len(self.__s2):
            self.__existsMapping = False
        else:
            for i in range(len(self.__s1)):
                # if a mapping already exists for the character, and the current mapping is different from what's already stored.
                if self.__s1[i] in self.__mapping and self.__mapping[self.__s1[i]] != self.__s2[i]:
                    self.__existsMapping = False
                    break
                
                # Mapping for this character doesn't currently exist.
                else:
                    self.__mapping[self.__s1[i]] = self.__s2[i]

    def existsMapping(self):
        return self.__existsMapping

# Only if the number of given arguments are more than 2 ( "main.py", s1, s2 )
if len(sys.argv) >= 3:
    mapper = Mapper(sys.argv[1], sys.argv[2])
    print (mapper.existsMapping())
else:
    print ("Invalid input. The program requires two strings as arguments.")