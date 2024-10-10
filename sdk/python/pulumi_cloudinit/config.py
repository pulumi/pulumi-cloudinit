# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

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
from . import outputs
from ._inputs import *

__all__ = ['ConfigArgs', 'Config']

@pulumi.input_type
class ConfigArgs:
    def __init__(__self__, *,
                 base64_encode: Optional[pulumi.Input[bool]] = None,
                 boundary: Optional[pulumi.Input[str]] = None,
                 gzip: Optional[pulumi.Input[bool]] = None,
                 parts: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigPartArgs']]]] = None):
        """
        The set of arguments for constructing a Config resource.
        :param pulumi.Input[bool] base64_encode: Specify whether or not to base64 encode the `rendered` output. Defaults to `true`, and cannot be disabled if gzip is `true`.
        :param pulumi.Input[str] boundary: Specify the Writer's default boundary separator. Defaults to `MIMEBOUNDARY`.
        :param pulumi.Input[bool] gzip: Specify whether or not to gzip the `rendered` output. Defaults to `true`.
        :param pulumi.Input[Sequence[pulumi.Input['ConfigPartArgs']]] parts: A nested block type which adds a file to the generated cloud-init configuration. Use multiple `part` blocks to specify multiple files, which will be included in order of declaration in the final MIME document.
        """
        if base64_encode is not None:
            pulumi.set(__self__, "base64_encode", base64_encode)
        if boundary is not None:
            pulumi.set(__self__, "boundary", boundary)
        if gzip is not None:
            pulumi.set(__self__, "gzip", gzip)
        if parts is not None:
            pulumi.set(__self__, "parts", parts)

    @property
    @pulumi.getter(name="base64Encode")
    def base64_encode(self) -> Optional[pulumi.Input[bool]]:
        """
        Specify whether or not to base64 encode the `rendered` output. Defaults to `true`, and cannot be disabled if gzip is `true`.
        """
        return pulumi.get(self, "base64_encode")

    @base64_encode.setter
    def base64_encode(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "base64_encode", value)

    @property
    @pulumi.getter
    def boundary(self) -> Optional[pulumi.Input[str]]:
        """
        Specify the Writer's default boundary separator. Defaults to `MIMEBOUNDARY`.
        """
        return pulumi.get(self, "boundary")

    @boundary.setter
    def boundary(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "boundary", value)

    @property
    @pulumi.getter
    def gzip(self) -> Optional[pulumi.Input[bool]]:
        """
        Specify whether or not to gzip the `rendered` output. Defaults to `true`.
        """
        return pulumi.get(self, "gzip")

    @gzip.setter
    def gzip(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "gzip", value)

    @property
    @pulumi.getter
    def parts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConfigPartArgs']]]]:
        """
        A nested block type which adds a file to the generated cloud-init configuration. Use multiple `part` blocks to specify multiple files, which will be included in order of declaration in the final MIME document.
        """
        return pulumi.get(self, "parts")

    @parts.setter
    def parts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigPartArgs']]]]):
        pulumi.set(self, "parts", value)


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
        :param pulumi.Input[bool] base64_encode: Specify whether or not to base64 encode the `rendered` output. Defaults to `true`, and cannot be disabled if gzip is `true`.
        :param pulumi.Input[str] boundary: Specify the Writer's default boundary separator. Defaults to `MIMEBOUNDARY`.
        :param pulumi.Input[bool] gzip: Specify whether or not to gzip the `rendered` output. Defaults to `true`.
        :param pulumi.Input[Sequence[pulumi.Input['ConfigPartArgs']]] parts: A nested block type which adds a file to the generated cloud-init configuration. Use multiple `part` blocks to specify multiple files, which will be included in order of declaration in the final MIME document.
        :param pulumi.Input[str] rendered: The final rendered multi-part cloud-init config.
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
        """
        Specify whether or not to base64 encode the `rendered` output. Defaults to `true`, and cannot be disabled if gzip is `true`.
        """
        return pulumi.get(self, "base64_encode")

    @base64_encode.setter
    def base64_encode(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "base64_encode", value)

    @property
    @pulumi.getter
    def boundary(self) -> Optional[pulumi.Input[str]]:
        """
        Specify the Writer's default boundary separator. Defaults to `MIMEBOUNDARY`.
        """
        return pulumi.get(self, "boundary")

    @boundary.setter
    def boundary(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "boundary", value)

    @property
    @pulumi.getter
    def gzip(self) -> Optional[pulumi.Input[bool]]:
        """
        Specify whether or not to gzip the `rendered` output. Defaults to `true`.
        """
        return pulumi.get(self, "gzip")

    @gzip.setter
    def gzip(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "gzip", value)

    @property
    @pulumi.getter
    def parts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConfigPartArgs']]]]:
        """
        A nested block type which adds a file to the generated cloud-init configuration. Use multiple `part` blocks to specify multiple files, which will be included in order of declaration in the final MIME document.
        """
        return pulumi.get(self, "parts")

    @parts.setter
    def parts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigPartArgs']]]]):
        pulumi.set(self, "parts", value)

    @property
    @pulumi.getter
    def rendered(self) -> Optional[pulumi.Input[str]]:
        """
        The final rendered multi-part cloud-init config.
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
                 parts: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ConfigPartArgs', 'ConfigPartArgsDict']]]]] = None,
                 __props__=None):
        """
        > **This resource is deprecated** Please use the Config
          data source instead.

        Renders a [multi-part MIME configuration](https://cloudinit.readthedocs.io/en/latest/explanation/format.html#mime-multi-part-archive) for use with [cloud-init](https://cloudinit.readthedocs.io/en/latest/).

        Cloud-init is a commonly-used startup configuration utility for cloud compute instances. It accepts configuration via provider-specific user data mechanisms, such as `user_data` for Amazon EC2 instances. Multi-part MIME is one of the data formats it accepts. For more information, see [User-Data Formats](https://cloudinit.readthedocs.io/en/latest/explanation/format.html) in the cloud-init manual.

        This is not a generalized utility for producing multi-part MIME messages. It's feature set is specialized for cloud-init multi-part MIME messages.

        ## Example Usage

        ### Config

        ### hello-script.sh

        ### cloud-config.yaml

        <!-- This schema was originally generated with tfplugindocs, then modified manually to ensure `part` block list is noted as Required -->

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] base64_encode: Specify whether or not to base64 encode the `rendered` output. Defaults to `true`, and cannot be disabled if gzip is `true`.
        :param pulumi.Input[str] boundary: Specify the Writer's default boundary separator. Defaults to `MIMEBOUNDARY`.
        :param pulumi.Input[bool] gzip: Specify whether or not to gzip the `rendered` output. Defaults to `true`.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ConfigPartArgs', 'ConfigPartArgsDict']]]] parts: A nested block type which adds a file to the generated cloud-init configuration. Use multiple `part` blocks to specify multiple files, which will be included in order of declaration in the final MIME document.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ConfigArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        > **This resource is deprecated** Please use the Config
          data source instead.

        Renders a [multi-part MIME configuration](https://cloudinit.readthedocs.io/en/latest/explanation/format.html#mime-multi-part-archive) for use with [cloud-init](https://cloudinit.readthedocs.io/en/latest/).

        Cloud-init is a commonly-used startup configuration utility for cloud compute instances. It accepts configuration via provider-specific user data mechanisms, such as `user_data` for Amazon EC2 instances. Multi-part MIME is one of the data formats it accepts. For more information, see [User-Data Formats](https://cloudinit.readthedocs.io/en/latest/explanation/format.html) in the cloud-init manual.

        This is not a generalized utility for producing multi-part MIME messages. It's feature set is specialized for cloud-init multi-part MIME messages.

        ## Example Usage

        ### Config

        ### hello-script.sh

        ### cloud-config.yaml

        <!-- This schema was originally generated with tfplugindocs, then modified manually to ensure `part` block list is noted as Required -->

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
                 parts: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ConfigPartArgs', 'ConfigPartArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigArgs.__new__(ConfigArgs)

            __props__.__dict__["base64_encode"] = base64_encode
            __props__.__dict__["boundary"] = boundary
            __props__.__dict__["gzip"] = gzip
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
            parts: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ConfigPartArgs', 'ConfigPartArgsDict']]]]] = None,
            rendered: Optional[pulumi.Input[str]] = None) -> 'Config':
        """
        Get an existing Config resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] base64_encode: Specify whether or not to base64 encode the `rendered` output. Defaults to `true`, and cannot be disabled if gzip is `true`.
        :param pulumi.Input[str] boundary: Specify the Writer's default boundary separator. Defaults to `MIMEBOUNDARY`.
        :param pulumi.Input[bool] gzip: Specify whether or not to gzip the `rendered` output. Defaults to `true`.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ConfigPartArgs', 'ConfigPartArgsDict']]]] parts: A nested block type which adds a file to the generated cloud-init configuration. Use multiple `part` blocks to specify multiple files, which will be included in order of declaration in the final MIME document.
        :param pulumi.Input[str] rendered: The final rendered multi-part cloud-init config.
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
    def base64_encode(self) -> pulumi.Output[bool]:
        """
        Specify whether or not to base64 encode the `rendered` output. Defaults to `true`, and cannot be disabled if gzip is `true`.
        """
        return pulumi.get(self, "base64_encode")

    @property
    @pulumi.getter
    def boundary(self) -> pulumi.Output[str]:
        """
        Specify the Writer's default boundary separator. Defaults to `MIMEBOUNDARY`.
        """
        return pulumi.get(self, "boundary")

    @property
    @pulumi.getter
    def gzip(self) -> pulumi.Output[bool]:
        """
        Specify whether or not to gzip the `rendered` output. Defaults to `true`.
        """
        return pulumi.get(self, "gzip")

    @property
    @pulumi.getter
    def parts(self) -> pulumi.Output[Optional[Sequence['outputs.ConfigPart']]]:
        """
        A nested block type which adds a file to the generated cloud-init configuration. Use multiple `part` blocks to specify multiple files, which will be included in order of declaration in the final MIME document.
        """
        return pulumi.get(self, "parts")

    @property
    @pulumi.getter
    def rendered(self) -> pulumi.Output[str]:
        """
        The final rendered multi-part cloud-init config.
        """
        return pulumi.get(self, "rendered")

