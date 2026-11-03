"""Aiolibrenms library."""

from __future__ import annotations

from aiohttp.client import ClientSession

from .alerts import LibrenmsAlerts
from .api import LibrenmsApi
from .devices import LibrenmsDevices
from .system import LibrenmsSystem


class Librenms:
    """Librenms instance."""

    __slots__ = ("alerts", "api", "devices", "system")

    alerts: LibrenmsAlerts
    api: LibrenmsApi
    devices: LibrenmsDevices
    system: LibrenmsSystem

    def __init__(
        self,
        aiohttp_session: ClientSession,
        api_key: str,
        host: str,
        port: int = 443,
        use_ssl: bool = True,
    ) -> None:
        """Librenms instance init."""
        self.api = LibrenmsApi(aiohttp_session, api_key, host, port, use_ssl)

        self.alerts = LibrenmsAlerts(self.api)
        self.devices = LibrenmsDevices(self.api)
        self.system = LibrenmsSystem(self.api)
