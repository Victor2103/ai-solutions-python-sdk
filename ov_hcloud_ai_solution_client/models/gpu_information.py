from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GpuInformation")


@define
class GpuInformation:
    """
    Attributes:
        gpu_brand (Union[Unset, None, str]):
        gpu_memory (Union[Unset, None, int]):
        gpu_model (Union[Unset, None, str]):
    """

    gpu_brand: Union[Unset, None, str] = UNSET
    gpu_memory: Union[Unset, None, int] = UNSET
    gpu_model: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gpu_brand = self.gpu_brand
        gpu_memory = self.gpu_memory
        gpu_model = self.gpu_model

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gpu_brand is not UNSET:
            field_dict["gpuBrand"] = gpu_brand
        if gpu_memory is not UNSET:
            field_dict["gpuMemory"] = gpu_memory
        if gpu_model is not UNSET:
            field_dict["gpuModel"] = gpu_model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gpu_brand = d.pop("gpuBrand", UNSET)

        gpu_memory = d.pop("gpuMemory", UNSET)

        gpu_model = d.pop("gpuModel", UNSET)

        gpu_information = cls(
            gpu_brand=gpu_brand,
            gpu_memory=gpu_memory,
            gpu_model=gpu_model,
        )

        gpu_information.additional_properties = d
        return gpu_information

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
