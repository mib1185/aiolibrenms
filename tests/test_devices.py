"""Tests for aiolibrenms."""

from __future__ import annotations

import json
import logging

import pytest
from syrupy.assertion import SnapshotAssertion

from aiolibrenms.devices.models import LibrenmsDeviceInfo

from .const import MOCK_DATA


async def test_get_devices(mock_librenms_with_data, snapshot: SnapshotAssertion):
    """Test async_get_devices."""
    api = await mock_librenms_with_data()
    devices = await api.devices.async_get_devices()
    assert len(devices) == 8
    assert devices == snapshot


async def test_get_devices_skips_unparsable(
    mock_librenms_with_data, caplog: pytest.LogCaptureFixture
):
    """Test async_get_devices skips devices which can not be parsed."""
    api = await mock_librenms_with_data()
    with caplog.at_level(logging.ERROR):
        devices = await api.devices.async_get_devices()

    assert [device.device_id for device in devices] == [29, 3, 25, 13, 1, 5, 2, 42]
    assert "Skipping device 43 (192.168.100.43)" in caplog.text
    assert "Skipping device 44 (192.168.100.44)" in caplog.text


async def test_get_devices_with_null_fields(mock_librenms_with_data):
    """Test async_get_devices with a device where all nullable fields are NULL."""
    api = await mock_librenms_with_data()
    devices = await api.devices.async_get_devices()

    device = next(device for device in devices if device.device_id == 42)
    assert device.hardware is None
    assert device.inserted is None
    assert device.ip is None
    assert device.last_discovered_timetaken is None
    assert device.last_polled is None
    assert device.last_polled_timetaken is None
    assert device.os is None
    assert device.override_sys_location is None
    assert device.sys_name is None


def test_device_of_old_librenms_instance():
    """Test parsing a device of a librenms instance without mtu_status."""
    raw_device = json.loads(MOCK_DATA["devices/13"]["body"])["devices"][0]
    del raw_device["mtu_status"]

    device = LibrenmsDeviceInfo.from_dict(raw_device)
    assert device.mtu_status is None


async def test_get_device(mock_librenms_with_data, snapshot: SnapshotAssertion):
    """Test async_get_device."""
    api = await mock_librenms_with_data()
    device = await api.devices.async_get_device("13")
    assert isinstance(device, LibrenmsDeviceInfo)
    assert device == snapshot
