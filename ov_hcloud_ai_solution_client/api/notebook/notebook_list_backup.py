from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notebook_backup_list import NotebookBackupList
from ...models.order import Order
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    page: Union[Unset, None, int] = UNSET,
    size: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, Order] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
    updated_after: Union[Unset, None, int] = UNSET,
    updated_before: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["page"] = page

    params["size"] = size

    json_order: Union[Unset, None, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value if order else None

    params["order"] = json_order

    params["sort"] = sort

    params["updatedAfter"] = updated_after

    params["updatedBefore"] = updated_before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v1/notebook/{id}/backup".format(
            id=id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, NotebookBackupList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = NotebookBackupList.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, NotebookBackupList]]:
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
    order: Union[Unset, None, Order] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
    updated_after: Union[Unset, None, int] = UNSET,
    updated_before: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, NotebookBackupList]]:
    """List all backups related to this notebook

    Args:
        id (str):
        page (Union[Unset, None, int]): page of the result set
        size (Union[Unset, None, int]): size of the result set
        order (Union[Unset, None, Order]):
        sort (Union[Unset, None, str]): sort the result set with field
        updated_after (Union[Unset, None, int]): timestamp to filter job updated after
        updated_before (Union[Unset, None, int]): timestamp to filter job updated before

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotebookBackupList]]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
        size=size,
        order=order,
        sort=sort,
        updated_after=updated_after,
        updated_before=updated_before,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, None, int] = UNSET,
    size: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, Order] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
    updated_after: Union[Unset, None, int] = UNSET,
    updated_before: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, NotebookBackupList]]:
    """List all backups related to this notebook

    Args:
        id (str):
        page (Union[Unset, None, int]): page of the result set
        size (Union[Unset, None, int]): size of the result set
        order (Union[Unset, None, Order]):
        sort (Union[Unset, None, str]): sort the result set with field
        updated_after (Union[Unset, None, int]): timestamp to filter job updated after
        updated_before (Union[Unset, None, int]): timestamp to filter job updated before

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotebookBackupList]
    """

    return sync_detailed(
        id=id,
        client=client,
        page=page,
        size=size,
        order=order,
        sort=sort,
        updated_after=updated_after,
        updated_before=updated_before,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, None, int] = UNSET,
    size: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, Order] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
    updated_after: Union[Unset, None, int] = UNSET,
    updated_before: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, NotebookBackupList]]:
    """List all backups related to this notebook

    Args:
        id (str):
        page (Union[Unset, None, int]): page of the result set
        size (Union[Unset, None, int]): size of the result set
        order (Union[Unset, None, Order]):
        sort (Union[Unset, None, str]): sort the result set with field
        updated_after (Union[Unset, None, int]): timestamp to filter job updated after
        updated_before (Union[Unset, None, int]): timestamp to filter job updated before

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotebookBackupList]]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
        size=size,
        order=order,
        sort=sort,
        updated_after=updated_after,
        updated_before=updated_before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, None, int] = UNSET,
    size: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, Order] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
    updated_after: Union[Unset, None, int] = UNSET,
    updated_before: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, NotebookBackupList]]:
    """List all backups related to this notebook

    Args:
        id (str):
        page (Union[Unset, None, int]): page of the result set
        size (Union[Unset, None, int]): size of the result set
        order (Union[Unset, None, Order]):
        sort (Union[Unset, None, str]): sort the result set with field
        updated_after (Union[Unset, None, int]): timestamp to filter job updated after
        updated_before (Union[Unset, None, int]): timestamp to filter job updated before

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotebookBackupList]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            page=page,
            size=size,
            order=order,
            sort=sort,
            updated_after=updated_after,
            updated_before=updated_before,
        )
    ).parsed
