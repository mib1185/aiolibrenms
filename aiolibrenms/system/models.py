"""aiolibrenms system models."""

from __future__ import annotations

from dataclasses import dataclass

from mashumaro.mixins.json import DataClassJSONMixin


@dataclass
class LibrenmsSystemInfo(DataClassJSONMixin):
    """Representation of the librenms system information."""

    # non-default parameters
    database_ver: str
    db_schema: str
    local_branch: str
    local_date: str
    local_sha: str
    local_ver: str
    netsnmp_ver: str
    php_ver: str
    python_ver: str
    rrdtool_ver: str
