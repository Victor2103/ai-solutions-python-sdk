from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_store_volume_source import DataStoreVolumeSource
    from ..models.private_swift_volume_source import PrivateSwiftVolumeSource
    from ..models.public_git_volume_source import PublicGitVolumeSource
    from ..models.public_swift_volume_source import PublicSwiftVolumeSource
    from ..models.standalone_volume_source import StandaloneVolumeSource


T = TypeVar("T", bound="VolumeSource")


@define
class VolumeSource:
    """
    Attributes:
        data_store (Union[Unset, DataStoreVolumeSource]):
        private_swift (Union[Unset, PrivateSwiftVolumeSource]):
        public_git (Union[Unset, PublicGitVolumeSource]):
        public_swift (Union[Unset, PublicSwiftVolumeSource]):
        standalone (Union[Unset, StandaloneVolumeSource]):
    """

    data_store: Union[Unset, "DataStoreVolumeSource"] = UNSET
    private_swift: Union[Unset, "PrivateSwiftVolumeSource"] = UNSET
    public_git: Union[Unset, "PublicGitVolumeSource"] = UNSET
    public_swift: Union[Unset, "PublicSwiftVolumeSource"] = UNSET
    standalone: Union[Unset, "StandaloneVolumeSource"] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_store: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_store, Unset):
            data_store = self.data_store.to_dict()

        private_swift: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.private_swift, Unset):
            private_swift = self.private_swift.to_dict()

        public_git: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.public_git, Unset):
            public_git = self.public_git.to_dict()

        public_swift: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.public_swift, Unset):
            public_swift = self.public_swift.to_dict()

        standalone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standalone, Unset):
            standalone = self.standalone.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_store is not UNSET:
            field_dict["dataStore"] = data_store
        if private_swift is not UNSET:
            field_dict["privateSwift"] = private_swift
        if public_git is not UNSET:
            field_dict["publicGit"] = public_git
        if public_swift is not UNSET:
            field_dict["publicSwift"] = public_swift
        if standalone is not UNSET:
            field_dict["standalone"] = standalone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_store_volume_source import DataStoreVolumeSource
        from ..models.private_swift_volume_source import PrivateSwiftVolumeSource
        from ..models.public_git_volume_source import PublicGitVolumeSource
        from ..models.public_swift_volume_source import PublicSwiftVolumeSource
        from ..models.standalone_volume_source import StandaloneVolumeSource

        d = src_dict.copy()
        _data_store = d.pop("dataStore", UNSET)
        data_store: Union[Unset, DataStoreVolumeSource]
        if isinstance(_data_store, Unset):
            data_store = UNSET
        else:
            data_store = DataStoreVolumeSource.from_dict(_data_store)

        _private_swift = d.pop("privateSwift", UNSET)
        private_swift: Union[Unset, PrivateSwiftVolumeSource]
        if isinstance(_private_swift, Unset):
            private_swift = UNSET
        else:
            private_swift = PrivateSwiftVolumeSource.from_dict(_private_swift)

        _public_git = d.pop("publicGit", UNSET)
        public_git: Union[Unset, PublicGitVolumeSource]
        if isinstance(_public_git, Unset):
            public_git = UNSET
        else:
            public_git = PublicGitVolumeSource.from_dict(_public_git)

        _public_swift = d.pop("publicSwift", UNSET)
        public_swift: Union[Unset, PublicSwiftVolumeSource]
        if isinstance(_public_swift, Unset):
            public_swift = UNSET
        else:
            public_swift = PublicSwiftVolumeSource.from_dict(_public_swift)

        _standalone = d.pop("standalone", UNSET)
        standalone: Union[Unset, StandaloneVolumeSource]
        if isinstance(_standalone, Unset):
            standalone = UNSET
        else:
            standalone = StandaloneVolumeSource.from_dict(_standalone)

        volume_source = cls(
            data_store=data_store,
            private_swift=private_swift,
            public_git=public_git,
            public_swift=public_swift,
            standalone=standalone,
        )

        volume_source.additional_properties = d
        return volume_source

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
