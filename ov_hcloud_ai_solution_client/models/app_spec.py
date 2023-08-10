from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define, field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_deployment_strategy import AppDeploymentStrategy
    from ..models.app_spec_labels import AppSpecLabels
    from ..models.env import Env
    from ..models.probe import Probe
    from ..models.resources import Resources
    from ..models.scaling_strategy import ScalingStrategy
    from ..models.volume import Volume


T = TypeVar("T", bound="AppSpec")


@define
class AppSpec:
    """
    Attributes:
        image (str): Docker or capability image to use in the app. App capability images must comply with the pattern
            image-id:version Example: ubuntu:latest.
        command (Union[Unset, None, List[str]]): App command to run Example: ['python3', 'script.py'].
        default_http_port (Union[Unset, int]):  Default: 8080. Example: 8080.
        deletion_requested (Union[Unset, bool]):
        deployment_strategy (Union[Unset, AppDeploymentStrategy]):
        env_vars (Union[Unset, None, List['Env']]): Environment variables that will be injected into the app
        labels (Union[Unset, None, AppSpecLabels]): some label, used to scope tokens, labels prefixed by 'ovh/' are
            owned by the platform and overridden Example: {'label': 'some-label'}.
        name (Union[Unset, None, str]): App name, generated if not provided Example: funny-ubuntu.
        probe (Union[Unset, Probe]):
        resources (Union[Unset, Resources]):
        scaling_strategy (Union[Unset, ScalingStrategy]):
        shutdown (Union[Unset, None, str]):
        unsecure_http (Union[Unset, bool]): true if app api port can be accessed without any authentication token, false
            otherwise
        volumes (Union[Unset, None, List['Volume']]):
    """

    image: str
    command: Union[Unset, None, List[str]] = UNSET
    default_http_port: Union[Unset, int] = 8080
    deletion_requested: Union[Unset, bool] = UNSET
    deployment_strategy: Union[Unset, "AppDeploymentStrategy"] = UNSET
    env_vars: Union[Unset, None, List["Env"]] = UNSET
    labels: Union[Unset, None, "AppSpecLabels"] = UNSET
    name: Union[Unset, None, str] = UNSET
    probe: Union[Unset, "Probe"] = UNSET
    resources: Union[Unset, "Resources"] = UNSET
    scaling_strategy: Union[Unset, "ScalingStrategy"] = UNSET
    shutdown: Union[Unset, None, str] = UNSET
    unsecure_http: Union[Unset, bool] = False
    volumes: Union[Unset, None, List["Volume"]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image = self.image
        command: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.command, Unset):
            if self.command is None:
                command = None
            else:
                command = self.command

        default_http_port = self.default_http_port
        deletion_requested = self.deletion_requested
        deployment_strategy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deployment_strategy, Unset):
            deployment_strategy = self.deployment_strategy.to_dict()

        env_vars: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.env_vars, Unset):
            if self.env_vars is None:
                env_vars = None
            else:
                env_vars = []
                for env_vars_item_data in self.env_vars:
                    env_vars_item = env_vars_item_data.to_dict()

                    env_vars.append(env_vars_item)

        labels: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict() if self.labels else None

        name = self.name
        probe: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.probe, Unset):
            probe = self.probe.to_dict()

        resources: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        scaling_strategy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scaling_strategy, Unset):
            scaling_strategy = self.scaling_strategy.to_dict()

        shutdown = self.shutdown
        unsecure_http = self.unsecure_http
        volumes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.volumes, Unset):
            if self.volumes is None:
                volumes = None
            else:
                volumes = []
                for volumes_item_data in self.volumes:
                    volumes_item = volumes_item_data.to_dict()

                    volumes.append(volumes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
            }
        )
        if command is not UNSET:
            field_dict["command"] = command
        if default_http_port is not UNSET:
            field_dict["defaultHttpPort"] = default_http_port
        if deletion_requested is not UNSET:
            field_dict["deletionRequested"] = deletion_requested
        if deployment_strategy is not UNSET:
            field_dict["deploymentStrategy"] = deployment_strategy
        if env_vars is not UNSET:
            field_dict["envVars"] = env_vars
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name
        if probe is not UNSET:
            field_dict["probe"] = probe
        if resources is not UNSET:
            field_dict["resources"] = resources
        if scaling_strategy is not UNSET:
            field_dict["scalingStrategy"] = scaling_strategy
        if shutdown is not UNSET:
            field_dict["shutdown"] = shutdown
        if unsecure_http is not UNSET:
            field_dict["unsecureHttp"] = unsecure_http
        if volumes is not UNSET:
            field_dict["volumes"] = volumes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.app_deployment_strategy import AppDeploymentStrategy
        from ..models.app_spec_labels import AppSpecLabels
        from ..models.env import Env
        from ..models.probe import Probe
        from ..models.resources import Resources
        from ..models.scaling_strategy import ScalingStrategy
        from ..models.volume import Volume

        d = src_dict.copy()
        image = d.pop("image")

        command = cast(List[str], d.pop("command", UNSET))

        default_http_port = d.pop("defaultHttpPort", UNSET)

        deletion_requested = d.pop("deletionRequested", UNSET)

        _deployment_strategy = d.pop("deploymentStrategy", UNSET)
        deployment_strategy: Union[Unset, AppDeploymentStrategy]
        if isinstance(_deployment_strategy, Unset):
            deployment_strategy = UNSET
        else:
            deployment_strategy = AppDeploymentStrategy.from_dict(_deployment_strategy)

        env_vars = []
        _env_vars = d.pop("envVars", UNSET)
        for env_vars_item_data in _env_vars or []:
            env_vars_item = Env.from_dict(env_vars_item_data)

            env_vars.append(env_vars_item)

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, None, AppSpecLabels]
        if _labels is None:
            labels = None
        elif isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = AppSpecLabels.from_dict(_labels)

        name = d.pop("name", UNSET)

        _probe = d.pop("probe", UNSET)
        probe: Union[Unset, Probe]
        if isinstance(_probe, Unset):
            probe = UNSET
        else:
            probe = Probe.from_dict(_probe)

        _resources = d.pop("resources", UNSET)
        resources: Union[Unset, Resources]
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = Resources.from_dict(_resources)

        _scaling_strategy = d.pop("scalingStrategy", UNSET)
        scaling_strategy: Union[Unset, ScalingStrategy]
        if isinstance(_scaling_strategy, Unset):
            scaling_strategy = UNSET
        else:
            scaling_strategy = ScalingStrategy.from_dict(_scaling_strategy)

        shutdown = d.pop("shutdown", UNSET)

        unsecure_http = d.pop("unsecureHttp", UNSET)

        volumes = []
        _volumes = d.pop("volumes", UNSET)
        for volumes_item_data in _volumes or []:
            volumes_item = Volume.from_dict(volumes_item_data)

            volumes.append(volumes_item)

        app_spec = cls(
            image=image,
            command=command,
            default_http_port=default_http_port,
            deletion_requested=deletion_requested,
            deployment_strategy=deployment_strategy,
            env_vars=env_vars,
            labels=labels,
            name=name,
            probe=probe,
            resources=resources,
            scaling_strategy=scaling_strategy,
            shutdown=shutdown,
            unsecure_http=unsecure_http,
            volumes=volumes,
        )

        app_spec.additional_properties = d
        return app_spec

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
