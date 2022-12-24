from src.backend.constants import ENDPOINTS, SEX, ERROR_MESSAGES
import pytest

"""
Validating API Response Data
"""


### MARATHON ENDPOINT TESTS ###
def test_marathons_endpoint(test_client):
    """
    GIVEN an AthleteService class
    WHEN get_all is called
    THEN return 1250 athletes (sample population)
    """
    response = test_client.get(ENDPOINTS.MARATHONS.value)
    response_json = response.get_json()
    assert response_json[0]["year"] == 2021
    assert response_json[0]["num_athletes"] == 33543
    assert response_json[0]["num_athletes_female"] == 11876
    assert response_json[0]["num_athletes_male"] == 14202
    assert len(response_json) == 25
    assert response.status_code == 200


@pytest.mark.parametrize(
    "input, output",
    [
        (
            "2012",
            {
                "id": 9.0,
                "num_athletes": 37505.0,
                "num_athletes_female": 16792.0,
                "num_athletes_male": 20681.0,
                "year": 2012.0,
            },
        ),
        ("2030", {"Error": "Invalid year, please try again."}),
    ],
)
def test_marathon_get_by_year_endpoint(test_client, input, output):
    """
    GIVEN a GET request to /marathon/<year>
    WHEN api is called
    THEN return marathon for that year
    """
    response = test_client.get(ENDPOINTS.MARATHONS.value + input)
    response_json = response.get_json()
    print(response_json)
    assert response_json == output
    assert response.status_code == 200


### athlete endpoint tests ###
def test_athletes_endpoint(test_client):
    """
    given a get request to /athletes endpoint
    when api is called
    then return 1250 athletes (sample population)
    """
    response = test_client.get(ENDPOINTS.ATHLETES.value)
    response_json = response.get_json()
    assert response_json[0]["gender"] == 1
    assert response_json[0]["first_name"] == "Tura Abdiwak"
    assert response_json[0]["id"] == 1
    assert len(response_json) == 1250
    assert response.status_code == 200


def test_athletes_get_by_year_endpoint(test_client):
    """
    given a get request to /athletes/<year>
    when api is called
    then return athletes for that year
    """
    response = test_client.get(ENDPOINTS.ATHLETES.value + "2018")
    response_json = response.get_json()
    assert response_json[0]["first_name"] == "Farah"
    assert response_json[0]["gender"] == 1
    assert len(response_json) == 50
    assert response.status_code == 200


def test_athletes_get_by_year_bad_input_endpoint(test_client):
    """
    GIVEN a GET request to /athletes/<year>
    WHEN api is called
    THEN return athletes for that year
    """
    response = test_client.get(ENDPOINTS.ATHLETES.value + "203123120")
    response_json = response.get_json()
    assert response_json == {"Error": "Invalid year, please try again."}
    assert response.status_code == 200

### RESULT ENDPOINT TESTS ###

def test_results_get_by_year(test_client):
    """
    GIVEN a GET request to /results/<year>
    WHEN api is called
    THEN return results for that year
    """
    response = test_client.get(ENDPOINTS.RESULTS.value + "2010")
    response_json = response.get_json()
    assert len(response_json) == 50
    assert response_json[0]['marathon_event']['year'] == 2010
    assert response.status_code == 200


def test_results_get_by_year_male(test_client):
    """
    GIVEN a GET request to /results/<year>/<sex>
    WHEN api is called
    THEN return male results for that year
    """
    response = test_client.get(ENDPOINTS.RESULTS.value + "2010" + '/M')
    response_json = response.get_json()
    assert len(response_json) == 25
    assert response.status_code == 200
    assert response_json[0]['marathon_event']['year'] == 2010
    assert response_json[0]['athlete']['gender'] == SEX.MALE.value


def test_results_get_by_year_female(test_client):
    """
    GIVEN a GET request to /results/<year>/<sex>
    WHEN api is called
    THEN return female results for that year
    """
    response = test_client.get(ENDPOINTS.RESULTS.value + "2010" + '/F')
    response_json = response.get_json()
    assert len(response_json) == 25
    assert response.status_code == 200
    assert response_json[0]['athlete']['gender'] == SEX.FEMALE.value

def test_results_get_by_year_invalid_year(test_client):
    """
    GIVEN a GET request to /results/<year>/<sex>
    WHEN api is called with invalid year
    THEN return error message
    """
    response = test_client.get(ENDPOINTS.RESULTS.value + "2030" + '/F')
    response_json = response.get_json()
    assert response.status_code == 200
    assert response_json['Error'] == ERROR_MESSAGES.INVALID_YEAR.value

def test_results_get_by_year_invalid_sex(test_client):
    """
    GIVEN a GET request to /results/<year>/<sex>
    WHEN api is called with invalid sex
    THEN return error message
    """
    response = test_client.get(ENDPOINTS.RESULTS.value + "2010" + '/W')
    response_json = response.get_json()
    assert response.status_code == 200
    assert response_json['Error'] == ERROR_MESSAGES.INVALID_SEX_INPUT.value