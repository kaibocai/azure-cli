# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network vnet-gateway revoked-cert delete",
)
class Delete(AAZCommand):
    """Delete a revoked certificate.

    :example: Delete a revoked certificate.
        az network vnet-gateway revoked-cert delete -g MyResourceGroup -n MyRootCertificate --gateway-name MyVnetGateway

    :example: Delete a revoked certificate.
        az network vnet-gateway revoked-cert delete --gateway-name MyVnetGateway --name MyRootCertificate --resource-group MyResourceGroup --subscription MySubscription
    """

    _aaz_info = {
        "version": "2015-06-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/virtualnetworkgateways/{}", "2015-06-15", "properties.vpnClientConfiguration.vpnClientRevokedCertificates[]"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self.SubresourceSelector(ctx=self.ctx, name="subresource")
        return self.build_lro_poller(self._execute_operations, None)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.gateway_name = AAZStrArg(
            options=["--gateway-name"],
            help="Virtual network gateway name.",
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Root certificate name.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.VirtualNetworkGatewaysGet(ctx=self.ctx)()
        self.pre_instance_delete()
        self.InstanceDeleteByJson(ctx=self.ctx)()
        self.post_instance_delete()
        yield self.VirtualNetworkGatewaysCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_delete(self):
        pass

    @register_callback
    def post_instance_delete(self):
        pass

    class SubresourceSelector(AAZJsonSelector):

        def _get(self):
            result = self.ctx.vars.instance
            result = result.properties.vpnClientConfiguration.vpnClientRevokedCertificates
            filters = enumerate(result)
            filters = filter(
                lambda e: e[1].name == self.ctx.args.name,
                filters
            )
            idx = next(filters)[0]
            return result[idx]

        def _set(self, value):
            result = self.ctx.vars.instance
            result = result.properties.vpnClientConfiguration.vpnClientRevokedCertificates
            filters = enumerate(result)
            filters = filter(
                lambda e: e[1].name == self.ctx.args.name,
                filters
            )
            idx = next(filters, [len(result)])[0]
            result[idx] = value
            return

    class VirtualNetworkGatewaysGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualNetworkGatewayName", self.ctx.args.gateway_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2015-06-15",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _DeleteHelper._build_schema_virtual_network_gateway_read(cls._schema_on_200)

            return cls._schema_on_200

    class VirtualNetworkGatewaysCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualNetworkGatewayName", self.ctx.args.gateway_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2015-06-15",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _DeleteHelper._build_schema_virtual_network_gateway_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceDeleteByJson(AAZJsonInstanceDeleteOperation):

        def __call__(self, *args, **kwargs):
            self.ctx.selectors.subresource.set(self._delete_instance())


class _DeleteHelper:
    """Helper class for Delete"""

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id

    _schema_virtual_network_gateway_read = None

    @classmethod
    def _build_schema_virtual_network_gateway_read(cls, _schema):
        if cls._schema_virtual_network_gateway_read is not None:
            _schema.etag = cls._schema_virtual_network_gateway_read.etag
            _schema.id = cls._schema_virtual_network_gateway_read.id
            _schema.location = cls._schema_virtual_network_gateway_read.location
            _schema.name = cls._schema_virtual_network_gateway_read.name
            _schema.properties = cls._schema_virtual_network_gateway_read.properties
            _schema.tags = cls._schema_virtual_network_gateway_read.tags
            _schema.type = cls._schema_virtual_network_gateway_read.type
            return

        cls._schema_virtual_network_gateway_read = _schema_virtual_network_gateway_read = AAZObjectType()

        virtual_network_gateway_read = _schema_virtual_network_gateway_read
        virtual_network_gateway_read.etag = AAZStrType()
        virtual_network_gateway_read.id = AAZStrType()
        virtual_network_gateway_read.location = AAZStrType()
        virtual_network_gateway_read.name = AAZStrType(
            flags={"read_only": True},
        )
        virtual_network_gateway_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        virtual_network_gateway_read.tags = AAZDictType()
        virtual_network_gateway_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_virtual_network_gateway_read.properties
        properties.bgp_settings = AAZObjectType(
            serialized_name="bgpSettings",
        )
        properties.enable_bgp = AAZBoolType(
            serialized_name="enableBgp",
        )
        properties.gateway_default_site = AAZObjectType(
            serialized_name="gatewayDefaultSite",
        )
        cls._build_schema_sub_resource_read(properties.gateway_default_site)
        properties.gateway_type = AAZStrType(
            serialized_name="gatewayType",
        )
        properties.ip_configurations = AAZListType(
            serialized_name="ipConfigurations",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.resource_guid = AAZStrType(
            serialized_name="resourceGuid",
        )
        properties.sku = AAZObjectType()
        properties.vpn_client_configuration = AAZObjectType(
            serialized_name="vpnClientConfiguration",
        )
        properties.vpn_type = AAZStrType(
            serialized_name="vpnType",
        )

        bgp_settings = _schema_virtual_network_gateway_read.properties.bgp_settings
        bgp_settings.asn = AAZIntType()
        bgp_settings.bgp_peering_address = AAZStrType(
            serialized_name="bgpPeeringAddress",
        )
        bgp_settings.peer_weight = AAZIntType(
            serialized_name="peerWeight",
        )

        ip_configurations = _schema_virtual_network_gateway_read.properties.ip_configurations
        ip_configurations.Element = AAZObjectType()

        _element = _schema_virtual_network_gateway_read.properties.ip_configurations.Element
        _element.etag = AAZStrType()
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_virtual_network_gateway_read.properties.ip_configurations.Element.properties
        properties.private_ip_address = AAZStrType(
            serialized_name="privateIPAddress",
        )
        properties.private_ip_allocation_method = AAZStrType(
            serialized_name="privateIPAllocationMethod",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.public_ip_address = AAZObjectType(
            serialized_name="publicIPAddress",
        )
        cls._build_schema_sub_resource_read(properties.public_ip_address)
        properties.subnet = AAZObjectType()
        cls._build_schema_sub_resource_read(properties.subnet)

        sku = _schema_virtual_network_gateway_read.properties.sku
        sku.capacity = AAZIntType()
        sku.name = AAZStrType()
        sku.tier = AAZStrType()

        vpn_client_configuration = _schema_virtual_network_gateway_read.properties.vpn_client_configuration
        vpn_client_configuration.vpn_client_address_pool = AAZObjectType(
            serialized_name="vpnClientAddressPool",
        )
        vpn_client_configuration.vpn_client_revoked_certificates = AAZListType(
            serialized_name="vpnClientRevokedCertificates",
        )
        vpn_client_configuration.vpn_client_root_certificates = AAZListType(
            serialized_name="vpnClientRootCertificates",
        )

        vpn_client_address_pool = _schema_virtual_network_gateway_read.properties.vpn_client_configuration.vpn_client_address_pool
        vpn_client_address_pool.address_prefixes = AAZListType(
            serialized_name="addressPrefixes",
        )

        address_prefixes = _schema_virtual_network_gateway_read.properties.vpn_client_configuration.vpn_client_address_pool.address_prefixes
        address_prefixes.Element = AAZStrType()

        vpn_client_revoked_certificates = _schema_virtual_network_gateway_read.properties.vpn_client_configuration.vpn_client_revoked_certificates
        vpn_client_revoked_certificates.Element = AAZObjectType()

        _element = _schema_virtual_network_gateway_read.properties.vpn_client_configuration.vpn_client_revoked_certificates.Element
        _element.etag = AAZStrType()
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_virtual_network_gateway_read.properties.vpn_client_configuration.vpn_client_revoked_certificates.Element.properties
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.thumbprint = AAZStrType()

        vpn_client_root_certificates = _schema_virtual_network_gateway_read.properties.vpn_client_configuration.vpn_client_root_certificates
        vpn_client_root_certificates.Element = AAZObjectType()

        _element = _schema_virtual_network_gateway_read.properties.vpn_client_configuration.vpn_client_root_certificates.Element
        _element.etag = AAZStrType()
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_virtual_network_gateway_read.properties.vpn_client_configuration.vpn_client_root_certificates.Element.properties
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.public_cert_data = AAZStrType(
            serialized_name="publicCertData",
        )

        tags = _schema_virtual_network_gateway_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_virtual_network_gateway_read.etag
        _schema.id = cls._schema_virtual_network_gateway_read.id
        _schema.location = cls._schema_virtual_network_gateway_read.location
        _schema.name = cls._schema_virtual_network_gateway_read.name
        _schema.properties = cls._schema_virtual_network_gateway_read.properties
        _schema.tags = cls._schema_virtual_network_gateway_read.tags
        _schema.type = cls._schema_virtual_network_gateway_read.type


__all__ = ["Delete"]
