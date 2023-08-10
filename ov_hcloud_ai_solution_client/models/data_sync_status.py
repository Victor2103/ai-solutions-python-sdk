import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_sync_progress import DataSyncProgress
    from ..models.info import Info


T = TypeVar("T", bound="DataSyncStatus")


@define
class DataSyncStatus:
    """
    Attributes:
        ended_at (Union[Unset, None, datetime.datetime]):
        info (Union[Unset, Info]):
        progress (Union[Unset, List['DataSyncProgress']]):
        queued_at (Union[Unset, datetime.datetime]):
        started_at (Union[Unset, None, datetime.datetime]):
        state (Union[Unset, str]):
    """

    ended_at: Union[Unset, None, datetime.datetime] = UNSET
    info: Union[Unset, "Info"] = UNSET
    progress: Union[Unset, List["DataSyncProgress"]] = UNSET
    queued_at: Union[Unset, datetime.datetime] = UNSET
    started_at: Union[Unset, None, datetime.datetime] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ended_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.ended_at, Unset):
            ended_at = self.ended_at.isoformat() if self.ended_at else None

        info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        progress: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.progress, Unset):
            progress = []
            for progress_item_data in self.progress:
                progress_item = progress_item_data.to_dict()

                progress.append(progress_item)

        queued_at: Union[Unset, str] = UNSET
        if not isinstance(self.queued_at, Unset):
            queued_at = self.queued_at.isoformat()

        started_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat() if self.started_at else None

        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if info is not UNSET:
            field_dict["info"] = info
        if progress is not UNSET:
            field_dict["progress"] = progress
        if queued_at is not UNSET:
            field_dict["queuedAt"] = queued_at
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_sync_progress import DataSyncProgress
        from ..models.info import Info

        d = src_dict.copy()
        _ended_at = d.pop("endedAt", UNSET)
        ended_at: Union[Unset, None, datetime.datetime]
        if _ended_at is None:
            ended_at = None
        elif isinstance(_ended_at, Unset):
            ended_at = UNSET
        else:
            ended_at = isoparse(_ended_at)

        _info = d.pop("info", UNSET)
        info: Union[Unset, Info]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = Info.from_dict(_info)

        progress = []
        _progress = d.pop("progress", UNSET)
        for progress_item_data in _progress or []:
            progress_item = DataSyncProgress.from_dict(progress_item_data)

            progress.append(progress_item)

        _queued_at = d.pop("queuedAt", UNSET)
        queued_at: Union[Unset, datetime.datetime]
        if isinstance(_queued_at, Unset):
            queued_at = UNSET
        else:
            queued_at = isoparse(_queued_at)

        _started_at = d.pop("startedAt", UNSET)
        started_at: Union[Unset, None, datetime.datetime]
        if _started_at is None:
            started_at = None
        elif isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        state = d.pop("state", UNSET)

        data_sync_status = cls(
            ended_at=ended_at,
            info=info,
            progress=progress,
            queued_at=queued_at,
            started_at=started_at,
            state=state,
        )

        data_sync_status.additional_properties = d
        return data_sync_status

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
