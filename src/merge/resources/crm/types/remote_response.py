# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .response_type_enum import ResponseTypeEnum


class RemoteResponse(pydantic.BaseModel):
    """
    # The RemoteResponse Object
    ### Description
    The `RemoteResponse` object is used to represent information returned from a third-party endpoint.

    ### Usage Example
    View the `RemoteResponse` returned from your `DataPassthrough`.
    """

    method: str
    path: str
    status: int
    response: typing.Any
    response_headers: typing.Optional[typing.Dict[str, typing.Any]]
    response_type: typing.Optional[ResponseTypeEnum]
    headers: typing.Optional[typing.Dict[str, typing.Any]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
