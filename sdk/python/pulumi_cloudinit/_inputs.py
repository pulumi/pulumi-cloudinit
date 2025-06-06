# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = [
    'ConfigPartArgs',
    'ConfigPartArgsDict',
    'GetConfigPartArgs',
    'GetConfigPartArgsDict',
]

MYPY = False

if not MYPY:
    class ConfigPartArgsDict(TypedDict):
        content: pulumi.Input[builtins.str]
        """
        Body content for the part.
        """
        content_type: NotRequired[pulumi.Input[builtins.str]]
        """
        A MIME-style content type to report in the header for the part. Defaults to `text/plain`
        """
        filename: NotRequired[pulumi.Input[builtins.str]]
        """
        A filename to report in the header for the part.
        """
        merge_type: NotRequired[pulumi.Input[builtins.str]]
        """
        A value for the `X-Merge-Type` header of the part, to control [cloud-init merging behavior](https://cloudinit.readthedocs.io/en/latest/reference/merging.html).
        """
elif False:
    ConfigPartArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ConfigPartArgs:
    def __init__(__self__, *,
                 content: pulumi.Input[builtins.str],
                 content_type: Optional[pulumi.Input[builtins.str]] = None,
                 filename: Optional[pulumi.Input[builtins.str]] = None,
                 merge_type: Optional[pulumi.Input[builtins.str]] = None):
        """
        :param pulumi.Input[builtins.str] content: Body content for the part.
        :param pulumi.Input[builtins.str] content_type: A MIME-style content type to report in the header for the part. Defaults to `text/plain`
        :param pulumi.Input[builtins.str] filename: A filename to report in the header for the part.
        :param pulumi.Input[builtins.str] merge_type: A value for the `X-Merge-Type` header of the part, to control [cloud-init merging behavior](https://cloudinit.readthedocs.io/en/latest/reference/merging.html).
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
    def content(self) -> pulumi.Input[builtins.str]:
        """
        Body content for the part.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A MIME-style content type to report in the header for the part. Defaults to `text/plain`
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter
    def filename(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A filename to report in the header for the part.
        """
        return pulumi.get(self, "filename")

    @filename.setter
    def filename(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "filename", value)

    @property
    @pulumi.getter(name="mergeType")
    def merge_type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A value for the `X-Merge-Type` header of the part, to control [cloud-init merging behavior](https://cloudinit.readthedocs.io/en/latest/reference/merging.html).
        """
        return pulumi.get(self, "merge_type")

    @merge_type.setter
    def merge_type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "merge_type", value)


if not MYPY:
    class GetConfigPartArgsDict(TypedDict):
        content: builtins.str
        """
        Body content for the part.
        """
        content_type: NotRequired[builtins.str]
        """
        A MIME-style content type to report in the header for the part. Defaults to `text/plain`
        """
        filename: NotRequired[builtins.str]
        """
        A filename to report in the header for the part.
        """
        merge_type: NotRequired[builtins.str]
        """
        A value for the `X-Merge-Type` header of the part, to control [cloud-init merging behavior](https://cloudinit.readthedocs.io/en/latest/reference/merging.html).
        """
elif False:
    GetConfigPartArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetConfigPartArgs:
    def __init__(__self__, *,
                 content: builtins.str,
                 content_type: Optional[builtins.str] = None,
                 filename: Optional[builtins.str] = None,
                 merge_type: Optional[builtins.str] = None):
        """
        :param builtins.str content: Body content for the part.
        :param builtins.str content_type: A MIME-style content type to report in the header for the part. Defaults to `text/plain`
        :param builtins.str filename: A filename to report in the header for the part.
        :param builtins.str merge_type: A value for the `X-Merge-Type` header of the part, to control [cloud-init merging behavior](https://cloudinit.readthedocs.io/en/latest/reference/merging.html).
        """
        pulumi.set(__self__, "content", content)
        if content_type is None:
            content_type = 'text/plain'
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if filename is not None:
            pulumi.set(__self__, "filename", filename)
        if merge_type is not None:
            pulumi.set(__self__, "merge_type", merge_type)

    @property
    @pulumi.getter
    def content(self) -> builtins.str:
        """
        Body content for the part.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: builtins.str):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[builtins.str]:
        """
        A MIME-style content type to report in the header for the part. Defaults to `text/plain`
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[builtins.str]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter
    def filename(self) -> Optional[builtins.str]:
        """
        A filename to report in the header for the part.
        """
        return pulumi.get(self, "filename")

    @filename.setter
    def filename(self, value: Optional[builtins.str]):
        pulumi.set(self, "filename", value)

    @property
    @pulumi.getter(name="mergeType")
    def merge_type(self) -> Optional[builtins.str]:
        """
        A value for the `X-Merge-Type` header of the part, to control [cloud-init merging behavior](https://cloudinit.readthedocs.io/en/latest/reference/merging.html).
        """
        return pulumi.get(self, "merge_type")

    @merge_type.setter
    def merge_type(self, value: Optional[builtins.str]):
        pulumi.set(self, "merge_type", value)


