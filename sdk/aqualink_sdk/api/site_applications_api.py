"""
    Aqualink API documentation

    The Aqualink public API documentation  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from aqualink_sdk.api_client import ApiClient, Endpoint as _Endpoint
from aqualink_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from aqualink_sdk.model.inline_object import InlineObject
from aqualink_sdk.model.inline_response404 import InlineResponse404
from aqualink_sdk.model.site_application import SiteApplication


class SiteApplicationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.site_applications_controller_find_one_from_site_endpoint = _Endpoint(
            settings={
                'response_type': (SiteApplication,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/site-applications/sites/{siteId}',
                'operation_id': 'site_applications_controller_find_one_from_site',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'site_id',
                ],
                'required': [
                    'site_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'site_id':
                        (float,),
                },
                'attribute_map': {
                    'site_id': 'siteId',
                },
                'location_map': {
                    'site_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.site_applications_controller_update_endpoint = _Endpoint(
            settings={
                'response_type': (SiteApplication,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/site-applications/{appId}/sites/{siteId}',
                'operation_id': 'site_applications_controller_update',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_id',
                    'inline_object',
                ],
                'required': [
                    'app_id',
                    'inline_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'app_id':
                        (float,),
                    'inline_object':
                        (InlineObject,),
                },
                'attribute_map': {
                    'app_id': 'appId',
                },
                'location_map': {
                    'app_id': 'path',
                    'inline_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def site_applications_controller_find_one_from_site(
        self,
        site_id,
        **kwargs
    ):
        """Returns site application of specified site  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.site_applications_controller_find_one_from_site(site_id, async_req=True)
        >>> result = thread.get()

        Args:
            site_id (float):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            SiteApplication
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['site_id'] = \
            site_id
        return self.site_applications_controller_find_one_from_site_endpoint.call_with_http_info(**kwargs)

    def site_applications_controller_update(
        self,
        app_id,
        inline_object,
        **kwargs
    ):
        """Updates site application by providing its appId. Needs authentication.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.site_applications_controller_update(app_id, inline_object, async_req=True)
        >>> result = thread.get()

        Args:
            app_id (float):
            inline_object (InlineObject):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            SiteApplication
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['app_id'] = \
            app_id
        kwargs['inline_object'] = \
            inline_object
        return self.site_applications_controller_update_endpoint.call_with_http_info(**kwargs)

