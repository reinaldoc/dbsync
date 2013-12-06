
class Strings(object):
	
    @staticmethod
    def replaceList(string, list, encoding="utf-8"):
	"""Receives a string template like 'My name is %0 and I am %1 years old' and
	   a list with values to be replaced, like ['Tiago Neves', '29']. This
	   example produces the string 'My name is Tiago Neves and I am 29 years old'"""
        for count in range(0,len(list)):
            if list[count] is not None:
                string = string.replace("%%%s" % count, list[count].decode(encoding))
        return string
