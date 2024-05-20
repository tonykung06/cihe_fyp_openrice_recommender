# Snippets API
Test description

## Version: v1

### Terms of service
https://www.google.com/policies/terms/

**Contact information:**  
contact@snippets.local  

**License:** BSD License

### Security
**Basic**  

| basic | *Basic* |
| ----- | ------- |

**Bearer**  

| apiKey | *API Key*     |
| ------ | ------------- |
| Name   | Authorization |
| In     | header        |

### /api-token-auth/

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema                  |
| ---- | ---------- | ----------- | -------- | ----------------------- |
| data | body       |             | Yes      | [AuthToken](#AuthToken) |

##### Responses

| Code | Description | Schema                  |
| ---- | ----------- | ----------------------- |
| 201  |             | [AuthToken](#AuthToken) |

### /review/

#### POST
##### Description:

A simple APIView for creating review entires.

##### Parameters

| Name | Located in | Description | Required | Schema            |
| ---- | ---------- | ----------- | -------- | ----------------- |
| data | body       |             | Yes      | [Review](#Review) |

##### Responses

| Code | Description | Schema            |
| ---- | ----------- | ----------------- |
| 201  |             | [Review](#Review) |

### /users/

#### GET
##### Description:

A simple ViewSet for listing or retrieving users.

##### Parameters

| Name   | Located in | Description                                         | Required | Schema  |
| ------ | ---------- | --------------------------------------------------- | -------- | ------- |
| search | query      | A search term.                                      | No       | string  |
| limit  | query      | Number of results to return per page.               | No       | integer |
| offset | query      | The initial index from which to return the results. | No       | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200  |             | object |

### /users/{id}/

#### GET
##### Description:

A simple ViewSet for listing or retrieving users.

##### Parameters

| Name | Located in | Description                           | Required | Schema  |
| ---- | ---------- | ------------------------------------- | -------- | ------- |
| id   | path       | A unique value identifying this user. | Yes      | integer |

##### Responses

| Code | Description | Schema        |
| ---- | ----------- | ------------- |
| 200  |             | [User](#User) |

### /users/{id}/reviews/

#### GET
##### Description:

A simple ViewSet for listing or retrieving users.

##### Parameters

| Name | Located in | Description                           | Required | Schema  |
| ---- | ---------- | ------------------------------------- | -------- | ------- |
| id   | path       | A unique value identifying this user. | Yes      | integer |

##### Responses

| Code | Description | Schema        |
| ---- | ----------- | ------------- |
| 200  |             | [User](#User) |

### /users/{user_pk}/restaurants/

#### GET
##### Description:

A simple ViewSet for listing or retrieving users.

##### Parameters

| Name    | Located in | Description                                         | Required | Schema  |
| ------- | ---------- | --------------------------------------------------- | -------- | ------- |
| user_pk | path       |                                                     | Yes      | string  |
| search  | query      | A search term.                                      | No       | string  |
| limit   | query      | Number of results to return per page.               | No       | integer |
| offset  | query      | The initial index from which to return the results. | No       | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200  |             | object |

### Models


#### AuthToken

| Name     | Type   | Description | Required |
| -------- | ------ | ----------- | -------- |
| username | string |             | Yes      |
| password | string |             | Yes      |
| token    | string |             | No       |

#### Review

| Name              | Type     | Description | Required |
| ----------------- | -------- | ----------- | -------- |
| id                | integer  |             | No       |
| rating_taste      | integer  |             | Yes      |
| rating_decor      | integer  |             | Yes      |
| rating_service    | integer  |             | Yes      |
| rating_hygiene    | integer  |             | Yes      |
| rating_value      | integer  |             | Yes      |
| dining_method     | string   |             | Yes      |
| review_date       | date     |             | No       |
| date_of_visit     | date     |             | No       |
| spending_per_head | string   |             | Yes      |
| title             | string   |             | Yes      |
| comment           | string   |             | Yes      |
| created_at        | dateTime |             | No       |
| modified_at       | dateTime |             | No       |
| user              | integer  |             | Yes      |
| restaurant        | integer  |             | Yes      |

#### User

| Name       | Type    | Description | Required |
| ---------- | ------- | ----------- | -------- |
| id         | integer |             | Yes      |
| name       | string  |             | Yes      |
| user_level | string  |             | Yes      |

#### District

| Name | Type    | Description | Required |
| ---- | ------- | ----------- | -------- |
| id   | integer |             | Yes      |
| name | string  |             | Yes      |

#### Category

| Name              | Type    | Description | Required |
| ----------------- | ------- | ----------- | -------- |
| id                | integer |             | Yes      |
| category_type_id  | integer |             | Yes      |
| category_type_key | string  |             | Yes      |
| name              | string  |             | Yes      |

#### RestaurantWithDistrictAndCategories

| Name       | Type                      | Description | Required |
| ---------- | ------------------------- | ----------- | -------- |
| id         | integer                   |             | Yes      |
| district   | [District](#District)     |             | No       |
| categories | [ [Category](#Category) ] |             | No       |
| name       | string                    |             | Yes      |
| address    | string                    |             | Yes      |
| image_url  | string (uri)              |             | Yes      |m