from typing import Any, Dict, List, Optional, Type, TypeVar

from attrs import define, field

T = TypeVar("T", bound="GetV1DataAuthAliasResponse200")


@define
class GetV1DataAuthAliasResponse200:
    """ """

    additional_properties: Dict[str, Optional[str]] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        get_v1_data_auth_alias_response_200 = cls()

        get_v1_data_auth_alias_response_200.additional_properties = d
        return get_v1_data_auth_alias_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Optional[str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Optional[str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
