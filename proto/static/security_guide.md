## Security Nets
1. Disable `sudo` command.
    + server.py runs command only when `"sudo" in message== False`.
<!-- 2. Disable  command. -->
3. XSS guard.
    + use `Helmet`
4. No CDN contents. Load local javascript files only.