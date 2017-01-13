from woocommerce import API


class REQ():
    def __init__(self):
        admin_consumer_key = "ck_0e16ac3057774f660f5b42f5263160033c800d0f"
        admin_consumer_secret = "cs_66019dffbf45add25636913ab54541aaba5100b4"

        self.wcapi = API(
            url="http://127.0.0.1/awstore/",
            consumer_key=admin_consumer_key,
            consumer_secret=admin_consumer_secret
        )

    def test_api(self):
        """

        :return:
        """

        print(self.wcapi.get("").json())

    def post(self, endpoint, data):
        """

        :param endpoint:
        :param data:
        :return:
        """

        result = self.wcapi.post(endpoint, data)

        rs_code = result.response_code
        rs_body = result.json()
        rs_url = result.url

        return [rs_code, rs_body, rs_url]

    def get(self, endpoint):
        """

        :param endpoint:
        :return:
        """

        result = self.wcapi.get(endpoint)

        rs_code = result.response_code
        rs_body = result.json()
        rs_url = result.url

        return [rs_code, rs_body, rs_url]
