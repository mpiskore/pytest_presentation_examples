def test_plugin(request):
    if request.config.getoption("--backend") == "webkit":
        print("webkit chosen")
    else:
        print("webengine chosen")
