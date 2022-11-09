from src.constants import ENDPOINTS
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
    assert response_json[0]['year'] == 2021
    assert response_json[0]['num_athletes'] == 33543
    assert response_json[0]['num_athletes_female'] == 11876
    assert response_json[0]['num_athletes_male'] == 14202
    assert len(response_json) == 25
    assert response.status_code == 200

### ATHLETE ENDPOINT TESTS ###
def test_athletes_endpoint(test_client):
    """
    GIVEN a GET request to /athletes endpoint
    WHEN api is called
    THEN return 1250 athletes (sample population)
    """
    response = test_client.get(ENDPOINTS.ATHLETES.value)
    response_json = response.get_json()
    assert response_json[0]['gender'] == 1
    assert response_json[0]['name'] == 'Tura Abdiwak, Seifu (ETH)'
    assert response_json[0]['id'] == 1
    assert len(response_json) == 1250
    assert response.status_code == 200

def test_athletes_get_by_year_endpoint(test_client):
    """
    GIVEN a GET request to /athletes/<year> 
    WHEN api is called
    THEN return athletes for that year
    """
    response = test_client.get(ENDPOINTS.ATHLETES.value + '2018')
    response_json = response.get_json()
    print(response_json)
    assert response_json[0]['name'] == 'Farah, Mo (GBR)'
    assert response_json[0]['gender'] == 1
    assert len(response_json) == 50
    assert response.status_code == 200