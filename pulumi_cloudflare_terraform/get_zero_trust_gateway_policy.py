# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
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

__all__ = [
    'GetZeroTrustGatewayPolicyResult',
    'AwaitableGetZeroTrustGatewayPolicyResult',
    'get_zero_trust_gateway_policy',
    'get_zero_trust_gateway_policy_output',
]

@pulumi.output_type
class GetZeroTrustGatewayPolicyResult:
    """
    A collection of values returned by getZeroTrustGatewayPolicy.
    """
    def __init__(__self__, account_id=None, action=None, created_at=None, deleted_at=None, description=None, device_posture=None, enabled=None, expiration=None, filters=None, id=None, identity=None, name=None, precedence=None, rule_id=None, rule_settings=None, schedule=None, traffic=None, updated_at=None, version=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if action and not isinstance(action, str):
            raise TypeError("Expected argument 'action' to be a str")
        pulumi.set(__self__, "action", action)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if deleted_at and not isinstance(deleted_at, str):
            raise TypeError("Expected argument 'deleted_at' to be a str")
        pulumi.set(__self__, "deleted_at", deleted_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if device_posture and not isinstance(device_posture, str):
            raise TypeError("Expected argument 'device_posture' to be a str")
        pulumi.set(__self__, "device_posture", device_posture)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if expiration and not isinstance(expiration, dict):
            raise TypeError("Expected argument 'expiration' to be a dict")
        pulumi.set(__self__, "expiration", expiration)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, str):
            raise TypeError("Expected argument 'identity' to be a str")
        pulumi.set(__self__, "identity", identity)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if precedence and not isinstance(precedence, float):
            raise TypeError("Expected argument 'precedence' to be a float")
        pulumi.set(__self__, "precedence", precedence)
        if rule_id and not isinstance(rule_id, str):
            raise TypeError("Expected argument 'rule_id' to be a str")
        pulumi.set(__self__, "rule_id", rule_id)
        if rule_settings and not isinstance(rule_settings, dict):
            raise TypeError("Expected argument 'rule_settings' to be a dict")
        pulumi.set(__self__, "rule_settings", rule_settings)
        if schedule and not isinstance(schedule, dict):
            raise TypeError("Expected argument 'schedule' to be a dict")
        pulumi.set(__self__, "schedule", schedule)
        if traffic and not isinstance(traffic, str):
            raise TypeError("Expected argument 'traffic' to be a str")
        pulumi.set(__self__, "traffic", traffic)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if version and not isinstance(version, float):
            raise TypeError("Expected argument 'version' to be a float")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def action(self) -> str:
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="deletedAt")
    def deleted_at(self) -> str:
        return pulumi.get(self, "deleted_at")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="devicePosture")
    def device_posture(self) -> str:
        return pulumi.get(self, "device_posture")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def expiration(self) -> 'outputs.GetZeroTrustGatewayPolicyExpirationResult':
        return pulumi.get(self, "expiration")

    @property
    @pulumi.getter
    def filters(self) -> Sequence[str]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> str:
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def precedence(self) -> float:
        return pulumi.get(self, "precedence")

    @property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> Optional[str]:
        return pulumi.get(self, "rule_id")

    @property
    @pulumi.getter(name="ruleSettings")
    def rule_settings(self) -> 'outputs.GetZeroTrustGatewayPolicyRuleSettingsResult':
        return pulumi.get(self, "rule_settings")

    @property
    @pulumi.getter
    def schedule(self) -> 'outputs.GetZeroTrustGatewayPolicyScheduleResult':
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def traffic(self) -> str:
        return pulumi.get(self, "traffic")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def version(self) -> float:
        return pulumi.get(self, "version")


class AwaitableGetZeroTrustGatewayPolicyResult(GetZeroTrustGatewayPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZeroTrustGatewayPolicyResult(
            account_id=self.account_id,
            action=self.action,
            created_at=self.created_at,
            deleted_at=self.deleted_at,
            description=self.description,
            device_posture=self.device_posture,
            enabled=self.enabled,
            expiration=self.expiration,
            filters=self.filters,
            id=self.id,
            identity=self.identity,
            name=self.name,
            precedence=self.precedence,
            rule_id=self.rule_id,
            rule_settings=self.rule_settings,
            schedule=self.schedule,
            traffic=self.traffic,
            updated_at=self.updated_at,
            version=self.version)


def get_zero_trust_gateway_policy(account_id: Optional[str] = None,
                                  rule_id: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZeroTrustGatewayPolicyResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['ruleId'] = rule_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getZeroTrustGatewayPolicy:getZeroTrustGatewayPolicy', __args__, opts=opts, typ=GetZeroTrustGatewayPolicyResult, package_ref=_utilities.get_package()).value

    return AwaitableGetZeroTrustGatewayPolicyResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        action=pulumi.get(__ret__, 'action'),
        created_at=pulumi.get(__ret__, 'created_at'),
        deleted_at=pulumi.get(__ret__, 'deleted_at'),
        description=pulumi.get(__ret__, 'description'),
        device_posture=pulumi.get(__ret__, 'device_posture'),
        enabled=pulumi.get(__ret__, 'enabled'),
        expiration=pulumi.get(__ret__, 'expiration'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        name=pulumi.get(__ret__, 'name'),
        precedence=pulumi.get(__ret__, 'precedence'),
        rule_id=pulumi.get(__ret__, 'rule_id'),
        rule_settings=pulumi.get(__ret__, 'rule_settings'),
        schedule=pulumi.get(__ret__, 'schedule'),
        traffic=pulumi.get(__ret__, 'traffic'),
        updated_at=pulumi.get(__ret__, 'updated_at'),
        version=pulumi.get(__ret__, 'version'))
def get_zero_trust_gateway_policy_output(account_id: Optional[pulumi.Input[str]] = None,
                                         rule_id: Optional[pulumi.Input[Optional[str]]] = None,
                                         opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetZeroTrustGatewayPolicyResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['ruleId'] = rule_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getZeroTrustGatewayPolicy:getZeroTrustGatewayPolicy', __args__, opts=opts, typ=GetZeroTrustGatewayPolicyResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetZeroTrustGatewayPolicyResult(
        account_id=pulumi.get(__response__, 'account_id'),
        action=pulumi.get(__response__, 'action'),
        created_at=pulumi.get(__response__, 'created_at'),
        deleted_at=pulumi.get(__response__, 'deleted_at'),
        description=pulumi.get(__response__, 'description'),
        device_posture=pulumi.get(__response__, 'device_posture'),
        enabled=pulumi.get(__response__, 'enabled'),
        expiration=pulumi.get(__response__, 'expiration'),
        filters=pulumi.get(__response__, 'filters'),
        id=pulumi.get(__response__, 'id'),
        identity=pulumi.get(__response__, 'identity'),
        name=pulumi.get(__response__, 'name'),
        precedence=pulumi.get(__response__, 'precedence'),
        rule_id=pulumi.get(__response__, 'rule_id'),
        rule_settings=pulumi.get(__response__, 'rule_settings'),
        schedule=pulumi.get(__response__, 'schedule'),
        traffic=pulumi.get(__response__, 'traffic'),
        updated_at=pulumi.get(__response__, 'updated_at'),
        version=pulumi.get(__response__, 'version')))
