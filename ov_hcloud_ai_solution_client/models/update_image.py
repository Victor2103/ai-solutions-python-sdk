from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..models.product_type import ProductType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateImage")


@define
class UpdateImage:
    """
    Attributes:
        description (Union[Unset, None, str]): Image description
        doc_url (Union[Unset, None, str]): Image documentation URL
        editor_id (Union[Unset, None, str]): Image editor ID, limited to notebook images
        framework_id (Union[Unset, None, str]): Image framework ID, limited to notebook images
        logo_url (Union[Unset, None, str]): Image logo URL
        name (Union[Unset, None, str]): Image Name
        product (Union[Unset, ProductType]):
        source (Union[Unset, None, str]): Docker image name, including host and port if not Docker Hub, excluding tag
    """

    description: Union[Unset, None, str] = UNSET
    doc_url: Union[Unset, None, str] = UNSET
    editor_id: Union[Unset, None, str] = UNSET
    framework_id: Union[Unset, None, str] = UNSET
    logo_url: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    product: Union[Unset, ProductType] = UNSET
    source: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        doc_url = self.doc_url
        editor_id = self.editor_id
        framework_id = self.framework_id
        logo_url = self.logo_url
        name = self.name
        product: Union[Unset, str] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.value

        source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if doc_url is not UNSET:
            field_dict["docUrl"] = doc_url
        if editor_id is not UNSET:
            field_dict["editorId"] = editor_id
        if framework_id is not UNSET:
            field_dict["frameworkId"] = framework_id
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if product is not UNSET:
            field_dict["product"] = product
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        doc_url = d.pop("docUrl", UNSET)

        editor_id = d.pop("editorId", UNSET)

        framework_id = d.pop("frameworkId", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        name = d.pop("name", UNSET)

        _product = d.pop("product", UNSET)
        product: Union[Unset, ProductType]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = ProductType(_product)

        source = d.pop("source", UNSET)

        update_image = cls(
            description=description,
            doc_url=doc_url,
            editor_id=editor_id,
            framework_id=framework_id,
            logo_url=logo_url,
            name=name,
            product=product,
            source=source,
        )

        update_image.additional_properties = d
        return update_image

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
