# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ...types.shared import remote_data

__all__ = ["Team"]


class Team(BaseModel):
    description: Optional[str]
    """The team's description."""

    field_mappings: Optional[object]

    id: Optional[str]

    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    name: Optional[str]
    """The team's name."""

    parent_team: Optional[str]
    """The team's parent team."""

    remote_data: Optional[List[remote_data.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""
