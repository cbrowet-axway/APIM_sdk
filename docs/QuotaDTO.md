# QuotaDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The quota identifier | 
**type** | **str** | The quota type, either API or APPLICATION | 
**name** | **str** | The name of the quota | 
**description** | **str** | The quota for MyApplication the overrides default Application quota | [optional] 
**restrictions** | [**list[QuotaApiConstraintDTO]**](QuotaApiConstraintDTO.md) | An array of restrictions imposed on the quota | [optional] 
**system** | **bool** | Indicates if the quota is system (protected) | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


