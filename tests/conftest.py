import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context()

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        page = context.new_page()

        yield page

        os.makedirs("traces", exist_ok=True)

        context.tracing.stop(
            path="traces/trace.zip"
        )

        context.close()
        browser.close()