import requests
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url='https://api.sheety.co/10e7da43b8c7170ba5a3dc4cd343997a/flightDeals/prices')
        data = response.json()
        response.raise_for_status()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint().
        # pprint(data)
        return self.destination_data

    def update_destination_codes(self,updated):

        for new_code in updated:
            PUT_REQUEST_URL = f'https://api.sheety.co/10e7da43b8c7170ba5a3dc4cd343997a/flightDeals/prices/{new_code["id"]}'
            parameters = {
            "price": {
                'city':new_code['city'],
                'iata code':new_code['iataCode'],
                'lowest price':['lowestprice']
                }
            }
            final = requests.put(url=PUT_REQUEST_URL,json=parameters)
            final.raise_for_status()
            print(final.text)

    #HOW IT SHOULD HAVE BEEN
    # def update_destination_codes(self):
    #     for city in self.destination_data:
    #         new_data = {
    #             "price": {
    #                 "iataCode": city["iataCode"]
    #             }
    #         }
    #         response = requests.put(
    #             url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
    #             json=new_data
    #         )
    #         print(response.text)


