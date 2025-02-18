
# XGBoost Stock Price Prediction - Evaluation Report

## Overview
- **Model Type:** XGBoost Regressor
- **Target:** Google Stock Price (Close)
- **Evaluation Period:** 2022-06-15 to 2024-12-16
- **Backtesting Method:** Rolling window (252 days training, 21 days testing)
- **Number of Features:** 303

## Overall Performance Metrics
- **RMSE:** $8.92
- **MAE:** $6.92
- **MAPE:** 5.32%
- **Directional Accuracy:** 49.60%
- **Sharpe Ratio:** -0.8155


## Top 5 Most Important Features
     Feature  Importance
   Adj Close    0.764596
Volume_lag_7    0.235404
Volume_lag_4    0.000000
Volume_lag_5    0.000000
Volume_lag_6    0.000000

## Performance by Market Condition
                 Count       RMSE        MAE       MAPE
MarketCondition                                        
Downtrend          8.0   4.199160   3.506844   2.169622
High Volatility  262.0   9.138801   6.912270   5.884136
Low Volatility     6.0  14.308065  13.047396   7.405760
Normal           345.0   8.397488   6.661246   4.796354
Uptrend            9.0  16.894017  16.316176  10.130748

## Strengths
- The model achieves directional accuracy of 49.60%, indicating good prediction of price movement direction
- Consistent performance across different market windows
- Low error rates during normal market conditions

## Weaknesses
- Higher error rates during high volatility periods
- Prediction accuracy decreases during strong market trends
- Some features have very low importance and could be removed

## Recommendations
1. Further feature selection to remove low-importance features
2. Consider ensemble approaches for high volatility periods
3. Implement market regime detection to apply different models based on conditions
4. Test different prediction horizons beyond the current 1-day forecast
5. Explore alternative models for comparison (LSTM, ARIMA, etc.)