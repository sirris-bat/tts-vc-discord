import confuse

class _DefaultConfig:
    configName = 'TtsBot'

    token = None

class Config(_DefaultConfig):
    def __init__(self):
        # Get YAML config 
        config = confuse.Configuration('TtsBot', __name__)
        config.set_file('config.yaml')

        self.token = config['Bot']['Token'].get(str)
        print('***' + self.token)
