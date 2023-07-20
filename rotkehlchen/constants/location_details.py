from rotkehlchen.types import Location, LocationDetails

LOCATION_DETAILS = {
    Location.EXTERNAL: LocationDetails(icon='mdi-book'),
    Location.KRAKEN: LocationDetails(image='kraken.svg'),
    Location.POLONIEX: LocationDetails(image='poloniex.svg'),
    Location.BITTREX: LocationDetails(image='bittrex.svg'),
    Location.BINANCE: LocationDetails(image='binance.svg'),
    Location.BITMEX: LocationDetails(image='bitmex.svg'),
    Location.COINBASE: LocationDetails(image='coinbase.svg'),
    Location.BANKS: LocationDetails(icon='mdi-bank'),
    Location.BLOCKCHAIN: LocationDetails(icon='mdi-link'),
    Location.COINBASEPRO: LocationDetails(
        image='coinbasepro.svg',
        label='Coinbase Pro',
    ),
    Location.GEMINI: LocationDetails(image='gemini.svg'),
    Location.EQUITIES: LocationDetails(icon='mdi-bag-suitcase'),
    Location.REALESTATE: LocationDetails(icon='mdi-home'),
    Location.COMMODITIES: LocationDetails(icon='mdi-basket'),
    Location.CRYPTOCOM: LocationDetails(image='crypto_com.svg'),
    Location.UNISWAP: LocationDetails(image='uniswap.svg'),
    Location.BITSTAMP: LocationDetails(image='bitstamp.svg'),
    Location.BINANCEUS: LocationDetails(
        label='Binance US',
        image='binance.svg',
    ),
    Location.BITFINEX: LocationDetails(image='bitfinex.svg'),
    Location.BITCOINDE: LocationDetails(image='btcde.svg'),
    Location.ICONOMI: LocationDetails(image='iconomi.svg'),
    Location.KUCOIN: LocationDetails(image='kucoin.svg'),
    Location.BALANCER: LocationDetails(image='balancer.svg'),
    Location.LOOPRING: LocationDetails(image='loopring.svg'),
    Location.FTX: LocationDetails(image='ftx.svg'),
    Location.NEXO: LocationDetails(image='nexo.svg'),
    Location.BLOCKFI: LocationDetails(image='blockfi.svg'),
    Location.INDEPENDENTRESERVE: LocationDetails(
        label='Independent Reserve',
        image='independentreserve.svg',
    ),
    Location.GITCOIN: LocationDetails(image='gitcoin.svg'),
    Location.SUSHISWAP: LocationDetails(image='sushiswap.svg'),
    Location.SHAPESHIFT: LocationDetails(image='shapeshift.svg'),
    Location.UPHOLD: LocationDetails(image='uphold.svg'),
    Location.BITPANDA: LocationDetails(image='bitpanda.svg'),
    Location.BISQ: LocationDetails(image='bisq.svg'),
    Location.FTXUS: LocationDetails(
        label='FTX US',
        image='ftxus.svg',
    ),
    Location.OKX: LocationDetails(image='okx.svg'),
    Location.ETHEREUM: LocationDetails(image='ethereum.svg'),
    Location.OPTIMISM: LocationDetails(image='optimism.svg'),
    Location.POLYGON_POS: LocationDetails(image='polygon_pos.svg'),
    Location.ARBITRUM_ONE: LocationDetails(image='arbitrum_one.svg'),
}
