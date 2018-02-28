# Nix development environment
#
# source <bbp-nixpkgs>/sourcethis.sh
#
# nix-build
# nix-shell
#
with import <nixpkgs> {};
{
  {{ cookiecutter.project_name }} = {{ cookiecutter.project_name }}.overrideDerivation (oldAtr: rec {
    version = "DEV_ENV";
    src = ./.;
  });
}
