from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSyncSpec")


@define
class DataSyncSpec:
    """
    Attributes:
        direction (str):
        app_id (Union[Unset, None, str]): readOnly
        job_id (Union[Unset, None, str]): readOnly
        manual (Union[Unset, bool]): true if the data sync is started by the user
        volume (Union[Unset, None, str]): readOnly
    """

    direction: str
    app_id: Union[Unset, None, str] = UNSET
    job_id: Union[Unset, None, str] = UNSET
    manual: Union[Unset, bool] = UNSET
    volume: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        direction = self.direction
        app_id = self.app_id
        job_id = self.job_id
        manual = self.manual
        volume = self.volume

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "direction": direction,
            }
        )
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if manual is not UNSET:
            field_dict["manual"] = manual
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        direction = d.pop("direction")

        app_id = d.pop("appId", UNSET)

        job_id = d.pop("jobId", UNSET)

        manual = d.pop("manual", UNSET)

        volume = d.pop("volume", UNSET)

        data_sync_spec = cls(
            direction=direction,
            app_id=app_id,
            job_id=job_id,
            manual=manual,
            volume=volume,
        )

        data_sync_spec.additional_properties = d
        return data_sync_spec

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
