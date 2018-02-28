{
  config,
  fetchgitPrivate,
  pythonPackages
}:


pythonPackages.buildPythonPackage rec {
    pname = "{{ cookiecutter.project_name }}";
    version = "0.0.0";
    name = "${pname}-${version}";

    src = fetchgitPrivate {
        url = config.bbp_git_ssh + "/{{ cookiecutter.gerrit_repo }}";
        rev = "";
        sha256 = "";
    };

    buildInputs = with pythonPackages; [
        nose
        mock
    ];

    propagatedBuildInputs = with pythonPackages; [
        # third-party packages
    ] ++ [
        # BBP packages 
    ];

    checkPhase = ''
        nosetests tests
    '';
}
