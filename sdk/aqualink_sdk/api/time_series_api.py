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
from aqualink_sdk.model.inline_response200 import InlineResponse200
from aqualink_sdk.model.inline_response2001 import InlineResponse2001


class TimeSeriesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.time_series_controller_find_site_data_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [],
                'endpoint_path': '/time-series/sites/{siteId}',
                'operation_id': 'time_series_controller_find_site_data',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'site_id',
                    'metrics',
                    'start',
                    'end',
                    'hourly',
                ],
                'required': [
                    'site_id',
                    'metrics',
                    'start',
                    'end',
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
                    'metrics':
                        ([str],),
                    'start':
                        (str,),
                    'end':
                        (str,),
                    'hourly':
                        (bool,),
                },
                'attribute_map': {
                    'site_id': 'siteId',
                    'metrics': 'metrics',
                    'start': 'start',
                    'end': 'end',
                    'hourly': 'hourly',
                },
                'location_map': {
                    'site_id': 'path',
                    'metrics': 'query',
                    'start': 'query',
                    'end': 'query',
                    'hourly': 'query',
                },
                'collection_format_map': {
                    'metrics': 'multi',
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
        self.time_series_controller_find_site_data_range_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2001,),
                'auth': [],
                'endpoint_path': '/time-series/sites/{siteId}/range',
                'operation_id': 'time_series_controller_find_site_data_range',
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
        self.time_series_controller_find_survey_point_data_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [],
                'endpoint_path': '/time-series/sites/{siteId}/site-survey-points/{surveyPointId}',
                'operation_id': 'time_series_controller_find_survey_point_data',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'site_id',
                    'survey_point_id',
                    'metrics',
                    'start',
                    'end',
                    'hourly',
                ],
                'required': [
                    'site_id',
                    'survey_point_id',
                    'metrics',
                    'start',
                    'end',
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
                    'survey_point_id':
                        (float,),
                    'metrics':
                        ([str],),
                    'start':
                        (str,),
                    'end':
                        (str,),
                    'hourly':
                        (bool,),
                },
                'attribute_map': {
                    'site_id': 'siteId',
                    'survey_point_id': 'surveyPointId',
                    'metrics': 'metrics',
                    'start': 'start',
                    'end': 'end',
                    'hourly': 'hourly',
                },
                'location_map': {
                    'site_id': 'path',
                    'survey_point_id': 'path',
                    'metrics': 'query',
                    'start': 'query',
                    'end': 'query',
                    'hourly': 'query',
                },
                'collection_format_map': {
                    'metrics': 'multi',
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
        self.time_series_controller_find_survey_point_data_range_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2001,),
                'auth': [],
                'endpoint_path': '/time-series/sites/{siteId}/site-survey-points/{surveyPointId}/range',
                'operation_id': 'time_series_controller_find_survey_point_data_range',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'site_id',
                    'survey_point_id',
                ],
                'required': [
                    'site_id',
                    'survey_point_id',
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
                    'survey_point_id':
                        (float,),
                },
                'attribute_map': {
                    'site_id': 'siteId',
                    'survey_point_id': 'surveyPointId',
                },
                'location_map': {
                    'site_id': 'path',
                    'survey_point_id': 'path',
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
        self.time_series_controller_upload_time_series_data_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/time-series/sites/{siteId}/site-survey-points/{surveyPointId}/upload',
                'operation_id': 'time_series_controller_upload_time_series_data',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'site_id',
                    'survey_point_id',
                    'fail_on_warning',
                ],
                'required': [
                    'site_id',
                    'survey_point_id',
                    'fail_on_warning',
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
                    'survey_point_id':
                        (float,),
                    'fail_on_warning':
                        (bool,),
                },
                'attribute_map': {
                    'site_id': 'siteId',
                    'survey_point_id': 'surveyPointId',
                    'fail_on_warning': 'failOnWarning',
                },
                'location_map': {
                    'site_id': 'path',
                    'survey_point_id': 'path',
                    'fail_on_warning': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )

    def time_series_controller_find_site_data(
        self,
        site_id,
        metrics,
        start,
        end,
        **kwargs
    ):
        """Returns specified time series data for a specified site  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.time_series_controller_find_site_data(site_id, metrics, start, end, async_req=True)
        >>> result = thread.get()

        Args:
            site_id (float):
            metrics ([str]):
            start (str):
            end (str):

        Keyword Args:
            hourly (bool): [optional]
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
            InlineResponse200
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
        kwargs['metrics'] = \
            metrics
        kwargs['start'] = \
            start
        kwargs['end'] = \
            end
        return self.time_series_controller_find_site_data_endpoint.call_with_http_info(**kwargs)

    def time_series_controller_find_site_data_range(
        self,
        site_id,
        **kwargs
    ):
        """Returns the range of the available time series data for a specified site  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.time_series_controller_find_site_data_range(site_id, async_req=True)
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
            InlineResponse2001
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
        return self.time_series_controller_find_site_data_range_endpoint.call_with_http_info(**kwargs)

    def time_series_controller_find_survey_point_data(
        self,
        site_id,
        survey_point_id,
        metrics,
        start,
        end,
        **kwargs
    ):
        """Returns specified time series data for a specified site point of interest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.time_series_controller_find_survey_point_data(site_id, survey_point_id, metrics, start, end, async_req=True)
        >>> result = thread.get()

        Args:
            site_id (float):
            survey_point_id (float):
            metrics ([str]):
            start (str):
            end (str):

        Keyword Args:
            hourly (bool): [optional]
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
            InlineResponse200
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
        kwargs['survey_point_id'] = \
            survey_point_id
        kwargs['metrics'] = \
            metrics
        kwargs['start'] = \
            start
        kwargs['end'] = \
            end
        return self.time_series_controller_find_survey_point_data_endpoint.call_with_http_info(**kwargs)

    def time_series_controller_find_survey_point_data_range(
        self,
        site_id,
        survey_point_id,
        **kwargs
    ):
        """Returns the range of the available time series data for a specified site point of interest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.time_series_controller_find_survey_point_data_range(site_id, survey_point_id, async_req=True)
        >>> result = thread.get()

        Args:
            site_id (float):
            survey_point_id (float):

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
            InlineResponse2001
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
        kwargs['survey_point_id'] = \
            survey_point_id
        return self.time_series_controller_find_survey_point_data_range_endpoint.call_with_http_info(**kwargs)

    def time_series_controller_upload_time_series_data(
        self,
        site_id,
        survey_point_id,
        fail_on_warning,
        **kwargs
    ):
        """Upload time series data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.time_series_controller_upload_time_series_data(site_id, survey_point_id, fail_on_warning, async_req=True)
        >>> result = thread.get()

        Args:
            site_id (float):
            survey_point_id (float):
            fail_on_warning (bool):

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
            None
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
        kwargs['survey_point_id'] = \
            survey_point_id
        kwargs['fail_on_warning'] = \
            fail_on_warning
        return self.time_series_controller_upload_time_series_data_endpoint.call_with_http_info(**kwargs)

