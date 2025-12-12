# Quick Setup Guide for GitHub Pages

This guide will help you enable GitHub Pages for the UniTrack repository in just a few steps.

## ✅ Prerequisites

All files are already in place:
- ✓ `docs/index.html` - Landing page
- ✓ `docs/.nojekyll` - GitHub Pages configuration
- ✓ `.github/workflows/github-pages.yml` - Deployment workflow
- ✓ Documentation in `README.md` and `GITHUB_PAGES.md`

## 🚀 Enable GitHub Pages (2 Methods)

### Method 1: Using GitHub Actions (Recommended)

1. Go to your repository on GitHub: `https://github.com/DulsaraPrasad/unitrack`
2. Click **Settings** (top navigation)
3. Click **Pages** (left sidebar)
4. Under **Build and deployment**:
   - **Source**: Select "GitHub Actions"
5. Push code to the `main` branch (or merge this PR)
6. The workflow will automatically run and deploy your site

**Your site will be live at**: `https://DulsaraPrasad.github.io/unitrack/`

### Method 2: Deploy from Branch

1. Go to your repository on GitHub: `https://github.com/DulsaraPrasad/unitrack`
2. Click **Settings** → **Pages**
3. Under **Build and deployment**:
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/docs`
4. Click **Save**

**Your site will be live at**: `https://DulsaraPrasad.github.io/unitrack/`

## 🔧 Workflow Permissions (If Using GitHub Actions)

If the workflow fails due to permissions:

1. Go to **Settings** → **Actions** → **General**
2. Scroll to **Workflow permissions**
3. Select **"Read and write permissions"**
4. Check **"Allow GitHub Actions to create and approve pull requests"**
5. Click **Save**

## ✨ What Gets Deployed

The GitHub Pages site includes:
- Beautiful landing page with project overview
- Key features showcase
- Technology stack information
- Installation instructions
- Demo credentials
- Use cases for different user roles
- Links to GitHub repository and documentation

## 📝 Important Notes

- **GitHub Pages hosts only the static landing page** (the `docs/` folder)
- **The Flask application** (with backend features) cannot run on GitHub Pages
- For the full application, deploy to **Render** or **Heroku** (see README.md)
- The landing page automatically updates when you push changes to `docs/index.html`

## 🎨 Customization

To customize the landing page:
1. Edit `docs/index.html`
2. Commit and push to `main` branch
3. GitHub Actions will automatically redeploy (or wait 1-2 minutes for branch deployment)

## 🧪 Test Locally

Before pushing, you can test the landing page locally:

```bash
cd docs
python3 -m http.server 8080
```

Then open `http://localhost:8080` in your browser.

## 🔍 Troubleshooting

### Site shows 404
- Wait 2-3 minutes after enabling GitHub Pages
- Check that `docs/index.html` exists in the `main` branch
- Verify the correct source is selected in Settings → Pages

### Workflow fails
- Check **Actions** tab for error details
- Verify workflow permissions are set correctly
- Ensure the `docs/` folder exists with `index.html`

### Changes not reflecting
- Clear browser cache (Ctrl+F5 or Cmd+Shift+R)
- Check the Actions tab to see if deployment completed
- Wait 1-2 minutes for GitHub's CDN to update

## 📚 Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/pages)
- [GitHub Actions Documentation](https://docs.github.com/actions)
- Full setup guide: `GITHUB_PAGES.md`
- Project documentation: `README.md`

## 🎉 Success!

Once enabled, share your GitHub Pages URL:
```
https://DulsaraPrasad.github.io/unitrack/
```

The page showcases your project beautifully and provides visitors with:
- Overview of features
- Installation instructions
- Links to the repository
- Deployment options
- Demo credentials
