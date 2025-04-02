
import pandas as pd
import matplotlib.pyplot as plt
from log import log

class BigMacStatistic:
    
    @log
    def plot_bigmac_prices(self):
        df = pd.read_csv('BigmacPrice.csv')
        country_col = 'name'
        price_col = 'dollar_price'
        selected_countries = ['China', 'Russia', 'Euro area', 'United States','Britain', 'Canada', 'Australia', 'Japan', 'Switzerland', 'Sweden','Norway', 'Brazil', 'Mexico','South Africa', 'Turkey', 'India', 'Thailand','Saudi Arabia', 'United Arab Emirates']
        df_filtered = df[df[country_col].isin(selected_countries)] \
                      .drop_duplicates(subset=[country_col], keep='last')
        df_filtered = df_filtered.sort_values(price_col, ascending=False)
        
    
        fig, ax = plt.subplots(figsize=(10, 6))
        df_filtered.plot(kind='barh', x=country_col, y=price_col, ax=ax,
                        title='РЯД 1', 
                        color='white', legend=False)
        fig.patch.set_facecolor('#0000B2')
        ax.set_facecolor('#0000B2')
        

        for i, v in enumerate(df_filtered[price_col]):
            ax.text(v + 0.1, i, f"${v:.2f}", color='white', va='center', fontsize=10)
        
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('white')
        ax.spines['bottom'].set_color('white')
        ax.set_ylabel('')
        ax.tick_params(axis='both', colors='white')
        ax.title.set_color('white')
        plt.tight_layout()
        plt.show()






       
         