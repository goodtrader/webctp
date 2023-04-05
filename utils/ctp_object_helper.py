class CTPObjectHelper(object):

    exclude_attrs = ["thisown"]

    @staticmethod
    def object_to_dict(obj: object) -> dict[str, any]:
        data = {}
        if obj:
            for attr, value in obj.__dict__.items():
                if attr not in CTPObjectHelper.exclude_attrs:
                    data[attr] = value
        return data
    
    @staticmethod
    def dict_to_object(data: dict[str, any], obj: object) -> None:
        for attr, value in data.items():
            obj.__setattr__(attr, value)
    
    @staticmethod
    def build_response_dict(message_type: str, rsp_info: object, request_id: int, is_last: bool) -> dict[str, any]:
        response = {
            "MsgType": message_type,
            "RspInfo": None,
            "RequestID": request_id,
            "IsLast": is_last
        }
        if rsp_info:
            response["RspInfo"] = {
                "ErrorID": rsp_info.ErrorID,
                "ErrorMsg": rsp_info.ErrorMsg
            }
        return response
    
    @staticmethod
    def extract_request(request_dict: dict[str, any], request_field_name: str, request_type):
        req = request_type()
        CTPObjectHelper.dict_to_object(request_dict[request_field_name], req)
        return (req, request_dict["RequestID"])