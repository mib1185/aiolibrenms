"""aiolibrenms alerts api."""

from collections.abc import Iterable

from ..api import LibrenmsSubApi
from .models import OPEN_ALERT_STATES, LibrenmsAlert, LibrenmsAlertState


class LibrenmsAlerts(LibrenmsSubApi):
    """Librenms alerts api."""

    async def async_get_alerts(
        self, states: Iterable[LibrenmsAlertState] = OPEN_ALERT_STATES
    ) -> list[LibrenmsAlert]:
        """Get alerts.

        Without a state, librenms returns only active alerts, so an alert
        that gets acknowledged would look recovered. By default all open
        states are fetched.

        Args:
            states (Iterable[LibrenmsAlertState]): states of the alerts to be fetched

        Returns:
            list of all matching alerts as `list[LibrenmsAlert]`
        """
        result = await self.api.async_do_request(
            "alerts", params={"state": ",".join(str(int(state)) for state in states)}
        )
        assert isinstance(result, dict)
        return [LibrenmsAlert.from_dict(alert) for alert in result["alerts"]]
