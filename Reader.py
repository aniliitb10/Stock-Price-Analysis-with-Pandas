import pandas as pd
from Params import Params


class Reader:
    def __init__(self, file_name, ignore_index=1):
        self.file_name = file_name
        self.file_data = pd.read_excel(self.file_name)
        self.data = pd.DataFrame()
        self.ignore_index = ignore_index
        self.int_cols = [Params.OpenInterest, Params.ChangeInOpenInterest, Params.Volume, Params.BidQuantity, Params.OfferQuantity]
        for e in Params:
            if e in self.int_cols:
                self.indexing_data(e, converter=Reader.ig_then_to_int)
            else:
                self.indexing_data(e, converter=Reader.ig_then_to_float)

    def indexing_data(self, attribute: Params, converter):
        self.data[attribute.name] = converter(self.file_data[self.file_data.columns[attribute.value]],
                                              self.ignore_index)

    def get_data(self):
        return self.data

    @staticmethod
    def ig_then_to_float(values, index=1):
        return [0 if v == '-' else float(v) for v in values[index:]]

    @staticmethod
    def ig_then_to_int(values, index=1):
        return [0 if v == '-' else int(v) for v in values[index:]]
