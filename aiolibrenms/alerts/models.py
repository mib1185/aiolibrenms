"""aiolibrenms alerts models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import IntEnum, StrEnum

from mashumaro import field_options
from mashumaro.mixins.json import DataClassJSONMixin


class LibrenmsAlertState(IntEnum):
    """Representation of the librenms alert states."""

    RECOVERED = 0
    ACTIVE = 1
    ACKNOWLEDGED = 2
    WORSE = 3
    BETTER = 4
    CHANGED = 5


class LibrenmsAlertSeverity(StrEnum):
    """Representation of the librenms alert rule severities."""

    OK = "ok"
    WARNING = "warning"
    CRITICAL = "critical"


OPEN_ALERT_STATES = (
    LibrenmsAlertState.ACTIVE,
    LibrenmsAlertState.ACKNOWLEDGED,
    LibrenmsAlertState.WORSE,
    LibrenmsAlertState.BETTER,
    LibrenmsAlertState.CHANGED,
)


@dataclass
class LibrenmsAlert(DataClassJSONMixin):
    """Representation of a librenms alert."""

    # non-default fields
    alert_id: int = field(metadata=field_options(alias="id"))
    alerted: int
    device_id: int
    hostname: str
    name: str
    open: int
    rule_id: int
    severity: LibrenmsAlertSeverity
    state: LibrenmsAlertState
    timestamp: datetime

    # default fields
    entity_id: int | None = field(default=None)
    entity_key: str | None = field(default=None)
    entity_type: str | None = field(default=None)
    first_seen: datetime | None = field(default=None)
    last_seen: datetime | None = field(default=None)
    note: str | None = field(default=None)
    notes: str | None = field(default=None)
    proc: str | None = field(default=None)
