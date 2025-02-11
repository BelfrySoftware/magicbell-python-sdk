import httpx
import pytest

from belfry_magicbell import MagicBell
from belfry_magicbell.configuration import Configuration
from tests.mock_server import api_key, api_secret, app, user_jwt


@pytest.fixture()
def configuration():
    """A configuration object with the default values."""

    return Configuration(
        api_key=api_key,
        api_secret=api_secret,
        user_jwt=user_jwt,
    )


@pytest.fixture()
async def magicbell_client(configuration: Configuration):
    """Async HTTP client for testing the MagicBell API clients against a mock ASGI server."""

    transport = httpx.ASGITransport(app=app)
    httpx_client = httpx.AsyncClient(transport=transport, base_url="http://test")
    async with MagicBell(configuration=configuration, http_client=httpx_client) as mb:
        yield mb
