
class Strings(object):
	
    @staticmethod
    def replaceList(string, list):
        for count in range(0,len(list)):
            if list[count] is not None:
                string = string.replace("%%%s" % count, list[count])
        return string
