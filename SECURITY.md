# Security

## Deployment architecture

This static website is hosted on GitHub Pages at the custom domain `yannickhamelryck.be`. DNS is managed through Cloudflare.

## Browser security headers

Security headers must be configured and verified at the hosting or proxy layer. Adding equivalent `<meta>` elements to the HTML is not a substitute: some directives, including `frame-ancestors`, are not supported there, and response headers provide consistent coverage for all pages and assets.

The following policy is a suitable baseline for the site's current local CSS, JavaScript, images, icons, and web manifest while allowing the contact form to submit to Web3Forms:

```http
Content-Security-Policy: default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'; form-action 'self' https://api.web3forms.com; script-src 'self'; style-src 'self'; img-src 'self' data:; font-src 'self'; manifest-src 'self'; connect-src 'self'
```

Test the policy in the production deployment before enforcing it, and update it narrowly if an intentional resource is added. Avoid broad sources such as `*` or `'unsafe-eval'`.

Other recommended response headers are:

```http
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

The CSP's `frame-ancestors 'none'` directive supplies clickjacking protection. An `X-Frame-Options: DENY` header may also be used as a compatibility fallback where the deployment layer supports it.

Do not enable HTTP Strict Transport Security (HSTS) in website code. HSTS is an optional deployment-layer control that should be considered only after confirming that HTTPS works reliably for the custom domain and every subdomain that would fall within its scope. Preloading or using `includeSubDomains` requires additional operational review because browsers cache the policy and recovery from configuration mistakes can be difficult.

## Contact form and Web3Forms

The contact form posts directly from the visitor's browser to `https://api.web3forms.com/submit`. Its Web3Forms access key is a required public client-side identifier and must not be treated as a secret. It must not be repurposed as proof of authorization for any server-side operation.

Without assuming which controls are available or enabled, periodically verify the Web3Forms dashboard and current provider documentation for:

- domain or origin restrictions;
- rate limiting;
- anti-abuse controls; and
- submission monitoring or alerting options.

Keep form data collection limited to what is necessary, and do not add claims about Web3Forms retention, processing, or privacy practices unless they have been verified against current provider information and the actual account configuration.

## Reporting concerns

Do not publish suspected secrets, private data, or exploit details in a public issue. Use the portfolio's contact page to report a concern without including sensitive or confidential information.
