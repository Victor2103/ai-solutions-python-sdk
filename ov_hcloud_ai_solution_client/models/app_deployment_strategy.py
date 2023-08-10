from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppDeploymentStrategy")


@define
class AppDeploymentStrategy:
    """
    Attributes:
        max_surge (Union[Unset, None, str]): specifies the maximum number of replicas that can be created over the
            desired number of Pods Default: '25%'.
        max_unavailable (Union[Unset, None, str]): specifies the maximum number of replicas that can be unavailable
            during the update process Default: '25%'.
        progress_deadline_seconds (Union[Unset, None, int]): specifies the number of seconds you want to wait for your
            Deployment to progress before the system reports back that the Deployment has failed progressing Default: 600.
    """

    max_surge: Union[Unset, None, str] = "25%"
    max_unavailable: Union[Unset, None, str] = "25%"
    progress_deadline_seconds: Union[Unset, None, int] = 600
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_surge = self.max_surge
        max_unavailable = self.max_unavailable
        progress_deadline_seconds = self.progress_deadline_seconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_surge is not UNSET:
            field_dict["maxSurge"] = max_surge
        if max_unavailable is not UNSET:
            field_dict["maxUnavailable"] = max_unavailable
        if progress_deadline_seconds is not UNSET:
            field_dict["progressDeadlineSeconds"] = progress_deadline_seconds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_surge = d.pop("maxSurge", UNSET)

        max_unavailable = d.pop("maxUnavailable", UNSET)

        progress_deadline_seconds = d.pop("progressDeadlineSeconds", UNSET)

        app_deployment_strategy = cls(
            max_surge=max_surge,
            max_unavailable=max_unavailable,
            progress_deadline_seconds=progress_deadline_seconds,
        )

        app_deployment_strategy.additional_properties = d
        return app_deployment_strategy

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
