default_app_config = "wagtail_hallo.apps.WagtailHalloAppConfig"


# This file is heavily inspired by django.utils.version


def get_version(version):
    """Return a PEP 440-compliant version number from VERSION."""
    version = get_complete_version(version)

    # Now build the two parts of the version number:
    # main = X.Y[.Z]
    # sub = .devN - for pre-alpha releases
    #     | {a|b|rc}N - for alpha, beta, and rc releases

    main = get_main_version(version)

    sub = ""
    if version[3] != "final":
        mapping = {"alpha": "a", "beta": "b", "rc": "rc", "dev": ".dev"}
        sub = mapping[version[3]] + str(version[4])

    return main + sub


def get_main_version(version):
    """Return main version (X.Y[.Z]) from VERSION."""
    version = get_complete_version(version)
    parts = 2 if version[2] == 0 else 3
    return ".".join(str(x) for x in version[:parts])


def get_complete_version(version):
    """
    Return a tuple of the Wagtail version. If version argument is non-empty,
    check for correctness of the tuple provided.
    """
    assert len(version) == 5
    assert version[3] in ("dev", "alpha", "beta", "rc", "final")

    return version


VERSION = (0, 6, 0)

__version__ = ".".join(map(str, VERSION))
