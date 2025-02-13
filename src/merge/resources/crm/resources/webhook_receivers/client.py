# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....environment import MergeEnvironment
from ...types.webhook_receiver import WebhookReceiver

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class WebhookReceiversClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: SyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    def list(self) -> typing.List[WebhookReceiver]:
        """
        Returns a list of `WebhookReceiver` objects.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/crm/v1/webhook-receivers"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[WebhookReceiver], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, event: str, is_active: bool, key: typing.Optional[str] = OMIT) -> WebhookReceiver:
        """
        Creates a `WebhookReceiver` object with the given values.

        Parameters:
            - event: str. <span style="white-space: nowrap">`non-empty`</span>

            - is_active: bool.

            - key: typing.Optional[str]. <span style="white-space: nowrap">`non-empty`</span>
        """
        _request: typing.Dict[str, typing.Any] = {"event": event, "is_active": is_active}
        if key is not OMIT:
            _request["key"] = key
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/crm/v1/webhook-receivers"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(WebhookReceiver, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncWebhookReceiversClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: AsyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    async def list(self) -> typing.List[WebhookReceiver]:
        """
        Returns a list of `WebhookReceiver` objects.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/crm/v1/webhook-receivers"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[WebhookReceiver], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, *, event: str, is_active: bool, key: typing.Optional[str] = OMIT) -> WebhookReceiver:
        """
        Creates a `WebhookReceiver` object with the given values.

        Parameters:
            - event: str. <span style="white-space: nowrap">`non-empty`</span>

            - is_active: bool.

            - key: typing.Optional[str]. <span style="white-space: nowrap">`non-empty`</span>
        """
        _request: typing.Dict[str, typing.Any] = {"event": event, "is_active": is_active}
        if key is not OMIT:
            _request["key"] = key
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/crm/v1/webhook-receivers"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(WebhookReceiver, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
