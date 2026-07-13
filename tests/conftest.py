"""Test config for aiolibrenms."""

from __future__ import annotations

from collections.abc import AsyncGenerator, Callable, Coroutine
from typing import Any

import aiohttp
import pytest
from aiointercept import aiointercept

from aiolibrenms import Librenms

from .const import MOCK_DATA, MOCK_LNMS_API_KEY, MOCK_LNMS_HOST


class MockLibrenms(Librenms):
    """Librenms test double that allows per-instance overrides."""


@pytest.fixture(name="mock_aiointercept")
async def aiointercept_fixture() -> AsyncGenerator[aiointercept, None]:
    """Mock a web request and provide a response."""
    async with aiointercept(mock_external_urls=True) as m:
        yield m


@pytest.fixture(name="mock_librenms")
async def librenms_fixture() -> AsyncGenerator[MockLibrenms, Any]:
    """Return Librenms session."""
    session = aiohttp.ClientSession()
    lnms = MockLibrenms(session, MOCK_LNMS_API_KEY, MOCK_LNMS_HOST)
    yield lnms
    await session.close()


@pytest.fixture
def mock_librenms_with_data(
    mock_aiointercept: aiointercept, mock_librenms: Librenms
) -> Callable[[], Coroutine[Any, Any, Librenms]]:
    """Comfort fixture to initialize librenms session."""

    async def data_to_librenms() -> Librenms:
        """Initialize librenms session."""
        for path, data in MOCK_DATA.items():
            mock_aiointercept.get(
                f"https://{MOCK_LNMS_HOST}:443/api/v0/{path}",
                status=data["status"],
                body=data["body"],
                exception=data.get("exception"),
                repeat=data.get("repeat", 1),
            )
        return mock_librenms

    return data_to_librenms
