
class Strings(object):
	
    @staticmethod
    def replaceList(string, list, encoding="utf-8"):
	"""Receives a string template like 'My name is %0 and I am %1 years old' and
	   a list with values to be replaced, like ['Tiago Neves', '29']. This
	   example produces the string 'My name is Tiago Neves and I am 29 years old'"""
        for count in range(len(list)-1, -1, -1):
            value = list[count]
            if value is not None:
                if type(value) == type('string'):
                  value = value.decode(encoding)
                string = string.replace("%%%s" % count, value)
        return string
