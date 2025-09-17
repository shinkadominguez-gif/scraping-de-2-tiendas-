from tienda_b import scrape_tienda_b
from tienda_a import scrape_tienda_a
import pandas as pd
import os
def main():
    print('iniciando tienda a')
    df_a = scrape_tienda_a()
    print('iniciando tienda b ')
    df_b = scrape_tienda_b()

    df = pd.concat([df_a, df_b], ignore_index=True)
    
    os.makedirs('data', exist_ok=True)

    df.to_csv('data/precios.csv', index=False, sep=';')
    print('scraping completo, datos guardados en data/precios')

if __name__ == '__main__':
    main()
