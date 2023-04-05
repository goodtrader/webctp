import json

class GlobalConfig(object):

    TdFrontAddress: str
    MdFrontAddress: str
    BrokerID: str
    AuthCode: str
    AppID: str
    Port: int

    @classmethod
    def load_config(cls, config_file_path: str):
        with open(config_file_path) as f:
            config = json.load(f)
            cls.TdFrontAddress = config["TdFrontAddress"]
            cls.MdFrontAddress = config["MdFrontAddress"]
            cls.BrokerID = config["BrokerID"]
            cls.AuthCode = config["AuthCode"]
            cls.AppID = config["AppID"]
            cls.Port = config["WebSocketPort"]