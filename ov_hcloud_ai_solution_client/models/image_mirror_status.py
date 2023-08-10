import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field
from dateutil.parser import isoparse

from ..models.image_mirror_state import ImageMirrorState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageMirrorStatus")


@define
class ImageMirrorStatus:
    """
    Attributes:
        done_at (Union[Unset, None, datetime.datetime]):
        failure_reason (Union[Unset, None, str]):
        last_done_at (Union[Unset, None, datetime.datetime]):
        retries_count (Union[Unset, int]):
        started_at (Union[Unset, None, datetime.datetime]):
        state (Union[Unset, ImageMirrorState]):
    """

    done_at: Union[Unset, None, datetime.datetime] = UNSET
    failure_reason: Union[Unset, None, str] = UNSET
    last_done_at: Union[Unset, None, datetime.datetime] = UNSET
    retries_count: Union[Unset, int] = UNSET
    started_at: Union[Unset, None, datetime.datetime] = UNSET
    state: Union[Unset, ImageMirrorState] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        done_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.done_at, Unset):
            done_at = self.done_at.isoformat() if self.done_at else None

        failure_reason = self.failure_reason
        last_done_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_done_at, Unset):
            last_done_at = self.last_done_at.isoformat() if self.last_done_at else None

        retries_count = self.retries_count
        started_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat() if self.started_at else None

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if done_at is not UNSET:
            field_dict["doneAt"] = done_at
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason
        if last_done_at is not UNSET:
            field_dict["lastDoneAt"] = last_done_at
        if retries_count is not UNSET:
            field_dict["retriesCount"] = retries_count
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _done_at = d.pop("doneAt", UNSET)
        done_at: Union[Unset, None, datetime.datetime]
        if _done_at is None:
            done_at = None
        elif isinstance(_done_at, Unset):
            done_at = UNSET
        else:
            done_at = isoparse(_done_at)

        failure_reason = d.pop("failureReason", UNSET)

        _last_done_at = d.pop("lastDoneAt", UNSET)
        last_done_at: Union[Unset, None, datetime.datetime]
        if _last_done_at is None:
            last_done_at = None
        elif isinstance(_last_done_at, Unset):
            last_done_at = UNSET
        else:
            last_done_at = isoparse(_last_done_at)

        retries_count = d.pop("retriesCount", UNSET)

        _started_at = d.pop("startedAt", UNSET)
        started_at: Union[Unset, None, datetime.datetime]
        if _started_at is None:
            started_at = None
        elif isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _state = d.pop("state", UNSET)
        state: Union[Unset, ImageMirrorState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ImageMirrorState(_state)

        image_mirror_status = cls(
            done_at=done_at,
            failure_reason=failure_reason,
            last_done_at=last_done_at,
            retries_count=retries_count,
            started_at=started_at,
            state=state,
        )

        image_mirror_status.additional_properties = d
        return image_mirror_status

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
