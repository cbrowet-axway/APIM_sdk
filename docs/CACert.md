# CACert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_blob** | **str** | Raw certificate data | [optional] 
**name** | **str** | Name of the certificate | [optional] 
**alias** | **str** | Certificate alias | [optional] 
**subject** | **str** | Certificate subject | [optional] 
**issuer** | **str** | Certificate issuer | [optional] 
**version** | **int** | Version of the certificate | [optional] 
**not_valid_before** | **int** | Start date of the certificate | [optional] 
**not_valid_after** | **int** | Expiry date of the certificate | [optional] 
**signature_algorithm** | **str** | The algorithm used to sign the certificate. | [optional] 
**sha1_fingerprint** | **str** | SHA1 fingerprint. | [optional] 
**md5_fingerprint** | **str** | MD5 fingerprint. | [optional] 
**expired** | **bool** | Flag indicating whether or not the certificate is expired. | [optional] [default to False]
**not_yet_valid** | **bool** | Flag indicating whether or not the certificate is valid yet. | [optional] [default to False]
**inbound** | **bool** | Flag indicating whether this certificate is used for inbound SSL connections when invoking the virtualized API. | [optional] [default to False]
**outbound** | **bool** | Flag indicating whether this certificate is used for outbound SSL connections when invoking the virtualized API. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


