from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_deployment_strategy import AppDeploymentStrategy


T = TypeVar("T", bound="AppUpdate")


@define
class AppUpdate:
    """
    Attributes:
        deployment_strategy (Union[Unset, AppDeploymentStrategy]):
        url (Union[Unset, None, str]): URL of the new Docker image
    """

    deployment_strategy: Union[Unset, "AppDeploymentStrategy"] = UNSET
    url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deployment_strategy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deployment_strategy, Unset):
            deployment_strategy = self.deployment_strategy.to_dict()

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deployment_strategy is not UNSET:
            field_dict["deploymentStrategy"] = deployment_strategy
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.app_deployment_strategy import AppDeploymentStrategy

        d = src_dict.copy()
        _deployment_strategy = d.pop("deploymentStrategy", UNSET)
        deployment_strategy: Union[Unset, AppDeploymentStrategy]
        if isinstance(_deployment_strategy, Unset):
            deployment_strategy = UNSET
        else:
            deployment_strategy = AppDeploymentStrategy.from_dict(_deployment_strategy)

        url = d.pop("url", UNSET)

        app_update = cls(
            deployment_strategy=deployment_strategy,
            url=url,
        )

        app_update.additional_properties = d
        return app_update

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
