import yaml


class Yamloperation:
    def __init__(self,path):
        with open(path,'r+', encoding='utf8') as file:
            self.data = yaml.load(file,Loader=yaml.FullLoader)

    def get_locator(self,page,locator_name):
        return self.data[page][locator_name]

# yamls = Yamloperation('../config/ecation.yaml')
# print(yamls.get_locator('Customerpage','customerNO'))