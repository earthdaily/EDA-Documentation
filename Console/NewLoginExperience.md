---
layout: default
title: Migrate to our new login experience
grand_parent: EDS Documentation
parent: Console
nav_order: 4
---

# Login system migration

On **March 10, 2025** EarthDaily will switch to an enhanced authentication system for all EarthDaily Console sites. This upgrade represents an improvement in our security infrastructure and lays the foundation for advanced security features in the future. The new authentication system is accessible now as a preview feature. In the unlikely event that it does not work for you, you can choose to revert to the legacy login system during our transition period.

{: .important}
> To ensure maximum security, **all existing users must reset their passwords to access the new login system**. You can reuse your current password if it meets the new security requirements. Note that passwords for the new and old systems are maintained separately, and should to choose to revert to the legacy login system for any reason, its password will remian unchanged.

## Try out the new login experience as a preview feature

To access the new login system, **leave the `Organization` field empty** on the login page (we will keep track of this for you). Instead, immediately look for the **Use New Login Experience (preview)** link in the bottom of the login box.

![Screenshot indicating link to new login experience](../Images/NewLogin/NewLoginFlowLink.png)

Clicking the link will take you to the new login flow, where you should see the following prompt:

![Screenshot showing new login dialogue box](../Images/NewLogin/NewLoginBox.png)

{: .highlight}
> After March 10, 2025, our log in page will look like this
>
> ![Screenshot of the new EDS console login page](../Images/NewLogin/NewEDSConsoleLoginPage.png)
>
> Simply enter your email in the text box and click on the *login* button to initialize the new login flow. If you wish to revert to the legacy login experience, click on the *use legacy login experience* link.


### Verifying that you're using the new login flow

Once in you see the new login prompt, verify that your browser URL starts with `login.earthdaily.com`. For your security, always ensure that you're entering login credentials in a page that's hosted on this domain. EarthDaily will never request your password through any other domain.

### Setting Up Your Password

{: .highlight}
> You can ignore this section if your account was created after March 10, 2025

If this is your first time using our new login system, you need to initiate a password reset process by clicking the **Forgot Password?** link after entering your email address:

![Screenshot indicating password reset link](../Images/NewLogin/PasswordResetLink.png)

You'll receive a password reset link via email that should look similar to the following screenshot. The link would be valid for 5 days, although you can always request a new link by clicking on **Forgot Password?** again. For your safety, always ensure the link in the email goes to an URL under `https://login.earthdaily.com`:

![Screenshot of a sample password reset link email](../Images/NewLogin/PasswordResetEmail.png)

After setting your password, you can return to the console to log in with your new credentials. Remember to always click on the **Use New Login Experience (preview)** link to be taken to the new login pages.

## Enhanced API Authentication

The new login system introduces an improved API token authentication system. Users now have the ability to revoke compromised tokens and generate new ones as needed. When provisioning a new API token, you may be asked to log in again if required for security purposes.

**Upon token generation, you'll be shown your API token exactly once.** Please save it immediately in a password manager or secure vault, as we cannot display it again. If you lose your token, you'll need to delete the old one before you can generate a new one.

### Using the new API token

Your new API token can be used with existing scripts and tools that use the **OAuth Client Credentials Flow** as described in the [Authentication Page](../GettingStarted/APIAuthentication). Simply use these values in place of your old credential information:

- **EDS_AUTH_URL**: `https://api.earthdaily.com/account_management/v1/authentication/api_tokens/exchange`
- **CLIENT_ID**: `EARTHDAILY_API_TOKEN`
- **CLIENT_SECRET**: (Use your new API Token here)

{: .warning}
> Your old API credentials will be **deleted** when the legacy authentication system is retired. We strongly recommend testing and transitioning to the new API token system as soon as possible to ensure uninterrupted service.

## Need Help?

Our support team is available to assist you with the transition to the new authentication system. Please don't hesitate to reach out if you have any questions or encounter any issues during the process.
