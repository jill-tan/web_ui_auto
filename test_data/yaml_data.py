
class YamlData:
    email: str
    pwd: str
    def __init__(self, test_data : dict ):
        self.email = test_data['account_info']['email']
        self.pwd = test_data['account_info']['pwd']
