# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'ConfigPartArgs',
    'GetConfigPartArgs',
]

@pulumi.input_type
class ConfigPartArgs:
    def __init__(__self__, *,
                 content: pulumi.Input[str],
                 content_type: Optional[pulumi.Input[str]] = None,
                 filename: Optional[pulumi.Input[str]] = None,
                 merge_type: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "content", content)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if filename is not None:
            pulumi.set(__self__, "filename", filename)
        if merge_type is not None:
            pulumi.set(__self__, "merge_type", merge_type)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter
    def filename(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "filename")

    @filename.setter
    def filename(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filename", value)

    @property
    @pulumi.getter(name="mergeType")
    def merge_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "merge_type")

    @merge_type.setter
    def merge_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "merge_type", value)


@pulumi.input_type
class GetConfigPartArgs:
    def __init__(__self__, *,
                 content: str,
                 content_type: Optional[str] = None,
                 filename: Optional[str] = None,
                 merge_type: Optional[str] = None):
        """
        :param str content: Body content for the part.
        :param str content_type: A MIME-style content type to report in the header for the part.
        :param str filename: A filename to report in the header for the part.
        :param str merge_type: A value for the `X-Merge-Type` header of the part,
               to control [cloud-init merging behavior](https://cloudinit.readthedocs.io/en/latest/topics/merging.html).
        """
        pulumi.set(__self__, "content", content)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if filename is not None:
            pulumi.set(__self__, "filename", filename)
        if merge_type is not None:
            pulumi.set(__self__, "merge_type", merge_type)

    @property
    @pulumi.getter
    def content(self) -> str:
        """
        Body content for the part.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: str):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[str]:
        """
        A MIME-style content type to report in the header for the part.
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[str]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter
    def filename(self) -> Optional[str]:
        """
        A filename to report in the header for the part.
        """
        return pulumi.get(self, "filename")

    @filename.setter
    def filename(self, value: Optional[str]):
        pulumi.set(self, "filename", value)

    @property
    @pulumi.getter(name="mergeType")
    def merge_type(self) -> Optional[str]:
        """
        A value for the `X-Merge-Type` header of the part,
        to control [cloud-init merging behavior](https://cloudinit.readthedocs.io/en/latest/topics/merging.html).
        """
        return pulumi.get(self, "merge_type")

    @merge_type.setter
    def merge_type(self, value: Optional[str]):
        pulumi.set(self, "merge_type", value)


