"""aiolibrenms devices models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from mashumaro import field_options
from mashumaro.mixins.json import DataClassJSONMixin


@dataclass
class LibrenmsDeviceInfo(DataClassJSONMixin):
    """Representation of the librenms device information.

    Only fields which are `NOT NULL` in the librenms database schema are
    required, everything else may legitimately be `null` in the api response
    (f.e. `hardware` of a device without snmp support) and therefore is
    optional.
    """

    # non-default fields
    agent_uptime: int
    device_id: int
    disable_notify: bool
    disabled: bool
    display: str
    hostname: str
    ignore_status: bool
    ignore: bool
    max_depth: int
    poller_group: int
    port_association_mode: int
    port: int
    snmp_disable: bool
    snmpver: str
    status_reason: str
    status: bool
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
    hardware: str | None = field(default=None)
    icon: str | None = field(default=None)
    inserted: datetime | None = field(default=None)
    ip: str | None = field(default=None)
    last_discovered_timetaken: float | None = field(default=None)
    last_discovered: datetime | None = field(default=None)
    last_ping_timetaken: float | None = field(default=None)
    last_ping: datetime | None = field(default=None)
    last_poll_attempted: datetime | None = field(default=None)
    last_polled_timetaken: float | None = field(default=None)
    last_polled: datetime | None = field(default=None)
    lat: float | None = field(default=None)
    lng: float | None = field(default=None)
    location_id: int | None = field(default=None)
    location: str | None = field(default=None)
    # mtu_status was added in librenms 25.12 and is missing on older instances
    mtu_status: bool | None = field(default=None)
    notes: str | None = field(default=None)
    os: str | None = field(default=None)
    override_sys_location: bool | None = field(
        default=None, metadata=field_options(alias="override_sysLocation")
    )
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
    sys_name: str | None = field(default=None, metadata=field_options(alias="sysName"))
    sys_object_id: str | None = field(
        default=None, metadata=field_options(alias="sysObjectID")
    )
    timeout: str | None = field(default=None)
    uptime: int | None = field(default=None)
    version: str | None = field(default=None)
