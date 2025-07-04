import httpx
from typing import Optional, Dict


class HTTPXService:
    def __init__(self, client: httpx.AsyncClient):
        """
        Initialises the HTTPXService with an async HTTP client.
        Args:
            client (httpx.AsyncClient): An instance of httpx.AsyncClient for making HTTP requests.
        """
        self.client = client

    async def get(self, url: str, params: Optional[Dict] = {}) -> httpx.Response:
        """
        Make an asynchronous GET request to the specified URL with optional parameters.

        Args:
            url (str): The URL to send the GET request to.
            params (Optional[Dict]): Optional dictionary of query parameters to include in the request.

        Returns:
            httpx.Response: The response object containing the server's response to the HTTP request.
        """
        response = await self.client.get(url, params=params)
        response.raise_for_status()
        return response

    async def post(self, url: str, data: Optional[Dict] = {}) -> httpx.Response:
        """
        Make an asynchronous POST request to the specified URL with optional data.

        Args:
            url (str): The URL to send the POST request to.
            data (Optional[Dict]): Optional dictionary of data to include in the request body.

        Returns:
            httpx.Response: The response object containing the server's response to the HTTP request.
        """
        response = await self.client.post(url, json=data)
        response.raise_for_status()
        return response

    async def put(self, url: str, data: Optional[Dict] = {}) -> httpx.Response:
        """
        Make an asynchronous PUT request to the specified URL with optional data.

        Args:
            url (str): The URL to send the PUT request to.
            data (Optional[Dict]): Optional dictionary of data to include in the request body.

        Returns:
            httpx.Response: The response object containing the server's response to the HTTP request.
        """
        response = await self.client.put(url, json=data)
        response.raise_for_status()
        return response

    async def delete(self, url: str) -> httpx.Response:
        """
        Make an asynchronous DELETE request to the specified URL.

        Args:
            url (str): The URL to send the DELETE request to.

        Returns:
            httpx.Response: The response object containing the server's response to the HTTP request.
        """
        response = await self.client.delete(url)
        response.raise_for_status()
        return response
