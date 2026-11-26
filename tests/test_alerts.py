"""Tests for aiolibrenms."""

from __future__ import annotations

from syrupy.assertion import SnapshotAssertion

from aiolibrenms.alerts.models import (
    LibrenmsAlert,
    LibrenmsAlertSeverity,
    LibrenmsAlertState,
)


async def test_get_alerts(mock_librenms_with_data, snapshot: SnapshotAssertion):
    """Test async_get_alerts with the default open states."""
    api = await mock_librenms_with_data()
    alerts = await api.alerts.async_get_alerts()
    assert len(alerts) == 2
    assert all(isinstance(alert, LibrenmsAlert) for alert in alerts)
    assert alerts[0].state is LibrenmsAlertState.ACKNOWLEDGED
    assert alerts[0].severity is LibrenmsAlertSeverity.CRITICAL
    assert alerts == snapshot


async def test_get_alerts_by_state(
    mock_librenms_with_data, snapshot: SnapshotAssertion
):
    """Test async_get_alerts with given states."""
    api = await mock_librenms_with_data()
    alerts = await api.alerts.async_get_alerts([LibrenmsAlertState.ACKNOWLEDGED])
    assert len(alerts) == 1
    assert alerts[0].alert_id == 4
    assert alerts[0].state is LibrenmsAlertState.ACKNOWLEDGED
    assert alerts[0].first_seen is None
    assert alerts == snapshot
