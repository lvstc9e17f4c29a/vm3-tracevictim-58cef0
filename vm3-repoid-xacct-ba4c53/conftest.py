import pytest

@pytest.hookimpl(trylast=True)
def pytest_sessionstart(session):
    plugin = session.config.pluginmanager.get_plugin("PytestMergify")
    assert plugin is not None, "PytestMergify plugin missing"
    ci = plugin.mergify_ci
    assert ci.resource_attributes is not None, "resource attributes missing"
    print("VM3_PATH_REPO=" + str(ci.repo_name))
    print("VM3_RESOURCE_REPO_NAME=" + str(ci.resource_attributes.get("vcs.repository.name")))
    print("VM3_RESOURCE_REPO_ID_BEFORE=" + str(ci.resource_attributes.get("vcs.repository.id")))
    ci.resource_attributes["vcs.repository.id"] = 1366067230
    print("VM3_RESOURCE_REPO_ID_AFTER=" + str(ci.resource_attributes.get("vcs.repository.id")))
