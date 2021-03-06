import confuse

class _DefaultConfig:
    configName = 'TtsBot'

    appName = 'TTS VC Discord'
    token = None
    commandsEnabled = False

    logLevel = "INFO"
    logFile = None

class Config(_DefaultConfig):
    def __init__(self):
        # Get YAML config 
        config = confuse.Configuration('TtsBot', __name__)
        config.set_file('config.yaml')

        self.token = config['Bot']['Token'].get(str)
        self.commandsEnabled = config['Bot']['commandsEnabled'].get(bool)
        self.appName = config['WebUI']['name'].get(str)
        self.logLevel = config['Logging']['logLevel'].get(str)
        self.logFile = config['Logging']['logFile'].get(str)
