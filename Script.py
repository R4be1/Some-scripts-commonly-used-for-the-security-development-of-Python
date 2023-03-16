def RANDOM(num:int=32)->str:
    #Random choice 0-9a-zA-z.
    #You can control the size of the return value through the num parameter.
    import random
    _RANDOM="".join([random.choice("1234567890abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(num)])
    return _RANDOM

def LoadModules(PATH:"Folder's path")->list:
    #Get all the py module files in the folder.
    #Note that this function will get all the py files under the path, including subfolders.
    return [os.path.join(root,file).replace(PATH,"").replace(".py","").replace("\\",".") for root,dirs,files in os.walk(PATH) for file in files if file.endswith(".py")]
