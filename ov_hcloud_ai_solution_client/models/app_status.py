import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_state_history import AppStateHistory
    from ..models.data_sync import DataSync
    from ..models.info import Info
    from ..models.volume_status import VolumeStatus


T = TypeVar("T", bound="AppStatus")


@define
class AppStatus:
    """
    Attributes:
        available_replicas (Union[Unset, int]):
        data_sync (Union[Unset, List['DataSync']]):
        history (Union[Unset, List['AppStateHistory']]):
        info (Union[Unset, Info]):
        info_url (Union[Unset, str]): Return the information UI URL about the app Example:
            https://ui.gra.ai.cloud.ovh.net/app/09b95180-e064-4643-a075-682e57b26036.
        last_transition_date (Union[Unset, None, datetime.datetime]):
        monitoring_url (Union[Unset, None, str]): Return the monitoring/grafana UI URL about the app Example:
            https://monitoring.gra.ai.cloud.ovh.net/d/app-gpu?var-
            app=09b95180-e064-4643-a075-682e57b26036&from=1623229322036.
        state (Union[Unset, str]):
        url (Union[Unset, str]): App access url Example:
            https://1cc98e20-c3f7-4555-ba0c-350524b7b591.app.gra.ai.cloud.ovh.net.
        volumes (Union[Unset, List['VolumeStatus']]):
    """

    available_replicas: Union[Unset, int] = UNSET
    data_sync: Union[Unset, List["DataSync"]] = UNSET
    history: Union[Unset, List["AppStateHistory"]] = UNSET
    info: Union[Unset, "Info"] = UNSET
    info_url: Union[Unset, str] = UNSET
    last_transition_date: Union[Unset, None, datetime.datetime] = UNSET
    monitoring_url: Union[Unset, None, str] = UNSET
    state: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    volumes: Union[Unset, List["VolumeStatus"]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available_replicas = self.available_replicas
        data_sync: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data_sync, Unset):
            data_sync = []
            for data_sync_item_data in self.data_sync:
                data_sync_item = data_sync_item_data.to_dict()

                data_sync.append(data_sync_item)

        history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()

                history.append(history_item)

        info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        info_url = self.info_url
        last_transition_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_transition_date, Unset):
            last_transition_date = self.last_transition_date.isoformat() if self.last_transition_date else None

        monitoring_url = self.monitoring_url
        state = self.state
        url = self.url
        volumes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.volumes, Unset):
            volumes = []
            for volumes_item_data in self.volumes:
                volumes_item = volumes_item_data.to_dict()

                volumes.append(volumes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_replicas is not UNSET:
            field_dict["availableReplicas"] = available_replicas
        if data_sync is not UNSET:
            field_dict["dataSync"] = data_sync
        if history is not UNSET:
            field_dict["history"] = history
        if info is not UNSET:
            field_dict["info"] = info
        if info_url is not UNSET:
            field_dict["infoUrl"] = info_url
        if last_transition_date is not UNSET:
            field_dict["lastTransitionDate"] = last_transition_date
        if monitoring_url is not UNSET:
            field_dict["monitoringUrl"] = monitoring_url
        if state is not UNSET:
            field_dict["state"] = state
        if url is not UNSET:
            field_dict["url"] = url
        if volumes is not UNSET:
            field_dict["volumes"] = volumes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.app_state_history import AppStateHistory
        from ..models.data_sync import DataSync
        from ..models.info import Info
        from ..models.volume_status import VolumeStatus

        d = src_dict.copy()
        available_replicas = d.pop("availableReplicas", UNSET)

        data_sync = []
        _data_sync = d.pop("dataSync", UNSET)
        for data_sync_item_data in _data_sync or []:
            data_sync_item = DataSync.from_dict(data_sync_item_data)

            data_sync.append(data_sync_item)

        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in _history or []:
            history_item = AppStateHistory.from_dict(history_item_data)

            history.append(history_item)

        _info = d.pop("info", UNSET)
        info: Union[Unset, Info]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = Info.from_dict(_info)

        info_url = d.pop("infoUrl", UNSET)

        _last_transition_date = d.pop("lastTransitionDate", UNSET)
        last_transition_date: Union[Unset, None, datetime.datetime]
        if _last_transition_date is None:
            last_transition_date = None
        elif isinstance(_last_transition_date, Unset):
            last_transition_date = UNSET
        else:
            last_transition_date = isoparse(_last_transition_date)

        monitoring_url = d.pop("monitoringUrl", UNSET)

        state = d.pop("state", UNSET)

        url = d.pop("url", UNSET)

        volumes = []
        _volumes = d.pop("volumes", UNSET)
        for volumes_item_data in _volumes or []:
            volumes_item = VolumeStatus.from_dict(volumes_item_data)

            volumes.append(volumes_item)

        app_status = cls(
            available_replicas=available_replicas,
            data_sync=data_sync,
            history=history,
            info=info,
            info_url=info_url,
            last_transition_date=last_transition_date,
            monitoring_url=monitoring_url,
            state=state,
            url=url,
            volumes=volumes,
        )

        app_status.additional_properties = d
        return app_status

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
