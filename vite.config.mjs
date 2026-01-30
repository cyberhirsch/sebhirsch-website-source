import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import { resolve } from 'path'

export default defineConfig(({ mode }) => ({
  plugins: [
    tailwindcss(),
  ],
  build: {
    // Output to Hugo's theme static directory
    outDir: 'static/css',
    // Clear only the output directory
    emptyOutDir: true,
    // Don't copy public directory
    copyPublicDir: false,

    rollupOptions: {
      input: {
        main: resolve(__dirname, 'assets/css/main.css'),
      },
      output: {
        // Use fixed naming during development to prevent filename accumulation
        // and inconsistent Hugo lookups.
        assetFileNames: (assetInfo) => {
          if (assetInfo.name && assetInfo.name.endsWith('.css')) {
            return mode === 'development' ? '[name].css' : '[name].[hash].css'
          }
          return mode === 'development' ? '[name].[ext]' : '[name].[hash].[ext]'
        },
        // Don't create random JS files for CSS-only builds in dev
        entryFileNames: () => {
          return mode === 'development' ? '[name].js' : '[name].[hash].js'
        }
      }
    },
    // Only generate manifest in production
    manifest: mode === 'production',
    // Don't use watch mode - causes infinite loops with Hugo
    watch: null,
  },
  // For development hot reloading
  server: {
    port: 5173,
    hmr: {
      port: 5173,
    },
    watch: {
      // Also ignore output directories in dev server
      ignored: ['**/static/css/**', '**/public/**']
    }
  }
}))