import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'http://localhost:4321',
  content: {
    dir: 'src/content'
  },
  integrations: [mdx(), sitemap()],
  alias: {
    '@layouts': 'src/layouts'
  }
});
