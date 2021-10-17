# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'ReleaseStatus',
]

@pulumi.output_type
class ReleaseStatus(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "appVersion":
            suggest = "app_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ReleaseStatus. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ReleaseStatus.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ReleaseStatus.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 app_version: str,
                 chart: str,
                 name: str,
                 namespace: str,
                 revision: int,
                 status: str,
                 version: str):
        """
        :param str app_version: The version number of the application being deployed.
        :param str chart: The name of the chart.
        :param str name: Name is the name of the release.
        :param str namespace: Namespace is the kubernetes namespace of the release.
        :param int revision: Version is an int32 which represents the version of the release.
        :param str status: Status of the release.
        :param str version: A SemVer 2 conformant version string of the chart.
        """
        pulumi.set(__self__, "app_version", app_version)
        pulumi.set(__self__, "chart", chart)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "revision", revision)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="appVersion")
    def app_version(self) -> str:
        """
        The version number of the application being deployed.
        """
        return pulumi.get(self, "app_version")

    @property
    @pulumi.getter
    def chart(self) -> str:
        """
        The name of the chart.
        """
        return pulumi.get(self, "chart")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name is the name of the release.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        """
        Namespace is the kubernetes namespace of the release.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def revision(self) -> int:
        """
        Version is an int32 which represents the version of the release.
        """
        return pulumi.get(self, "revision")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the release.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        A SemVer 2 conformant version string of the chart.
        """
        return pulumi.get(self, "version")


