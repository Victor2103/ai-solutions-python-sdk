from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateImageVersion")


@define
class UpdateImageVersion:
    """
    Attributes:
        default (Union[Unset, None, bool]): Set as true for marking the version as image default (notebook image
            versions only)
        editor_version (Union[Unset, None, str]): Editor version (notebook image versions only)
        framework_version (Union[Unset, None, str]): Framework version (notebook image versions only)
        published (Union[Unset, None, bool]): Version publishing
    """

    default: Union[Unset, None, bool] = UNSET
    editor_version: Union[Unset, None, str] = UNSET
    framework_version: Union[Unset, None, str] = UNSET
    published: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default = self.default
        editor_version = self.editor_version
        framework_version = self.framework_version
        published = self.published

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default is not UNSET:
            field_dict["default"] = default
        if editor_version is not UNSET:
            field_dict["editorVersion"] = editor_version
        if framework_version is not UNSET:
            field_dict["frameworkVersion"] = framework_version
        if published is not UNSET:
            field_dict["published"] = published

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        default = d.pop("default", UNSET)

        editor_version = d.pop("editorVersion", UNSET)

        framework_version = d.pop("frameworkVersion", UNSET)

        published = d.pop("published", UNSET)

        update_image_version = cls(
            default=default,
            editor_version=editor_version,
            framework_version=framework_version,
            published=published,
        )

        update_image_version.additional_properties = d
        return update_image_version

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
