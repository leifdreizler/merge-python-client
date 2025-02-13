# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EmploymentStatusEnum(str, enum.Enum):
    """
    * `ACTIVE` - ACTIVE
    * `PENDING` - PENDING
    * `INACTIVE` - INACTIVE
    """

    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    INACTIVE = "INACTIVE"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmploymentStatusEnum.ACTIVE:
            return active()
        if self is EmploymentStatusEnum.PENDING:
            return pending()
        if self is EmploymentStatusEnum.INACTIVE:
            return inactive()
