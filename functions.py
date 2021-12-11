import pandas as pd
def stonks(x):
    data = pd.read_csv('financials.csv')
    data = data.rename(columns={'Price/Earnings': 'Price_Earnings_Ratio', 'Earnings/Share': 'Earnings_Share_Ratio',
                                'Dividend Yield': 'Dividend_Yield', '52 Week Low': '52_Week_Low',
                                '52 Week High': '52_Week_High', 'Market Cap': 'Market_Cap',
                                'Price/Sales': 'Price_Sales_Ratio', 'Price/Book': 'Price_Book_Ratio'})
    dp_intro = data.drop(['SEC Filings', 'EBITDA', '52_Week_Low', '52_Week_High', 'Symbol'], axis=1)

    groups = dp_intro.groupby('Sector')
    # Removing Sector wise above PER outliers:
    filtered_df = groups.apply(lambda x: x[
        x['Price_Earnings_Ratio'] <= Quartile75(x['Price_Earnings_Ratio']) + 1.5 * Interquartilerange(
            x['Price_Earnings_Ratio'])])
    len(filtered_df)
    # Removing sector wise below PER outliers:
    filtered_df = filtered_df.reset_index(drop=True)

    groups = filtered_df.groupby('Sector')
    filtered_df = groups.apply(lambda x: x[
        x['Price_Earnings_Ratio'] >= Quartile25(x['Price_Earnings_Ratio']) - 1.5 * Interquartilerange(
            x['Price_Earnings_Ratio'])])

    # Same operation for Price Book Ratio(BV):
    filtered_df = filtered_df.reset_index(drop=True)
    groups = filtered_df.groupby('Sector')
    filtered_df = groups.apply(lambda x: x[
        x['Price_Book_Ratio'] >= Quartile25(x['Price_Book_Ratio']) - 1.5 * Interquartilerange(
            x['Price_Book_Ratio'])])

    filtered_df = filtered_df.reset_index(drop=True)

    groups = filtered_df.groupby('Sector')
    filtered_df = groups.apply(lambda x: x[
        x['Price_Book_Ratio'] <= Quartile75(x['Price_Book_Ratio']) + 1.5 * Interquartilerange(
            x['Price_Book_Ratio'])])
    filtered_df = filtered_df.reset_index(drop=True)

    filtered_df_123 = filtered_df.reset_index(drop=True)

    groups = filtered_df_123.groupby('Sector')
    filtered_df_123 = groups.apply(lambda x: x[
        x['Price_Book_Ratio'] >= Mean(x['Price_Book_Ratio'] - 0.005 * StDeviation(x['Price_Book_Ratio']))])

    filtered_df_123 = filtered_df_123.reset_index(drop=True)
    groups = filtered_df_123.groupby('Sector')
    filtered_df_123 = groups.apply(
        lambda x: x[
            x['Price_Book_Ratio'] <= Mean(x['Price_Book_Ratio'] + 0.01 * StDeviation(x['Price_Book_Ratio']))])

    filtered_df_1234 = filtered_df_123.reset_index(drop=True)

    groups = filtered_df_1234.groupby('Sector')
    filtered_df_1234 = groups.apply(lambda x: x[x['Price_Earnings_Ratio'] >= Mean(
        x['Price_Earnings_Ratio'] - 0.005 * StDeviation(x['Price_Earnings_Ratio']))])

    filtered_df_1234 = filtered_df_1234.reset_index(drop=True)
    groups = filtered_df_1234.groupby('Sector')
    filtered_df_RES = groups.apply(lambda x: x[x['Price_Earnings_Ratio'] <= Mean(
        x['Price_Earnings_Ratio'] + 0.005 * StDeviation(x['Price_Earnings_Ratio']))])
    filtered_df_RES = filtered_df_RES.reset_index(drop=True)

    sample = filtered_df_RES.sample(n=10)[['Sector', 'Name', 'Price', 'Dividend_Yield']]
    return sample.Name

def Quartile25(x):
    return x.quantile(0.25)
def Quartile75(x):
    return x.quantile(0.75)
def Interquartilerange(x):
    return x.quantile(0.75) - x.quantile(0.25)
#Functions to have a clean table (with caps)
def Mean(x):
    return x.mean()
def Median(x):
    return x.median()
def StDeviation(x):
    return x.std()

def task7(BVSTD, PERSTD):
    filtered_df_123 = jp.filtered_df.reset_index(drop=True)

    groups = filtered_df_123.groupby('Sector')
    filtered_df_123 = groups.apply(lambda x: x[
        x['Price_Book_Ratio'] >= Mean(x['Price_Book_Ratio'] - BVSTD * StDeviation(x['Price_Book_Ratio']))])

    filtered_df_123 = filtered_df_123.reset_index(drop=True)
    groups = filtered_df_123.groupby('Sector')
    filtered_df_123 = groups.apply(
        lambda x: x[
            x['Price_Book_Ratio'] <= Mean(x['Price_Book_Ratio'] + BVSTD * StDeviation(x['Price_Book_Ratio']))])
    filtered_df_1234 = filtered_df_123.reset_index(drop=True)

    groups = filtered_df_1234.groupby('Sector')
    filtered_df_1234 = groups.apply(lambda x: x[x['Price_Earnings_Ratio'] >= Mean(
        x['Price_Earnings_Ratio'] -PERSTD * StDeviation(x['Price_Earnings_Ratio']))])

    filtered_df_1234 = filtered_df_1234.reset_index(drop=True)
    groups = filtered_df_1234.groupby('Sector')
    filtered_df_RES = groups.apply(lambda x: x[x['Price_Earnings_Ratio'] <= Mean(
        x['Price_Earnings_Ratio'] + PERSTD * StDeviation(x['Price_Earnings_Ratio']))])
    filtered_df_RES = filtered_df_RES.reset_index(drop=True)
    return filtered_df_RES