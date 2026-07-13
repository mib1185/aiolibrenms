"""aiolibrenms exceptions."""

from __future__ import annotations


class LibrenmsError(Exception):
    """Base class for librenms errors."""


class LibrenmsUnauthenticatedError(LibrenmsError):
    """Unauthenticated error."""


class LibrenmsForbiddenError(LibrenmsError):
    """Forbidden error."""


class LibrenmsFoundError(LibrenmsError):
    """Not found error."""
