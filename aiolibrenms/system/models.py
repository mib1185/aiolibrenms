"""aiolibrenms system models."""

from __future__ import annotations

from dataclasses import dataclass

from mashumaro.mixins.json import DataClassJSONMixin


@dataclass
class LibrenmsSystemInfo(DataClassJSONMixin):
    """Representation of the librenms system information."""

    # non-default parameters
    local_ver: str
    local_sha: str
    local_date: str
    local_branch: str
    db_schema: str
    php_ver: str
    database_ver: str
    rrdtool_ver: str
    netsnmp_ver: str
