## Security Nets
1. Disable some commands such as `sudo` and `rm`.
2. XSS guard.
    + use `Helmet`
3. No CDN contents. Load local javascript files only.
4. Allow only one client to connect a server.