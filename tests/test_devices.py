"""Tests for aiolibrenms."""

from __future__ import annotations

from syrupy.assertion import SnapshotAssertion

from aiolibrenms.devices.models import LibrenmsDeviceAvailabilities, LibrenmsDeviceInfo


async def test_get_devices(mock_librenms_with_data, snapshot: SnapshotAssertion):
    """Test async_get_devices."""
    api = await mock_librenms_with_data()
    devices = await api.devices.async_get_devices()
    assert len(devices) == 7
    assert devices == snapshot


async def test_get_device(mock_librenms_with_data, snapshot: SnapshotAssertion):
    """Test async_get_device."""
    api = await mock_librenms_with_data()
    device = await api.devices.async_get_device("13")
    assert isinstance(device, LibrenmsDeviceInfo)
    assert device == snapshot


async def test_get_device_with_null_fields(
    mock_librenms_with_data, snapshot: SnapshotAssertion
):
    """Test async_get_device with columns librenms leaves NULL."""
    api = await mock_librenms_with_data()
    device = await api.devices.async_get_device("31")
    assert isinstance(device, LibrenmsDeviceInfo)
    assert device.inserted is None
    assert device.ip is None
    assert device.last_polled is None
    assert device.os is None
    assert device.sys_name is None
    assert device == snapshot


async def test_get_device_availabilities(
    mock_librenms_with_data, snapshot: SnapshotAssertion
):
    """Test async_get_device_availability."""
    api = await mock_librenms_with_data()
    availabilities = await api.devices.async_get_device_availability("13")
    assert isinstance(availabilities, LibrenmsDeviceAvailabilities)
    assert availabilities == snapshot
