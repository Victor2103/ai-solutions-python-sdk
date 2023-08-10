import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_sync import DataSync
    from ..models.info import Info
    from ..models.job_state_history import JobStateHistory
    from ..models.volume_status import VolumeStatus


T = TypeVar("T", bound="JobStatus")


@define
class JobStatus:
    """
    Attributes:
        data_sync (Union[Unset, List['DataSync']]):
        duration (Union[Unset, int]): Time since the job is RUNNING in seconds
        exit_code (Union[Unset, None, int]): If job is terminated, return the exit code of the job
        external_ip (Union[Unset, None, str]): Job External IP
        finalized_at (Union[Unset, None, datetime.datetime]):
        history (Union[Unset, List['JobStateHistory']]):
        info (Union[Unset, Info]):
        info_url (Union[Unset, str]): Return the information UI URL about the job Example:
            https://ui.gra.ai.cloud.ovh.net/job/09b95180-e064-4643-a075-682e57b26036.
        initializing_at (Union[Unset, None, datetime.datetime]):
        ip (Union[Unset, None, str]): Job internal IP
        last_transition_date (Union[Unset, None, datetime.datetime]):
        monitoring_url (Union[Unset, None, str]): Return the monitoring/grafana UI URL about the job Example:
            https://monitoring.gra.ai.cloud.ovh.net/d/gpu?var-job=09b95180-e064-4643-a075-682e57b26036&from=1623229322036.
        queued_at (Union[Unset, None, datetime.datetime]):
        ssh_url (Union[Unset, None, str]): Return ssh host and user to connect Example:
            ssh://1cc98e20-c3f7-4555-ba0c-350524b7b591@gra.ai.cloud.ovh.net.
        started_at (Union[Unset, None, datetime.datetime]):
        state (Union[Unset, str]):
        stopped_at (Union[Unset, None, datetime.datetime]):
        timeout_at (Union[Unset, None, datetime.datetime]):
        url (Union[Unset, str]): Job access url Example:
            https://1cc98e20-c3f7-4555-ba0c-350524b7b591.job.gra.ai.cloud.ovh.net.
        volumes (Union[Unset, List['VolumeStatus']]):
    """

    data_sync: Union[Unset, List["DataSync"]] = UNSET
    duration: Union[Unset, int] = UNSET
    exit_code: Union[Unset, None, int] = UNSET
    external_ip: Union[Unset, None, str] = UNSET
    finalized_at: Union[Unset, None, datetime.datetime] = UNSET
    history: Union[Unset, List["JobStateHistory"]] = UNSET
    info: Union[Unset, "Info"] = UNSET
    info_url: Union[Unset, str] = UNSET
    initializing_at: Union[Unset, None, datetime.datetime] = UNSET
    ip: Union[Unset, None, str] = UNSET
    last_transition_date: Union[Unset, None, datetime.datetime] = UNSET
    monitoring_url: Union[Unset, None, str] = UNSET
    queued_at: Union[Unset, None, datetime.datetime] = UNSET
    ssh_url: Union[Unset, None, str] = UNSET
    started_at: Union[Unset, None, datetime.datetime] = UNSET
    state: Union[Unset, str] = UNSET
    stopped_at: Union[Unset, None, datetime.datetime] = UNSET
    timeout_at: Union[Unset, None, datetime.datetime] = UNSET
    url: Union[Unset, str] = UNSET
    volumes: Union[Unset, List["VolumeStatus"]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_sync: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data_sync, Unset):
            data_sync = []
            for data_sync_item_data in self.data_sync:
                data_sync_item = data_sync_item_data.to_dict()

                data_sync.append(data_sync_item)

        duration = self.duration
        exit_code = self.exit_code
        external_ip = self.external_ip
        finalized_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.finalized_at, Unset):
            finalized_at = self.finalized_at.isoformat() if self.finalized_at else None

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
        initializing_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.initializing_at, Unset):
            initializing_at = self.initializing_at.isoformat() if self.initializing_at else None

        ip = self.ip
        last_transition_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_transition_date, Unset):
            last_transition_date = self.last_transition_date.isoformat() if self.last_transition_date else None

        monitoring_url = self.monitoring_url
        queued_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.queued_at, Unset):
            queued_at = self.queued_at.isoformat() if self.queued_at else None

        ssh_url = self.ssh_url
        started_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat() if self.started_at else None

        state = self.state
        stopped_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.stopped_at, Unset):
            stopped_at = self.stopped_at.isoformat() if self.stopped_at else None

        timeout_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.timeout_at, Unset):
            timeout_at = self.timeout_at.isoformat() if self.timeout_at else None

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
        if data_sync is not UNSET:
            field_dict["dataSync"] = data_sync
        if duration is not UNSET:
            field_dict["duration"] = duration
        if exit_code is not UNSET:
            field_dict["exitCode"] = exit_code
        if external_ip is not UNSET:
            field_dict["externalIp"] = external_ip
        if finalized_at is not UNSET:
            field_dict["finalizedAt"] = finalized_at
        if history is not UNSET:
            field_dict["history"] = history
        if info is not UNSET:
            field_dict["info"] = info
        if info_url is not UNSET:
            field_dict["infoUrl"] = info_url
        if initializing_at is not UNSET:
            field_dict["initializingAt"] = initializing_at
        if ip is not UNSET:
            field_dict["ip"] = ip
        if last_transition_date is not UNSET:
            field_dict["lastTransitionDate"] = last_transition_date
        if monitoring_url is not UNSET:
            field_dict["monitoringUrl"] = monitoring_url
        if queued_at is not UNSET:
            field_dict["queuedAt"] = queued_at
        if ssh_url is not UNSET:
            field_dict["sshUrl"] = ssh_url
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if state is not UNSET:
            field_dict["state"] = state
        if stopped_at is not UNSET:
            field_dict["stoppedAt"] = stopped_at
        if timeout_at is not UNSET:
            field_dict["timeoutAt"] = timeout_at
        if url is not UNSET:
            field_dict["url"] = url
        if volumes is not UNSET:
            field_dict["volumes"] = volumes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_sync import DataSync
        from ..models.info import Info
        from ..models.job_state_history import JobStateHistory
        from ..models.volume_status import VolumeStatus

        d = src_dict.copy()
        data_sync = []
        _data_sync = d.pop("dataSync", UNSET)
        for data_sync_item_data in _data_sync or []:
            data_sync_item = DataSync.from_dict(data_sync_item_data)

            data_sync.append(data_sync_item)

        duration = d.pop("duration", UNSET)

        exit_code = d.pop("exitCode", UNSET)

        external_ip = d.pop("externalIp", UNSET)

        _finalized_at = d.pop("finalizedAt", UNSET)
        finalized_at: Union[Unset, None, datetime.datetime]
        if _finalized_at is None:
            finalized_at = None
        elif isinstance(_finalized_at, Unset):
            finalized_at = UNSET
        else:
            finalized_at = isoparse(_finalized_at)

        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in _history or []:
            history_item = JobStateHistory.from_dict(history_item_data)

            history.append(history_item)

        _info = d.pop("info", UNSET)
        info: Union[Unset, Info]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = Info.from_dict(_info)

        info_url = d.pop("infoUrl", UNSET)

        _initializing_at = d.pop("initializingAt", UNSET)
        initializing_at: Union[Unset, None, datetime.datetime]
        if _initializing_at is None:
            initializing_at = None
        elif isinstance(_initializing_at, Unset):
            initializing_at = UNSET
        else:
            initializing_at = isoparse(_initializing_at)

        ip = d.pop("ip", UNSET)

        _last_transition_date = d.pop("lastTransitionDate", UNSET)
        last_transition_date: Union[Unset, None, datetime.datetime]
        if _last_transition_date is None:
            last_transition_date = None
        elif isinstance(_last_transition_date, Unset):
            last_transition_date = UNSET
        else:
            last_transition_date = isoparse(_last_transition_date)

        monitoring_url = d.pop("monitoringUrl", UNSET)

        _queued_at = d.pop("queuedAt", UNSET)
        queued_at: Union[Unset, None, datetime.datetime]
        if _queued_at is None:
            queued_at = None
        elif isinstance(_queued_at, Unset):
            queued_at = UNSET
        else:
            queued_at = isoparse(_queued_at)

        ssh_url = d.pop("sshUrl", UNSET)

        _started_at = d.pop("startedAt", UNSET)
        started_at: Union[Unset, None, datetime.datetime]
        if _started_at is None:
            started_at = None
        elif isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        state = d.pop("state", UNSET)

        _stopped_at = d.pop("stoppedAt", UNSET)
        stopped_at: Union[Unset, None, datetime.datetime]
        if _stopped_at is None:
            stopped_at = None
        elif isinstance(_stopped_at, Unset):
            stopped_at = UNSET
        else:
            stopped_at = isoparse(_stopped_at)

        _timeout_at = d.pop("timeoutAt", UNSET)
        timeout_at: Union[Unset, None, datetime.datetime]
        if _timeout_at is None:
            timeout_at = None
        elif isinstance(_timeout_at, Unset):
            timeout_at = UNSET
        else:
            timeout_at = isoparse(_timeout_at)

        url = d.pop("url", UNSET)

        volumes = []
        _volumes = d.pop("volumes", UNSET)
        for volumes_item_data in _volumes or []:
            volumes_item = VolumeStatus.from_dict(volumes_item_data)

            volumes.append(volumes_item)

        job_status = cls(
            data_sync=data_sync,
            duration=duration,
            exit_code=exit_code,
            external_ip=external_ip,
            finalized_at=finalized_at,
            history=history,
            info=info,
            info_url=info_url,
            initializing_at=initializing_at,
            ip=ip,
            last_transition_date=last_transition_date,
            monitoring_url=monitoring_url,
            queued_at=queued_at,
            ssh_url=ssh_url,
            started_at=started_at,
            state=state,
            stopped_at=stopped_at,
            timeout_at=timeout_at,
            url=url,
            volumes=volumes,
        )

        job_status.additional_properties = d
        return job_status

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
