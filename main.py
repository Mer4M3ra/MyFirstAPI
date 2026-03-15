from functions import get_tool, display_tool

print("Minecraft Tool Finder")

tool_name = input("Enter tool name: ")

tool = get_tool(tool_name)
display_tool(tool)