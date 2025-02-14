from shining_pebbles import open_df_in_file_folder_by_regex
from .path_director import FILE_FOLDER
from .file_name_formatter import format_regex_for_snapshot, format_regex_for_timeseries, format_regex_for_period, format_regex_for_bbg_price, format_regex_for_market

def load_menu2160(fund_code):
    regex = format_regex_for_timeseries(menu_code='2160', fund_code=fund_code)
    df = open_df_in_file_folder_by_regex(file_folder=FILE_FOLDER['2160'], regex=regex)
    return df

def load_menu2160_snapshot(date_ref):
    regex = format_regex_for_snapshot(menu_code='2160', fund_code='000000', date_ref=date_ref)
    df = open_df_in_file_folder_by_regex(file_folder=FILE_FOLDER['2160-snapshot'], regex=regex)
    return df

def load_menu8186_snapshot(date_ref):
    regex = format_regex_for_snapshot(menu_code='8186', fund_code='000000', date_ref=date_ref)
    df = open_df_in_file_folder_by_regex(file_folder=FILE_FOLDER['8186-snapshot'], regex=regex)
    return df

def load_menu4165(fund_code, date_ref):
    regex = format_regex_for_period(menu_code='4165', fund_code=fund_code, date_ref=date_ref)
    df = open_df_in_file_folder_by_regex(file_folder=FILE_FOLDER['4165'], regex=regex)
    return df

def load_menu4165_snapshot(fund_code, date_ref):
    regex = format_regex_for_snapshot(menu_code='4165', fund_code=fund_code, date_ref=date_ref)
    df = open_df_in_file_folder_by_regex(file_folder=FILE_FOLDER['4165'], regex=regex)
    return df

def load_index(ticker_bbg_index):
    regex = format_regex_for_bbg_price(ticker_bbg=ticker_bbg_index)
    df = open_df_in_file_folder_by_regex(file_folder=FILE_FOLDER['index'], regex=regex)
    return df

def load_currency(ticker_bbg_currency):
    regex = format_regex_for_bbg_price(ticker_bbg=ticker_bbg_currency)
    df = open_df_in_file_folder_by_regex(file_folder=FILE_FOLDER['currency'], regex=regex)
    return df

def load_market(market_name, date_ref=None):
    regex = format_regex_for_market(market_name=market_name, date_ref=date_ref)
    df = open_df_in_file_folder_by_regex(file_folder=FILE_FOLDER['market'], regex=regex)
    return df
