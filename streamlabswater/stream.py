from urllib.parse import urljoin
import requests
import os
import datetime

class Stream(object):
    __STREAMLABSWATER_API_HOST = ""

    def __init__(self, api_key: str = None, api_host:str = None):
        api_key= api_key or os.environ.get('STREAMLABSWATER_API_KEY')

        if api_key is None:
            raise ValueError('api_key is required')

        self.__STREAMLABSWATER_API_HOST = (api_host or os.environ.get('__STREAMLABSWATER_API_HOST', 'https://dev-api.streamlabswater.com'))

        self.__headers = {
            "Authorization" : "Bearer {}".format(api_key),
            "Content-Type" : "application/json"
        }

    def get_locations(self) -> dict:
        """Retrieves information for all locations

        :return: dictionary containing information for all locations
        """
        url = urljoin(self.__STREAMLABSWATER_API_HOST,'v1/locations')
        return requests.get(url, headers=self.__headers).json()

    def get_location(self, location_id: str) -> dict:
        """Retrieves information for a specific location

        :param location_id: id of location to retrieve
        :return: dictionary containing information for the specified location
        """

        if location_id is None:
            raise ValueError('location_id is required')

        url = urljoin(self.__STREAMLABSWATER_API_HOST, 'v1/locations/{}'.format(location_id))

        return requests.get(url, headers=self.__headers).json()

    def update_location(self, location_id: str, params: dict) -> dict:
        """Updates home/away state of location

        :param location_id: id of location to update
        :param params: dictionary settings that contain the  homeAway mode. home to indicate location is occupied, away to indicate it is vacant
        :return: dictionary containing updated information for the specified location
        """
        if location_id is None:
            raise ValueError('location_id is required')

        if 'homeAway' not in params:
            raise ValueError("Invalid homeAway setting")

        url = urljoin(self.__STREAMLABSWATER_API_HOST, 'v1/locations/{}'.format(location_id))

        return requests.put(url, json=params, headers=self.__headers).json()

    def subscribe_to_location_alerts(self, location_id: str, endpoint: str) -> dict:
        """Subscribes to a locations alerts

        :param location_id: id of location to update
        :param endpoint: a url to send the alerts to
        :return: dictionary containing subscription information for the specified location
        """
        if location_id is None:
            raise ValueError('location_id is required')

        if endpoint is None:
            raise ValueError("endpoint is required")

        url = urljoin(self.__STREAMLABSWATER_API_HOST, 'v1/locations/{}/subscriptions'.format(location_id))

        return requests.post(url, json={"endpoint": endpoint}, headers=self.__headers).json()

    def get_location_subscriptions(self, location_id: str) -> dict:
        """Retrieves information for a specific location

        :param location_id: id of location to retrieve
        :return: dictionary containing all the subscriptions for the specified location
        """

        if location_id is None:
            raise ValueError('location_id is required')

        url = urljoin(self.__STREAMLABSWATER_API_HOST, 'v1/locations/{}/subscriptions'.format(location_id))

        return requests.get(url, headers=self.__headers).json()

    def get_location_water_usage_summary(self, location_id: str) -> dict:
        """Retrieves water usage summary for the location

        :param location_id: id of location to retrieve usage for
        :return: dictionary containing usage in gallons for the current day, month, and year
        """

        if location_id is None:
            raise ValueError('location_id is required')

        url = urljoin(self.__STREAMLABSWATER_API_HOST, 'v1/locations/{}/readings/water-usage/summary'.format(location_id))

        return requests.get(url, headers=self.__headers).json()

    def get_location_water_usage(self, location_id: str, params: dict) -> dict:
        """Retrieves water usage readings for the location

        :param location_id: id of location to retrieve usage for
        :param params: dictionary containing startTime, endTime, groupBy,  page and perPage options. Only startTime is required
        :return: dictionary containing usage in gallons for the current day, month, and year
        """

        if location_id is None:
            raise ValueError('location_id is required')

        if 'startTime' not in params:
            raise ValueError("startTime in params is required")

        start_time = params.get('startTime').isoformat()
        url = urljoin(self.__STREAMLABSWATER_API_HOST, 'v1/locations/{}/readings/water-usage?startTime={}'
                      .format(location_id, start_time+'Z'))
        print(url)

        return requests.get(url, headers=self.__headers).json()
