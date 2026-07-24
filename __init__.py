# Marwan Custom Nodes
# -------------------------------------------------------
# Import the mappings from separate nodes logic file
# from .MarwanUNetNameToCKPTName import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
# -------------------------------------------------------
import os
import glob
import importlib

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# 1. Look up all Python files in this folder (excluding __init__.py)
current_dir = os.path.dirname(__file__)
py_files = glob.glob(os.path.join(current_dir, "*.py"))

for file_path in py_files:
    file_name = os.path.basename(file_path)
    if file_name == "__init__.py":
        continue

    # 2. Convert file path to a relative module name (e.g., ".my_node_file")
    module_name = f".{file_name[:-3]}"
    
    try:
        # 3. Dynamically import the module
        imported_module = importlib.import_module(module_name, package=__package__)
        
        # 4. Extract mappings if they exist in the file
        if hasattr(imported_module, "NODE_CLASS_MAPPINGS"):
            NODE_CLASS_MAPPINGS.update(imported_module.NODE_CLASS_MAPPINGS)
            
        if hasattr(imported_module, "NODE_DISPLAY_NAME_MAPPINGS"):
            NODE_DISPLAY_NAME_MAPPINGS.update(imported_module.NODE_DISPLAY_NAME_MAPPINGS)
            
    except Exception as e:
        print(f"[Marwan Nodes] Failed to load module {module_name}: {e}")

# 5. Expose the consolidated mappings to ComfyUI
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
# Expose the mappings so ComfyUI can register the nodes upon server startup
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']