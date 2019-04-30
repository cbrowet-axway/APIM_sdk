# RemoteHost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the remote host | [optional] 
**name** | **str** | The host name of the remote host | 
**port** | **int** | The host port of the remote host | 
**created_on** | **int** | Epoch/Unix time stamp when the remote host was created | [optional] 
**created_by** | **str** | The unique identifier for user that created the remote host | [optional] 
**organization_id** | **str** | The organization identifier to which the remote host belongs | [optional] 
**max_connections** | **int** | The maximum number of connections to open to a Remote Host. If the maximum number of connections has already been established, the API Gateway instance waits for a connection to drop or become idle before making another request. The default value is -1, meaning there is no limit | [optional] 
**allow_http11** | **bool** | Enables the API Gateway to use HTTP 1.1 when connecting to the remote host. Default value is false, meaning HTTP 1.0 is used | [optional] [default to False]
**include_content_length_request** | **bool** | If this option is set, the API Gateway will include the Content-Length HTTP header in all requests to this Remote Host. Default value is false. | [optional] [default to False]
**include_content_length_response** | **bool** | If this option is set, if the API Gateway receives a response from this Remote Host that contains a Content-Length HTTP header, it returns this length to the client. Default value is false. | [optional] [default to False]
**offer_tls_server_name** | **bool** | Adds a field to outbound TLS/SSL calls that shows the name that the client used to connect. Default value is false. | [optional] [default to False]
**verify_server_hostname** | **bool** | Ensures that the certificate presented by the server matches the name of the remote host being connected to. This prevents host spoofing and man-in-the-middle attacks. Default value is false. | [optional] [default to False]
**connection_timeout** | **int** | If a connection to this remote host is not established within the time set in this field, the connection times out and the connection fails. Default value is 30000 milliseconds (30 seconds). | [optional] 
**active_timeout** | **int** | The maximum amount of time permitted between reading successive blocks of data. If the Active Timeout is exceeded, the API Gateway closes the connection. This prevents a Remote Host from closing the connection while sending data. Default value is 30000 milliseconds (30 seconds). | [optional] 
**transaction_timeout** | **int** | The maximum amount of time permitted to complete the transaction. Default value is 240000 milliseconds (4 minutes). | [optional] 
**idle_timeout** | **int** | The maximum amount of time that API Gateway waits after sending a message over a persistent connection to the Remote Host before it closes the connection. Default value is 15000 milliseconds (15 seconds). | [optional] 
**max_receive_bytes** | **int** | The maximum amount of data the API Gateway can receive per transaction. Default value is 20971520 bytes (20MiB). | [optional] 
**max_send_bytes** | **int** | The maximum amount of data the API Gateway can transmit per transaction. Default value is 20971520 bytes (20MiB). | [optional] 
**input_buffer_size** | **int** | The maximum amount of memory allocated to each request. Default value is 8192 bytes. | [optional] 
**output_buffer_size** | **int** | The maximum amount of memory allocated to each response. Default value is 8192 bytes. | [optional] 
**address_cache_timeout** | **int** | The period of time to cache addressing information after it has been received from the naming service. Default value is 300000 milliseconds (5 minutes) | [optional] 
**ssl_session_cache_size** | **int** | Specifies the size of the SSL session cache for connections to the remote host, which controls the number of idle SSL sessions that can be kept in memory. Default value is 32. | [optional] 
**input_encodings** | **list[str]** | Specifies the HTTP content encodings that the API Gateway can accept from peers. Supported encodings: *deflate*, *gzip*. If no encodings are specified the default encoding is applied. | [optional] 
**output_encodings** | **list[str]** | Specifies the HTTP content encodings that the API Gateway can apply to outgoing messages. Supported encodings: *deflate*, *gzip*. If no encodings are specified the default encoding is applied. | [optional] 
**export_correlation_id** | **bool** | Specifies whether to add the X-CorrelationID header to outbound messages | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


