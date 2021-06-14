import pandas as pd


def PrintBestCombination(Total_weight, weight, fees, sample_len):
    """
    :param Total_weight: Limit of the transaction weight in block
    :param weight: weight list of the transactions
    :param fees: fees list of the transactions
    :param sample_len: size of the sampling taking full lenght of csv
    :return: prints fees and weights
    """
    dp = [[0 for _ in range(Total_weight + 1)]
          for _ in range(sample_len + 1)]

    # tabulation
    # Complexity 0(sample_len x Total_weight) or O(N^2)
    # takes too much time to complete not feasible

    for i in range(sample_len + 1):
        for w in range(Total_weight + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weight[i - 1] <= w:
                dp[i][w] = max(fees[i - 1]
                               + dp[i - 1][w - weight[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Print optimized fee
    optimized_fee = dp[sample_len][Total_weight]
    print(optimized_fee)

    w = Total_weight
    for i in range(sample_len, 0, -1):
        if optimized_fee <= 0:
            break
        if optimized_fee == dp[i - 1][w]:
            continue
        else:
            print(weight[i - 1])
            optimized_fee = optimized_fee - fees[i - 1]
            w = w - weight[i - 1]


df = pd.read_csv('mempool.csv')
print(PrintBestCombination(4000000, df['weight'], df['fee'], len(df)))
