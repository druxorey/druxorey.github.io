import fs from 'fs';
import { resolve } from 'path';
import { defineConfig } from 'vite';

// Collect all compiled blog articles from blog/ (root level only)
const blogInputs: Record<string, string> = {};
const blogDir = resolve(__dirname, 'blog');

if (fs.existsSync(blogDir)) {
  fs.readdirSync(blogDir)
    .filter((f) => f.endsWith('.html'))
    .forEach((file) => {
      const entryKey = `blog_${file.replace('.html', '').replace(/[^a-zA-Z0-9_]/g, '_')}`;
      blogInputs[entryKey] = resolve(blogDir, file);
    });
}

export default defineConfig({
  base: './',
  build: {
    rollupOptions: {
      input: {
        main:     resolve(__dirname, 'index.html'),
        about:    resolve(__dirname, 'about.html'),
        projects: resolve(__dirname, 'projects.html'),
        blog:     resolve(__dirname, 'blog.html'),
        contact:  resolve(__dirname, 'contact.html'),
        ...blogInputs,
      },
    },
  },
});
