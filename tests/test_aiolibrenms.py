"""Tests for aiolibrenms."""

from __future__ import annotations

import pytest
from aiohttp import ClientError

from aiolibrenms.exceptions import (
    LibrenmsForbiddenError,
    LibrenmsFoundError,
    LibrenmsUnauthenticatedError,
)


async def test_errors(mock_librenms_with_data):
    """Test api errors."""
    api = await mock_librenms_with_data()

    with pytest.raises(LibrenmsUnauthenticatedError, match="Unauthenticated."):
        await api.devices.async_get_device("INVALID_API_KEY")

    with pytest.raises(
        LibrenmsForbiddenError, match="Insufficient permissions to access this device"
    ):
        await api.devices.async_get_device("FORBIDDEN")

    with pytest.raises(LibrenmsFoundError, match="Device 99 does not exist"):
        await api.devices.async_get_device("NOTFOUND")

    with pytest.raises(ClientError):
        await api.devices.async_get_device("CLIENT_ERROR")
