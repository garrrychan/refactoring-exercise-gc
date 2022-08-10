from typing import Dict, List, Union
import pandas as pd

class FundingEvent:

    def __init__(self, file_path):
        self.file_path = file_path

    def filter_funding_events(self, filter_dict: Dict, is_first_event: bool) -> Union[List[Dict], Dict]:
        """
        :param filter_dict: Dict where key represents the csv field column and value represents the str
        to filter against. Options are: company_name, city, state, round
        :return: Return funding row events that match the filter dict.
        """
        df = pd.read_csv(self.file_path)
        for key, value in filter_dict.items():
            df = df[df[key] == value]
        return self.format_rows(df, is_first_event)

    def format_rows(self, df: pd.DataFrame, is_first_event: bool) -> Union[List[Dict], Dict]:
        if not is_first_event:
            return df.to_dict('records')
        elif not df.empty:
            return df.head(1).to_dict('records')[0]
        else:
            raise RecordNotFound("This funding event does not exist.")

class RecordNotFound(Exception):
    pass
