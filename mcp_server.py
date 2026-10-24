from typing import Any, Callable, Protocol, TypeVar, cast

T = TypeVar("T", bound=Callable[..., Any])


class _FastMCPToolDecorator(Protocol):
	def __call__(self, func: T) -> T: ...


class _FastMCPServer(Protocol):
	def tool(self, *args: Any, **kwargs: Any) -> _FastMCPToolDecorator: ...

	def run(self) -> None: ...


class _FastMCPFallback:
	def __init__(self, name: str):
		self.name = name

	def tool(self, *args: Any, **kwargs: Any) -> _FastMCPToolDecorator:
		def decorator(func: T) -> T:
			return func

		return cast(_FastMCPToolDecorator, decorator)

	def run(self) -> None:
		raise RuntimeError(
			"The 'mcp' package is required to run this server. Install it with 'pip install mcp'."
		)


try:
	from mcp.server.fastmcp import FastMCP as FastMCP  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover
	FastMCP = _FastMCPFallback


mcp: _FastMCPServer = cast(_FastMCPServer, FastMCP("SkyApp"))


@mcp.tool()
def status() -> str:
	return "SkyApp MCP Server läuft reibungslos."


if __name__ == "__main__":
	mcp.run()
