import importlib
import pkgutil
import tools

class ToolRegistry:
    def __init__(self):
        self.tools = {}
        self._load_tools()

    def _load_tools(self):
        for _, name, _ in pkgutil.iter_modules(tools.__path__):
            module = importlib.import_module(f"tools.{name}")
            if hasattr(module, "execute"):
                self.tools[name] = module.execute

    def execute_tool(self, name: str, args: dict):
        if name not in self.tools:
            raise ValueError(f"Tool {name} not found.")
        return self.tools[name](args)

registry = ToolRegistry()
