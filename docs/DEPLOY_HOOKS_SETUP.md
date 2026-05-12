# Render Deploy Hooks Setup Guide

## 🚀 Setting Up Automated Deployment

This guide explains how to configure Render Deploy Hooks with GitHub Actions for automatic deployments.

---

## 📋 Overview

**Deploy Hooks** are special URLs that GitHub Actions can call to trigger deployments on Render automatically when your CI/CD pipeline passes all tests.

**Deployment Flow:**
```
Code Push → GitHub Actions → Tests Pass → Deploy Hooks → Render Deploys
```

---

## Step 1: Get Deploy Hooks from Render

### Backend Service Deploy Hook

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click on your **backend service**: `trending-collections-backend`
3. Navigate to **Settings** tab (left sidebar)
4. Scroll down to **"Deploy Hook"** section
5. Click **"Create Deploy Hook"** button
6. Copy the generated URL (format: `https://api.render.com/deploy/srv-xxxxx?key=yyyyy`)
7. Save this URL temporarily

### Frontend Service Deploy Hook

1. Return to Render Dashboard
2. Click on your **frontend service**: `trending-collections-frontend`
3. Navigate to **Settings** tab
4. Scroll down to **"Deploy Hook"** section
5. Click **"Create Deploy Hook"** button
6. Copy the generated URL
7. Save this URL temporarily

---

## Step 2: Add Deploy Hooks to GitHub Secrets

### Navigate to GitHub Secrets

1. Go to your repository: https://github.com/LasheO/trending-collections-devops
2. Click **"Settings"** tab (top navigation)
3. Click **"Secrets and variables"** → **"Actions"** (left sidebar)
4. Click **"New repository secret"** button

### Add Backend Deploy Hook

- **Name:** `RENDER_DEPLOY_HOOK_BACKEND`
- **Secret:** Paste the backend deploy hook URL you copied
- Click **"Add secret"**

### Add Frontend Deploy Hook

- **Name:** `RENDER_DEPLOY_HOOK_FRONTEND`
- **Secret:** Paste the frontend deploy hook URL you copied
- Click **"Add secret"**

### Verify Secrets

You should now see two secrets in your repository:
- ✅ `RENDER_DEPLOY_HOOK_BACKEND`
- ✅ `RENDER_DEPLOY_HOOK_FRONTEND`

---

## Step 3: Test the Automated Deployment

### Push Code Changes

The GitHub Actions workflow is already configured to use these deploy hooks!

```bash
# Make any small change (e.g., update README)
echo "# Deployment test" >> README.md
git add README.md
git commit -m "test: verify automated deployment"
git push
```

### Watch the Pipeline

1. Go to **Actions** tab on GitHub
2. Click on the latest workflow run
3. Watch all stages complete:
   - ✅ Lint
   - ✅ Backend Tests
   - ✅ Frontend Tests
   - ✅ Build Verification
   - ✅ **Deploy** ← This will now trigger Render!

### Monitor Render Deployment

1. Go to [Render Dashboard](https://dashboard.render.com)
2. You'll see deployments starting for both services
3. Watch the build logs in real-time
4. Wait for "Live" status (typically 3-5 minutes)

---

## 🎯 How It Works

### GitHub Actions Workflow

The `.github/workflows/ci-cd.yml` file contains:

```yaml
deploy:
  name: Deploy to Render
  runs-on: ubuntu-latest
  needs: [build]
  if: github.ref == 'refs/heads/main' && github.event_name == 'push'
  
  steps:
    - name: Deploy Backend to Render
      if: secrets.RENDER_DEPLOY_HOOK_BACKEND != ''
      run: |
        curl -X POST "${{ secrets.RENDER_DEPLOY_HOOK_BACKEND }}"
    
    - name: Deploy Frontend to Render
      if: secrets.RENDER_DEPLOY_HOOK_FRONTEND != ''
      run: |
        curl -X POST "${{ secrets.RENDER_DEPLOY_HOOK_FRONTEND }}"
```

### Key Features

- ✅ **Conditional Deployment**: Only runs on `main` branch pushes
- ✅ **Gated Releases**: Deployment only happens if tests pass
- ✅ **Secret Protection**: Deploy hooks stored securely in GitHub Secrets
- ✅ **Automatic Triggers**: No manual intervention needed

---

## 🔍 Troubleshooting

### Deploy Hook Not Triggering

**Problem:** Deployment doesn't start after pipeline completes

**Solutions:**
1. Verify secrets are correctly named:
   - `RENDER_DEPLOY_HOOK_BACKEND`
   - `RENDER_DEPLOY_HOOK_FRONTEND`
2. Check secret values don't have extra spaces
3. Ensure you're pushing to `main` branch
4. Check GitHub Actions logs for curl errors

### Deployment Fails on Render

**Problem:** Render deployment triggered but build fails

**Solutions:**
1. Check Render dashboard logs for specific errors
2. Verify build commands in `render.yaml`
3. Ensure all environment variables are set on Render
4. Check for dependency version issues

### Secrets Not Working

**Problem:** GitHub Actions says secrets are empty

**Solutions:**
1. Re-add secrets with exact names
2. Make sure you're adding them as **repository secrets**, not environment secrets
3. Try pushing a new commit to re-trigger the workflow

---

## 🎓 Benefits for Your Assignment

This setup demonstrates:

✅ **Continuous Deployment**: Automated deployment pipeline  
✅ **Quality Gates**: Deployment only after tests pass  
✅ **Infrastructure as Code**: Deployment configuration in git  
✅ **Secret Management**: Secure handling of API credentials  
✅ **Integration**: Connecting multiple platforms (GitHub + Render)  

---

## 📚 Additional Resources

- [Render Deploy Hooks Documentation](https://render.com/docs/deploy-hooks)
- [GitHub Actions Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Continuous Deployment Best Practices](https://www.atlassian.com/continuous-delivery/continuous-deployment)

---

## ✅ Success Checklist

- [ ] Deploy hooks created on Render (backend + frontend)
- [ ] Secrets added to GitHub (RENDER_DEPLOY_HOOK_BACKEND + RENDER_DEPLOY_HOOK_FRONTEND)
- [ ] Workflow file updated with deploy hook logic
- [ ] Test deployment triggered successfully
- [ ] Both services deployed and running on Render
- [ ] Screenshots taken for assignment evidence

---

**Last Updated:** December 2026  
**Author:** Lashe Onamusi  
**Purpose:** DevOps Assignment - Continuous Deployment Setup
