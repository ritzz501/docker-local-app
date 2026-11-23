cat > infra/BRANCHING-POLICY.md <<'EOF'
# Infrastructure Branching Policy

## Branching Strategy

- main: Stable and production-ready branch.
- feature/*: Used for new infrastructure changes.
- bugfix/*: Used for infrastructure bug fixes.
- hotfix/*: Used for urgent production fixes.

## Development Workflow

1. Start from the latest main branch.
2. Create a feature branch.
3. Make infrastructure changes.
4. Validate changes before committing.
5. Push the feature branch to GitHub.
6. Create a Pull Request.
7. Request review and approval.
8. Merge the approved Pull Request into main.

## Commit Convention

Use descriptive commit messages:

- feat: Add infrastructure feature
- fix: Fix infrastructure configuration
- docs: Update infrastructure documentation

## Review Policy

All infrastructure changes must be reviewed through a Pull Request before merging into main.
EOF