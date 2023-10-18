def RANDOM(num:int=32)->str:
    #Random choice 0-9a-zA-z.
    #You can control the size of the return value through the num parameter.
    import random
    _RANDOM="".join([random.choice("1234567890abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(num)])
    return _RANDOM

def LoadModules(PATH:"Folder's path")->list:
    #Get all the py module files in the folder.
    #Note that this function will get all the py files under the path, including subfolders.
    import os
    return [os.path.join(root,file).replace(PATH,"").replace(".py","").replace("\\",".") for root,dirs,files in os.walk(PATH) for file in files if file.endswith(".py")]

def URL(url):
    url=url if url.startswith("http://") or url.startswith("https://") else "http://"+url
    return url

def Parameter(para):
    if para in sys.argv:
        para=sys.argv.index(para)
        para=sys.argv[para+1] if len(sys.argv) > para+1 else None
        return para

def GetTitle(text):
    match = re.search(r'<title.*?>(.+?)</title>', text)
    if match: return match.group(1)
    else: return str()

class AttribDict(dict):
    """
    This class defines the dictionary with added capability to access members as attributes

    >>> foo = AttribDict()
    >>> foo.bar = 1
    >>> foo.bar
    1
    """

    def __init__(self, indict=None, attribute=None, keycheck=True):
        if indict is None:
            indict = {}

        # Set any attributes here - before initialisation
        # these remain as normal attributes
        self.attribute = attribute
        self.keycheck = keycheck
        dict.__init__(self, indict)
        self.__initialised = True

        # After initialisation, setting attributes
        # is the same as setting an item

    def __getattr__(self, item):
        """
        Maps values to attributes
        Only called if there *is NOT* an attribute with this name
        """

        try:
            return self.__getitem__(item)
        except KeyError:
            if self.keycheck:
                raise AttributeError("unable to access item '%s'" % item)
            else:
                return None

    def __setattr__(self, item, value):
        """
        Maps attributes to values
        Only if we are initialised
        """

        # This test allows attributes to be set in the __init__ method
        if "_AttribDict__initialised" not in self.__dict__:
            return dict.__setattr__(self, item, value)

        # Any normal attributes are handled normally
        elif item in self.__dict__:
            dict.__setattr__(self, item, value)

        else:
            self.__setitem__(item, value)

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, dict):
        self.__dict__ = dict

    def __deepcopy__(self, memo):
        retVal = self.__class__()
        memo[id(self)] = retVal

        for attr in dir(self):
            if not attr.startswith('_'):
                value = getattr(self, attr)
                if not isinstance(value, (types.BuiltinFunctionType, types.FunctionType, types.MethodType)):
                    setattr(retVal, attr, copy.deepcopy(value, memo))

        for key, value in self.items():
            retVal.__setitem__(key, copy.deepcopy(value, memo))

        return retVal
