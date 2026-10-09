# External originals

Large audio, documents and archives belong outside Git. The rewritten history
preserves source code, current text and published HTML. Original files in existing
working copies remain in place and are ignored.

This revision has 0 current originals recorded in `repo-assets.json`.
The manifest contains their original paths, sizes and SHA256 checksums. Reproducible
processing caches remain in the full private backup and are rebuilt as needed.

Restore missing originals after cloning:

```bash
uv run /home/rocky/projects/tools-utils/bin/repo-history-cleanup.py restore . \
  --assets repo-assets.json --apply
```

SSH access to the private OVH archive is required. Recovery verifies checksums
and refuses to replace an existing file with different bytes or follow symlinks.
Internal media aliases restore as portable regular files.

The original history and removed objects are verified in both private archives:

- `root@217.216.76.5:/opt/repo-history-backups/20261009/soft-fish-speech`
- `ovh-immich:/home/ubuntu/backups/git-media/20261009/soft-fish-speech`

These archives are outside web roots. Do not merge old history into the cleaned
repository or add original files back to Git. Existing local unpublished work
is retained separately from the rewritten remote branches.

The standard cleanup and verification procedure is
`tools-utils/docs/repo-history-cleanup.md`.
