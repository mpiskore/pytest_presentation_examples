def test_plugin(request):
    assert request.config.getoption("--backend") != "webkit", \
        "Don't be silly, don't use the default values!"
