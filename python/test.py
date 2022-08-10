from funding_raised import FundingEvent
import unittest

class FundingEventTests(unittest.TestCase):

    def setUp(self):
        self.file_path = '../startup_funding.csv'
        self.funding_raised = FundingEvent(file_path=self.file_path)

    def test_where_returns_events(self):
        assert len(self.funding_raised.filter_funding_events({'company_name': 'Facebook'})) == 7

    def test_where_returns_correct_keys(self):
        funding_raised = self.funding_raised
        row = funding_raised.filter_funding_events({'company_name': 'Facebook'})[0]
        keys = ['permalink', 'company_name', 'number_employees', 'category', 'city', 'state', 'funded_date', 'raised_amount', 'raised_currency', 'round']
        values = ['facebook', 'Facebook', 450, 'web', 'Palo Alto', 'CA', '1-Sep-04', 500000, 'USD', 'angel']
        for i in range(0, len(keys)):
            assert row[keys[i]] == values[i]

    def test_where_returns_events_by_city(self):
        assert len(self.funding_raised.filter_funding_events({'city': 'Tempe'})) == 3

    def test_where_returns_events_by_state(self):
        assert len(self.funding_raised.filter_funding_events({'state': 'CA'})) == 873

    def test_where_returns_events_by_company(self):
        assert len(self.funding_raised.filter_funding_events({'company_name': 'Facebook', 'round': 'a'})) == 1

    def test_where_returns_events_by_type(self):
        assert len(self.funding_raised.filter_funding_events({'round': 'a'})) == 582

    def test_where_returns_no_events(self):
        assert len(self.funding_raised.filter_funding_events({'company_name': 'NotFacebook'})) == 0

if __name__ == '__main__':
    unittest.main()

    # def test_find_by_event_by_company_name():
    #   row = FundingRaised.find_by({'company_name': 'Facebook'})
    #   keys = ['permalink', 'company_name', 'number_employees', 'category', 'city', 'state', 'funded_date', 'raised_amount', 'raised_currency', 'round']
    #   values = ['facebook', 'Facebook', '450', 'web', 'Palo Alto', 'CA', '1-Sep-04', '500000', 'USD', 'angel']
    #   for i in range(0, len(keys)):
    #     assert row[keys[i]] == values[i]
    #
    # def test_find_by_event_by_state():
    #   row = FundingRaised.find_by({'state': 'CA'})
    #   keys = ['permalink', 'company_name', 'number_employees', 'category', 'city', 'state', 'funded_date', 'raised_amount', 'raised_currency', 'round']
    #   values = ['digg', 'Digg', '60', 'web', 'San Francisco', 'CA', '1-Dec-06', '8500000', 'USD', 'b']
    #   for i in range(0, len(keys)):
    #     assert row[keys[i]] == values[i]

# test_find_by_event_by_company_name()
# test_find_by_event_by_state()
