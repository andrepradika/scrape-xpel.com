from playwright.sync_api import sync_playwright
import csv
import openpyxl

def main():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to the page with timeout
        try:
            page.goto("https://www.xpel.com/installer-locator", timeout=15000)  # 15s timeout
        except:
            print("Failed to load page within the timeout")
            browser.close()
            return
        
        # Click "Load More" until it disappears
        while True:
            try:
                page.click("button.pagination-load-more", timeout=5000)
                page.wait_for_timeout(2000)
            except:
                print("No more 'Load More' buttons or timeout reached")
                break
        
        # Extract installer data
        installers = []
        cards = page.query_selector_all(".installer-card")
        
        for card in cards:
            try:
                name = card.query_selector(".location-name").inner_text()
            except:
                name = "N/A"
            
            try:
                address = card.query_selector(".location-information p").inner_text().strip().replace('\n', ', ')
            except:
                address = "N/A"
            
            try:
                phone = card.query_selector("a[href^='tel:']").get_attribute("href").split(":")[1]
            except:
                phone = "N/A"
            
            try:
                website = card.query_selector("a[href^='http']").get_attribute("href")
            except:
                website = "N/A"
            
            products = []
            try:
                product_elements = card.query_selector_all(".tag")
                products = [p.inner_text() for p in product_elements]
            except:
                pass
            
            installers.append({
                "Name": name,
                "Address": address,
                "Phone": phone,
                "Website": website,
                "Products": ", ".join(products)
            })
        
        # Close browser
        browser.close()
        
        # Save to CSV
        if installers:
            filename = 'xpel_installers_playwright'
            keys = list(installers[0].keys())
            csv_filename = 'data/' + filename + '.csv'
            with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(installers)
            print(f"Saved {len(installers)} records to {csv_filename}")
            
            # Save to XLSX
            xlsx_filename = 'data/' + filename + '.xlsx'
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.append(keys)  # Convert dict_keys to list
            for installer in installers:
                ws.append(list(installer.values()))
            wb.save(xlsx_filename)
            print(f"Saved {len(installers)} records to {xlsx_filename}")
        else:
            print("No data found")

if __name__ == "__main__":
    main()
