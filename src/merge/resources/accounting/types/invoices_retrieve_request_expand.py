# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InvoicesRetrieveRequestExpand(str, enum.Enum):
    COMPANY = "company"
    CONTACT = "contact"
    CONTACT_COMPANY = "contact,company"
    LINE_ITEMS = "line_items"
    LINE_ITEMS_COMPANY = "line_items,company"
    LINE_ITEMS_CONTACT = "line_items,contact"
    LINE_ITEMS_CONTACT_COMPANY = "line_items,contact,company"
    LINE_ITEMS_TRACKING_CATEGORIES = "line_items,tracking_categories"
    LINE_ITEMS_TRACKING_CATEGORIES_COMPANY = "line_items,tracking_categories,company"
    LINE_ITEMS_TRACKING_CATEGORIES_CONTACT = "line_items,tracking_categories,contact"
    LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_COMPANY = "line_items,tracking_categories,contact,company"
    PAYMENTS = "payments"
    PAYMENTS_COMPANY = "payments,company"
    PAYMENTS_CONTACT = "payments,contact"
    PAYMENTS_CONTACT_COMPANY = "payments,contact,company"
    PAYMENTS_LINE_ITEMS = "payments,line_items"
    PAYMENTS_LINE_ITEMS_COMPANY = "payments,line_items,company"
    PAYMENTS_LINE_ITEMS_CONTACT = "payments,line_items,contact"
    PAYMENTS_LINE_ITEMS_CONTACT_COMPANY = "payments,line_items,contact,company"
    PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES = "payments,line_items,tracking_categories"
    PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_COMPANY = "payments,line_items,tracking_categories,company"
    PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_CONTACT = "payments,line_items,tracking_categories,contact"
    PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_COMPANY = "payments,line_items,tracking_categories,contact,company"
    PAYMENTS_TRACKING_CATEGORIES = "payments,tracking_categories"
    PAYMENTS_TRACKING_CATEGORIES_COMPANY = "payments,tracking_categories,company"
    PAYMENTS_TRACKING_CATEGORIES_CONTACT = "payments,tracking_categories,contact"
    PAYMENTS_TRACKING_CATEGORIES_CONTACT_COMPANY = "payments,tracking_categories,contact,company"
    TRACKING_CATEGORIES = "tracking_categories"
    TRACKING_CATEGORIES_COMPANY = "tracking_categories,company"
    TRACKING_CATEGORIES_CONTACT = "tracking_categories,contact"
    TRACKING_CATEGORIES_CONTACT_COMPANY = "tracking_categories,contact,company"

    def visit(
        self,
        company: typing.Callable[[], T_Result],
        contact: typing.Callable[[], T_Result],
        contact_company: typing.Callable[[], T_Result],
        line_items: typing.Callable[[], T_Result],
        line_items_company: typing.Callable[[], T_Result],
        line_items_contact: typing.Callable[[], T_Result],
        line_items_contact_company: typing.Callable[[], T_Result],
        line_items_tracking_categories: typing.Callable[[], T_Result],
        line_items_tracking_categories_company: typing.Callable[[], T_Result],
        line_items_tracking_categories_contact: typing.Callable[[], T_Result],
        line_items_tracking_categories_contact_company: typing.Callable[[], T_Result],
        payments: typing.Callable[[], T_Result],
        payments_company: typing.Callable[[], T_Result],
        payments_contact: typing.Callable[[], T_Result],
        payments_contact_company: typing.Callable[[], T_Result],
        payments_line_items: typing.Callable[[], T_Result],
        payments_line_items_company: typing.Callable[[], T_Result],
        payments_line_items_contact: typing.Callable[[], T_Result],
        payments_line_items_contact_company: typing.Callable[[], T_Result],
        payments_line_items_tracking_categories: typing.Callable[[], T_Result],
        payments_line_items_tracking_categories_company: typing.Callable[[], T_Result],
        payments_line_items_tracking_categories_contact: typing.Callable[[], T_Result],
        payments_line_items_tracking_categories_contact_company: typing.Callable[[], T_Result],
        payments_tracking_categories: typing.Callable[[], T_Result],
        payments_tracking_categories_company: typing.Callable[[], T_Result],
        payments_tracking_categories_contact: typing.Callable[[], T_Result],
        payments_tracking_categories_contact_company: typing.Callable[[], T_Result],
        tracking_categories: typing.Callable[[], T_Result],
        tracking_categories_company: typing.Callable[[], T_Result],
        tracking_categories_contact: typing.Callable[[], T_Result],
        tracking_categories_contact_company: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoicesRetrieveRequestExpand.COMPANY:
            return company()
        if self is InvoicesRetrieveRequestExpand.CONTACT:
            return contact()
        if self is InvoicesRetrieveRequestExpand.CONTACT_COMPANY:
            return contact_company()
        if self is InvoicesRetrieveRequestExpand.LINE_ITEMS:
            return line_items()
        if self is InvoicesRetrieveRequestExpand.LINE_ITEMS_COMPANY:
            return line_items_company()
        if self is InvoicesRetrieveRequestExpand.LINE_ITEMS_CONTACT:
            return line_items_contact()
        if self is InvoicesRetrieveRequestExpand.LINE_ITEMS_CONTACT_COMPANY:
            return line_items_contact_company()
        if self is InvoicesRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES:
            return line_items_tracking_categories()
        if self is InvoicesRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_COMPANY:
            return line_items_tracking_categories_company()
        if self is InvoicesRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_CONTACT:
            return line_items_tracking_categories_contact()
        if self is InvoicesRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_COMPANY:
            return line_items_tracking_categories_contact_company()
        if self is InvoicesRetrieveRequestExpand.PAYMENTS:
            return payments()
        if self is InvoicesRetrieveRequestExpand.PAYMENTS_COMPANY:
            return payments_company()
        if self is InvoicesRetrieveRequestExpand.PAYMENTS_CONTACT:
            return payments_contact()
        if self is InvoicesRetrieveRequestExpand.PAYMENTS_CONTACT_COMPANY:
            return payments_contact_company()
        if self is InvoicesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS:
            return payments_line_items()
        if self is InvoicesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_COMPANY:
            return payments_line_items_company()
        if self is InvoicesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_CONTACT:
            return payments_line_items_contact()
        if self is InvoicesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_CONTACT_COMPANY:
            return payments_line_items_contact_company()
        if self is InvoicesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES:
            return payments_line_items_tracking_categories()
        if self is InvoicesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_COMPANY:
            return payments_line_items_tracking_categories_company()
        if self is InvoicesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_CONTACT:
            return payments_line_items_tracking_categories_contact()
        if self is InvoicesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_COMPANY:
            return payments_line_items_tracking_categories_contact_company()
        if self is InvoicesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES:
            return payments_tracking_categories()
        if self is InvoicesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES_COMPANY:
            return payments_tracking_categories_company()
        if self is InvoicesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES_CONTACT:
            return payments_tracking_categories_contact()
        if self is InvoicesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES_CONTACT_COMPANY:
            return payments_tracking_categories_contact_company()
        if self is InvoicesRetrieveRequestExpand.TRACKING_CATEGORIES:
            return tracking_categories()
        if self is InvoicesRetrieveRequestExpand.TRACKING_CATEGORIES_COMPANY:
            return tracking_categories_company()
        if self is InvoicesRetrieveRequestExpand.TRACKING_CATEGORIES_CONTACT:
            return tracking_categories_contact()
        if self is InvoicesRetrieveRequestExpand.TRACKING_CATEGORIES_CONTACT_COMPANY:
            return tracking_categories_contact_company()
