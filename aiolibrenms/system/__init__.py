"""aiolibrenms system api."""

from ..api import LibrenmsSubApi
from .models import LibrenmsSystemInfo


class LibrenmsSystem(LibrenmsSubApi):
    """Librenms system api."""

    async def async_get_system_info(self) -> LibrenmsSystemInfo:
        """Get system info.

        Returns:
            system info as `LibrenmsSystemInfo`
        """
        result = await self.api.async_do_request("system")
        assert isinstance(result, dict)
        return LibrenmsSystemInfo.from_dict(result["system"][0])
