# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ConfigArgs', 'Config']

@pulumi.input_type
class ConfigArgs:
    def __init__(__self__, *,
                 parts: pulumi.Input[Sequence[pulumi.Input['ConfigPartArgs']]],
                 base64_encode: Optional[pulumi.Input[bool]] = None,
                 boundary: Optional[pulumi.Input[str]] = None,
                 gzip: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Config resource.
        """
        pulumi.set(__self__, "parts", parts)
        if base64_encode is not None:
            pulumi.set(__self__, "base64_encode", base64_encode)
        if boundary is not None:
            pulumi.set(__self__, "boundary", boundary)
        if gzip is not None:
            pulumi.set(__self__, "gzip", gzip)

    @property
    @pulumi.getter
    def parts(self) -> pulumi.Input[Sequence[pulumi.Input['ConfigPartArgs']]]:
        return pulumi.get(self, "parts")

    @parts.setter
    def parts(self, value: pulumi.Input[Sequence[pulumi.Input['ConfigPartArgs']]]):
        pulumi.set(self, "parts", value)

    @property
    @pulumi.getter(name="base64Encode")
    def base64_encode(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "base64_encode")

    @base64_encode.setter
    def base64_encode(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "base64_encode", value)

    @property
    @pulumi.getter
    def boundary(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "boundary")

    @boundary.setter
    def boundary(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "boundary", value)

    @property
    @pulumi.getter
    def gzip(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "gzip")

    @gzip.setter
    def gzip(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "gzip", value)


@pulumi.input_type
class _ConfigState:
    def __init__(__self__, *,
                 base64_encode: Optional[pulumi.Input[bool]] = None,
                 boundary: Optional[pulumi.Input[str]] = None,
                 gzip: Optional[pulumi.Input[bool]] = None,
                 parts: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigPartArgs']]]] = None,
                 rendered: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Config resources.
        :param pulumi.Input[str] rendered: rendered cloudinit configuration
        """
        if base64_encode is not None:
            pulumi.set(__self__, "base64_encode", base64_encode)
        if boundary is not None:
            pulumi.set(__self__, "boundary", boundary)
        if gzip is not None:
            pulumi.set(__self__, "gzip", gzip)
        if parts is not None:
            pulumi.set(__self__, "parts", parts)
        if rendered is not None:
            pulumi.set(__self__, "rendered", rendered)

    @property
    @pulumi.getter(name="base64Encode")
    def base64_encode(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "base64_encode")

    @base64_encode.setter
    def base64_encode(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "base64_encode", value)

    @property
    @pulumi.getter
    def boundary(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "boundary")

    @boundary.setter
    def boundary(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "boundary", value)

    @property
    @pulumi.getter
    def gzip(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "gzip")

    @gzip.setter
    def gzip(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "gzip", value)

    @property
    @pulumi.getter
    def parts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConfigPartArgs']]]]:
        return pulumi.get(self, "parts")

    @parts.setter
    def parts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigPartArgs']]]]):
        pulumi.set(self, "parts", value)

    @property
    @pulumi.getter
    def rendered(self) -> Optional[pulumi.Input[str]]:
        """
        rendered cloudinit configuration
        """
        return pulumi.get(self, "rendered")

    @rendered.setter
    def rendered(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rendered", value)


class Config(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base64_encode: Optional[pulumi.Input[bool]] = None,
                 boundary: Optional[pulumi.Input[str]] = None,
                 gzip: Optional[pulumi.Input[bool]] = None,
                 parts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigPartArgs']]]]] = None,
                 __props__=None):
        """
        Create a Config resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Config resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base64_encode: Optional[pulumi.Input[bool]] = None,
                 boundary: Optional[pulumi.Input[str]] = None,
                 gzip: Optional[pulumi.Input[bool]] = None,
                 parts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigPartArgs']]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigArgs.__new__(ConfigArgs)

            __props__.__dict__["base64_encode"] = base64_encode
            __props__.__dict__["boundary"] = boundary
            __props__.__dict__["gzip"] = gzip
            if parts is None and not opts.urn:
                raise TypeError("Missing required property 'parts'")
            __props__.__dict__["parts"] = parts
            __props__.__dict__["rendered"] = None
        super(Config, __self__).__init__(
            'cloudinit:index/config:Config',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            base64_encode: Optional[pulumi.Input[bool]] = None,
            boundary: Optional[pulumi.Input[str]] = None,
            gzip: Optional[pulumi.Input[bool]] = None,
            parts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigPartArgs']]]]] = None,
            rendered: Optional[pulumi.Input[str]] = None) -> 'Config':
        """
        Get an existing Config resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] rendered: rendered cloudinit configuration
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConfigState.__new__(_ConfigState)

        __props__.__dict__["base64_encode"] = base64_encode
        __props__.__dict__["boundary"] = boundary
        __props__.__dict__["gzip"] = gzip
        __props__.__dict__["parts"] = parts
        __props__.__dict__["rendered"] = rendered
        return Config(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="base64Encode")
    def base64_encode(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "base64_encode")

    @property
    @pulumi.getter
    def boundary(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "boundary")

    @property
    @pulumi.getter
    def gzip(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "gzip")

    @property
    @pulumi.getter
    def parts(self) -> pulumi.Output[Sequence['outputs.ConfigPart']]:
        return pulumi.get(self, "parts")

    @property
    @pulumi.getter
    def rendered(self) -> pulumi.Output[str]:
        """
        rendered cloudinit configuration
        """
        return pulumi.get(self, "rendered")

