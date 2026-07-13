"""Tests for aiolibrenms."""

from __future__ import annotations

from syrupy.assertion import SnapshotAssertion

from aiolibrenms.system.models import LibrenmsSystemInfo


async def test_get_system_info(mock_librenms_with_data, snapshot: SnapshotAssertion):
    """Test async_get_system_info."""
    api = await mock_librenms_with_data()
    systm_info = await api.system.async_get_system_info()

    assert isinstance(systm_info, LibrenmsSystemInfo)
    assert systm_info == snapshot
