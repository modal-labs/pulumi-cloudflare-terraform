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
from ._inputs import *

__all__ = [
    'GetAccountMemberResult',
    'AwaitableGetAccountMemberResult',
    'get_account_member',
    'get_account_member_output',
]

@pulumi.output_type
class GetAccountMemberResult:
    """
    A collection of values returned by getAccountMember.
    """
    def __init__(__self__, account_id=None, filter=None, id=None, member_id=None, policies=None, roles=None, status=None, user=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        pulumi.set(__self__, "filter", filter)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if member_id and not isinstance(member_id, str):
            raise TypeError("Expected argument 'member_id' to be a str")
        pulumi.set(__self__, "member_id", member_id)
        if policies and not isinstance(policies, list):
            raise TypeError("Expected argument 'policies' to be a list")
        pulumi.set(__self__, "policies", policies)
        if roles and not isinstance(roles, list):
            raise TypeError("Expected argument 'roles' to be a list")
        pulumi.set(__self__, "roles", roles)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if user and not isinstance(user, dict):
            raise TypeError("Expected argument 'user' to be a dict")
        pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.GetAccountMemberFilterResult']:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> Optional[str]:
        return pulumi.get(self, "member_id")

    @property
    @pulumi.getter
    def policies(self) -> Sequence['outputs.GetAccountMemberPolicyResult']:
        return pulumi.get(self, "policies")

    @property
    @pulumi.getter
    def roles(self) -> Sequence['outputs.GetAccountMemberRoleResult']:
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def user(self) -> 'outputs.GetAccountMemberUserResult':
        return pulumi.get(self, "user")


class AwaitableGetAccountMemberResult(GetAccountMemberResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountMemberResult(
            account_id=self.account_id,
            filter=self.filter,
            id=self.id,
            member_id=self.member_id,
            policies=self.policies,
            roles=self.roles,
            status=self.status,
            user=self.user)


def get_account_member(account_id: Optional[str] = None,
                       filter: Optional[Union['GetAccountMemberFilterArgs', 'GetAccountMemberFilterArgsDict']] = None,
                       member_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountMemberResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['filter'] = filter
    __args__['memberId'] = member_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getAccountMember:getAccountMember', __args__, opts=opts, typ=GetAccountMemberResult, package_ref=_utilities.get_package()).value

    return AwaitableGetAccountMemberResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        filter=pulumi.get(__ret__, 'filter'),
        id=pulumi.get(__ret__, 'id'),
        member_id=pulumi.get(__ret__, 'member_id'),
        policies=pulumi.get(__ret__, 'policies'),
        roles=pulumi.get(__ret__, 'roles'),
        status=pulumi.get(__ret__, 'status'),
        user=pulumi.get(__ret__, 'user'))
def get_account_member_output(account_id: Optional[pulumi.Input[str]] = None,
                              filter: Optional[pulumi.Input[Optional[Union['GetAccountMemberFilterArgs', 'GetAccountMemberFilterArgsDict']]]] = None,
                              member_id: Optional[pulumi.Input[Optional[str]]] = None,
                              opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetAccountMemberResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['filter'] = filter
    __args__['memberId'] = member_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getAccountMember:getAccountMember', __args__, opts=opts, typ=GetAccountMemberResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetAccountMemberResult(
        account_id=pulumi.get(__response__, 'account_id'),
        filter=pulumi.get(__response__, 'filter'),
        id=pulumi.get(__response__, 'id'),
        member_id=pulumi.get(__response__, 'member_id'),
        policies=pulumi.get(__response__, 'policies'),
        roles=pulumi.get(__response__, 'roles'),
        status=pulumi.get(__response__, 'status'),
        user=pulumi.get(__response__, 'user')))
