from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define, field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFramework")


@define
class CreateFramework:
    """
    Attributes:
        description (str): Framework description
        id (str): Framework ID
        name (str): Framework Name
        doc_url (Union[Unset, None, str]): Framework documentation URL
        logo_url (Union[Unset, None, str]): Framework logo URL
        saved_paths (Union[Unset, None, List[str]]): Saved paths
    """

    description: str
    id: str
    name: str
    doc_url: Union[Unset, None, str] = UNSET
    logo_url: Union[Unset, None, str] = UNSET
    saved_paths: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        id = self.id
        name = self.name
        doc_url = self.doc_url
        logo_url = self.logo_url
        saved_paths: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.saved_paths, Unset):
            if self.saved_paths is None:
                saved_paths = None
            else:
                saved_paths = self.saved_paths

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "id": id,
                "name": name,
            }
        )
        if doc_url is not UNSET:
            field_dict["docUrl"] = doc_url
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if saved_paths is not UNSET:
            field_dict["savedPaths"] = saved_paths

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        doc_url = d.pop("docUrl", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        saved_paths = cast(List[str], d.pop("savedPaths", UNSET))

        create_framework = cls(
            description=description,
            id=id,
            name=name,
            doc_url=doc_url,
            logo_url=logo_url,
            saved_paths=saved_paths,
        )

        create_framework.additional_properties = d
        return create_framework

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
