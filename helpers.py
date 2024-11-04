from jproperties import Properties

configs = Properties()

isConfigLoaded = False

def getConf(prop: str) -> Properties:
    if not isConfigLoaded:
        with open('.env', 'rb') as configFile:
            configs.load(configFile)
            configFile.close()
    return configs.get(prop).data

def logDebug(data: str):
    if getConf("IS_DEV"):
        print(data)