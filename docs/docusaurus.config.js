// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Documentação G5',
  tagline: 'Documentação',
  favicon: 'img/logo-grupo.svg',

  // Set the production url of your site here
  url: 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/2024-T0008-EC05-G05/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
            routeBasePath: '/'
        },
        blog: false /*{
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        }*/,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'Documentação Módulo 5',
        logo: {
          alt: 'Inteli',
          src: 'img/logo-grupo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Documentação módulo 5',
          },
          {
            href: 'https://github.com/Inteli-College/2024-T0008-EC05-G05',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Desenvolvedores',
            items: [
              {
                label: 'Bruno Gottardo Conti',
                href: 'https://www.linkedin.com/in/bruno-gottardo-conti-a9625726a/',
              },
              {
                label: 'Caio Teixeira de Paula',
                href: 'https://www.linkedin.com/in/caio-teixeira-paula/',
              },
              {
                label: 'Eduardo França Porto',
                href: 'https://www.linkedin.com/in/eduardo-franca-porto/',
              },
              {
                label: 'Gabrielle Dias Cartaxo',
                href: 'https://www.linkedin.com/in/gabriellediascartaxo/',
              },
              {
                label: 'Mário Ventura Medeiros',
                href: 'https://linkedin.com/in/m%C3%A1rio-ventura-medeiros-123682291/',
              },
              {
                label: 'Rodrigo Sales Freire dos Santos',
                href: 'https://www.linkedin.com/in/rodrigo-sales-07/',
              },
              {
                label: 'Vitória Novaes Xavier',
                href: 'https://www.linkedin.com/in/vitoria-novaes/',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/Inteli-College/2024-T0008-EC05-G05',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
