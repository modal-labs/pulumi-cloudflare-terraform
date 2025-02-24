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

__all__ = ['EmailSecurityTrustedDomainsArgs', 'EmailSecurityTrustedDomains']

@pulumi.input_type
class EmailSecurityTrustedDomainsArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 bodies: Optional[pulumi.Input[Sequence[pulumi.Input['EmailSecurityTrustedDomainsBodyArgs']]]] = None,
                 comments: Optional[pulumi.Input[str]] = None,
                 is_recent: Optional[pulumi.Input[bool]] = None,
                 is_regex: Optional[pulumi.Input[bool]] = None,
                 is_similarity: Optional[pulumi.Input[bool]] = None,
                 pattern: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EmailSecurityTrustedDomains resource.
        :param pulumi.Input[str] account_id: Account Identifier
        :param pulumi.Input[bool] is_recent: Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.
        :param pulumi.Input[bool] is_similarity: Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed
               domains from triggering a Spoof disposition.
        """
        pulumi.set(__self__, "account_id", account_id)
        if bodies is not None:
            pulumi.set(__self__, "bodies", bodies)
        if comments is not None:
            pulumi.set(__self__, "comments", comments)
        if is_recent is not None:
            pulumi.set(__self__, "is_recent", is_recent)
        if is_regex is not None:
            pulumi.set(__self__, "is_regex", is_regex)
        if is_similarity is not None:
            pulumi.set(__self__, "is_similarity", is_similarity)
        if pattern is not None:
            pulumi.set(__self__, "pattern", pattern)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        Account Identifier
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def bodies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EmailSecurityTrustedDomainsBodyArgs']]]]:
        return pulumi.get(self, "bodies")

    @bodies.setter
    def bodies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EmailSecurityTrustedDomainsBodyArgs']]]]):
        pulumi.set(self, "bodies", value)

    @property
    @pulumi.getter
    def comments(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "comments")

    @comments.setter
    def comments(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comments", value)

    @property
    @pulumi.getter(name="isRecent")
    def is_recent(self) -> Optional[pulumi.Input[bool]]:
        """
        Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.
        """
        return pulumi.get(self, "is_recent")

    @is_recent.setter
    def is_recent(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_recent", value)

    @property
    @pulumi.getter(name="isRegex")
    def is_regex(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_regex")

    @is_regex.setter
    def is_regex(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_regex", value)

    @property
    @pulumi.getter(name="isSimilarity")
    def is_similarity(self) -> Optional[pulumi.Input[bool]]:
        """
        Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed
        domains from triggering a Spoof disposition.
        """
        return pulumi.get(self, "is_similarity")

    @is_similarity.setter
    def is_similarity(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_similarity", value)

    @property
    @pulumi.getter
    def pattern(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "pattern")

    @pattern.setter
    def pattern(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pattern", value)


@pulumi.input_type
class _EmailSecurityTrustedDomainsState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 bodies: Optional[pulumi.Input[Sequence[pulumi.Input['EmailSecurityTrustedDomainsBodyArgs']]]] = None,
                 comments: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 email_security_trusted_domains_id: Optional[pulumi.Input[float]] = None,
                 is_recent: Optional[pulumi.Input[bool]] = None,
                 is_regex: Optional[pulumi.Input[bool]] = None,
                 is_similarity: Optional[pulumi.Input[bool]] = None,
                 last_modified: Optional[pulumi.Input[str]] = None,
                 pattern: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering EmailSecurityTrustedDomains resources.
        :param pulumi.Input[str] account_id: Account Identifier
        :param pulumi.Input[float] email_security_trusted_domains_id: The unique identifier for the trusted domain.
        :param pulumi.Input[bool] is_recent: Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.
        :param pulumi.Input[bool] is_similarity: Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed
               domains from triggering a Spoof disposition.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if bodies is not None:
            pulumi.set(__self__, "bodies", bodies)
        if comments is not None:
            pulumi.set(__self__, "comments", comments)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if email_security_trusted_domains_id is not None:
            pulumi.set(__self__, "email_security_trusted_domains_id", email_security_trusted_domains_id)
        if is_recent is not None:
            pulumi.set(__self__, "is_recent", is_recent)
        if is_regex is not None:
            pulumi.set(__self__, "is_regex", is_regex)
        if is_similarity is not None:
            pulumi.set(__self__, "is_similarity", is_similarity)
        if last_modified is not None:
            pulumi.set(__self__, "last_modified", last_modified)
        if pattern is not None:
            pulumi.set(__self__, "pattern", pattern)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Account Identifier
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def bodies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EmailSecurityTrustedDomainsBodyArgs']]]]:
        return pulumi.get(self, "bodies")

    @bodies.setter
    def bodies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EmailSecurityTrustedDomainsBodyArgs']]]]):
        pulumi.set(self, "bodies", value)

    @property
    @pulumi.getter
    def comments(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "comments")

    @comments.setter
    def comments(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comments", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="emailSecurityTrustedDomainsId")
    def email_security_trusted_domains_id(self) -> Optional[pulumi.Input[float]]:
        """
        The unique identifier for the trusted domain.
        """
        return pulumi.get(self, "email_security_trusted_domains_id")

    @email_security_trusted_domains_id.setter
    def email_security_trusted_domains_id(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "email_security_trusted_domains_id", value)

    @property
    @pulumi.getter(name="isRecent")
    def is_recent(self) -> Optional[pulumi.Input[bool]]:
        """
        Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.
        """
        return pulumi.get(self, "is_recent")

    @is_recent.setter
    def is_recent(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_recent", value)

    @property
    @pulumi.getter(name="isRegex")
    def is_regex(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_regex")

    @is_regex.setter
    def is_regex(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_regex", value)

    @property
    @pulumi.getter(name="isSimilarity")
    def is_similarity(self) -> Optional[pulumi.Input[bool]]:
        """
        Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed
        domains from triggering a Spoof disposition.
        """
        return pulumi.get(self, "is_similarity")

    @is_similarity.setter
    def is_similarity(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_similarity", value)

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "last_modified")

    @last_modified.setter
    def last_modified(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified", value)

    @property
    @pulumi.getter
    def pattern(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "pattern")

    @pattern.setter
    def pattern(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pattern", value)


class EmailSecurityTrustedDomains(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 bodies: Optional[pulumi.Input[Sequence[pulumi.Input[Union['EmailSecurityTrustedDomainsBodyArgs', 'EmailSecurityTrustedDomainsBodyArgsDict']]]]] = None,
                 comments: Optional[pulumi.Input[str]] = None,
                 is_recent: Optional[pulumi.Input[bool]] = None,
                 is_regex: Optional[pulumi.Input[bool]] = None,
                 is_similarity: Optional[pulumi.Input[bool]] = None,
                 pattern: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a EmailSecurityTrustedDomains resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Account Identifier
        :param pulumi.Input[bool] is_recent: Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.
        :param pulumi.Input[bool] is_similarity: Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed
               domains from triggering a Spoof disposition.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EmailSecurityTrustedDomainsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a EmailSecurityTrustedDomains resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param EmailSecurityTrustedDomainsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EmailSecurityTrustedDomainsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 bodies: Optional[pulumi.Input[Sequence[pulumi.Input[Union['EmailSecurityTrustedDomainsBodyArgs', 'EmailSecurityTrustedDomainsBodyArgsDict']]]]] = None,
                 comments: Optional[pulumi.Input[str]] = None,
                 is_recent: Optional[pulumi.Input[bool]] = None,
                 is_regex: Optional[pulumi.Input[bool]] = None,
                 is_similarity: Optional[pulumi.Input[bool]] = None,
                 pattern: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EmailSecurityTrustedDomainsArgs.__new__(EmailSecurityTrustedDomainsArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["bodies"] = bodies
            __props__.__dict__["comments"] = comments
            __props__.__dict__["is_recent"] = is_recent
            __props__.__dict__["is_regex"] = is_regex
            __props__.__dict__["is_similarity"] = is_similarity
            __props__.__dict__["pattern"] = pattern
            __props__.__dict__["created_at"] = None
            __props__.__dict__["email_security_trusted_domains_id"] = None
            __props__.__dict__["last_modified"] = None
        super(EmailSecurityTrustedDomains, __self__).__init__(
            'cloudflare:index/emailSecurityTrustedDomains:EmailSecurityTrustedDomains',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            bodies: Optional[pulumi.Input[Sequence[pulumi.Input[Union['EmailSecurityTrustedDomainsBodyArgs', 'EmailSecurityTrustedDomainsBodyArgsDict']]]]] = None,
            comments: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            email_security_trusted_domains_id: Optional[pulumi.Input[float]] = None,
            is_recent: Optional[pulumi.Input[bool]] = None,
            is_regex: Optional[pulumi.Input[bool]] = None,
            is_similarity: Optional[pulumi.Input[bool]] = None,
            last_modified: Optional[pulumi.Input[str]] = None,
            pattern: Optional[pulumi.Input[str]] = None) -> 'EmailSecurityTrustedDomains':
        """
        Get an existing EmailSecurityTrustedDomains resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Account Identifier
        :param pulumi.Input[float] email_security_trusted_domains_id: The unique identifier for the trusted domain.
        :param pulumi.Input[bool] is_recent: Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.
        :param pulumi.Input[bool] is_similarity: Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed
               domains from triggering a Spoof disposition.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EmailSecurityTrustedDomainsState.__new__(_EmailSecurityTrustedDomainsState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["bodies"] = bodies
        __props__.__dict__["comments"] = comments
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["email_security_trusted_domains_id"] = email_security_trusted_domains_id
        __props__.__dict__["is_recent"] = is_recent
        __props__.__dict__["is_regex"] = is_regex
        __props__.__dict__["is_similarity"] = is_similarity
        __props__.__dict__["last_modified"] = last_modified
        __props__.__dict__["pattern"] = pattern
        return EmailSecurityTrustedDomains(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        Account Identifier
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def bodies(self) -> pulumi.Output[Sequence['outputs.EmailSecurityTrustedDomainsBody']]:
        return pulumi.get(self, "bodies")

    @property
    @pulumi.getter
    def comments(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "comments")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="emailSecurityTrustedDomainsId")
    def email_security_trusted_domains_id(self) -> pulumi.Output[float]:
        """
        The unique identifier for the trusted domain.
        """
        return pulumi.get(self, "email_security_trusted_domains_id")

    @property
    @pulumi.getter(name="isRecent")
    def is_recent(self) -> pulumi.Output[Optional[bool]]:
        """
        Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.
        """
        return pulumi.get(self, "is_recent")

    @property
    @pulumi.getter(name="isRegex")
    def is_regex(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "is_regex")

    @property
    @pulumi.getter(name="isSimilarity")
    def is_similarity(self) -> pulumi.Output[Optional[bool]]:
        """
        Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed
        domains from triggering a Spoof disposition.
        """
        return pulumi.get(self, "is_similarity")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[str]:
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def pattern(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "pattern")

