"""aiolibrenms devices api."""

from ..api import LibrenmsSubApi
from .models import LibrenmsDeviceInfo


class LibrenmsDevices(LibrenmsSubApi):
    """Librenms devices api."""

    async def async_get_devices(self) -> list[LibrenmsDeviceInfo]:
        """Get all devices.

        Returns:
            list of all device infos as `list[LibrenmsDeviceInfo]`
        """
        result = await self.api.async_do_request("devices")
        assert isinstance(result, dict)
        return [LibrenmsDeviceInfo.from_dict(device) for device in result["devices"]]

    async def async_get_device(self, device_id: str) -> LibrenmsDeviceInfo:
        """Get device information.

        Args:
            device_id (str): id of hostname of the device to be fetched

        Returns:
            device info as `LibrenmsDeviceInfo`
        """
        result = await self.api.async_do_request(f"devices/{device_id}")
        assert isinstance(result, dict)
        return LibrenmsDeviceInfo.from_dict(result["devices"][0])
