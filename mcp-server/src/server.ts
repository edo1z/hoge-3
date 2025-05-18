import { chromium } from 'playwright';
import { startServer } from 'playwright-mcp';

async function main() {
  const browser = await chromium.launch();
  const server = await startServer({ browser, port: 3322 });
  console.log('MCP server listening on http://localhost:3322');
  await server.waitForClose();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
