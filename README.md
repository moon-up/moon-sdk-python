# moon-sdk
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.4.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import moonsdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import moonsdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import moonsdk
from moonsdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.usemoon.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = moonsdk.Configuration(
    host = "https://beta.usemoon.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'


# Enter a context with an instance of the API client
async with moonsdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moonsdk.AaveApi(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    aave_input = moonsdk.AaveInput() # AaveInput | 

    try:
        api_response = await api_instance.borrow(authorization, name, aave_input)
        print("The response of AaveApi->borrow:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AaveApi->borrow: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://beta.usemoon.ai*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AaveApi* | [**borrow**](docs/AaveApi.md#borrow) | **POST** /aave/{name}/borrow | 
*AaveApi* | [**lend**](docs/AaveApi.md#lend) | **POST** /aave/{name}/lend | 
*AaveApi* | [**repay**](docs/AaveApi.md#repay) | **POST** /aave/{name}/repay | 
*AaveApi* | [**user_reserve_data**](docs/AaveApi.md#user_reserve_data) | **POST** /aave/{name}/user-reserve-data | 
*AccountsApi* | [**broadcast_tx**](docs/AccountsApi.md#broadcast_tx) | **POST** /accounts/{accountName}/broadcast-tx | 
*AccountsApi* | [**create_account**](docs/AccountsApi.md#create_account) | **POST** /accounts | 
*AccountsApi* | [**delete_account**](docs/AccountsApi.md#delete_account) | **DELETE** /accounts/{accountName} | 
*AccountsApi* | [**deploy_contract**](docs/AccountsApi.md#deploy_contract) | **POST** /accounts/{accountName}/deploy | 
*AccountsApi* | [**get_account**](docs/AccountsApi.md#get_account) | **GET** /accounts/{accountName} | 
*AccountsApi* | [**get_balance**](docs/AccountsApi.md#get_balance) | **GET** /accounts/{accountName}/balance | 
*AccountsApi* | [**get_nonce**](docs/AccountsApi.md#get_nonce) | **GET** /accounts/{accountName}/nonce | 
*AccountsApi* | [**list_accounts**](docs/AccountsApi.md#list_accounts) | **GET** /accounts | 
*AccountsApi* | [**sign_message**](docs/AccountsApi.md#sign_message) | **POST** /accounts/{accountName}/sign-message | 
*AccountsApi* | [**sign_transaction**](docs/AccountsApi.md#sign_transaction) | **POST** /accounts/{accountName}/sign-transaction | 
*AccountsApi* | [**sign_typed_data**](docs/AccountsApi.md#sign_typed_data) | **POST** /accounts/{accountName}/sign-typed-data | 
*AccountsApi* | [**transfer_eth**](docs/AccountsApi.md#transfer_eth) | **POST** /accounts/{accountName}/transfer-eth | 
*BitcoinApi* | [**create_bitcoin_account**](docs/BitcoinApi.md#create_bitcoin_account) | **POST** /bitcoin | 
*BitcoinApi* | [**get_bitcoin_account**](docs/BitcoinApi.md#get_bitcoin_account) | **GET** /bitcoin/{accountName} | 
*BitcoinApi* | [**list_bitcoin_accounts**](docs/BitcoinApi.md#list_bitcoin_accounts) | **GET** /bitcoin | 
*BitcoinApi* | [**sign_bitcoin_transaction**](docs/BitcoinApi.md#sign_bitcoin_transaction) | **POST** /bitcoin/{accountName}/sign-tx | 
*ConveyorFinanceApi* | [**swap**](docs/ConveyorFinanceApi.md#swap) | **POST** /conveyorfinance/{name}/swap | 
*CosmosApi* | [**create_cosmos_account**](docs/CosmosApi.md#create_cosmos_account) | **POST** /cosmos | 
*CosmosApi* | [**get_cosmos_account**](docs/CosmosApi.md#get_cosmos_account) | **GET** /cosmos/{accountName} | 
*CosmosApi* | [**list_cosmos_accounts**](docs/CosmosApi.md#list_cosmos_accounts) | **GET** /cosmos | 
*CosmosApi* | [**sign_cosmos_transaction**](docs/CosmosApi.md#sign_cosmos_transaction) | **POST** /cosmos/{accountName}/sign-tx | 
*DogeCoinApi* | [**create_doge_coin_account**](docs/DogeCoinApi.md#create_doge_coin_account) | **POST** /dogecoin | 
*DogeCoinApi* | [**get_doge_coin_account**](docs/DogeCoinApi.md#get_doge_coin_account) | **GET** /dogecoin/{accountName} | 
*DogeCoinApi* | [**list_doge_coin_accounts**](docs/DogeCoinApi.md#list_doge_coin_accounts) | **GET** /dogecoin | 
*DogeCoinApi* | [**sign_doge_coin_transaction**](docs/DogeCoinApi.md#sign_doge_coin_transaction) | **POST** /dogecoin/{accountName}/sign-tx | 
*ENSApi* | [**resolve**](docs/ENSApi.md#resolve) | **POST** /ens/resolve | 
*ERC1155Api* | [**balance_of**](docs/ERC1155Api.md#balance_of) | **POST** /erc1155/{name}/balance-of | 
*ERC1155Api* | [**balance_of_batch**](docs/ERC1155Api.md#balance_of_batch) | **POST** /erc1155/{name}/balance-of-batch | 
*ERC1155Api* | [**is_approved_for_all**](docs/ERC1155Api.md#is_approved_for_all) | **POST** /erc1155/{name}/is-approved-for-all | 
*ERC1155Api* | [**safe_batch_transfer_from**](docs/ERC1155Api.md#safe_batch_transfer_from) | **POST** /erc1155/{name}/safe-batch-transfer-from | 
*ERC1155Api* | [**safe_transfer_from**](docs/ERC1155Api.md#safe_transfer_from) | **POST** /erc1155/{name}/safe-transfer-from | 
*ERC1155Api* | [**set_approval_for_all**](docs/ERC1155Api.md#set_approval_for_all) | **POST** /erc1155/{name}/set-approval-for-all | 
*Erc20Api* | [**allowance_erc20**](docs/Erc20Api.md#allowance_erc20) | **POST** /erc20/{name}/allowance | 
*Erc20Api* | [**approve_erc20**](docs/Erc20Api.md#approve_erc20) | **POST** /erc20/{name}/approve | 
*Erc20Api* | [**balance_of_erc20**](docs/Erc20Api.md#balance_of_erc20) | **POST** /erc20/{name}/balance-of | 
*Erc20Api* | [**decimals_erc20**](docs/Erc20Api.md#decimals_erc20) | **POST** /erc20/{name}/decimals | 
*Erc20Api* | [**name_erc20**](docs/Erc20Api.md#name_erc20) | **POST** /erc20/{name}/name | 
*Erc20Api* | [**symbol_erc20**](docs/Erc20Api.md#symbol_erc20) | **POST** /erc20/{name}/symbol | 
*Erc20Api* | [**total_supply_erc20**](docs/Erc20Api.md#total_supply_erc20) | **POST** /erc20/{name}/total-supply | 
*Erc20Api* | [**transfer_erc20**](docs/Erc20Api.md#transfer_erc20) | **POST** /erc20/{name}/transfer | 
*Erc20Api* | [**transfer_from_erc20**](docs/Erc20Api.md#transfer_from_erc20) | **POST** /erc20/{name}/transfer-from | 
*Erc721Api* | [**approve**](docs/Erc721Api.md#approve) | **POST** /erc721/{name}/approve | 
*Erc721Api* | [**balance_of**](docs/Erc721Api.md#balance_of) | **POST** /erc721/{name}/balance-of | 
*Erc721Api* | [**get_approved**](docs/Erc721Api.md#get_approved) | **POST** /erc721/{name}/get-approved | 
*Erc721Api* | [**is_approved_for_all**](docs/Erc721Api.md#is_approved_for_all) | **POST** /erc721/{name}/is-approved-for-all | 
*Erc721Api* | [**name**](docs/Erc721Api.md#name) | **POST** /erc721/{name}/name | 
*Erc721Api* | [**owner_of**](docs/Erc721Api.md#owner_of) | **POST** /erc721/{name}/owner-of | 
*Erc721Api* | [**safe_transfer_from**](docs/Erc721Api.md#safe_transfer_from) | **POST** /erc721/{name}/safe-transfer-from | 
*Erc721Api* | [**set_approval_for_all**](docs/Erc721Api.md#set_approval_for_all) | **POST** /erc721/{name}/set-approval-for-all | 
*Erc721Api* | [**symbol**](docs/Erc721Api.md#symbol) | **POST** /erc721/{name}/symbol | 
*Erc721Api* | [**token_uri**](docs/Erc721Api.md#token_uri) | **POST** /erc721/{name}/token-uri | 
*Erc721Api* | [**transfer**](docs/Erc721Api.md#transfer) | **POST** /erc721/{name}/transfer | 
*Erc721Api* | [**transfer_from**](docs/Erc721Api.md#transfer_from) | **POST** /erc721/{name}/transfer-from | 
*LitecoinApi* | [**create_litecoin_account**](docs/LitecoinApi.md#create_litecoin_account) | **POST** /litecoin | 
*LitecoinApi* | [**get_litecoin_account**](docs/LitecoinApi.md#get_litecoin_account) | **GET** /litecoin/{accountName} | 
*LitecoinApi* | [**list_litecoin_accounts**](docs/LitecoinApi.md#list_litecoin_accounts) | **GET** /litecoin | 
*LitecoinApi* | [**sign_litecoin_transaction**](docs/LitecoinApi.md#sign_litecoin_transaction) | **POST** /litecoin/{accountName}/sign-tx | 
*SolanaApi* | [**create_solana_account**](docs/SolanaApi.md#create_solana_account) | **POST** /solana | 
*SolanaApi* | [**get_solana_account**](docs/SolanaApi.md#get_solana_account) | **GET** /solana/{accountName} | 
*SolanaApi* | [**list_solana_accounts**](docs/SolanaApi.md#list_solana_accounts) | **GET** /solana | 
*SolanaApi* | [**sign_solana_transaction**](docs/SolanaApi.md#sign_solana_transaction) | **POST** /solana/{accountName}/sign-tx | 
*TronApi* | [**create_tron_account**](docs/TronApi.md#create_tron_account) | **POST** /tron | 
*TronApi* | [**get_tron_account**](docs/TronApi.md#get_tron_account) | **GET** /tron/{accountName} | 
*TronApi* | [**list_tron_accounts**](docs/TronApi.md#list_tron_accounts) | **GET** /tron | 
*TronApi* | [**sign_tron_transaction**](docs/TronApi.md#sign_tron_transaction) | **POST** /tron/{accountName}/sign-tx | 
*UniSwapApi* | [**add_liquidity**](docs/UniSwapApi.md#add_liquidity) | **POST** /uniswap/{name}/add-liquidity | 
*UniSwapApi* | [**remove_liquidity**](docs/UniSwapApi.md#remove_liquidity) | **POST** /uniswap/{name}/remove-liquidity | 
*UniSwapApi* | [**swap_exact_eth_for_tokens**](docs/UniSwapApi.md#swap_exact_eth_for_tokens) | **POST** /uniswap/{name}/swap-exact-eth-for-tokens | 
*UniSwapApi* | [**swap_exact_tokens_for_tokens**](docs/UniSwapApi.md#swap_exact_tokens_for_tokens) | **POST** /uniswap/{name}/swap-exact-tokens-for-tokens | 
*BitcoincashApi* | [**create_bitcoin_cash_account**](docs/BitcoincashApi.md#create_bitcoin_cash_account) | **POST** /bitcoincash | 
*BitcoincashApi* | [**get_bitcoin_cash_account**](docs/BitcoincashApi.md#get_bitcoin_cash_account) | **GET** /bitcoincash/{accountName} | 
*BitcoincashApi* | [**list_bitcoin_cash_accounts**](docs/BitcoincashApi.md#list_bitcoin_cash_accounts) | **GET** /bitcoincash | 
*BitcoincashApi* | [**sign_bitcoin_cash_transaction**](docs/BitcoincashApi.md#sign_bitcoin_cash_transaction) | **POST** /bitcoincash/{accountName}/sign-tx | 
*DefaultApi* | [**get_message**](docs/DefaultApi.md#get_message) | **GET** /ping | 
*EosApi* | [**create_eos_account**](docs/EosApi.md#create_eos_account) | **POST** /eos | 
*EosApi* | [**get_eos_account**](docs/EosApi.md#get_eos_account) | **GET** /eos/{accountName} | 
*EosApi* | [**list_eos_accounts**](docs/EosApi.md#list_eos_accounts) | **GET** /eos | 
*EosApi* | [**sign_eos_transaction**](docs/EosApi.md#sign_eos_transaction) | **POST** /eos/{accountName}/sign-tx | 
*OneinchApi* | [**approve_call_data**](docs/OneinchApi.md#approve_call_data) | **POST** /oneinch/approve-call-data | 
*OneinchApi* | [**approve_spender**](docs/OneinchApi.md#approve_spender) | **POST** /oneinch/approve-spender | 
*OneinchApi* | [**protocols**](docs/OneinchApi.md#protocols) | **POST** /oneinch/protocols | 
*OneinchApi* | [**quote**](docs/OneinchApi.md#quote) | **POST** /oneinch/quote | 
*OneinchApi* | [**swap**](docs/OneinchApi.md#swap) | **POST** /oneinch/{accountName}/swap | 
*OneinchApi* | [**tokens**](docs/OneinchApi.md#tokens) | **POST** /oneinch/tokens | 
*OnramperApi* | [**on_ramper_checkout**](docs/OnramperApi.md#on_ramper_checkout) | **POST** /onramper/fund/${accountName} | 
*OnramperApi* | [**on_ramper_get_quotes_buy**](docs/OnramperApi.md#on_ramper_get_quotes_buy) | **GET** /onramper/quotes/buy | 
*OnramperApi* | [**on_ramper_get_quotes_sell**](docs/OnramperApi.md#on_ramper_get_quotes_sell) | **GET** /onramper/quotes/sell | 
*OnramperApi* | [**on_ramper_get_supported_assets**](docs/OnramperApi.md#on_ramper_get_supported_assets) | **GET** /onramper/assets | 
*OnramperApi* | [**on_ramper_get_supported_currencies**](docs/OnramperApi.md#on_ramper_get_supported_currencies) | **GET** /onramper/currencies | 
*OnramperApi* | [**on_ramper_get_supported_defaults_all**](docs/OnramperApi.md#on_ramper_get_supported_defaults_all) | **GET** /onramper/defaults | 
*OnramperApi* | [**on_ramper_get_supported_on_ramps_all**](docs/OnramperApi.md#on_ramper_get_supported_on_ramps_all) | **GET** /onramper/onramps | 
*OnramperApi* | [**on_ramper_get_supported_payment_types**](docs/OnramperApi.md#on_ramper_get_supported_payment_types) | **GET** /onramper/payment-types | 
*OnramperApi* | [**on_ramper_get_supported_payment_types_fiat**](docs/OnramperApi.md#on_ramper_get_supported_payment_types_fiat) | **GET** /onramper/payment-types/fiat | 
*RippleApi* | [**create_ripple_account**](docs/RippleApi.md#create_ripple_account) | **POST** /ripple | 
*RippleApi* | [**get_ripple_account**](docs/RippleApi.md#get_ripple_account) | **GET** /ripple/{accountName} | 
*RippleApi* | [**list_ripple_accounts**](docs/RippleApi.md#list_ripple_accounts) | **GET** /ripple | 
*RippleApi* | [**sign_ripple_transaction**](docs/RippleApi.md#sign_ripple_transaction) | **POST** /ripple/{accountName}/sign-tx | 
*YearnApi* | [**add_liquidity**](docs/YearnApi.md#add_liquidity) | **POST** /yearn/{name}/add-liquidity | 
*YearnApi* | [**add_liquidity_weth**](docs/YearnApi.md#add_liquidity_weth) | **POST** /yearn/{name}/add-liquidity-weth | 
*YearnApi* | [**remove_liquidity**](docs/YearnApi.md#remove_liquidity) | **POST** /yearn/{name}/remove-liquidity | 
*YearnApi* | [**remove_liquidity_weth**](docs/YearnApi.md#remove_liquidity_weth) | **POST** /yearn/{name}/remove-liquidity-weth | 


## Documentation For Models

 - [AaveInput](docs/AaveInput.md)
 - [AaveReservesAPIResponse](docs/AaveReservesAPIResponse.md)
 - [AaveReservesData](docs/AaveReservesData.md)
 - [AccountAPIResponse](docs/AccountAPIResponse.md)
 - [AccountData](docs/AccountData.md)
 - [AccountResponse](docs/AccountResponse.md)
 - [AvailablePaymentMethod](docs/AvailablePaymentMethod.md)
 - [BalanceAPIResponse](docs/BalanceAPIResponse.md)
 - [BalanceResponse](docs/BalanceResponse.md)
 - [BitcoinAPIResponse](docs/BitcoinAPIResponse.md)
 - [BitcoinCashAPIResponse](docs/BitcoinCashAPIResponse.md)
 - [BitcoinCashInput](docs/BitcoinCashInput.md)
 - [BitcoinCashTransactionInput](docs/BitcoinCashTransactionInput.md)
 - [BitcoinCashTransactionOutput](docs/BitcoinCashTransactionOutput.md)
 - [BitcoinInput](docs/BitcoinInput.md)
 - [BitcoinTransactionInput](docs/BitcoinTransactionInput.md)
 - [BitcoinTransactionOutput](docs/BitcoinTransactionOutput.md)
 - [BroadCastRawTransactionAPIResponse](docs/BroadCastRawTransactionAPIResponse.md)
 - [BroadCastRawTransactionResponse](docs/BroadCastRawTransactionResponse.md)
 - [BroadcastInput](docs/BroadcastInput.md)
 - [ConveyorFinanceControllerResponse](docs/ConveyorFinanceControllerResponse.md)
 - [CosmosAPIResponse](docs/CosmosAPIResponse.md)
 - [CosmosInput](docs/CosmosInput.md)
 - [CosmosTransactionInput](docs/CosmosTransactionInput.md)
 - [CosmosTransactionOutput](docs/CosmosTransactionOutput.md)
 - [CreateAccountInput](docs/CreateAccountInput.md)
 - [CryptoCurrency](docs/CryptoCurrency.md)
 - [DeployInput](docs/DeployInput.md)
 - [DogeCoinAPIResponse](docs/DogeCoinAPIResponse.md)
 - [DogeCoinInput](docs/DogeCoinInput.md)
 - [DogeCoinTransactionInput](docs/DogeCoinTransactionInput.md)
 - [DogeCoinTransactionOutput](docs/DogeCoinTransactionOutput.md)
 - [EnsResolveAPIResponse](docs/EnsResolveAPIResponse.md)
 - [EnsResolveInput](docs/EnsResolveInput.md)
 - [EnsResolveResponse](docs/EnsResolveResponse.md)
 - [EosAPIResponse](docs/EosAPIResponse.md)
 - [EosInput](docs/EosInput.md)
 - [EosTransactionInput](docs/EosTransactionInput.md)
 - [EosTransactionOutput](docs/EosTransactionOutput.md)
 - [Erc1155Request](docs/Erc1155Request.md)
 - [Erc721Request](docs/Erc721Request.md)
 - [FiatCurrency](docs/FiatCurrency.md)
 - [GetSupportedOnRampsResponse](docs/GetSupportedOnRampsResponse.md)
 - [GetSupportedOnRampsResponseMessageInner](docs/GetSupportedOnRampsResponseMessageInner.md)
 - [GetSupportedOnRampsResponseMessageInnerIcons](docs/GetSupportedOnRampsResponseMessageInnerIcons.md)
 - [GetSupportedOnRampsResponseMessageInnerIconsPng](docs/GetSupportedOnRampsResponseMessageInnerIconsPng.md)
 - [GetSwapDto](docs/GetSwapDto.md)
 - [InputBody](docs/InputBody.md)
 - [LitecoinAPIResponse](docs/LitecoinAPIResponse.md)
 - [LitecoinInput](docs/LitecoinInput.md)
 - [LitecoinTransactionInput](docs/LitecoinTransactionInput.md)
 - [LitecoinTransactionOutput](docs/LitecoinTransactionOutput.md)
 - [Message](docs/Message.md)
 - [NonceAPIResponse](docs/NonceAPIResponse.md)
 - [NonceResponse](docs/NonceResponse.md)
 - [PaymentType](docs/PaymentType.md)
 - [PingResponse](docs/PingResponse.md)
 - [Quote](docs/Quote.md)
 - [RippleAPIResponse](docs/RippleAPIResponse.md)
 - [RippleInput](docs/RippleInput.md)
 - [RippleTransactionInput](docs/RippleTransactionInput.md)
 - [RippleTransactionOutput](docs/RippleTransactionOutput.md)
 - [SellQuote](docs/SellQuote.md)
 - [SignMessage](docs/SignMessage.md)
 - [SignMessageAPIResponse](docs/SignMessageAPIResponse.md)
 - [SignTypedData](docs/SignTypedData.md)
 - [SolanaAPIResponse](docs/SolanaAPIResponse.md)
 - [SolanaInput](docs/SolanaInput.md)
 - [SolanaTransactionInput](docs/SolanaTransactionInput.md)
 - [SolanaTransactionOutput](docs/SolanaTransactionOutput.md)
 - [SupportedAssetResponse](docs/SupportedAssetResponse.md)
 - [SupportedAssetResponseAssetsInner](docs/SupportedAssetResponseAssetsInner.md)
 - [SupportedCurrenciesResponse](docs/SupportedCurrenciesResponse.md)
 - [SupportedDefaultResponse](docs/SupportedDefaultResponse.md)
 - [SupportedDefaultResponseDefaults](docs/SupportedDefaultResponseDefaults.md)
 - [SupportedDefaultResponseDefaultsId](docs/SupportedDefaultResponseDefaultsId.md)
 - [SupportedPaymentTypesCurrencyResponse](docs/SupportedPaymentTypesCurrencyResponse.md)
 - [SupportedPaymentTypesMessage](docs/SupportedPaymentTypesMessage.md)
 - [TokenSwapParams](docs/TokenSwapParams.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionAPIResponse](docs/TransactionAPIResponse.md)
 - [TransactionData](docs/TransactionData.md)
 - [TransactionInput](docs/TransactionInput.md)
 - [TransactionInputMetaData](docs/TransactionInputMetaData.md)
 - [TransactionInputSupportedParams](docs/TransactionInputSupportedParams.md)
 - [TransactionInputSupportedParamsPartnerData](docs/TransactionInputSupportedParamsPartnerData.md)
 - [TransactionInputSupportedParamsPartnerDataRedirectUrl](docs/TransactionInputSupportedParamsPartnerDataRedirectUrl.md)
 - [TransactionInputSupportedParamsTheme](docs/TransactionInputSupportedParamsTheme.md)
 - [TransactionInputWallet](docs/TransactionInputWallet.md)
 - [TransactionRequest](docs/TransactionRequest.md)
 - [TransactionResponse](docs/TransactionResponse.md)
 - [TransactionResponseInfo](docs/TransactionResponseInfo.md)
 - [TransactionResponseTx](docs/TransactionResponseTx.md)
 - [TronAPIResponse](docs/TronAPIResponse.md)
 - [TronInput](docs/TronInput.md)
 - [TronTransactionInput](docs/TronTransactionInput.md)
 - [TronTransactionOutput](docs/TronTransactionOutput.md)
 - [Tx](docs/Tx.md)
 - [UniswapInput](docs/UniswapInput.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
### BearerAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a id="OAuth2"></a>
### OAuth2

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: 
 - **authorization_code**: grants authorization_code

<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


## Author




