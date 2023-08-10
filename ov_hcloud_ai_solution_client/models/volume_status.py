import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="VolumeStatus")


@define
class VolumeStatus:
    """
    Attributes:
        id (Union[Unset, str]):
        last_pulled_created_at (Union[Unset, None, datetime.datetime]):
        last_pushed_created_at (Union[Unset, None, datetime.datetime]):
        mount_path (Union[Unset, str]):
        user_volume_id (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    last_pulled_created_at: Union[Unset, None, datetime.datetime] = UNSET
    last_pushed_created_at: Union[Unset, None, datetime.datetime] = UNSET
    mount_path: Union[Unset, str] = UNSET
    user_volume_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        last_pulled_created_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_pulled_created_at, Unset):
            last_pulled_created_at = self.last_pulled_created_at.isoformat() if self.last_pulled_created_at else None

        last_pushed_created_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_pushed_created_at, Unset):
            last_pushed_created_at = self.last_pushed_created_at.isoformat() if self.last_pushed_created_at else None

        mount_path = self.mount_path
        user_volume_id = self.user_volume_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if last_pulled_created_at is not UNSET:
            field_dict["lastPulledCreatedAt"] = last_pulled_created_at
        if last_pushed_created_at is not UNSET:
            field_dict["lastPushedCreatedAt"] = last_pushed_created_at
        if mount_path is not UNSET:
            field_dict["mountPath"] = mount_path
        if user_volume_id is not UNSET:
            field_dict["userVolumeId"] = user_volume_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _last_pulled_created_at = d.pop("lastPulledCreatedAt", UNSET)
        last_pulled_created_at: Union[Unset, None, datetime.datetime]
        if _last_pulled_created_at is None:
            last_pulled_created_at = None
        elif isinstance(_last_pulled_created_at, Unset):
            last_pulled_created_at = UNSET
        else:
            last_pulled_created_at = isoparse(_last_pulled_created_at)

        _last_pushed_created_at = d.pop("lastPushedCreatedAt", UNSET)
        last_pushed_created_at: Union[Unset, None, datetime.datetime]
        if _last_pushed_created_at is None:
            last_pushed_created_at = None
        elif isinstance(_last_pushed_created_at, Unset):
            last_pushed_created_at = UNSET
        else:
            last_pushed_created_at = isoparse(_last_pushed_created_at)

        mount_path = d.pop("mountPath", UNSET)

        user_volume_id = d.pop("userVolumeId", UNSET)

        volume_status = cls(
            id=id,
            last_pulled_created_at=last_pulled_created_at,
            last_pushed_created_at=last_pushed_created_at,
            mount_path=mount_path,
            user_volume_id=user_volume_id,
        )

        volume_status.additional_properties = d
        return volume_status

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
