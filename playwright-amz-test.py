from playwright.sync_api import sync_playwright

# this is a demo and is for education purposes only.

asins = ['B07PZR3PVB', 'B00Q2KEVA2', 'B08XMPGL7Q', 'B014RD6RC0', 'B08WJ6MGKJ']

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 '
                                             'Firefox/91.0')
    page = context.new_page()

for asin in asins:
    page.goto(f"https://www.amazon.co.uk/gp/product/{asin}")
    name = page.query_selector('h1#title').text_content()
    stock = page.query_selector('div#availability span').text_content()
    price = page.query_selector('span#priceblock_ourprice').text_content()
    product = (
        asin,
        name.strip(),
        price.strip(),
        stock.strip()
    )

    print(product)
browser.close()
