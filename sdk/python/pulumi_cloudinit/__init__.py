# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
from . import _utilities
import typing
# Export this package's modules as members:
from .config import *
from .get_config import *
from .provider import *
from ._inputs import *
from . import outputs
_utilities.register(
    resource_modules="""
[
 {
  "pkg": "cloudinit",
  "mod": "index/config",
  "fqn": "pulumi_cloudinit",
  "classes": {
   "cloudinit:index/config:Config": "Config"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "cloudinit",
  "token": "pulumi:providers:cloudinit",
  "fqn": "pulumi_cloudinit",
  "class": "Provider"
 }
]
"""
)
