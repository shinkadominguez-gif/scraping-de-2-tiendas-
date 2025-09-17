from tienda_b import scrape_tienda_b

if __name__ == "__main__":
    df = scrape_tienda_b()
    print(df.head())