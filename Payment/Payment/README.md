## Payment-Team

Payment is responsible for the following payment functionality (live-document):

* User-to-NTTF
* NTTF-to-Restaurant
* NTTF-to-Driver

### Git workflow:
Please branch off `origin\payment-main\`

Using the convention`origin\payment-main\{your-initials}\{short-descriptor}`

An example of this workflow would be:

`git checkout payment-main`

`git checkout -b AS/get-cart-total payment-main`

Similarly to how there is often a `dev` branch off of `main` in most git workflows, this branch will act as `dev-for-payment-team` with the purpose of (hopefully) not disturbing the working codebase of `main` and improving visibility within our team. If this is dumb and everyone wants to branch off main directly then we can shut this branch down.
