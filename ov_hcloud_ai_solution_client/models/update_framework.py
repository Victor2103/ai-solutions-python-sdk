from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define, field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFramework")


@define
class UpdateFramework:
    """
    Attributes:
        description (Union[Unset, None, str]): Framework description
        doc_url (Union[Unset, None, str]): Framework documentation URL
        logo_url (Union[Unset, None, str]): Framework logo URL
        name (Union[Unset, None, str]): Framework Name
        saved_paths (Union[Unset, None, List[str]]): Saved paths
    """

    description: Union[Unset, None, str] = UNSET
    doc_url: Union[Unset, None, str] = UNSET
    logo_url: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    saved_paths: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        doc_url = self.doc_url
        logo_url = self.logo_url
        name = self.name
        saved_paths: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.saved_paths, Unset):
            if self.saved_paths is None:
                saved_paths = None
            else:
                saved_paths = self.saved_paths

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if doc_url is not UNSET:
            field_dict["docUrl"] = doc_url
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if saved_paths is not UNSET:
            field_dict["savedPaths"] = saved_paths

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        doc_url = d.pop("docUrl", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        name = d.pop("name", UNSET)

        saved_paths = cast(List[str], d.pop("savedPaths", UNSET))

        update_framework = cls(
            description=description,
            doc_url=doc_url,
            logo_url=logo_url,
            name=name,
            saved_paths=saved_paths,
        )

        update_framework.additional_properties = d
        return update_framework

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
