from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobSpecUpdate")


@define
class JobSpecUpdate:
    """
    Attributes:
        timeout (Union[Unset, None, int]):
        timeout_auto_restart (Union[Unset, None, bool]):
    """

    timeout: Union[Unset, None, int] = UNSET
    timeout_auto_restart: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timeout = self.timeout
        timeout_auto_restart = self.timeout_auto_restart

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if timeout_auto_restart is not UNSET:
            field_dict["timeoutAutoRestart"] = timeout_auto_restart

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timeout = d.pop("timeout", UNSET)

        timeout_auto_restart = d.pop("timeoutAutoRestart", UNSET)

        job_spec_update = cls(
            timeout=timeout,
            timeout_auto_restart=timeout_auto_restart,
        )

        job_spec_update.additional_properties = d
        return job_spec_update

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
