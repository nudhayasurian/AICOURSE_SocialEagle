from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


URL = "https://www.cricbuzz.com/"
SCREENSHOT = "cricbuzz_live_score.png"


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page(viewport={"width": 1440, "height": 900})

        try:
            print("Opening Cricbuzz...")
            page.goto(URL, wait_until="domcontentloaded", timeout=30000)

            # Wait for the page to finish loading its dynamic content.
            # This is better than sleep(5) because Playwright waits
            # for the actual page condition.
            try:
                page.wait_for_load_state("networkidle", timeout=15000)
            except PlaywrightTimeoutError:
                # Cricbuzz may continue making background requests.
                # That doesn't necessarily mean the page failed.
                print("Page is still loading background content...")

            # Look for the live-score section.
            # The locator is checked repeatedly until it appears or times out.
            live_scores = page.locator(
                "div.cb-col.cb-col-100.cb-lv-main"
            )

            try:
                live_scores.wait_for(
                    state="visible",
                    timeout=15000
                )

                score_text = live_scores.inner_text().strip()

                if score_text:
                    print("\n===== LIVE SCORE =====")
                    print(score_text)
                    print("======================\n")
                else:
                    print("No live score is currently available.")

            except PlaywrightTimeoutError:
                print("No live match/score was found on Cricbuzz.")

            # Save screenshot whether or not a live match exists.
            page.screenshot(
                path=SCREENSHOT,
                full_page=True
            )

            print(f"Screenshot saved as: {SCREENSHOT}")

        except Exception as e:
            print(f"An error occurred: {e}")

            # Try to save a screenshot even when something goes wrong.
            try:
                page.screenshot(
                    path="cricbuzz_error.png",
                    full_page=True
                )
                print("Error screenshot saved as: cricbuzz_error.png")
            except Exception:
                pass

        finally:
            browser.close()


if __name__ == "__main__":
    main()