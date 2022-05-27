# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""Context Providers Subpackage."""
from typing import Any

# flake8: noqa: F403
from ..common.utility import ImportPlaceholder
from .geoip import GeoLiteLookup, IPStackLookup
from .tilookup import TILookup

vtlookupv3: Any
try:
    import vt

    from .vtlookupv3 import vtlookupv3
except ImportError:
    # vtlookup3 will not load if vt package not installed
    vtlookupv3 = ImportPlaceholder(  # type: ignore
        "vtlookupv3", ["vt-py", "vt-graph-api", "nest_asyncio"]
    )