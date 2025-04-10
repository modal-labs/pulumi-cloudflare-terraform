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

__all__ = ['CloudforceOneRequestAssetArgs', 'CloudforceOneRequestAsset']

@pulumi.input_type
class CloudforceOneRequestAssetArgs:
    def __init__(__self__, *,
                 account_identifier: pulumi.Input[str],
                 page: pulumi.Input[float],
                 per_page: pulumi.Input[float],
                 request_identifier: pulumi.Input[str],
                 source: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CloudforceOneRequestAsset resource.
        :param pulumi.Input[str] account_identifier: Identifier
        :param pulumi.Input[float] page: Page number of results
        :param pulumi.Input[float] per_page: Number of results per page
        :param pulumi.Input[str] request_identifier: UUID
        :param pulumi.Input[str] source: Asset file to upload
        """
        pulumi.set(__self__, "account_identifier", account_identifier)
        pulumi.set(__self__, "page", page)
        pulumi.set(__self__, "per_page", per_page)
        pulumi.set(__self__, "request_identifier", request_identifier)
        if source is not None:
            pulumi.set(__self__, "source", source)

    @property
    @pulumi.getter(name="accountIdentifier")
    def account_identifier(self) -> pulumi.Input[str]:
        """
        Identifier
        """
        return pulumi.get(self, "account_identifier")

    @account_identifier.setter
    def account_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_identifier", value)

    @property
    @pulumi.getter
    def page(self) -> pulumi.Input[float]:
        """
        Page number of results
        """
        return pulumi.get(self, "page")

    @page.setter
    def page(self, value: pulumi.Input[float]):
        pulumi.set(self, "page", value)

    @property
    @pulumi.getter(name="perPage")
    def per_page(self) -> pulumi.Input[float]:
        """
        Number of results per page
        """
        return pulumi.get(self, "per_page")

    @per_page.setter
    def per_page(self, value: pulumi.Input[float]):
        pulumi.set(self, "per_page", value)

    @property
    @pulumi.getter(name="requestIdentifier")
    def request_identifier(self) -> pulumi.Input[str]:
        """
        UUID
        """
        return pulumi.get(self, "request_identifier")

    @request_identifier.setter
    def request_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "request_identifier", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        Asset file to upload
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)


@pulumi.input_type
class _CloudforceOneRequestAssetState:
    def __init__(__self__, *,
                 account_identifier: Optional[pulumi.Input[str]] = None,
                 cloudforce_one_request_asset_id: Optional[pulumi.Input[float]] = None,
                 created: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 file_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 page: Optional[pulumi.Input[float]] = None,
                 per_page: Optional[pulumi.Input[float]] = None,
                 request_identifier: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CloudforceOneRequestAsset resources.
        :param pulumi.Input[str] account_identifier: Identifier
        :param pulumi.Input[float] cloudforce_one_request_asset_id: Asset ID
        :param pulumi.Input[str] created: Asset creation time
        :param pulumi.Input[str] description: Asset description
        :param pulumi.Input[str] file_type: Asset file type
        :param pulumi.Input[str] name: Asset name
        :param pulumi.Input[float] page: Page number of results
        :param pulumi.Input[float] per_page: Number of results per page
        :param pulumi.Input[str] request_identifier: UUID
        :param pulumi.Input[str] source: Asset file to upload
        """
        if account_identifier is not None:
            pulumi.set(__self__, "account_identifier", account_identifier)
        if cloudforce_one_request_asset_id is not None:
            pulumi.set(__self__, "cloudforce_one_request_asset_id", cloudforce_one_request_asset_id)
        if created is not None:
            pulumi.set(__self__, "created", created)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if file_type is not None:
            pulumi.set(__self__, "file_type", file_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if page is not None:
            pulumi.set(__self__, "page", page)
        if per_page is not None:
            pulumi.set(__self__, "per_page", per_page)
        if request_identifier is not None:
            pulumi.set(__self__, "request_identifier", request_identifier)
        if source is not None:
            pulumi.set(__self__, "source", source)

    @property
    @pulumi.getter(name="accountIdentifier")
    def account_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier
        """
        return pulumi.get(self, "account_identifier")

    @account_identifier.setter
    def account_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_identifier", value)

    @property
    @pulumi.getter(name="cloudforceOneRequestAssetId")
    def cloudforce_one_request_asset_id(self) -> Optional[pulumi.Input[float]]:
        """
        Asset ID
        """
        return pulumi.get(self, "cloudforce_one_request_asset_id")

    @cloudforce_one_request_asset_id.setter
    def cloudforce_one_request_asset_id(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "cloudforce_one_request_asset_id", value)

    @property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[str]]:
        """
        Asset creation time
        """
        return pulumi.get(self, "created")

    @created.setter
    def created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Asset description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="fileType")
    def file_type(self) -> Optional[pulumi.Input[str]]:
        """
        Asset file type
        """
        return pulumi.get(self, "file_type")

    @file_type.setter
    def file_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Asset name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def page(self) -> Optional[pulumi.Input[float]]:
        """
        Page number of results
        """
        return pulumi.get(self, "page")

    @page.setter
    def page(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "page", value)

    @property
    @pulumi.getter(name="perPage")
    def per_page(self) -> Optional[pulumi.Input[float]]:
        """
        Number of results per page
        """
        return pulumi.get(self, "per_page")

    @per_page.setter
    def per_page(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "per_page", value)

    @property
    @pulumi.getter(name="requestIdentifier")
    def request_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        UUID
        """
        return pulumi.get(self, "request_identifier")

    @request_identifier.setter
    def request_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_identifier", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        Asset file to upload
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)


class CloudforceOneRequestAsset(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_identifier: Optional[pulumi.Input[str]] = None,
                 page: Optional[pulumi.Input[float]] = None,
                 per_page: Optional[pulumi.Input[float]] = None,
                 request_identifier: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a CloudforceOneRequestAsset resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_identifier: Identifier
        :param pulumi.Input[float] page: Page number of results
        :param pulumi.Input[float] per_page: Number of results per page
        :param pulumi.Input[str] request_identifier: UUID
        :param pulumi.Input[str] source: Asset file to upload
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CloudforceOneRequestAssetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a CloudforceOneRequestAsset resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param CloudforceOneRequestAssetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CloudforceOneRequestAssetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_identifier: Optional[pulumi.Input[str]] = None,
                 page: Optional[pulumi.Input[float]] = None,
                 per_page: Optional[pulumi.Input[float]] = None,
                 request_identifier: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CloudforceOneRequestAssetArgs.__new__(CloudforceOneRequestAssetArgs)

            if account_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'account_identifier'")
            __props__.__dict__["account_identifier"] = account_identifier
            if page is None and not opts.urn:
                raise TypeError("Missing required property 'page'")
            __props__.__dict__["page"] = page
            if per_page is None and not opts.urn:
                raise TypeError("Missing required property 'per_page'")
            __props__.__dict__["per_page"] = per_page
            if request_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'request_identifier'")
            __props__.__dict__["request_identifier"] = request_identifier
            __props__.__dict__["source"] = source
            __props__.__dict__["cloudforce_one_request_asset_id"] = None
            __props__.__dict__["created"] = None
            __props__.__dict__["description"] = None
            __props__.__dict__["file_type"] = None
            __props__.__dict__["name"] = None
        super(CloudforceOneRequestAsset, __self__).__init__(
            'cloudflare:index/cloudforceOneRequestAsset:CloudforceOneRequestAsset',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_identifier: Optional[pulumi.Input[str]] = None,
            cloudforce_one_request_asset_id: Optional[pulumi.Input[float]] = None,
            created: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            file_type: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            page: Optional[pulumi.Input[float]] = None,
            per_page: Optional[pulumi.Input[float]] = None,
            request_identifier: Optional[pulumi.Input[str]] = None,
            source: Optional[pulumi.Input[str]] = None) -> 'CloudforceOneRequestAsset':
        """
        Get an existing CloudforceOneRequestAsset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_identifier: Identifier
        :param pulumi.Input[float] cloudforce_one_request_asset_id: Asset ID
        :param pulumi.Input[str] created: Asset creation time
        :param pulumi.Input[str] description: Asset description
        :param pulumi.Input[str] file_type: Asset file type
        :param pulumi.Input[str] name: Asset name
        :param pulumi.Input[float] page: Page number of results
        :param pulumi.Input[float] per_page: Number of results per page
        :param pulumi.Input[str] request_identifier: UUID
        :param pulumi.Input[str] source: Asset file to upload
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CloudforceOneRequestAssetState.__new__(_CloudforceOneRequestAssetState)

        __props__.__dict__["account_identifier"] = account_identifier
        __props__.__dict__["cloudforce_one_request_asset_id"] = cloudforce_one_request_asset_id
        __props__.__dict__["created"] = created
        __props__.__dict__["description"] = description
        __props__.__dict__["file_type"] = file_type
        __props__.__dict__["name"] = name
        __props__.__dict__["page"] = page
        __props__.__dict__["per_page"] = per_page
        __props__.__dict__["request_identifier"] = request_identifier
        __props__.__dict__["source"] = source
        return CloudforceOneRequestAsset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountIdentifier")
    def account_identifier(self) -> pulumi.Output[str]:
        """
        Identifier
        """
        return pulumi.get(self, "account_identifier")

    @property
    @pulumi.getter(name="cloudforceOneRequestAssetId")
    def cloudforce_one_request_asset_id(self) -> pulumi.Output[float]:
        """
        Asset ID
        """
        return pulumi.get(self, "cloudforce_one_request_asset_id")

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        Asset creation time
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Asset description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="fileType")
    def file_type(self) -> pulumi.Output[str]:
        """
        Asset file type
        """
        return pulumi.get(self, "file_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Asset name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def page(self) -> pulumi.Output[float]:
        """
        Page number of results
        """
        return pulumi.get(self, "page")

    @property
    @pulumi.getter(name="perPage")
    def per_page(self) -> pulumi.Output[float]:
        """
        Number of results per page
        """
        return pulumi.get(self, "per_page")

    @property
    @pulumi.getter(name="requestIdentifier")
    def request_identifier(self) -> pulumi.Output[str]:
        """
        UUID
        """
        return pulumi.get(self, "request_identifier")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[str]]:
        """
        Asset file to upload
        """
        return pulumi.get(self, "source")

