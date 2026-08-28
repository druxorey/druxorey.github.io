export interface Project {
  id: string;
  title: string;
  description: string;
  tags: string[];
  featured?: boolean;
  links: {
    github?: string;
    demo?: string | null;
    docs?: string | null;
  };
  year?: string;
}

export const projectsData: Project[] = [
  {
    "id": "dotfiles",
    "title": "dotfiles",
    "description": "A minimalist repository of my dotfiles for arch linux and a bootstrap to automate its installation",
    "tags": [
      "Shell",
      "Archlinux",
      "Customization",
      "Dotfiles",
      "Guide"
    ],
    "featured": true,
    "links": {
      "github": "https://github.com/druxorey/dotfiles",
      "demo": "https://druxorey.github.io"
    },
    "year": "2026"
  },
  {
    "id": "druxorey.github.io",
    "title": "druxorey.github.io",
    "description": "A personal portfolio and blog showcasing my projects and writings",
    "tags": [
      "HTML"
    ],
    "featured": true,
    "links": {
      "github": "https://github.com/druxorey/druxorey.github.io",
      "demo": "https://druxorey.github.io/"
    },
    "year": "2026"
  },
  {
    "id": "drxpkg",
    "title": "drxpkg",
    "description": "A terminal user interface for searching and installing Arch Linux packages",
    "tags": [
      "Go"
    ],
    "featured": true,
    "links": {
      "github": "https://github.com/druxorey/drxpkg",
      "demo": null
    },
    "year": "2026"
  },
  {
    "id": "minimal-dracula-for-obsidian",
    "title": "minimal-dracula-for-obsidian",
    "description": "Are you tired of the same boring colors on Obsidian? Try Dracula For Obsidian",
    "tags": [
      "CSS",
      "Dark-theme",
      "Dracula-colorscheme",
      "Dracula-theme",
      "Light-theme"
    ],
    "featured": true,
    "links": {
      "github": "https://github.com/druxorey/minimal-dracula-for-obsidian",
      "demo": "https://publish.obsidian.md/hub/02+-+Community+Expansions/02.05+All+Community+Expansions/Themes/Minimal+Dracula"
    },
    "year": "2026"
  },
  {
    "id": "dracula-for-stylus",
    "title": "dracula-for-stylus",
    "description": "Are you tired of the same boring colors on your websites? Then try Dracula For Stylus",
    "tags": [
      "Less",
      "Custom-css",
      "Stylus"
    ],
    "featured": true,
    "links": {
      "github": "https://github.com/druxorey/dracula-for-stylus",
      "demo": "https://userstyles.world/user/druxorey"
    },
    "year": "2026"
  },
  {
    "id": "gba-icons",
    "title": "gba-icons",
    "description": "A collection of icons for GBA games",
    "tags": [
      "Gba",
      "Icons",
      "Nintendo-ds"
    ],
    "featured": false,
    "links": {
      "github": "https://github.com/druxorey/gba-icons",
      "demo": null
    },
    "year": "2026"
  },
  {
    "id": "romyr-tweaks",
    "title": "romyr-tweaks",
    "description": "My survival texture pack for Minecraft 1.21.11",
    "tags": [
      "GLSL",
      "Minecraft",
      "Redstone",
      "Resource-pack",
      "Vanilla-like"
    ],
    "featured": false,
    "links": {
      "github": "https://github.com/druxorey/romyr-tweaks",
      "demo": null
    },
    "year": "2026"
  },
  {
    "id": "wallpapers",
    "title": "wallpapers",
    "description": "A curated collection of wallpapers for dracula and alucard desktop setups",
    "tags": [
      "Shell",
      "Alucard-colorscheme",
      "Dracula-colorscheme",
      "Wallpapers"
    ],
    "featured": false,
    "links": {
      "github": "https://github.com/druxorey/wallpapers",
      "demo": null
    },
    "year": "2026"
  },
  {
    "id": "ucv-ayed",
    "title": "ucv-ayed",
    "description": "Respuestas y ejercicios resueltos de las guías de Algoritmos y Estructuras de Datos en C++, organizados por temas.",
    "tags": [
      "C++",
      "Algorithms-and-data-structures",
      "Cpp",
      "Ucv"
    ],
    "featured": false,
    "links": {
      "github": "https://github.com/druxorey/ucv-ayed",
      "demo": "https://druxorey.github.io/"
    },
    "year": "2026"
  },
  {
    "id": "ucv-proyecto-lucario",
    "title": "ucv-proyecto-lucario",
    "description": "Implementation of a virtual hardware architecture running on Linux to support a microkernel",
    "tags": [
      "C",
      "Kernel",
      "Operating-system",
      "Ucv"
    ],
    "featured": false,
    "links": {
      "github": "https://github.com/druxorey/ucv-proyecto-lucario",
      "demo": null
    },
    "year": "2026"
  },
  {
    "id": "ucv-proyecto-chandelure",
    "title": "ucv-proyecto-chandelure",
    "description": "Repositorio de software libre en Python.",
    "tags": [
      "Python",
      "Abd",
      "Ucv"
    ],
    "featured": false,
    "links": {
      "github": "https://github.com/druxorey/ucv-proyecto-chandelure",
      "demo": null
    },
    "year": "2026"
  },
  {
    "id": "ucv-proyecto-cacerola",
    "title": "ucv-proyecto-cacerola",
    "description": "Sistema para la gestión del comedor universitario de la UCV",
    "tags": [
      "Java",
      "Inge",
      "Maven",
      "Ucv"
    ],
    "featured": false,
    "links": {
      "github": "https://github.com/druxorey/ucv-proyecto-cacerola",
      "demo": null
    },
    "year": "2026"
  },
  {
    "id": "ucv-runatril-proscrito",
    "title": "ucv-runatril-proscrito",
    "description": "A powerful system for detecting and managing illegal spells using advanced techno-arcane methodologies.",
    "tags": [
      "C++",
      "Ayed",
      "Cpp",
      "Ucv"
    ],
    "featured": false,
    "links": {
      "github": "https://github.com/druxorey/ucv-runatril-proscrito",
      "demo": null
    },
    "year": "2026"
  },
  {
    "id": "ucv-retrotraza-arcana",
    "title": "ucv-retrotraza-arcana",
    "description": "A powerful tool to uncover the truth behind shape-shifting using advanced facial recognition algorithms.",
    "tags": [
      "C++",
      "Ayed",
      "Cpp",
      "Ucv"
    ],
    "featured": false,
    "links": {
      "github": "https://github.com/druxorey/ucv-retrotraza-arcana",
      "demo": null
    },
    "year": "2026"
  },
  {
    "id": "ucv-project-redscape",
    "title": "ucv-project-redscape",
    "description": "Text-based card game, developed in C++ for TheGame.cpp.",
    "tags": [
      "C++",
      "Cpp",
      "Gamejam-2024",
      "Ucv"
    ],
    "featured": false,
    "links": {
      "github": "https://github.com/druxorey/ucv-project-redscape",
      "demo": "https://henrzven.github.io/the-game/"
    },
    "year": "2026"
  },
  {
    "id": "startpage",
    "title": "startpage",
    "description": "A minimalist startpage designed for quick access to your favorite websites.",
    "tags": [
      "CSS",
      "Startpage"
    ],
    "featured": false,
    "links": {
      "github": "https://github.com/druxorey/startpage",
      "demo": "https://druxorey.github.io/startpage/"
    },
    "year": "2026"
  },
  {
    "id": "ucv-ayp",
    "title": "ucv-ayp",
    "description": "Respuestas y ejercicios resueltos de las guías de Algoritmos y Programación en C++, organizados por temas.",
    "tags": [
      "C++",
      "Algorithms",
      "Cpp",
      "Ucv"
    ],
    "featured": false,
    "links": {
      "github": "https://github.com/druxorey/ucv-ayp",
      "demo": "https://druxorey.github.io/"
    },
    "year": "2026"
  },
  {
    "id": "druxorey",
    "title": "druxorey",
    "description": "Here you can find the readme.md file for my profile and learn more about me, my skills, my projects and my contact information.",
    "tags": [
      "About-me",
      "Profile",
      "Readme",
      "Readme-profile"
    ],
    "featured": false,
    "links": {
      "github": "https://github.com/druxorey/druxorey",
      "demo": "https://druxorey.github.io/"
    },
    "year": "2026"
  },
  {
    "id": "colorscheme-test",
    "title": "colorscheme-test",
    "description": "A tool to test and preview color schemes and configurations",
    "tags": [
      "CSS"
    ],
    "featured": false,
    "links": {
      "github": "https://github.com/druxorey/colorscheme-test",
      "demo": "https://druxorey.github.io/colorscheme-test/"
    },
    "year": "2026"
  },
  {
    "id": "windots",
    "title": "windots",
    "description": "A streamlined collection of my configuration files for Windows",
    "tags": [
      "PowerShell",
      "Dotfiles-windows",
      "Windows"
    ],
    "featured": false,
    "links": {
      "github": "https://github.com/druxorey/windots",
      "demo": null
    },
    "year": "2026"
  }
];
