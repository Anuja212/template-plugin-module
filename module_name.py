

# Please change to your module name
class ModuleName:
    def __init__(self):
        self.method_description = [
            {'name': 'process', 'params': []},
            {'name': 'change_param', 'params': [{'x': 'int'}, {'y': 'bool'}]}
        ]
        # variable type of params can be int, float, bool
        # Put the code to initial your project
        print(self.method_description)

    def process(self):
        """
        @brinf: This is the description of your method
        @params: The input argument (except self)
        @return: The structure of return variable
                 In case of the return value is dict. 
                 You have to explain whole structure
        """
        return None 

    def change_param(self, x, y):
        pass

    def capture(self):
        pass

if __name__ == "__main__":
    test = ModuleName()
