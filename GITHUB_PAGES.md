# GitHub Pages Configuration for UniTrack

This document explains how to configure GitHub Pages for the UniTrack project.

## Overview

UniTrack uses GitHub Pages to host a **static landing page** that showcases the project. The landing page is located in the `docs/` folder and is automatically deployed via GitHub Actions.

## Important Note

⚠️ **GitHub Pages only hosts static HTML/CSS/JS files**. The UniTrack Flask application (with backend features like database, authentication, and file uploads) **cannot run on GitHub Pages**.

The GitHub Pages site serves as:
- Project documentation and showcase
- Installation instructions
- Feature highlights
- Links to the actual deployed application (Render/Heroku)

## Setup Instructions

### Option 1: GitHub Actions (Recommended)

1. The repository includes `.github/workflows/github-pages.yml` that automatically deploys to GitHub Pages
2. Go to **Settings → Pages** in your GitHub repository
3. Under **Build and deployment**, select:
   - **Source**: GitHub Actions
4. The workflow will automatically run on every push to `main` branch

### Option 2: Deploy from Branch

1. Go to **Settings → Pages** in your GitHub repository
2. Under **Build and deployment**, select:
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/docs`
3. Click **Save**

## Accessing Your Site

Once configured, your GitHub Pages site will be available at:
- `https://<username>.github.io/unitrack/`

Replace `<username>` with your GitHub username.

## Files Structure

```
docs/
├── index.html          # Main landing page
└── .nojekyll          # Disables Jekyll processing
```

## Customization

To customize the landing page:
1. Edit `docs/index.html`
2. Commit and push to the `main` branch
3. GitHub Actions will automatically deploy the changes

## For Full Application Deployment

To deploy the actual Flask application with all features:
- **Render**: Use `.github/workflows/deploy-to-render.yml`
- **Heroku**: Use `.github/workflows/heroku-deploy.yml`
- **Local**: Run `python app.py` after installing dependencies

See the main README.md for detailed deployment instructions.

## Troubleshooting

### Site not updating
- Check the Actions tab for workflow run status
- Ensure the workflow has proper permissions (Settings → Actions → General → Workflow permissions)
- Allow read and write permissions

### 404 Error
- Verify that `docs/index.html` exists
- Check that the branch and folder are correctly configured in Settings → Pages
- Wait a few minutes for GitHub to build and deploy

### Custom Domain
- Go to Settings → Pages
- Add your custom domain in the "Custom domain" field
- Configure DNS settings as per GitHub's instructions

## Security

The `.nojekyll` file prevents GitHub from processing the site with Jekyll, which ensures that files starting with underscores are served correctly.

## Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/pages)
- [GitHub Actions Documentation](https://docs.github.com/actions)
- [UniTrack Repository](https://github.com/DulsaraPrasad/unitrack)
