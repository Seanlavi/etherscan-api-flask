from flask_restful import Resource
from flask import make_response, request
import config as conf
from utils import fetch_html, get_html_parser


class Etherscan(Resource):
    """ Etherscan Class """

    def get_etherscan_data(self, address):
        """ for each address get labels and tag """

        # fetch html by url
        html = fetch_html(f'{conf.BASE_URL}/{address}')
        # get parser instance to scrap html
        soup = get_html_parser(html)

        etherscan_labels = []

        for labels in soup.findAll('a', class_='u-label'):
            [etherscan_labels.append(label.get_text()) for label in labels]

        etherscan_tag = soup.find('span', title='Public Name Tag (viewable by anyone)')

        tag = "" if etherscan_tag is None  else etherscan_tag.get_text()

        return {
            "address": address,
            "labels": etherscan_labels,
            "tag": tag
            }


    def get_labels_and_tag(self, eth_addresses_list):
        """ Loop over each address and get labels and tag """
        return [self.get_etherscan_data(eth_address) for eth_address in eth_addresses_list] 

    def post(self):
        """ POST endpoint """

        body = request.get_json()
        # Validate payload
        if not body.get("addresses"):
            return make_response({"message": "You must supply addresses"}, 400)
        if not isinstance(body["addresses"], list):
            return make_response({"message": "Addresses must be list"}, 400)

        # Get tag and labels for each addresses
        etherscan_response = self.get_labels_and_tag(body["addresses"])

        try:
            return make_response(etherscan_response, 200)
        except Exception as e:
            print(f"internal server error {e}")
            return make_response('', 500)