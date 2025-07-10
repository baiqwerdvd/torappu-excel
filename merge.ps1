git checkout main
git pull origin main

$branches = @("auto-update/25-04-25-08-42-16_acb2f8")

foreach ($branch in $branches) {
    git checkout $branch
    git pull origin $branch

    Write-Host "Merging main into $branch..."
    git merge main
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Merge conflict detected. Resolving JSON files from main (ours)..."

        $conflictFiles = git diff --name-only --diff-filter=U | Where-Object { $_ -like "*.json" }
        foreach ($file in $conflictFiles) {
            git checkout --ours $file
            git add $file
        }
        git commit -m "Auto-merge main into $branch, preferring JSON from current branch ($branch)"
    }

    git push origin $branch
}
