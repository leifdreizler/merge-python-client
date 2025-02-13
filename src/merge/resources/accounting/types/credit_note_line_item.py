# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime


class CreditNoteLineItem(pydantic.BaseModel):
    item: typing.Optional[str]
    name: typing.Optional[str] = pydantic.Field(description="The credit note line item's name.")
    description: typing.Optional[str] = pydantic.Field(description="The description of the item that is owed.")
    quantity: typing.Optional[str] = pydantic.Field(description="The credit note line item's quantity.")
    memo: typing.Optional[str] = pydantic.Field(description="The credit note line item's memo.")
    unit_price: typing.Optional[str] = pydantic.Field(description="The credit note line item's unit price.")
    tax_rate: typing.Optional[str] = pydantic.Field(description="The credit note line item's tax rate.")
    total_line_amount: typing.Optional[str] = pydantic.Field(description="The credit note line item's total.")
    tracking_category: typing.Optional[str] = pydantic.Field(
        description="The credit note line item's associated tracking category."
    )
    tracking_categories: typing.List[str] = pydantic.Field(
        description="The credit note line item's associated tracking categories."
    )
    account: typing.Optional[str] = pydantic.Field(description="The credit note line item's account.")
    company: typing.Optional[str] = pydantic.Field(description="The company the credit note belongs to.")
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    modified_at: typing.Optional[str] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
