# REST API Test Cases: Product API

These test cases are written for Jira and assume a standard REST Product API. Update endpoint paths if the implemented API uses different URLs.

## Assumed Product API Contract

Base URL: `/api/products/`

Detail URL: `/api/products/{product_id}/`

Expected product fields:

- `id`
- `category`
- `name`
- `quantity`
- `unit`
- `image`

Allowed unit values:

- `kg`
- `g`
- `l`
- `ml`
- `pcs`

Authentication assumption:

- Read operations may be public or authenticated depending on project rules.
- Create, update, partial update, and delete operations should require an authenticated authorized user.

| Test ID | Preconditions | Test Steps | Expected Results | Priority |
|---|---|---|---|---|
| PROD-API-TC-001 | Product API is deployed. At least one product exists. | 1. Send `GET /api/products/`. | Response status is `200 OK`. Response returns a list of products. Each product includes expected fields: `id`, `category`, `name`, `quantity`, `unit`, and `image`. | High |
| PROD-API-TC-002 | Product API is deployed. No products exist in database. | 1. Send `GET /api/products/`. | Response status is `200 OK`. Response returns an empty list. API does not return server error. | Medium |
| PROD-API-TC-003 | Product API is deployed. Multiple products exist. | 1. Send `GET /api/products/`. | All available products are returned according to API pagination rules. Product data is accurate. | High |
| PROD-API-TC-004 | Product API is deployed. Product A exists. | 1. Send `GET /api/products/{product_a_id}/`. | Response status is `200 OK`. Response body contains Product A details. | High |
| PROD-API-TC-005 | Product API is deployed. Product ID does not exist. | 1. Send `GET /api/products/999999/`. | Response status is `404 Not Found`. Error response is clear and does not expose internal details. | High |
| PROD-API-TC-006 | Product API is deployed. Valid category exists. User is authenticated and authorized. | 1. Send `POST /api/products/` with valid `category`, `name`, `quantity`, and `unit`. | Response status is `201 Created`. Product is created in database. Response body contains the new product ID and submitted values. | High |
| PROD-API-TC-007 | Product API is deployed. Valid category exists. User is not authenticated. | 1. Send `POST /api/products/` with valid product payload. | Response status is `401 Unauthorized` or `403 Forbidden`. Product is not created. | High |
| PROD-API-TC-008 | Product API is deployed. User is authenticated but lacks required permission. | 1. Send `POST /api/products/` with valid product payload. | Response status is `403 Forbidden`. Product is not created. | High |
| PROD-API-TC-009 | Product API is deployed. User is authenticated and authorized. | 1. Send `POST /api/products/` without `name`. | Response status is `400 Bad Request`. Error response identifies `name` as required. Product is not created. | High |
| PROD-API-TC-010 | Product API is deployed. User is authenticated and authorized. | 1. Send `POST /api/products/` without `category`. | Response status is `400 Bad Request`. Error response identifies `category` as required. Product is not created. | High |
| PROD-API-TC-011 | Product API is deployed. User is authenticated and authorized. | 1. Send `POST /api/products/` without `quantity`. | Response status is `201 Created` if API uses model default `0`, or `400 Bad Request` if API requires quantity. Behavior matches API specification. | Medium |
| PROD-API-TC-012 | Product API is deployed. User is authenticated and authorized. | 1. Send `POST /api/products/` without `unit`. | Response status is `201 Created` if API uses model default `pcs`, or `400 Bad Request` if API requires unit. Behavior matches API specification. | Medium |
| PROD-API-TC-013 | Product API is deployed. User is authenticated and authorized. Existing Product A has name `Milk`. | 1. Send `POST /api/products/` with name `Milk`. | Response status is `400 Bad Request`. Duplicate product name is rejected. | High |
| PROD-API-TC-014 | Product API is deployed. User is authenticated and authorized. Existing Product A has name `Milk`. | 1. Send `POST /api/products/` with name `milk`. | Response status is `400 Bad Request` if case-insensitive uniqueness is enforced. Duplicate product name is rejected. | High |
| PROD-API-TC-015 | Product API is deployed. User is authenticated and authorized. Category ID does not exist. | 1. Send `POST /api/products/` with invalid `category` ID. | Response status is `400 Bad Request`. Error response identifies invalid category. Product is not created. | High |
| PROD-API-TC-016 | Product API is deployed. User is authenticated and authorized. Valid category exists. | 1. Send `POST /api/products/` with `quantity` set to `1.50`. | Response status is `201 Created`. Quantity is saved as `1.50` or equivalent decimal representation. | High |
| PROD-API-TC-017 | Product API is deployed. User is authenticated and authorized. Valid category exists. | 1. Send `POST /api/products/` with `quantity` set to `abc`. | Response status is `400 Bad Request`. Error response identifies invalid decimal value. Product is not created. | High |
| PROD-API-TC-018 | Product API is deployed. User is authenticated and authorized. Valid category exists. | 1. Send `POST /api/products/` with `quantity` exceeding model precision, such as `1234567.89`. | Response status is `400 Bad Request`. Error response identifies quantity precision or range issue. Product is not created. | Medium |
| PROD-API-TC-019 | Product API is deployed. User is authenticated and authorized. Valid category exists. | 1. Send `POST /api/products/` with `unit` set to `kg`. | Response status is `201 Created`. Product is created with unit `kg`. | Medium |
| PROD-API-TC-020 | Product API is deployed. User is authenticated and authorized. Valid category exists. | 1. Send `POST /api/products/` with `unit` set to `invalid_unit`. | Response status is `400 Bad Request`. Error response identifies invalid unit choice. Product is not created. | High |
| PROD-API-TC-021 | Product API is deployed. Product A exists. User is authenticated and authorized. Valid Category B exists. | 1. Send `PUT /api/products/{product_a_id}/` with a full valid payload changing name, category, quantity, and unit. | Response status is `200 OK`. Product A is fully updated in database. Response body reflects updated values. | High |
| PROD-API-TC-022 | Product API is deployed. Product A exists. User is not authenticated. | 1. Send `PUT /api/products/{product_a_id}/` with valid payload. | Response status is `401 Unauthorized` or `403 Forbidden`. Product A is not updated. | High |
| PROD-API-TC-023 | Product API is deployed. Product ID does not exist. User is authenticated and authorized. | 1. Send `PUT /api/products/999999/` with valid payload. | Response status is `404 Not Found`. No product is created or updated. | High |
| PROD-API-TC-024 | Product API is deployed. Product A exists. User is authenticated and authorized. | 1. Send `PUT /api/products/{product_a_id}/` with missing required `name`. | Response status is `400 Bad Request`. Product A remains unchanged. | High |
| PROD-API-TC-025 | Product API is deployed. Product A and Product B exist. User is authenticated and authorized. | 1. Send `PUT /api/products/{product_a_id}/` with Product B's existing name. | Response status is `400 Bad Request`. Duplicate name is rejected. Product A remains unchanged. | High |
| PROD-API-TC-026 | Product API is deployed. Product A exists. User is authenticated and authorized. | 1. Send `PATCH /api/products/{product_a_id}/` with only `name`. | Response status is `200 OK`. Only product name is updated. Other fields remain unchanged. | High |
| PROD-API-TC-027 | Product API is deployed. Product A exists. User is authenticated and authorized. | 1. Send `PATCH /api/products/{product_a_id}/` with only `quantity`. | Response status is `200 OK`. Only quantity is updated. Other fields remain unchanged. | High |
| PROD-API-TC-028 | Product API is deployed. Product A exists. User is authenticated and authorized. | 1. Send `PATCH /api/products/{product_a_id}/` with invalid `unit`. | Response status is `400 Bad Request`. Product A remains unchanged. | High |
| PROD-API-TC-029 | Product API is deployed. Product ID does not exist. User is authenticated and authorized. | 1. Send `PATCH /api/products/999999/` with valid payload. | Response status is `404 Not Found`. No product is updated. | Medium |
| PROD-API-TC-030 | Product API is deployed. Product A exists. User is authenticated and authorized. | 1. Send `DELETE /api/products/{product_a_id}/`. 2. Send `GET /api/products/{product_a_id}/`. | Delete response status is `204 No Content` or documented success status. Follow-up GET returns `404 Not Found`. | High |
| PROD-API-TC-031 | Product API is deployed. Product A exists. User is not authenticated. | 1. Send `DELETE /api/products/{product_a_id}/`. | Response status is `401 Unauthorized` or `403 Forbidden`. Product A is not deleted. | High |
| PROD-API-TC-032 | Product API is deployed. Product ID does not exist. User is authenticated and authorized. | 1. Send `DELETE /api/products/999999/`. | Response status is `404 Not Found`. | Medium |
| PROD-API-TC-033 | Product API is deployed. Product A exists with related cart items or prices. User is authenticated and authorized. | 1. Send `DELETE /api/products/{product_a_id}/`. | Product deletion follows expected cascade behavior. Related cart items and prices are removed if model cascade applies. API does not return server error. | High |
| PROD-API-TC-034 | Product API supports filtering by category. Products exist across multiple categories. | 1. Send `GET /api/products/?category={category_id}`. | Response status is `200 OK`. Only products from the requested category are returned. | Medium |
| PROD-API-TC-035 | Product API supports search by name. Product `Milk` exists. | 1. Send `GET /api/products/?search=milk`. | Response status is `200 OK`. Matching products are returned according to search rules. | Medium |
| PROD-API-TC-036 | Product API supports ordering. Multiple products exist. | 1. Send `GET /api/products/?ordering=name`. | Response status is `200 OK`. Products are sorted by name ascending. | Low |
| PROD-API-TC-037 | Product API supports pagination. More products exist than page size. | 1. Send `GET /api/products/?page=1`. 2. Send `GET /api/products/?page=2`. | Response status is `200 OK` for valid pages. Page metadata and product results match pagination rules. | Medium |
| PROD-API-TC-038 | Product API supports pagination. Invalid page number is requested. | 1. Send `GET /api/products/?page=999999`. | Response status is `404 Not Found` or documented pagination error. API does not return server error. | Low |
| PROD-API-TC-039 | Product API is deployed. | 1. Send `POST /api/products/` with malformed JSON body. | Response status is `400 Bad Request`. Error response explains request body could not be parsed. | High |
| PROD-API-TC-040 | Product API is deployed. | 1. Send `POST /api/products/` with `Content-Type: text/plain` and a valid-looking JSON string. | Response status is `415 Unsupported Media Type` or `400 Bad Request`, depending on API configuration. Product is not created. | Medium |
| PROD-API-TC-041 | Product API is deployed. User is authenticated and authorized. Valid category exists. | 1. Send `POST /api/products/` with extra unknown field `unexpected_field`. | API either ignores the unknown field or returns `400 Bad Request`, according to API specification. Product data is not polluted with unknown fields. | Medium |
| PROD-API-TC-042 | Product API is deployed. Product A exists. | 1. Send `GET /api/products/{product_a_id}/`. 2. Verify response headers. | Response includes expected content type, such as `application/json`. | Low |
| PROD-API-TC-043 | Product API is deployed. User is authenticated and authorized. Valid category exists. | 1. Send `POST /api/products/` with leading/trailing spaces in `name`, such as `  Apples  `. | Product name is trimmed if trimming is part of API rules, or saved exactly if documented. Duplicate validation remains consistent. | Medium |
| PROD-API-TC-044 | Product API is deployed. User is authenticated and authorized. Valid category exists. | 1. Send `POST /api/products/` with an empty string for `name`. | Response status is `400 Bad Request`. Error response identifies name as invalid or required. Product is not created. | High |
| PROD-API-TC-045 | Product API supports image upload. User is authenticated and authorized. Valid category exists. | 1. Send multipart `POST /api/products/` with valid image file. | Response status is `201 Created`. Product is created and image path or URL is returned. Uploaded file is stored correctly. | Medium |
| PROD-API-TC-046 | Product API supports image upload. User is authenticated and authorized. Valid category exists. | 1. Send multipart `POST /api/products/` with invalid image file type. | Response status is `400 Bad Request`. Product is not created with invalid image. | Medium |
| PROD-API-TC-047 | Product API is deployed. Product A exists. | 1. Send unsupported method `OPTIONS /api/products/{product_a_id}/` or verify allowed methods using API metadata. | API returns allowed methods according to framework behavior. Unsupported methods are not allowed. | Low |
| PROD-API-TC-048 | Product API is deployed. Product A exists. | 1. Send `POST /api/products/{product_a_id}/` to detail endpoint if not supported. | Response status is `405 Method Not Allowed`. Product remains unchanged. | Medium |
| PROD-API-TC-049 | Product API is deployed. User is authenticated and authorized. Valid category exists. | 1. Send `POST /api/products/` with SQL/script-like text in name, such as `<script>alert(1)</script>`. | API stores or rejects input according to validation rules without executing it. JSON response is safely encoded. No server error occurs. | High |
| PROD-API-TC-050 | Product API is deployed. Product A exists. | 1. Send repeated `GET /api/products/{product_a_id}/` requests. | API consistently returns the same product data unless the product is changed. No intermittent server errors occur. | Low |

