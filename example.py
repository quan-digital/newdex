from newdex import NewdexV1, setup_logger
import logging

if __name__ == '__main__':
    logger = setup_logger('main')
    nd = NewdexV1('access_key', 'secret_key','theonlykarma-karma-wax', logging.DEBUG)
    logger.info(nd.open_orders())
    logger.info(nd.filled_orders())
    logger.info(nd.canceled_orders())
    logger.info(nd.order_history())
    logger.info(nd.get_pairs())
    logger.info(nd.get_tickers())
    logger.info(nd.get_ticker())
    logger.info(nd.get_price())
    logger.info(nd.get_depth())
    logger.info(nd.get_trades())
    logger.info(nd.get_candles())