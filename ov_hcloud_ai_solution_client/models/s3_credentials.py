from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

T = TypeVar("T", bound="S3Credentials")


@define
class S3Credentials:
    """
    Attributes:
        access_key (Union[Unset, str]):
        region (Union[Unset, str]):
        secret_key (Union[Unset, str]):
    """

    access_key: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    secret_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_key = self.access_key
        region = self.region
        secret_key = self.secret_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_key is not UNSET:
            field_dict["access_key"] = access_key
        if region is not UNSET:
            field_dict["region"] = region
        if secret_key is not UNSET:
            field_dict["secret_key"] = secret_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_key = d.pop("access_key", UNSET)

        region = d.pop("region", UNSET)

        secret_key = d.pop("secret_key", UNSET)

        s3_credentials = cls(
            access_key=access_key,
            region=region,
            secret_key=secret_key,
        )

        s3_credentials.additional_properties = d
        return s3_credentials

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
