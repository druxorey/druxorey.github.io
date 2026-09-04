import fs from 'fs';
import { resolve } from 'path';
import { defineConfig } from 'vite';

// Collect all compiled articles from publications/ and notes/
const dynamicInputs: Record<string, string> = {};

['publications', 'notes'].forEach((folder) => {
  const dir = resolve(__dirname, folder);
  if (fs.existsSync(dir)) {
    fs.readdirSync(dir)
      .filter((f) => f.endsWith('.html'))
      .forEach((file) => {
        const entryKey = `${folder}_${file.replace('.html', '').replace(/[^a-zA-Z0-9_]/g, '_')}`;
        dynamicInputs[entryKey] = resolve(dir, file);
      });
  }
});

export default defineConfig({
  base: './',
  build: {
    rollupOptions: {
      input: {
        main:         resolve(__dirname, 'index.html'),
        about:        resolve(__dirname, 'about.html'),
        projects:     resolve(__dirname, 'projects.html'),
        publications: resolve(__dirname, 'publications.html'),
        notes:        resolve(__dirname, 'notes.html'),
        contact:      resolve(__dirname, 'contact.html'),
        ...dynamicInputs,
      },
    },
  },
});
