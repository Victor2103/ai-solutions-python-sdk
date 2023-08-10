from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FixedScalingStrategy")


@define
class FixedScalingStrategy:
    """
    Attributes:
        replicas (Union[Unset, int]): Number of replicas wanted
    """

    replicas: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        replicas = self.replicas

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if replicas is not UNSET:
            field_dict["replicas"] = replicas

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        replicas = d.pop("replicas", UNSET)

        fixed_scaling_strategy = cls(
            replicas=replicas,
        )

        fixed_scaling_strategy.additional_properties = d
        return fixed_scaling_strategy

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
