from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define, field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notebook_spec_update_labels import NotebookSpecUpdateLabels
    from ..models.resources import Resources
    from ..models.volume import Volume


T = TypeVar("T", bound="NotebookSpecUpdate")


@define
class NotebookSpecUpdate:
    """
    Attributes:
        labels (Union[Unset, None, NotebookSpecUpdateLabels]):
        resources (Union[Unset, Resources]):
        ssh_public_keys (Union[Unset, None, List[str]]): SSH Public keys allowed to SSH into the notebook
        timeout_auto_restart (Union[Unset, None, bool]): Auto restart notebook on timeout
        unsecure_http (Union[Unset, None, bool]):
        volumes (Union[Unset, None, List['Volume']]):
    """

    labels: Union[Unset, None, "NotebookSpecUpdateLabels"] = UNSET
    resources: Union[Unset, "Resources"] = UNSET
    ssh_public_keys: Union[Unset, None, List[str]] = UNSET
    timeout_auto_restart: Union[Unset, None, bool] = UNSET
    unsecure_http: Union[Unset, None, bool] = UNSET
    volumes: Union[Unset, None, List["Volume"]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        labels: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict() if self.labels else None

        resources: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

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
        if labels is not UNSET:
            field_dict["labels"] = labels
        if resources is not UNSET:
            field_dict["resources"] = resources
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
        from ..models.notebook_spec_update_labels import NotebookSpecUpdateLabels
        from ..models.resources import Resources
        from ..models.volume import Volume

        d = src_dict.copy()
        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, None, NotebookSpecUpdateLabels]
        if _labels is None:
            labels = None
        elif isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = NotebookSpecUpdateLabels.from_dict(_labels)

        _resources = d.pop("resources", UNSET)
        resources: Union[Unset, Resources]
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = Resources.from_dict(_resources)

        ssh_public_keys = cast(List[str], d.pop("sshPublicKeys", UNSET))

        timeout_auto_restart = d.pop("timeoutAutoRestart", UNSET)

        unsecure_http = d.pop("unsecureHttp", UNSET)

        volumes = []
        _volumes = d.pop("volumes", UNSET)
        for volumes_item_data in _volumes or []:
            volumes_item = Volume.from_dict(volumes_item_data)

            volumes.append(volumes_item)

        notebook_spec_update = cls(
            labels=labels,
            resources=resources,
            ssh_public_keys=ssh_public_keys,
            timeout_auto_restart=timeout_auto_restart,
            unsecure_http=unsecure_http,
            volumes=volumes,
        )

        notebook_spec_update.additional_properties = d
        return notebook_spec_update

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
