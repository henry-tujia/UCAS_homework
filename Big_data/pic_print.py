import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def save_pic(name):
    df = pd.read_csv(name + '.csv', sep='\t')

    for i in range(1, len(df.columns) + 1, 2):
        index_x = name + '-' + str(i)
        index_y = name + '-' + str(i + 1)
        fig = sns.scatterplot(x=index_x, y=index_y, data=df)
        scatter_fig = fig.get_figure()
        scatter_fig.savefig(index_x + '.png', dpi=400)
        print(index_x + '.png is done!')
        plt.clf()
    print('ok')


if __name__ == '__main__':
    save_pic('TW_U')
    save_pic('TW_V')
