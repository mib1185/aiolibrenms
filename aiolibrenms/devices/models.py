"""aiolibrenms devices models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from mashumaro import field_options
from mashumaro.mixins.json import DataClassJSONMixin


@dataclass
class LibrenmsDeviceInfo(DataClassJSONMixin):
    """Representation of the librenms device information."""

    # non-default fields
    device_id: int
    inserted: datetime
    hostname: str
    sys_name: str = field(metadata=field_options(alias="sysName"))
    display: str
    ip: str
    community: str
    snmpver: str
    port: int
    transport: str
    snmp_disable: bool
    sys_object_id: str = field(metadata=field_options(alias="sysObjectID"))
    sys_descr: str = field(metadata=field_options(alias="sysDescr"))
    sys_contact: str = field(metadata=field_options(alias="sysContact"))
    version: str
    hardware: str
    features: str
    os: str
    status: bool
    status_reason: str
    ignore: bool
    disabled: bool
    agent_uptime: int
    last_polled: datetime
    last_polled_timetaken: float
    last_discovered_timetaken: float
    type: str
    icon: str
    poller_group: int
    override_sys_location: bool = field(
        metadata=field_options(alias="override_sysLocation")
    )
    port_association_mode: int
    max_depth: int
    disable_notify: bool
    ignore_status: bool
    mtu_status: bool

    # default fields
    display_template: str | None = field(default=None)
    overwrite_ip: str | None = field(default=None)
    authlevel: str | None = field(default=None)
    authname: str | None = field(default=None)
    authpass: str | None = field(default=None)
    authalgo: str | None = field(default=None)
    cryptopass: str | None = field(default=None)
    cryptoalgo: str | None = field(default=None)
    location_id: int | None = field(default=None)
    uptime: int | None = field(default=None)
    timeout: str | None = field(default=None)
    retries: str | None = field(default=None)
    bgp_local_as: str | None = field(
        default=None, metadata=field_options(alias="bgpLocalAs")
    )
    snmp_engine_id: str | None = field(
        default=None, metadata=field_options(alias="snmpEngineID")
    )
    last_poll_attempted: datetime | None = field(default=None)
    last_discovered: datetime | None = field(default=None)
    last_ping: datetime | None = field(default=None)
    last_ping_timetaken: float | None = field(default=None)
    purpose: str | None = field(default=None)
    serial: str | None = field(default=None)
    notes: str | None = field(default=None)
    dependency_parent_id: str | None = field(default=None)
    dependency_parent_hostname: str | None = field(default=None)
    location: str | None = field(default=None)
    lat: float | None = field(default=None)
    lng: float | None = field(default=None)
