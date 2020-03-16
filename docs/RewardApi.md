# marax_server_sdk.RewardApi

All URIs are relative to *https://&lt;client-name&gt;.marax.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_event**](RewardApi.md#process_event) | **POST** /event/process | Perform reward post-processing


# **process_event**
> Response200 process_event(request_body=request_body)

Perform reward post-processing

Process events like ORDER_COMPLETED and do the necessary changes to the validity of the reward object (if applicable) (Eg., increasing the count of reward redeemed, changing reward status to redeemed) 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import marax_server_sdk
from marax_server_sdk.rest import ApiException
from pprint import pprint
configuration = marax_server_sdk.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Defining host is optional and default to https://<client-name>.marax.ai
configuration.host = "https://<client-name>.marax.ai"
# Enter a context with an instance of the API client
with marax_server_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marax_server_sdk.RewardApi(api_client)
    request_body = marax_server_sdk.RequestBody() # RequestBody | Details of transactional event (optional)

    try:
        # Perform reward post-processing
        api_response = api_instance.process_event(request_body=request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RewardApi->process_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**RequestBody**](RequestBody.md)| Details of transactional event | [optional] 

### Return type

[**Response200**](Response200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

