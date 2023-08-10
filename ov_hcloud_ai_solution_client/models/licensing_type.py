from enum import Enum


class LicensingType(str, Enum):
    PER_APP = "per-app"
    PER_REPLICA = "per-replica"
    PER_RESOURCE = "per-resource"

    def __str__(self) -> str:
        return str(self.value)
