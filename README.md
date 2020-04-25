# Newdex Python API
Python 3 client for Newdex V1 REST API.


## Overview

Newdex api_key needs to be binded with EOS account. [Apply for Newdex Market API_KEY](https://api.newdex.io/signup)  


## REST Market and Trade API


### get_pairs()
Get the list of all exchange pairs.  

Name | Data type | Description
------------ | ------------ | ------------
id | int | Exchange pair id
symbol | string | Exchange pair name, such as: eosblackteam-black-eos
contract | string | Contract name, such as: eosblackteam
currency | string | Currency name, such as: BLACK
price_precision | int | The price precision on Newdex
currency_precision | int | The currency precision  

### get_ticker()  
Get the market of a particular exchange pair.

Name | Data type | Description
------------ | ------------ | ------------
symbol | string | Exchange pair name
last | double | Latest price
change | double | Price change (price change from 08:00 (GMT) to present time)
high | double | Highest price in 24 hours
low | double | Lowest price in 24 hours
amount | double | 24-hour trading volume
volume | double | 24-hour trading amount (converted to accounted currency, such as EOS, USDT

### get_tickers

Get the market of all exchange pairs.  

Name | Data type | Description
------------ | ------------ | ------------
symbol | string | Exchange pair name
last | double | Latest price
change | double | Price change (price change from 08:00 (GMT) to present time)
high | double | Highest price in 24 hours
low | double | Lowest price in 24 hours
amount | double | 24-hour trading volume
volume | double | 24-hour trading amount (converted to accounted currency, such as EOS, USDT


### get_price()

Get the price of an exchange pair.

Name | Data type | Description
------------ | ------------ | ------------
symbol | string | Exchange pair name
price | double | Latest price

### GET get_depth()

Get order book (quoted depth)

Name | Data type | Description
------------ | ------------ | ------------
asks | array | Ask orders depth
bids | array | Bid orders depth

Data example:
```
/* GET /v1/depth?symbol=eosblackteam-black-eos */
{
  "code":200,
  "data":{
      "bids":[
       [0.035,1299.1857],
       [0.03493,11400],
       [0.0344,1612.4186],
       [0.0335,24299.6626],
       [0.0315,95103.6126],
       [0.03046,6744.3959],
       [0.03002,316.439],
       [0.03,3333.3333],
       [0.02961,31.9587],
       [0.02926,17.7101]
     ],
     "asks":[
       [0.068,549.1971],
       [0.067,18106.8275],
       [0.06666,3000],
       [0.066,15373.3999],
       [0.06539,20.6],
       [0.065,9347.6336],
       [0.064,6767.0784],
       [0.06398,676.949],
       [0.063,6265.8133],
       [0.062,92.3191]
     ]
   }
 }
```

### get_trades() 
Get deals record of exchange pair 

Name | Data type | Description
------------ | ------------ | ------------
id | array | Trade ID
price | double | Dealt price 
amount | double | Dealt volume 
volume | double | Dealt amount (converted to accounted currency, such as EOS, USDT)
time | int | 10-digit timestamp 

### get_candles()

Get K-Line data of exchange pair

Request:  

Name | Data type | Description
------------ | ------------ | ------------
symbol | string | Exchange pair name
time_frame | string | (optional) time interval, defaulted 1 hour, options: 1 min, 5 mins, 30 mins, 1 hour, 4 hours, 6 hours, 1 day, 1 week, 1 month, 1 year.
size | int |  (optional) quantity, defaulted 100, 2000 maximum


Response Object[]  

Name | Data type | Description
------------ | ------------ | ------------
0 | int | K-Line ID
1 | double | Opening price
2 | double | Closing price
3 | double | Highest price in 24 hours
4 | double | Lowest price in 24 hours
5 | double | Trading volume
6 | double | Trading amount (converted to accounted currency, such as EOS, USDT)

Data example: 

```
/* GET /v1/candles?symbol=eosblackteam-black-eos&time_frame=1hour&size=10 */
{
  "code":200,
  "data":[
    [1544140800,0.04075,0.046,0.046,0.04075,100882.9715,4518.451],
    [1544144400,0.046,0.043,0.046,0.04271,8857.6799,381.6711],
    [1544148000,0.043,0.04441,0.046,0.043,63614.3411,2811.6175],
    [1544151600,0.04441,0.04444,0.046,0.04354,5183.5131,234.7778],
    [1544155200,0.04444,0.04257,0.04444,0.04255,12290.0635,528.4927],
    [1544158800,0.04257,0.04599,0.04599,0.04257,1160.6585,53.2085],
    [1544162400,0.04599,0.04531,0.0469,0.04416,129433.0583,5809.5475],
    [1544166000,0.04531,0.0445,0.0469,0.0445,14117.186,631.1711],
    [1544169600,0.0445,0.0456,0.04684,0.0445,469.2888,21.2106],
    [1544173200,0.0456,0.04777,0.04777,0.0456,4895.7245,231.3036]
  ]
}
```

### open_orders()
### filled_orders()
### canceled_orders()
### order_history()

Response Object[]  

Name | Data type | Description
------------ | ------------ | ------------
id | int | Order ID
pair_id | int | Exchange pair id
trx_id | string | Trx ID on chain
side | string | Trade direction: sell, buy
type | string | Trade type: sell-limit, sell-market, buy-limit, buy-market
price | double | Order price
amount | double | Order amount
deal_price | double | Dealt price (average)
deal_amount | double | Dealt amount
deal_volume | double | Dealt volume
state | double | Status: new, partially-filled, filled, canceled, partial-canceled 
created_at | int | Create time, 10-digit timestamp
updated_at | int | Update time, 10-digit timestamp


### cancel_order()

Cancel order based on trx_id.

Request:  

Name | Data type | Description
------------ | ------------ | ------------
trx_id | string | Trx ID on chain

Response: String, If succeeded, response "Order successfully canceled"

**Note: this interface only supports old orders (account: newdexpocket), and the orders which created by contract (account: newdexpublic) can only be cancelled by contract action.**


)

## Error Codes
Code = 200, it means request succeeded, other situations mean error. See error code reference form below:

| Error Code | Explanation |
| ------ | -------- |
| -1001 | The request is beyond limit, if you don’t have API_KEY, please [apply for API_KEY](/api-for-cn/signup_app_key.md) as soon as possible. |
| -1002 | Invalid API_KEY  |
| -1003 | Invalid signature , pleas refer to [signature verification](/api-for-cn/REST_authentication.md) |
| -1004 | Request timestamp has expired |
| -1005 | No permission, request trade and order API need to verify API_KEY |
| -1101 | Invalid account |
| -1102 | Invalid email |
| -1103 | Invalid symbol |
| -1104 | Invalid trx_id |
| -1105 | Order has been canceled |
| -1106 | Order is dealt, cannot be cancel |
| -1500 | Unknown error |