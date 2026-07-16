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
    agent_uptime: int
    device_id: int
    disable_notify: bool
    disabled: bool
    display: str
    hardware: str
    hostname: str
    ignore_status: bool
    ignore: bool
    inserted: datetime
    ip: str
    last_discovered_timetaken: float
    last_polled_timetaken: float
    last_polled: datetime
    max_depth: int
    mtu_status: bool
    os: str
    override_sys_location: bool = field(
        metadata=field_options(alias="override_sysLocation")
    )
    poller_group: int
    port_association_mode: int
    port: int
    snmp_disable: bool
    snmpver: str
    status_reason: str
    status: bool
    sys_name: str = field(metadata=field_options(alias="sysName"))
    transport: str
    type: str

    # default fields
    authalgo: str | None = field(default=None)
    authlevel: str | None = field(default=None)
    authname: str | None = field(default=None)
    authpass: str | None = field(default=None)
    bgp_local_as: str | None = field(
        default=None, metadata=field_options(alias="bgpLocalAs")
    )
    community: str | None = field(default=None)
    cryptoalgo: str | None = field(default=None)
    cryptopass: str | None = field(default=None)
    dependency_parent_hostname: str | None = field(default=None)
    dependency_parent_id: str | None = field(default=None)
    display_template: str | None = field(default=None)
    features: str | None = field(default=None)
    icon: str | None = field(default=None)
    last_discovered: datetime | None = field(default=None)
    last_ping_timetaken: float | None = field(default=None)
    last_ping: datetime | None = field(default=None)
    last_poll_attempted: datetime | None = field(default=None)
    lat: float | None = field(default=None)
    lng: float | None = field(default=None)
    location_id: int | None = field(default=None)
    location: str | None = field(default=None)
    notes: str | None = field(default=None)
    overwrite_ip: str | None = field(default=None)
    purpose: str | None = field(default=None)
    retries: str | None = field(default=None)
    serial: str | None = field(default=None)
    snmp_engine_id: str | None = field(
        default=None, metadata=field_options(alias="snmpEngineID")
    )
    sys_contact: str | None = field(
        default=None, metadata=field_options(alias="sysContact")
    )
    sys_descr: str | None = field(
        default=None, metadata=field_options(alias="sysDescr")
    )
    sys_object_id: str | None = field(
        default=None, metadata=field_options(alias="sysObjectID")
    )
    timeout: str | None = field(default=None)
    uptime: int | None = field(default=None)
    version: str | None = field(default=None)
