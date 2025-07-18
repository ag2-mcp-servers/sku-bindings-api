# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T12:04:38+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity
from fastapi import Header, Path, Query

from models import (
    CatalogPvtSkusellersSkuIdGetResponse,
    SkuBindingPvtSkusellerAdminGetResponse,
    SkuBindingPvtSkusellerInsertionPostRequest,
    SkuBindingPvtSkusellerListBysellerIdSellerIdGetResponse,
    SkuBindingPvtSkusellerPagedSelleridSellerIdGetResponse,
    SkuBindingPvtSkusellerSellerIdSellerSkuIdGetResponse,
    SkuBindingPvtSkusellerSellerIdSellerSkuIdPutRequest,
)

app = MCPProxy(
    contact={},
    title='SKU Bindings API',
    version='1.0',
    servers=[
        {'url': 'https://vtex.local'},
        {
            'description': 'VTEX server URL.',
            'url': 'https://{accountName}.{environment}.com.br/api',
            'variables': {
                'accountName': {
                    'default': '{accountName}',
                    'description': 'Name of the VTEX account. Used as part of the URL.',
                },
                'environment': {
                    'default': '{environment}',
                    'description': 'Environment to use. Used as part of the URL.',
                },
            },
        },
    ],
)


@app.get(
    '/catalog/pvt/skusellers/{skuId}',
    description=""" Retrieves SKU Bindings details by SKU ID.

## Response body example

```json
[
    {
        "Id": 48,
        "SellerId": "cosmetics1",
        "StockKeepingUnitId": 1,
        "SellerSkuId": "42",
        "IsActive": true,
        "LastUpdateDate": "2020-10-21T19:13:00.657",
        "SalesPolicy": 0
    }
]
``` """,
    tags=['sku_information_retrieval', 'sku_binding_management'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def getby_sku_id(
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    sku_id: str = Path(..., alias='skuId'),
):
    """
    Get SKU Bindings by SKU ID
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/sku-binding/pvt/skuseller/activate/{sellerId}/{skuSellerId}',
    description=""" Changes the status of an SKU Binding to active, setting `isActive` to `true`.

 > ℹ This path is an updated version of `/api/catalog_system/pvt/skuseller/activate/{sellerId}/{skuSellerId}`. """,
    tags=['sku_binding_management'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def activate_s_k_u_binding(
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    seller_id: str = Path(..., alias='sellerId'),
    sku_seller_id: str = Path(..., alias='skuSellerId'),
):
    """
    Activate SKU Binding
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/sku-binding/pvt/skuseller/admin',
    description=""" Retrieves SKU Bindings administrative information using optional query params `sellerId`, `skuId`, `sellerSkuId` and `IsActive` to filter results and `size` to restrict the amount of results. 

 > ℹ This path is an updated version of `/api/catalog_system/pvt/skuseller/admin`.

## Response body example

```json
[
    {
        "IsPersisted": true,
        "IsRemoved": false,
        "SkuSellerId": 1,
        "UpdateDate": "2019-12-04T01:56:00.673Z",
        "RequestedUpdateDate": null,
        "SellerStockKeepingUnitId": "12",
        "SellerId": "cosmetics1",
        "StockKeepingUnitId": 25,
        "IsActive": true
    }
]
``` """,
    tags=['sku_information_retrieval', 'sku_binding_management'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def getpagedadmin(
    seller_id: Optional[str] = Query(None, alias='sellerId'),
    sku_id: Optional[str] = Query(None, alias='skuId'),
    seller_sku_id: Optional[str] = Query(None, alias='sellerSkuId'),
    is_active: Optional[bool] = Query(None, alias='isActive'),
    size: Optional[str] = None,
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
):
    """
    Get SKU Bindings information
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/sku-binding/pvt/skuseller/changenotification/{sellerId}/{sellerSkuId}',
    description=""" The seller is responsible for suggesting new SKUs to be sold in the VTEX marketplace and also for informing the marketplace about changes in their SKUs that already exist in the marketplace. Both actions start with a catalog notification, which is made by this request.

With this notification, the seller is telling the marketplace that something has changed about a specific SKU, like price or inventory, or that this is a new SKU that the seller would like to offer to the marketplace.

There are two information expected by the marketplace in this request: the `sellerId`, which identifies the seller, and the `sellerSkuId`, which identifies the binding of the seller with the SKU.

Both information are passed through the request URL. The body of the request should be empty.
 > ℹ This path is an updated version of `/api/catalog_system/pvt/skuseller/changenotification/{sellerId}/{sellerSkuId}`.

## Example

Let's say your seller has the ID `123` in the marketplace and you want to inform the marketplace that has been a change in the SKU with ID `700`.

In this case, you would have to replace the `sellerId` parameter with the value `123` and the `skuId` parameter with the value `700`. The URL of the request would be the following.

```
https://{{accountName}}.vtexcommercestable.com.br/api/sku-binding/pvt/skuseller/changenotification/123/700
```

## Response codes

The following response codes are possible for this request.
* 200: the SKU whose ID was informed in the URL already exists in the marketplace and was found. The marketplace can now proceed with a fulfillment simulation in order to get updated information about this SKU's inventory and price.
* 403: Failure in the authentication.
* 404: the SKU was not found in the marketplace. The body of the response, in this case, should follow this format: "Seller StockKeepingUnit `{{skuId}}` not found for this seller id `{{sellerId}}`. This means that the seller can now proceed with sending an offer to the marketplace in order to suggest that this SKU is sold there.
* 429: Failure due to too many requests. """,
    tags=['sku_notification_management', 'sku_binding_management'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def change_notification_seller_sku(
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    seller_id: str = Path(..., alias='sellerId'),
    seller_sku_id: str = Path(..., alias='sellerSkuId'),
):
    """
    Change Notification with Seller ID and Seller SKU ID
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/sku-binding/pvt/skuseller/changenotification/{skuId}',
    description=""" The seller is responsible for suggesting new SKUs to be sold in the VTEX marketplace and also for informing the marketplace about changes in their SKUs that already exist in the marketplace. Both actions start with a catalog notification, which is made by this request.

With this notification, the seller is telling the marketplace that something has changed about a specific SKU, like price or inventory, or that this is a new SKU that the seller would like to offer to the marketplace.

The body of the request should be empty.

 > ℹ This path is an updated version of `/api/catalog_system/pvt/skuseller/changenotification/{skuId}`. """,
    tags=['sku_notification_management'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def change_notification(
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    sku_id: str = Path(..., alias='skuId'),
):
    """
    Change Notification with SKU ID
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/sku-binding/pvt/skuseller/inactivate/{sellerId}/{skuSellerId}',
    description=""" Changes the status of an SKU Binding to inactive, setting `isActive` to `false`.

  > ℹ This path is an updated version of `/api/catalog_system/pvt/skuseller/inactivate/{sellerId}/{skuSellerId}`. """,
    tags=['sku_binding_management', 'sku_binding_association'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def deactivate_s_k_u_binding(
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    seller_id: str = Path(..., alias='sellerId'),
    sku_seller_id: str = Path(..., alias='skuSellerId'),
):
    """
    Deactivate SKU Binding
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/sku-binding/pvt/skuseller/insertion',
    description=""" Creates an SKU Binding, associating a seller's SKU with a marketplace's SKU.

 > ℹ This path is an updated version of `/api/catalog_system/pvt/skuseller/insertion`. """,
    tags=['sku_binding_management'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def insert_s_k_u_binding(
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    body: SkuBindingPvtSkusellerInsertionPostRequest = ...,
):
    """
    Insert SKU Binding
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/sku-binding/pvt/skuseller/list/bysellerId/{sellerId}',
    description=""" Retrieves a list of SKU Bindings given a specific Seller ID. 

 > ℹ This path is an updated version of `/api/catalog_system/pvt/skuseller/list/bysellerId/{sellerId}`.

## Response body example

```json
[
    {
        "SellerStockKeepingUnitId": "24",
        "FreightCommissionPercentage": null,
        "ProductCommissionPercentage": null,
        "SellerId": "vtxkfj7352",
        "StockKeepingUnitId": 121,
        "IsActive": true
    }
]
``` """,
    tags=['sku_information_retrieval', 'sku_binding_management'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def getallby_seller_id(
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    seller_id: str = Path(..., alias='sellerId'),
):
    """
    Get all SKU Bindings by Seller ID
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/sku-binding/pvt/skuseller/paged/sellerid/{sellerId}',
    description=""" Retrieves a paged list of SKU Bindings given a specific Seller ID. 

 > ℹ This path is an updated version of `/api/catalog_system/pvt/skuseller/paged/sellerid/{sellerId}`.

## Response body example

```json
[
    {
        "SellerId": "vtxkfj7352",
        "StockKeepingUnitId": 121,
        "SellerStockKeepingUnitId": "24",
        "IsActive": true,
        "FreightCommissionPercentage": null,
        "ProductCommissionPercentage": null
    },
    {
        "SellerId": "vtxkfj7352",
        "StockKeepingUnitId": 14,
        "SellerStockKeepingUnitId": "60",
        "IsActive": true,
        "FreightCommissionPercentage": null,
        "ProductCommissionPercentage": null
    }
]
``` """,
    tags=['sku_information_retrieval', 'sku_binding_management'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def getpagedby_seller_id(
    page: str,
    size: str = ...,
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    seller_id: str = Path(..., alias='sellerId'),
):
    """
    Get paged SKU Bindings by Seller ID
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/sku-binding/pvt/skuseller/remove/{sellerId}/{sellerSkuId}',
    description=""" Remove a seller's SKU binding, given the Seller ID and the SKU ID in the seller's store.

  > ℹ This path is an updated version of `/api/catalog_system/pvt/skuseller/remove/{sellerId}/{sellerSkuId}`. """,
    tags=['sku_binding_management', 'sku_binding_association'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def delete_s_k_usellerassociation(
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    seller_id: str = Path(..., alias='sellerId'),
    seller_sku_id: str = Path(..., alias='sellerSkuId'),
):
    """
    Remove a seller's SKU Binding
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/sku-binding/pvt/skuseller/{sellerId}/{sellerSkuId}',
    description=""" Retrieves the details of a seller's SKU given a seller ID and the SKU ID in the seller's store. 

 > ℹ This path is an updated version of `/api/catalog_system/pvt/skuseller/{sellerId}/{sellerSkuId}`.

## Response body example

```json
{
    "IsPersisted": true,
    "IsRemoved": false,
    "SkuSellerId": 102,
    "UpdateDate": "2021-04-12T20:06:59.413Z",
    "RequestedUpdateDate": null,
    "SellerStockKeepingUnitId": "71",
    "SellerId": "vtxkfj7352",
    "StockKeepingUnitId": 1,
    "IsActive": true
}
``` """,
    tags=['sku_information_retrieval'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def get_s_k_useller(
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    seller_id: str = Path(..., alias='sellerId'),
    seller_sku_id: str = Path(..., alias='sellerSkuId'),
):
    """
    Get details of a seller's SKU
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/sku-binding/pvt/skuseller/{sellerId}/{sellerSkuId}',
    description=""" Associates a seller's SKU to another marketplace SKU.

 > ℹ This path is an updated version of `/api/catalog_system/pvt/skuseller/{sellerId}/{sellerSkuId}`.

## Request body example

```json
{
    "StockKeepingUnitId": 1
}
``` """,
    tags=['sku_binding_management', 'sku_binding_association'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def bindtoanothersku(
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    seller_id: str = Path(..., alias='sellerId'),
    seller_sku_id: str = Path(..., alias='sellerSkuId'),
    body: SkuBindingPvtSkusellerSellerIdSellerSkuIdPutRequest = None,
):
    """
    Bind a seller's SKU to another SKU
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
