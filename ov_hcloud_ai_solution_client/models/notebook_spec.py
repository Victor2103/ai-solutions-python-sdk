from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define, field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.env import Env
    from ..models.notebook_env import NotebookEnv
    from ..models.notebook_spec_labels import NotebookSpecLabels
    from ..models.resources import Resources
    from ..models.volume import Volume


T = TypeVar("T", bound="NotebookSpec")


@define
class NotebookSpec:
    """
    Attributes:
        env (Union[Unset, NotebookEnv]):
        env_vars (Union[Unset, None, List['Env']]): Environment variables that will be injected into the notebook
        labels (Union[Unset, None, NotebookSpecLabels]): some label, used to scope tokens, labels prefixed by 'ovh/' are
            owned by the platform and overridden Example: {'label': 'some-label'}.
        name (Union[Unset, str]):
        resources (Union[Unset, Resources]):
        shutdown (Union[Unset, None, str]):
        ssh_public_keys (Union[Unset, None, List[str]]): SSH Public keys allowed to SSH into the notebook
        timeout_auto_restart (Union[Unset, None, bool]): Auto restart notebook on timeout
        unsecure_http (Union[Unset, bool]):
        volumes (Union[Unset, None, List['Volume']]):
    """

    env: Union[Unset, "NotebookEnv"] = UNSET
    env_vars: Union[Unset, None, List["Env"]] = UNSET
    labels: Union[Unset, None, "NotebookSpecLabels"] = UNSET
    name: Union[Unset, str] = UNSET
    resources: Union[Unset, "Resources"] = UNSET
    shutdown: Union[Unset, None, str] = UNSET
    ssh_public_keys: Union[Unset, None, List[str]] = UNSET
    timeout_auto_restart: Union[Unset, None, bool] = UNSET
    unsecure_http: Union[Unset, bool] = UNSET
    volumes: Union[Unset, None, List["Volume"]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        env: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.env, Unset):
            env = self.env.to_dict()

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
        resources: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        shutdown = self.shutdown
        ssh_public_keys: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.ssh_public_keys, Unset):
            if self.ssh_public_keys is None:
                ssh_public_keys = None
            else:
                ssh_public_keys = self.ssh_public_keys

        timeout_auto_restart = self.timeout_auto_restart
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
        field_dict.update({})
        if env is not UNSET:
            field_dict["env"] = env
        if env_vars is not UNSET:
            field_dict["envVars"] = env_vars
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name
        if resources is not UNSET:
            field_dict["resources"] = resources
        if shutdown is not UNSET:
            field_dict["shutdown"] = shutdown
        if ssh_public_keys is not UNSET:
            field_dict["sshPublicKeys"] = ssh_public_keys
        if timeout_auto_restart is not UNSET:
            field_dict["timeoutAutoRestart"] = timeout_auto_restart
        if unsecure_http is not UNSET:
            field_dict["unsecureHttp"] = unsecure_http
        if volumes is not UNSET:
            field_dict["volumes"] = volumes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.env import Env
        from ..models.notebook_env import NotebookEnv
        from ..models.notebook_spec_labels import NotebookSpecLabels
        from ..models.resources import Resources
        from ..models.volume import Volume

        d = src_dict.copy()
        _env = d.pop("env", UNSET)
        env: Union[Unset, NotebookEnv]
        if isinstance(_env, Unset):
            env = UNSET
        else:
            env = NotebookEnv.from_dict(_env)

        env_vars = []
        _env_vars = d.pop("envVars", UNSET)
        for env_vars_item_data in _env_vars or []:
            env_vars_item = Env.from_dict(env_vars_item_data)

            env_vars.append(env_vars_item)

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, None, NotebookSpecLabels]
        if _labels is None:
            labels = None
        elif isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = NotebookSpecLabels.from_dict(_labels)

        name = d.pop("name", UNSET)

        _resources = d.pop("resources", UNSET)
        resources: Union[Unset, Resources]
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = Resources.from_dict(_resources)

        shutdown = d.pop("shutdown", UNSET)

        ssh_public_keys = cast(List[str], d.pop("sshPublicKeys", UNSET))

        timeout_auto_restart = d.pop("timeoutAutoRestart", UNSET)

        unsecure_http = d.pop("unsecureHttp", UNSET)

        volumes = []
        _volumes = d.pop("volumes", UNSET)
        for volumes_item_data in _volumes or []:
            volumes_item = Volume.from_dict(volumes_item_data)

            volumes.append(volumes_item)

        notebook_spec = cls(
            env=env,
            env_vars=env_vars,
            labels=labels,
            name=name,
            resources=resources,
            shutdown=shutdown,
            ssh_public_keys=ssh_public_keys,
            timeout_auto_restart=timeout_auto_restart,
            unsecure_http=unsecure_http,
            volumes=volumes,
        )

        notebook_spec.additional_properties = d
        return notebook_spec

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
