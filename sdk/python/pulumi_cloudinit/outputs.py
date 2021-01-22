# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'ConfigPart',
    'GetConfigPartResult',
]

@pulumi.output_type
class ConfigPart(dict):
    def __init__(__self__, *,
                 content: str,
                 content_type: Optional[str] = None,
                 filename: Optional[str] = None,
                 merge_type: Optional[str] = None):
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
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[str]:
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter
    def filename(self) -> Optional[str]:
        return pulumi.get(self, "filename")

    @property
    @pulumi.getter(name="mergeType")
    def merge_type(self) -> Optional[str]:
        return pulumi.get(self, "merge_type")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetConfigPartResult(dict):
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

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[str]:
        """
        A MIME-style content type to report in the header for the part.
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter
    def filename(self) -> Optional[str]:
        """
        A filename to report in the header for the part.
        """
        return pulumi.get(self, "filename")

    @property
    @pulumi.getter(name="mergeType")
    def merge_type(self) -> Optional[str]:
        """
        A value for the `X-Merge-Type` header of the part,
        to control [cloud-init merging behavior](https://cloudinit.readthedocs.io/en/latest/topics/merging.html).
        """
        return pulumi.get(self, "merge_type")


