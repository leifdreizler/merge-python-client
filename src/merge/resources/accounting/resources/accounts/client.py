# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic
import typing_extensions

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from .....environment import MergeEnvironment
from ...types.account import Account
from ...types.account_request import AccountRequest
from ...types.account_response import AccountResponse
from ...types.accounts_list_request_remote_fields import AccountsListRequestRemoteFields
from ...types.accounts_list_request_show_enum_origins import AccountsListRequestShowEnumOrigins
from ...types.accounts_retrieve_request_remote_fields import AccountsRetrieveRequestRemoteFields
from ...types.accounts_retrieve_request_show_enum_origins import AccountsRetrieveRequestShowEnumOrigins
from ...types.meta_response import MetaResponse
from ...types.paginated_account_list import PaginatedAccountList

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AccountsClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: SyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        company_id: typing.Optional[str] = None,
        created_after: typing.Optional[str] = None,
        created_before: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[typing_extensions.Literal["company"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[str] = None,
        modified_before: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[AccountsListRequestRemoteFields] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[AccountsListRequestShowEnumOrigins] = None,
    ) -> PaginatedAccountList:
        """
        Returns a list of `Account` objects.

        Parameters:
            - company_id: typing.Optional[str]. If provided, will only return accounts for this company.

            - created_after: typing.Optional[str]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[str]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - expand: typing.Optional[typing_extensions.Literal["company"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - modified_after: typing.Optional[str]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[str]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_fields: typing.Optional[AccountsListRequestRemoteFields]. Deprecated. Use show_enum_origins.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - show_enum_origins: typing.Optional[AccountsListRequestShowEnumOrigins]. Which fields should be returned in non-normalized form.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/accounting/v1/accounts"),
            params=remove_none_from_dict(
                {
                    "company_id": company_id,
                    "created_after": created_after,
                    "created_before": created_before,
                    "cursor": cursor,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "modified_after": modified_after,
                    "modified_before": modified_before,
                    "page_size": page_size,
                    "remote_fields": remote_fields,
                    "remote_id": remote_id,
                    "show_enum_origins": show_enum_origins,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedAccountList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: AccountRequest,
    ) -> AccountResponse:
        """
        Creates an `Account` object with the given values.

        Parameters:
            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: AccountRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/accounting/v1/accounts"),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccountResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[typing_extensions.Literal["company"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[AccountsRetrieveRequestRemoteFields] = None,
        show_enum_origins: typing.Optional[AccountsRetrieveRequestShowEnumOrigins] = None,
    ) -> Account:
        """
        Returns an `Account` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[typing_extensions.Literal["company"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - remote_fields: typing.Optional[AccountsRetrieveRequestRemoteFields]. Deprecated. Use show_enum_origins.

            - show_enum_origins: typing.Optional[AccountsRetrieveRequestShowEnumOrigins]. Which fields should be returned in non-normalized form.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"api/accounting/v1/accounts/{id}"),
            params=remove_none_from_dict(
                {
                    "expand": expand,
                    "include_remote_data": include_remote_data,
                    "remote_fields": remote_fields,
                    "show_enum_origins": show_enum_origins,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Account, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_post_retrieve(self) -> MetaResponse:
        """
        Returns metadata for `Account` POSTs.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/accounting/v1/accounts/meta/post"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAccountsClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: AsyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        company_id: typing.Optional[str] = None,
        created_after: typing.Optional[str] = None,
        created_before: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[typing_extensions.Literal["company"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[str] = None,
        modified_before: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[AccountsListRequestRemoteFields] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[AccountsListRequestShowEnumOrigins] = None,
    ) -> PaginatedAccountList:
        """
        Returns a list of `Account` objects.

        Parameters:
            - company_id: typing.Optional[str]. If provided, will only return accounts for this company.

            - created_after: typing.Optional[str]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[str]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - expand: typing.Optional[typing_extensions.Literal["company"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - modified_after: typing.Optional[str]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[str]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_fields: typing.Optional[AccountsListRequestRemoteFields]. Deprecated. Use show_enum_origins.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - show_enum_origins: typing.Optional[AccountsListRequestShowEnumOrigins]. Which fields should be returned in non-normalized form.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/accounting/v1/accounts"),
            params=remove_none_from_dict(
                {
                    "company_id": company_id,
                    "created_after": created_after,
                    "created_before": created_before,
                    "cursor": cursor,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "modified_after": modified_after,
                    "modified_before": modified_before,
                    "page_size": page_size,
                    "remote_fields": remote_fields,
                    "remote_id": remote_id,
                    "show_enum_origins": show_enum_origins,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedAccountList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: AccountRequest,
    ) -> AccountResponse:
        """
        Creates an `Account` object with the given values.

        Parameters:
            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: AccountRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/accounting/v1/accounts"),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccountResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[typing_extensions.Literal["company"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[AccountsRetrieveRequestRemoteFields] = None,
        show_enum_origins: typing.Optional[AccountsRetrieveRequestShowEnumOrigins] = None,
    ) -> Account:
        """
        Returns an `Account` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[typing_extensions.Literal["company"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - remote_fields: typing.Optional[AccountsRetrieveRequestRemoteFields]. Deprecated. Use show_enum_origins.

            - show_enum_origins: typing.Optional[AccountsRetrieveRequestShowEnumOrigins]. Which fields should be returned in non-normalized form.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"api/accounting/v1/accounts/{id}"),
            params=remove_none_from_dict(
                {
                    "expand": expand,
                    "include_remote_data": include_remote_data,
                    "remote_fields": remote_fields,
                    "show_enum_origins": show_enum_origins,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Account, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_post_retrieve(self) -> MetaResponse:
        """
        Returns metadata for `Account` POSTs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/accounting/v1/accounts/meta/post"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
