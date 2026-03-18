# FlashCart Web App

Small Flask web app that simulates a mini e-commerce flow:

- Product listing
- Add/remove cart items
- Checkout form (name, customer tier, coupon)
- Final order confirmation with calculated totals

## Run locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start app:

```bash
python app.py
```

3. Open:

```text
http://127.0.0.1:5000/
```
## Demo flow

- Add products from home page
- Visit cart
- Checkout with tier and optional coupon (try `WELCOME10`)
- Confirm order totals after discounts and tax
