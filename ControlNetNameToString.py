# Marwan Custom Nodes
# UNET Name to CKPT_NAME
# -------------------------------------------------------
class MarControlNetNameToString:
    @classmethod
    def INPUT_TYPES(cls):
        import folder_paths
        return {
            "required": {
                "mar_name": (folder_paths.get_filename_list("controlnet"),),
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("String",)
    FUNCTION = "get_name"
    CATEGORY = "MarNodes/utils/text"

    def get_name(self, mar_name):
        return (mar_name,)
        
NODE_CLASS_MAPPINGS = {"MarControlNetNameToString": MarControlNetNameToString}
NODE_DISPLAY_NAME_MAPPINGS = {"MarControlNetNameToString": "ControlNet Name To String"}