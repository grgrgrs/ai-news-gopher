import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import mdx from '@astrojs/mdx';
import node from '@astrojs/node';

export default defineConfig({
  site: 'https://ai-news-gopher.fly.dev', // ← update to your actual domain or Fly.io subdomain
  output: 'static',
  // adapter: node({ mode: 'standalone' }),  ← remove this line

  content: { dir: 'src/content' },
  integrations: [mdx(), sitemap()],
  alias: {
    '@layouts': './src/layouts',
    '@components': './src/components',     // (optional but useful if you have reusable components)
    '@assets': './src/assets'              // (optional, for organizing images/fonts)
  }
});
