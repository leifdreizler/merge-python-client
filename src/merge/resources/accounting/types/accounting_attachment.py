# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .remote_data import RemoteData


class AccountingAttachment(pydantic.BaseModel):
    """
    # The Accounting Attachment Object
    ### Description
    The `AccountingAttachment` object is used to represent a company's attachments.

    ### Usage Example
    Fetch from the `LIST AccountingAttachments` endpoint and view a company's attachments.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    file_name: typing.Optional[str] = pydantic.Field(description="The attachment's name.")
    file_url: typing.Optional[str] = pydantic.Field(description="The attachment's url.")
    company: typing.Optional[str] = pydantic.Field(description="The company the accounting attachment belongs to.")
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted by third party webhooks."
    )
    modified_at: typing.Optional[str] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
