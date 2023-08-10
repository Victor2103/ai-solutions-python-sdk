from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define, field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.env import Env
    from ..models.job_spec_labels import JobSpecLabels
    from ..models.resources import Resources
    from ..models.volume import Volume


T = TypeVar("T", bound="JobSpec")


@define
class JobSpec:
    """
    Attributes:
        image (str): Docker image to use in the job Example: ubuntu.
        command (Union[Unset, None, List[str]]): Job command to run Example: ['python3', 'script.py'].
        default_http_port (Union[Unset, int]):  Default: 8080. Example: 8080.
        deletion_requested (Union[Unset, bool]):
        env_vars (Union[Unset, None, List['Env']]): Environment variables that will be injected into the job
        labels (Union[Unset, None, JobSpecLabels]): some label, used to scope tokens, labels prefixed by 'ovh/' are
            owned by the platform and overridden Example: {'label': 'some-label'}.
        name (Union[Unset, None, str]): Job name, generated if not provided Example: funny-ubuntu.
        resources (Union[Unset, Resources]):
        shutdown (Union[Unset, None, str]):
        ssh_public_keys (Union[Unset, None, List[str]]): SSH Public to be able to connect through SSH on the job
        timeout (Union[Unset, int]): Time in second after the job will shutdown automatically
        timeout_auto_restart (Union[Unset, bool]): If set to true, the job will be rescheduled after a timeout
        unsecure_http (Union[Unset, bool]): true if job api port can be accessed without any authentication token, false
            otherwise
        volumes (Union[Unset, None, List['Volume']]):
    """

    image: str
    command: Union[Unset, None, List[str]] = UNSET
    default_http_port: Union[Unset, int] = 8080
    deletion_requested: Union[Unset, bool] = UNSET
    env_vars: Union[Unset, None, List["Env"]] = UNSET
    labels: Union[Unset, None, "JobSpecLabels"] = UNSET
    name: Union[Unset, None, str] = UNSET
    resources: Union[Unset, "Resources"] = UNSET
    shutdown: Union[Unset, None, str] = UNSET
    ssh_public_keys: Union[Unset, None, List[str]] = UNSET
    timeout: Union[Unset, int] = 0
    timeout_auto_restart: Union[Unset, bool] = False
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

        timeout = self.timeout
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
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
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
        from ..models.job_spec_labels import JobSpecLabels
        from ..models.resources import Resources
        from ..models.volume import Volume

        d = src_dict.copy()
        image = d.pop("image")

        command = cast(List[str], d.pop("command", UNSET))

        default_http_port = d.pop("defaultHttpPort", UNSET)

        deletion_requested = d.pop("deletionRequested", UNSET)

        env_vars = []
        _env_vars = d.pop("envVars", UNSET)
        for env_vars_item_data in _env_vars or []:
            env_vars_item = Env.from_dict(env_vars_item_data)

            env_vars.append(env_vars_item)

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, None, JobSpecLabels]
        if _labels is None:
            labels = None
        elif isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = JobSpecLabels.from_dict(_labels)

        name = d.pop("name", UNSET)

        _resources = d.pop("resources", UNSET)
        resources: Union[Unset, Resources]
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = Resources.from_dict(_resources)

        shutdown = d.pop("shutdown", UNSET)

        ssh_public_keys = cast(List[str], d.pop("sshPublicKeys", UNSET))

        timeout = d.pop("timeout", UNSET)

        timeout_auto_restart = d.pop("timeoutAutoRestart", UNSET)

        unsecure_http = d.pop("unsecureHttp", UNSET)

        volumes = []
        _volumes = d.pop("volumes", UNSET)
        for volumes_item_data in _volumes or []:
            volumes_item = Volume.from_dict(volumes_item_data)

            volumes.append(volumes_item)

        job_spec = cls(
            image=image,
            command=command,
            default_http_port=default_http_port,
            deletion_requested=deletion_requested,
            env_vars=env_vars,
            labels=labels,
            name=name,
            resources=resources,
            shutdown=shutdown,
            ssh_public_keys=ssh_public_keys,
            timeout=timeout,
            timeout_auto_restart=timeout_auto_restart,
            unsecure_http=unsecure_http,
            volumes=volumes,
        )

        job_spec.additional_properties = d
        return job_spec

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
