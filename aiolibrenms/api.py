"""aiolibrenms api."""

from __future__ import annotations

from aiohttp import StreamReader
from aiohttp.client import ClientSession

from .const import CONNECT_ERRORS, LOGGER
from .exceptions import (
    LibrenmsError,
    LibrenmsForbiddenError,
    LibrenmsFoundError,
    LibrenmsUnauthenticatedError,
)


class LibrenmsApi:
    """librenms api."""

    def __init__(
        self,
        aiohttp_session: ClientSession,
        api_key: str,
        host: str,
        port: int = 443,
        use_ssl: bool = True,
    ) -> None:
        """Librenms api init."""
        self.session: ClientSession = aiohttp_session
        self.api_key = api_key
        self.base_url = f"{'https' if use_ssl else 'http'}://{host}:{port}/api/v0"

    async def async_do_request(
        self,
        end_point: str,
        params: dict | None = None,
        data: dict | None = None,
        raw_data: dict | None = None,
        method: str = "GET",
    ) -> list | dict | bytes | StreamReader | None:
        """Perform the request and handle errors."""
        headers = {"X-Auth-Token": self.api_key}
        url = f"{self.base_url}/{end_point}"

        LOGGER.debug(
            "REQUEST url: %s params: %s data: %s headers: %s",
            url,
            params,
            data,
            {**headers, "X-Auth-Token": "**********"},
        )

        try:
            resp = await self.session.request(
                method, url, params=params, json=data, data=raw_data, headers=headers
            )
            LOGGER.debug("RESPONSE headers: %s", dict(resp.headers))

            if 200 <= resp.status < 300:
                result = await resp.json()
                LOGGER.debug("RESPONSE: %s", result)
                return result

            err_result = await resp.json()
            LOGGER.debug("RESPONSE %s", err_result)

            err_msg = err_result["message"]
            if resp.status == 400:
                raise LibrenmsError(err_msg)
            if resp.status == 401:
                raise LibrenmsUnauthenticatedError(err_msg)
            if resp.status == 403:
                raise LibrenmsForbiddenError(err_msg)
            if resp.status == 404:
                raise LibrenmsFoundError(err_msg)
            return resp.raise_for_status()

        except CONNECT_ERRORS as err:
            LOGGER.debug("connection error", exc_info=True)
            LOGGER.error(
                "Error while getting data: %s: %s",
                err.__class__.__name__,
                err.__class__.__cause__,
            )
            raise err


class LibrenmsSubApi:
    """librenms sub api."""

    def __init__(self, api: LibrenmsApi) -> None:
        """Librenms sub api init."""
        self.api = api
