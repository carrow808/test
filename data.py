import pandas as pd
class Data():
    def __init__(self):
        self.data_dict = {}
    def buildDataframe(self):
        self.data_dict['df1'] = pd.DataFrame({'col':[1,2,3,4,5]})
        return self.data_dict