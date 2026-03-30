"""Extension to update the context of Copier."""
import os
import subprocess

from copier_templates_extensions import ContextHook


class ContextUpdater(ContextHook):
    """Context updater."""

    update = False

    def hook(self, context):
        """Update the context before applying the template."""
        # Skip git initialization if the git repository is already initialized
        twd = context.get("_copier_conf", {}).get("dst_path")
        cwd = os.getcwd()
        target_dir = os.fspath(twd) if twd is not None else None

        try:
            if target_dir is not None and os.path.exists(target_dir):
                os.chdir(target_dir)
            status = subprocess.run(["git", "status"], capture_output=True, check=False)
        finally:
            os.chdir(cwd)

        if status.returncode == 0:
            context["init_git"] = False
