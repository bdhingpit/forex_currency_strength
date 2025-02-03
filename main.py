import pandas as pd
import matplotlib.pyplot as plt
from library import dataRelated as dR
from library import forexNotifier as fN

length_list = [30, 60]

for n in length_list:
    all_ohlc_dict = dR.data_collection('H1', n)
    pc_change_dict, diffs_dict = dR.percent_change(all_ohlc_dict)

    print('CURRENCY STRENGTH (%d)' % n)
    with open('currStrengthOutputs/currStrengthValues.txt', 'w') as f:
        for key in pc_change_dict.keys():
            print(key, pc_change_dict[key])

            f.write('%s %.2f\n' % (key, pc_change_dict[key]))

    print('\n\nTRADEABLE CURRENCY PAIRS (%d)' % n)
    with open('currStrengthOutputs/tradeableCurrPair.txt', 'w') as f:
        for key in diffs_dict.keys():
            print(key, diffs_dict[key])

            f.write('%s %.2f\n' % (key, diffs_dict[key]))

    plt.bar(x=[2, 4, 6, 8, 10, 12, 14, 16], height=pc_change_dict.values(), tick_label=list(pc_change_dict.keys()))

    time = pd.to_datetime('now').strftime('%Y-%m-%d %H-%M')
    fname = 'currStrengthOutputs/strengthBar-{}.jpg'.format(str(time))

    plt.savefig(fname=fname, dpi=300, quality=95)

    fN.message_curr_strength(fname)
