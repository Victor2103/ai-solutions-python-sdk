from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    page: Union[Unset, None, int] = UNSET,
    size: Union[Unset, None, int] = UNSET,
    follow: Union[Unset, None, bool] = UNSET,
    replica: Union[Unset, None, str] = UNSET,
    tail: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["page"] = page

    params["size"] = size

    params["follow"] = follow

    params["replica"] = replica

    params["tail"] = tail

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v1/app/{id}/log".format(
            id=id,
        ),
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, None, int] = UNSET,
    size: Union[Unset, None, int] = UNSET,
    follow: Union[Unset, None, bool] = UNSET,
    replica: Union[Unset, None, str] = UNSET,
    tail: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """Retrieve app logs

    Args:
        id (str):
        page (Union[Unset, None, int]):
        size (Union[Unset, None, int]):
        follow (Union[Unset, None, bool]):
        replica (Union[Unset, None, str]):
        tail (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
        size=size,
        follow=follow,
        replica=replica,
        tail=tail,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, None, int] = UNSET,
    size: Union[Unset, None, int] = UNSET,
    follow: Union[Unset, None, bool] = UNSET,
    replica: Union[Unset, None, str] = UNSET,
    tail: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """Retrieve app logs

    Args:
        id (str):
        page (Union[Unset, None, int]):
        size (Union[Unset, None, int]):
        follow (Union[Unset, None, bool]):
        replica (Union[Unset, None, str]):
        tail (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
        size=size,
        follow=follow,
        replica=replica,
        tail=tail,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
