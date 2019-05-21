# CustomProperty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label for the custom property, which will be displayed in the API Manager UI | [optional] 
**type** | **str** | The type of the custom property. Can be one of the following values: [&#39;custom&#39;, &#39;switch&#39;, &#39;select&#39;, &#39;number&#39;]. Default value is &#39;custom&#39; (i.e. free-form text) | [optional] 
**disabled** | **bool** | Specifies whether the custom property is disabled. Default value is false | [optional] [default to False]
**required** | **bool** | Specifies whether the custom property is required or optional. Default value is false | [optional] [default to False]
**help** | **str** | Specifies the help text for the custom property that will appear in the API Manager UI. This field is optional | [optional] 
**permissions** | [**dict(str, CustomPropertyPermission)**](CustomPropertyPermission.md) | Specifies the read/write permissions per role (admin, oadmin and user) for the custom property. This field is optional. By default all roles have read/write access | [optional] 
**options** | [**list[CustomPropertyOption]**](CustomPropertyOption.md) | Specifies the options for &#39;switch&#39; and &#39;select&#39; custom properties which will be available in the API Manager UI. This field is conditional and only required for custom properties of type &#39;switch&#39; or &#39;select&#39;, otherwise it is ignored. | [optional] 
**default_value** | **object** | Specifies the default value for the custom property. This field is optional, but recommended. This type of this field depends on the type of the custom property. It can be one of the following: string, integer, double, boolean | [optional] 
**regex** | **str** | Specifies a validation regular expression for custom properties of type &#39;custom&#39;. This field is conditional, i.e. optional for custom properties of type &#39;custom&#39;, otherwise ignored | [optional] 
**min_value** | **object** | Specifies a validation minimum value for custom properties of type &#39;number&#39;. Can be an integer, a floating point number, or a string represation of an integer or floating point number. This field is conditional, i.e. optional for custom properties of type &#39;number&#39;, otherwise ignored. minValue and maxValue must both be of the same type so as to avoid unexpected behaviour during validation. Scientific notation is not supported. | [optional] 
**max_value** | **object** | Specifies a validation maximum value for custom properties of type &#39;number&#39;. Can be an integer, a floating point number, or a string represation of an integer or floating point number. This field is conditional, i.e. optional for custom properties of type &#39;number&#39;, otherwise ignored. minValue and maxValue must both be of the same type so as to avoid unexpected behaviour during validation. Scientific notation is not supported. | [optional] 
**decimal_places** | **int** | Specifies the number of decimal places to be used when validating &#39;number&#39; fields. Default value is 0, which indicates that the value is a whole number. | [optional] 
**error** | **str** | Specifies an error message which will appear when input validation fails. The format of this field is a string. This field is only valid for custom properties of type &#39;custom&#39; and &#39;number&#39;, otherwise ignored | [optional] 
**custom** | **object** | Optional field allowing for the definition of custom metadata for the custom property. This will be used by clients other than API Manager, but API Manager may populate this field with API Manager-specific values in the future. If present, must be a valid JSON &#39;object&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


