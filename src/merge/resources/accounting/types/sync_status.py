# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .selective_sync_configurations_usage_enum import SelectiveSyncConfigurationsUsageEnum
from .sync_status_status_enum import SyncStatusStatusEnum


class SyncStatus(pydantic.BaseModel):
    """
    # The SyncStatus Object
    ### Description
    The `SyncStatus` object is used to represent the syncing state of an account

    ### Usage Example
    View the `SyncStatus` for an account to see how recently its models were synced.
    """

    model_name: str
    model_id: str
    last_sync_start: typing.Optional[str]
    next_sync_start: typing.Optional[str]
    status: SyncStatusStatusEnum
    is_initial_sync: bool
    selective_sync_configurations_usage: typing.Optional[SelectiveSyncConfigurationsUsageEnum]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
