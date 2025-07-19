import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import mdx from '@astrojs/mdx';
import node from '@astrojs/node';

export default defineConfig({
  site: 'https://yourdomain.com',
  output: 'server',
  adapter: node({ mode: 'standalone' }),
  content: { dir: 'src/content' },
  integrations: [mdx(), sitemap()],
  alias: { '@layouts': 'src/layouts' }
});