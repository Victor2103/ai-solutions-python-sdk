import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field
from dateutil.parser import isoparse

from ..models.licensing_type import LicensingType
from ..models.product_type import ProductType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.framework import Framework
    from ..models.partner import Partner


T = TypeVar("T", bound="Image")


@define
class Image:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        description (Union[Unset, None, str]):
        doc_url (Union[Unset, None, str]):
        editor_id (Union[Unset, None, str]):
        framework (Union[Unset, Framework]):
        framework_id (Union[Unset, None, str]):
        id (Union[Unset, str]):
        licensing (Union[Unset, LicensingType]):
        logo_url (Union[Unset, None, str]):
        name (Union[Unset, str]):
        partner (Union[Unset, Partner]):
        partner_id (Union[Unset, None, str]):
        product (Union[Unset, ProductType]):
        source (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, str]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, None, str] = UNSET
    doc_url: Union[Unset, None, str] = UNSET
    editor_id: Union[Unset, None, str] = UNSET
    framework: Union[Unset, "Framework"] = UNSET
    framework_id: Union[Unset, None, str] = UNSET
    id: Union[Unset, str] = UNSET
    licensing: Union[Unset, LicensingType] = UNSET
    logo_url: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    partner: Union[Unset, "Partner"] = UNSET
    partner_id: Union[Unset, None, str] = UNSET
    product: Union[Unset, ProductType] = UNSET
    source: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description = self.description
        doc_url = self.doc_url
        editor_id = self.editor_id
        framework: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.framework, Unset):
            framework = self.framework.to_dict()

        framework_id = self.framework_id
        id = self.id
        licensing: Union[Unset, str] = UNSET
        if not isinstance(self.licensing, Unset):
            licensing = self.licensing.value

        logo_url = self.logo_url
        name = self.name
        partner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.partner, Unset):
            partner = self.partner.to_dict()

        partner_id = self.partner_id
        product: Union[Unset, str] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.value

        source = self.source
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        uuid = self.uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if doc_url is not UNSET:
            field_dict["docUrl"] = doc_url
        if editor_id is not UNSET:
            field_dict["editorId"] = editor_id
        if framework is not UNSET:
            field_dict["framework"] = framework
        if framework_id is not UNSET:
            field_dict["frameworkId"] = framework_id
        if id is not UNSET:
            field_dict["id"] = id
        if licensing is not UNSET:
            field_dict["licensing"] = licensing
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if partner is not UNSET:
            field_dict["partner"] = partner
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if product is not UNSET:
            field_dict["product"] = product
        if source is not UNSET:
            field_dict["source"] = source
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.framework import Framework
        from ..models.partner import Partner

        d = src_dict.copy()
        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        description = d.pop("description", UNSET)

        doc_url = d.pop("docUrl", UNSET)

        editor_id = d.pop("editorId", UNSET)

        _framework = d.pop("framework", UNSET)
        framework: Union[Unset, Framework]
        if isinstance(_framework, Unset):
            framework = UNSET
        else:
            framework = Framework.from_dict(_framework)

        framework_id = d.pop("frameworkId", UNSET)

        id = d.pop("id", UNSET)

        _licensing = d.pop("licensing", UNSET)
        licensing: Union[Unset, LicensingType]
        if isinstance(_licensing, Unset):
            licensing = UNSET
        else:
            licensing = LicensingType(_licensing)

        logo_url = d.pop("logoUrl", UNSET)

        name = d.pop("name", UNSET)

        _partner = d.pop("partner", UNSET)
        partner: Union[Unset, Partner]
        if isinstance(_partner, Unset):
            partner = UNSET
        else:
            partner = Partner.from_dict(_partner)

        partner_id = d.pop("partnerId", UNSET)

        _product = d.pop("product", UNSET)
        product: Union[Unset, ProductType]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = ProductType(_product)

        source = d.pop("source", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        uuid = d.pop("uuid", UNSET)

        image = cls(
            created_at=created_at,
            description=description,
            doc_url=doc_url,
            editor_id=editor_id,
            framework=framework,
            framework_id=framework_id,
            id=id,
            licensing=licensing,
            logo_url=logo_url,
            name=name,
            partner=partner,
            partner_id=partner_id,
            product=product,
            source=source,
            updated_at=updated_at,
            uuid=uuid,
        )

        image.additional_properties = d
        return image

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
