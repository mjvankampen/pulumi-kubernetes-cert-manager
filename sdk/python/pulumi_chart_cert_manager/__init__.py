# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .cert_manager import *
from .provider import *
from ._inputs import *
from . import outputs
_utilities.register(
    resource_modules="""
[
 {
  "pkg": "chart-cert-manager",
  "mod": "index",
  "fqn": "pulumi_chart_cert_manager",
  "classes": {
   "chart-cert-manager:index:CertManager": "CertManager"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "chart-cert-manager",
  "token": "pulumi:providers:chart-cert-manager",
  "fqn": "pulumi_chart_cert_manager",
  "class": "Provider"
 }
]
"""
)