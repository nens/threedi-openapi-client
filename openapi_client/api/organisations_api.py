# coding: utf-8

"""
    3DI API

    3DI simulation API  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient


class OrganisationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def organisations_list(self, **kwargs):  # noqa: E501
        """Read-only API endpoint for interacting with organisations.  # noqa: E501

        ##Authorization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.organisations_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name:
        :param str name__contains:
        :param str name__in: Multiple values may be separated by commas.
        :param str name__startswith:
        :param str name__istartswith:
        :param str name__endswith:
        :param str name__regex:
        :param str unique_id:
        :param str unique_id__contains:
        :param str unique_id__in: Multiple values may be separated by commas.
        :param str unique_id__startswith:
        :param str unique_id__istartswith:
        :param str unique_id__endswith:
        :param str unique_id__regex:
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.organisations_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.organisations_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def organisations_list_with_http_info(self, **kwargs):  # noqa: E501
        """Read-only API endpoint for interacting with organisations.  # noqa: E501

        ##Authorization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.organisations_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name:
        :param str name__contains:
        :param str name__in: Multiple values may be separated by commas.
        :param str name__startswith:
        :param str name__istartswith:
        :param str name__endswith:
        :param str name__regex:
        :param str unique_id:
        :param str unique_id__contains:
        :param str unique_id__in: Multiple values may be separated by commas.
        :param str unique_id__startswith:
        :param str unique_id__istartswith:
        :param str unique_id__endswith:
        :param str unique_id__regex:
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['name', 'name__contains', 'name__in', 'name__startswith', 'name__istartswith', 'name__endswith', 'name__regex', 'unique_id', 'unique_id__contains', 'unique_id__in', 'unique_id__startswith', 'unique_id__istartswith', 'unique_id__endswith', 'unique_id__regex', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method organisations_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'name__contains' in local_var_params:
            query_params.append(('name__contains', local_var_params['name__contains']))  # noqa: E501
        if 'name__in' in local_var_params:
            query_params.append(('name__in', local_var_params['name__in']))  # noqa: E501
        if 'name__startswith' in local_var_params:
            query_params.append(('name__startswith', local_var_params['name__startswith']))  # noqa: E501
        if 'name__istartswith' in local_var_params:
            query_params.append(('name__istartswith', local_var_params['name__istartswith']))  # noqa: E501
        if 'name__endswith' in local_var_params:
            query_params.append(('name__endswith', local_var_params['name__endswith']))  # noqa: E501
        if 'name__regex' in local_var_params:
            query_params.append(('name__regex', local_var_params['name__regex']))  # noqa: E501
        if 'unique_id' in local_var_params:
            query_params.append(('unique_id', local_var_params['unique_id']))  # noqa: E501
        if 'unique_id__contains' in local_var_params:
            query_params.append(('unique_id__contains', local_var_params['unique_id__contains']))  # noqa: E501
        if 'unique_id__in' in local_var_params:
            query_params.append(('unique_id__in', local_var_params['unique_id__in']))  # noqa: E501
        if 'unique_id__startswith' in local_var_params:
            query_params.append(('unique_id__startswith', local_var_params['unique_id__startswith']))  # noqa: E501
        if 'unique_id__istartswith' in local_var_params:
            query_params.append(('unique_id__istartswith', local_var_params['unique_id__istartswith']))  # noqa: E501
        if 'unique_id__endswith' in local_var_params:
            query_params.append(('unique_id__endswith', local_var_params['unique_id__endswith']))  # noqa: E501
        if 'unique_id__regex' in local_var_params:
            query_params.append(('unique_id__regex', local_var_params['unique_id__regex']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/organisations/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def organisations_permissions(self, unique_id, **kwargs):  # noqa: E501
        """Read-only API endpoint for interacting with organisations.  # noqa: E501

        ##Authorization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.organisations_permissions(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str unique_id: (required)
        :return: list[OrganisationRole]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.organisations_permissions_with_http_info(unique_id, **kwargs)  # noqa: E501
        else:
            (data) = self.organisations_permissions_with_http_info(unique_id, **kwargs)  # noqa: E501
            return data

    def organisations_permissions_with_http_info(self, unique_id, **kwargs):  # noqa: E501
        """Read-only API endpoint for interacting with organisations.  # noqa: E501

        ##Authorization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.organisations_permissions_with_http_info(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str unique_id: (required)
        :return: list[OrganisationRole]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['unique_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method organisations_permissions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'unique_id' is set
        if ('unique_id' not in local_var_params or
                local_var_params['unique_id'] is None):
            raise ValueError("Missing the required parameter `unique_id` when calling `organisations_permissions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'unique_id' in local_var_params:
            path_params['unique_id'] = local_var_params['unique_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/organisations/{unique_id}/permissions/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[OrganisationRole]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def organisations_read(self, unique_id, **kwargs):  # noqa: E501
        """Read-only API endpoint for interacting with organisations.  # noqa: E501

        ##Authorization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.organisations_read(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str unique_id: (required)
        :return: Organisation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.organisations_read_with_http_info(unique_id, **kwargs)  # noqa: E501
        else:
            (data) = self.organisations_read_with_http_info(unique_id, **kwargs)  # noqa: E501
            return data

    def organisations_read_with_http_info(self, unique_id, **kwargs):  # noqa: E501
        """Read-only API endpoint for interacting with organisations.  # noqa: E501

        ##Authorization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.organisations_read_with_http_info(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str unique_id: (required)
        :return: Organisation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['unique_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method organisations_read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'unique_id' is set
        if ('unique_id' not in local_var_params or
                local_var_params['unique_id'] is None):
            raise ValueError("Missing the required parameter `unique_id` when calling `organisations_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'unique_id' in local_var_params:
            path_params['unique_id'] = local_var_params['unique_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/organisations/{unique_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Organisation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
