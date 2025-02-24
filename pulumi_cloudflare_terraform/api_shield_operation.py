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

__all__ = ['ApiShieldOperationArgs', 'ApiShieldOperation']

@pulumi.input_type
class ApiShieldOperationArgs:
    def __init__(__self__, *,
                 endpoint: pulumi.Input[str],
                 host: pulumi.Input[str],
                 method: pulumi.Input[str],
                 zone_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a ApiShieldOperation resource.
        :param pulumi.Input[str] endpoint: The endpoint which can contain path parameter templates in curly braces, each will be replaced from left to right with
               {varN}, starting with {var1}, during insertion. This will further be Cloudflare-normalized upon insertion. See:
               https://developers.cloudflare.com/rules/normalization/how-it-works/.
        :param pulumi.Input[str] host: RFC3986-compliant host.
        :param pulumi.Input[str] method: The HTTP method used to access the endpoint.
        :param pulumi.Input[str] zone_id: Identifier
        """
        pulumi.set(__self__, "endpoint", endpoint)
        pulumi.set(__self__, "host", host)
        pulumi.set(__self__, "method", method)
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[str]:
        """
        The endpoint which can contain path parameter templates in curly braces, each will be replaced from left to right with
        {varN}, starting with {var1}, during insertion. This will further be Cloudflare-normalized upon insertion. See:
        https://developers.cloudflare.com/rules/normalization/how-it-works/.
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter
    def host(self) -> pulumi.Input[str]:
        """
        RFC3986-compliant host.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: pulumi.Input[str]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def method(self) -> pulumi.Input[str]:
        """
        The HTTP method used to access the endpoint.
        """
        return pulumi.get(self, "method")

    @method.setter
    def method(self, value: pulumi.Input[str]):
        pulumi.set(self, "method", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[str]:
        """
        Identifier
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_id", value)


@pulumi.input_type
class _ApiShieldOperationState:
    def __init__(__self__, *,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 features: Optional[pulumi.Input['ApiShieldOperationFeaturesArgs']] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 last_updated: Optional[pulumi.Input[str]] = None,
                 method: Optional[pulumi.Input[str]] = None,
                 operation_id: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ApiShieldOperation resources.
        :param pulumi.Input[str] endpoint: The endpoint which can contain path parameter templates in curly braces, each will be replaced from left to right with
               {varN}, starting with {var1}, during insertion. This will further be Cloudflare-normalized upon insertion. See:
               https://developers.cloudflare.com/rules/normalization/how-it-works/.
        :param pulumi.Input[str] host: RFC3986-compliant host.
        :param pulumi.Input[str] method: The HTTP method used to access the endpoint.
        :param pulumi.Input[str] operation_id: UUID
        :param pulumi.Input[str] zone_id: Identifier
        """
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if features is not None:
            pulumi.set(__self__, "features", features)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if last_updated is not None:
            pulumi.set(__self__, "last_updated", last_updated)
        if method is not None:
            pulumi.set(__self__, "method", method)
        if operation_id is not None:
            pulumi.set(__self__, "operation_id", operation_id)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The endpoint which can contain path parameter templates in curly braces, each will be replaced from left to right with
        {varN}, starting with {var1}, during insertion. This will further be Cloudflare-normalized upon insertion. See:
        https://developers.cloudflare.com/rules/normalization/how-it-works/.
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter
    def features(self) -> Optional[pulumi.Input['ApiShieldOperationFeaturesArgs']]:
        return pulumi.get(self, "features")

    @features.setter
    def features(self, value: Optional[pulumi.Input['ApiShieldOperationFeaturesArgs']]):
        pulumi.set(self, "features", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        RFC3986-compliant host.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "last_updated")

    @last_updated.setter
    def last_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_updated", value)

    @property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[str]]:
        """
        The HTTP method used to access the endpoint.
        """
        return pulumi.get(self, "method")

    @method.setter
    def method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "method", value)

    @property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> Optional[pulumi.Input[str]]:
        """
        UUID
        """
        return pulumi.get(self, "operation_id")

    @operation_id.setter
    def operation_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operation_id", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class ApiShieldOperation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 method: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ApiShieldOperation resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] endpoint: The endpoint which can contain path parameter templates in curly braces, each will be replaced from left to right with
               {varN}, starting with {var1}, during insertion. This will further be Cloudflare-normalized upon insertion. See:
               https://developers.cloudflare.com/rules/normalization/how-it-works/.
        :param pulumi.Input[str] host: RFC3986-compliant host.
        :param pulumi.Input[str] method: The HTTP method used to access the endpoint.
        :param pulumi.Input[str] zone_id: Identifier
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiShieldOperationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ApiShieldOperation resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ApiShieldOperationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiShieldOperationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 method: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiShieldOperationArgs.__new__(ApiShieldOperationArgs)

            if endpoint is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint'")
            __props__.__dict__["endpoint"] = endpoint
            if host is None and not opts.urn:
                raise TypeError("Missing required property 'host'")
            __props__.__dict__["host"] = host
            if method is None and not opts.urn:
                raise TypeError("Missing required property 'method'")
            __props__.__dict__["method"] = method
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
            __props__.__dict__["features"] = None
            __props__.__dict__["last_updated"] = None
            __props__.__dict__["operation_id"] = None
        super(ApiShieldOperation, __self__).__init__(
            'cloudflare:index/apiShieldOperation:ApiShieldOperation',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            endpoint: Optional[pulumi.Input[str]] = None,
            features: Optional[pulumi.Input[Union['ApiShieldOperationFeaturesArgs', 'ApiShieldOperationFeaturesArgsDict']]] = None,
            host: Optional[pulumi.Input[str]] = None,
            last_updated: Optional[pulumi.Input[str]] = None,
            method: Optional[pulumi.Input[str]] = None,
            operation_id: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'ApiShieldOperation':
        """
        Get an existing ApiShieldOperation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] endpoint: The endpoint which can contain path parameter templates in curly braces, each will be replaced from left to right with
               {varN}, starting with {var1}, during insertion. This will further be Cloudflare-normalized upon insertion. See:
               https://developers.cloudflare.com/rules/normalization/how-it-works/.
        :param pulumi.Input[str] host: RFC3986-compliant host.
        :param pulumi.Input[str] method: The HTTP method used to access the endpoint.
        :param pulumi.Input[str] operation_id: UUID
        :param pulumi.Input[str] zone_id: Identifier
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApiShieldOperationState.__new__(_ApiShieldOperationState)

        __props__.__dict__["endpoint"] = endpoint
        __props__.__dict__["features"] = features
        __props__.__dict__["host"] = host
        __props__.__dict__["last_updated"] = last_updated
        __props__.__dict__["method"] = method
        __props__.__dict__["operation_id"] = operation_id
        __props__.__dict__["zone_id"] = zone_id
        return ApiShieldOperation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        The endpoint which can contain path parameter templates in curly braces, each will be replaced from left to right with
        {varN}, starting with {var1}, during insertion. This will further be Cloudflare-normalized upon insertion. See:
        https://developers.cloudflare.com/rules/normalization/how-it-works/.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def features(self) -> pulumi.Output['outputs.ApiShieldOperationFeatures']:
        return pulumi.get(self, "features")

    @property
    @pulumi.getter
    def host(self) -> pulumi.Output[str]:
        """
        RFC3986-compliant host.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> pulumi.Output[str]:
        return pulumi.get(self, "last_updated")

    @property
    @pulumi.getter
    def method(self) -> pulumi.Output[str]:
        """
        The HTTP method used to access the endpoint.
        """
        return pulumi.get(self, "method")

    @property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> pulumi.Output[str]:
        """
        UUID
        """
        return pulumi.get(self, "operation_id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        Identifier
        """
        return pulumi.get(self, "zone_id")

