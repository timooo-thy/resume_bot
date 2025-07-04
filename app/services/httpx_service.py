import httpx


class HTTPXService:
    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    async def get(self, url: str, params: dict = {}) -> httpx.Response:
        response = await self.client.get(url, params=params)
        response.raise_for_status()
        return response

    async def post(self, url: str, data: dict = {}) -> httpx.Response:
        response = await self.client.post(url, json=data)
        response.raise_for_status()
        return response

    async def put(self, url: str, data: dict = {}) -> httpx.Response:
        response = await self.client.put(url, json=data)
        response.raise_for_status()
        return response

    async def delete(self, url: str) -> httpx.Response:
        response = await self.client.delete(url)
        response.raise_for_status()
        return response
