import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image import Image
    from ..models.image_mirror_status import ImageMirrorStatus


T = TypeVar("T", bound="ImageVersion")


@define
class ImageVersion:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        default (Union[Unset, bool]):
        editor_version (Union[Unset, None, str]):
        framework_version (Union[Unset, None, str]):
        image (Union[Unset, Image]):
        image_id (Union[Unset, None, str]):
        mirror_status (Union[Unset, ImageMirrorStatus]):
        partner_id (Union[Unset, None, str]):
        published (Union[Unset, bool]):
        published_at (Union[Unset, None, datetime.datetime]):
        size (Union[Unset, None, int]):
        tag (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, str]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    default: Union[Unset, bool] = UNSET
    editor_version: Union[Unset, None, str] = UNSET
    framework_version: Union[Unset, None, str] = UNSET
    image: Union[Unset, "Image"] = UNSET
    image_id: Union[Unset, None, str] = UNSET
    mirror_status: Union[Unset, "ImageMirrorStatus"] = UNSET
    partner_id: Union[Unset, None, str] = UNSET
    published: Union[Unset, bool] = UNSET
    published_at: Union[Unset, None, datetime.datetime] = UNSET
    size: Union[Unset, None, int] = UNSET
    tag: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        default = self.default
        editor_version = self.editor_version
        framework_version = self.framework_version
        image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        image_id = self.image_id
        mirror_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mirror_status, Unset):
            mirror_status = self.mirror_status.to_dict()

        partner_id = self.partner_id
        published = self.published
        published_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.published_at, Unset):
            published_at = self.published_at.isoformat() if self.published_at else None

        size = self.size
        tag = self.tag
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        uuid = self.uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if default is not UNSET:
            field_dict["default"] = default
        if editor_version is not UNSET:
            field_dict["editorVersion"] = editor_version
        if framework_version is not UNSET:
            field_dict["frameworkVersion"] = framework_version
        if image is not UNSET:
            field_dict["image"] = image
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
        if mirror_status is not UNSET:
            field_dict["mirrorStatus"] = mirror_status
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if published is not UNSET:
            field_dict["published"] = published
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if size is not UNSET:
            field_dict["size"] = size
        if tag is not UNSET:
            field_dict["tag"] = tag
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image import Image
        from ..models.image_mirror_status import ImageMirrorStatus

        d = src_dict.copy()
        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        default = d.pop("default", UNSET)

        editor_version = d.pop("editorVersion", UNSET)

        framework_version = d.pop("frameworkVersion", UNSET)

        _image = d.pop("image", UNSET)
        image: Union[Unset, Image]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = Image.from_dict(_image)

        image_id = d.pop("imageId", UNSET)

        _mirror_status = d.pop("mirrorStatus", UNSET)
        mirror_status: Union[Unset, ImageMirrorStatus]
        if isinstance(_mirror_status, Unset):
            mirror_status = UNSET
        else:
            mirror_status = ImageMirrorStatus.from_dict(_mirror_status)

        partner_id = d.pop("partnerId", UNSET)

        published = d.pop("published", UNSET)

        _published_at = d.pop("publishedAt", UNSET)
        published_at: Union[Unset, None, datetime.datetime]
        if _published_at is None:
            published_at = None
        elif isinstance(_published_at, Unset):
            published_at = UNSET
        else:
            published_at = isoparse(_published_at)

        size = d.pop("size", UNSET)

        tag = d.pop("tag", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        uuid = d.pop("uuid", UNSET)

        image_version = cls(
            created_at=created_at,
            default=default,
            editor_version=editor_version,
            framework_version=framework_version,
            image=image,
            image_id=image_id,
            mirror_status=mirror_status,
            partner_id=partner_id,
            published=published,
            published_at=published_at,
            size=size,
            tag=tag,
            updated_at=updated_at,
            uuid=uuid,
        )

        image_version.additional_properties = d
        return image_version

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
