export NODE_OPTIONS=--openssl-legacy-provider
npm install --no-fund --no-audit
nohup npm run serve 2>&1 & exit