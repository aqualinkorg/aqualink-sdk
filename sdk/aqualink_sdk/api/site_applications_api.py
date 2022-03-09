# coding: utf-8

"""
    Aqualink API documentation

    The Aqualink public API documentation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from aqualink_sdk.api_client import ApiClient


class SiteApplicationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def site_applications_controller_find_one_from_site(self, site_id, **kwargs):  # noqa: E501
        """Returns site application of specified site  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.site_applications_controller_find_one_from_site(site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float site_id: (required)
        :return: SiteApplication
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.site_applications_controller_find_one_from_site_with_http_info(site_id, **kwargs)  # noqa: E501
        else:
            (data) = self.site_applications_controller_find_one_from_site_with_http_info(site_id, **kwargs)  # noqa: E501
            return data

    def site_applications_controller_find_one_from_site_with_http_info(self, site_id, **kwargs):  # noqa: E501
        """Returns site application of specified site  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.site_applications_controller_find_one_from_site_with_http_info(site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float site_id: (required)
        :return: SiteApplication
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method site_applications_controller_find_one_from_site" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `site_applications_controller_find_one_from_site`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/site-applications/sites/{siteId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SiteApplication',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def site_applications_controller_update(self, body, app_id, **kwargs):  # noqa: E501
        """Updates site application by providing its appId. Needs authentication.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.site_applications_controller_update(body, app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SitesSiteIdBody body: (required)
        :param float app_id: (required)
        :return: SiteApplication
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.site_applications_controller_update_with_http_info(body, app_id, **kwargs)  # noqa: E501
        else:
            (data) = self.site_applications_controller_update_with_http_info(body, app_id, **kwargs)  # noqa: E501
            return data

    def site_applications_controller_update_with_http_info(self, body, app_id, **kwargs):  # noqa: E501
        """Updates site application by providing its appId. Needs authentication.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.site_applications_controller_update_with_http_info(body, app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SitesSiteIdBody body: (required)
        :param float app_id: (required)
        :return: SiteApplication
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'app_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method site_applications_controller_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `site_applications_controller_update`")  # noqa: E501
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params or
                params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `site_applications_controller_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['appId'] = params['app_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/site-applications/{appId}/sites/{siteId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SiteApplication',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
