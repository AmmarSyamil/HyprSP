# #WTF IS PYTHON IMPORTING IDK NOSFFNOIWAIBUASDASBFABF
# mod_path = (Path(__file__).resolve().parents[1] / "compiled" / "page_main_ui.py")
# spec = importlib.util.spec_from_file_location("compiled.page_main_ui", str(mod_path))
# module = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(module)

# ROOT = Path(__file__).resolve().parents[1]
# if str(ROOT) not in sys.path:
#     sys.path.insert(0, str(ROOT))

# def _load_module(name, relative_path):
#     path = ROOT / relative_path
#     spec = importlib.util.spec_from_file_location(name, str(path))
#     module = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(module)
#     sys.modules[name] = module
#     return module

# _compiled = _load_module("compiled.page_main_ui", Path("compiled") / "page_main_ui.py")
# Ui_Form = _compiled.Ui_Form

# _specs_mod = _load_module("extra.specs", Path("extra") / "specs.py")
# Specs = _specs_mod.Specs

# _config_mod = _load_module("config", Path("") / "config.py")
# config = _config_mod