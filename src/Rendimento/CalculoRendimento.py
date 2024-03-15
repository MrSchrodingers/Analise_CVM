import pandas as pd

class MonthlyReturnCalculator:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def calculateMonthlyReturns(self):
        self.dataframe = self.dataframe.sort_values(by='DT_COMPTC')
        dfCopy = self.dataframe.copy()

        if not pd.api.types.is_datetime64_any_dtype(dfCopy['DT_COMPTC']):
            dfCopy['DT_COMPTC'] = pd.to_datetime(dfCopy['DT_COMPTC'])

        monthlyReturn = pd.DataFrame(columns=['DT_COMPTC', 'Monthly Return (%)', 'Standard Deviation', 'Annualized Return (%)', 'Annualized Standard Deviation'])

        for cnpj, group in dfCopy.groupby('CNPJ_FUNDO'):
            groupByMonth = group.groupby(group['DT_COMPTC'].dt.to_period('M'))

            annualizedReturn = 0
            annualizedStdDev = 0

            for month, data in groupByMonth:
                firstDayData = data.iloc[0]
                lastDayData = data.iloc[-1]
                monthlyReturnVal = ((lastDayData['VL_QUOTA'] - firstDayData['VL_QUOTA']) / firstDayData['VL_QUOTA']) * 100
                stdDev = data['VL_QUOTA'].pct_change().std() * 100

                annualizedReturn += monthlyReturnVal
                annualizedStdDev = ((annualizedStdDev ** 2 + stdDev ** 2) ** 0.5) / 2

                monthlyReturn = pd.concat([monthlyReturn, pd.DataFrame({'DT_COMPTC': [month.to_timestamp()], 'Monthly Return (%)': [monthlyReturnVal], 'Standard Deviation': [stdDev], 'Annualized Return (%)': [annualizedReturn], 'Annualized Standard Deviation': [annualizedStdDev]})], ignore_index=True)

        return monthlyReturn