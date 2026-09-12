"""aiolibrenms devices api."""

from mashumaro.exceptions import InvalidFieldValue, MissingField

from ..api import LibrenmsSubApi
from ..const import LOGGER
from .models import LibrenmsDeviceInfo


class LibrenmsDevices(LibrenmsSubApi):
    """Librenms devices api."""

    async def async_get_devices(self) -> list[LibrenmsDeviceInfo]:
        """Get all devices.

        Devices which can not be parsed are logged and skipped, so a single
        broken device does not fail the whole request.

        Returns:
            list of all device infos as `list[LibrenmsDeviceInfo]`
        """
        result = await self.api.async_do_request("devices")
        assert isinstance(result, dict)
        devices: list[LibrenmsDeviceInfo] = []
        for device in result["devices"]:
            try:
                devices.append(LibrenmsDeviceInfo.from_dict(device))
            except (InvalidFieldValue, MissingField) as err:
                LOGGER.error(
                    "Skipping device %s (%s), could not parse api response: %s",
                    device.get("device_id"),
                    device.get("hostname"),
                    err,
                )
                LOGGER.debug("unparsable device: %s", device)
        return devices

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
