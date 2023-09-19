import requests


ECOSCORE_GRADE = 'd'
STATUS_CODE_200 = 200


def mock_openfoodfact_success(self, method, url):
    def monkey_json():
        return {
            'product': {
                'ecoscore_grade': ECOSCORE_GRADE,
            },
        }

    response = requests.Response()
    response.status_code = STATUS_CODE_200
    response.json = monkey_json

    return response

