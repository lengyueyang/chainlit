import asyncio
from typing import Dict, List, Optional

from chainlit.context import context
from chainlit.element import ElementBased


class ElementSidebar:
    """Helper class to open/close the element sidebar server side.
    The element sidebar accepts a title and list of elements."""

    @staticmethod
    async def set_title(title: str):
        """
        Sets the title of the element sidebar and opens it.

        The sidebar will automatically open when a title is set using this method.

        Args:
            title (str): The title to display at the top of the sidebar.

        Returns:
            None: This method does not return anything.
        """
        await context.emitter.emit("set_sidebar_title", title)

    @staticmethod
    async def set_elements(elements: List[ElementBased], key: Optional[str] = None):
        """
        Sets the elements to display in the sidebar and controls sidebar visibility.

        This method sends all provided elements to the client and updates the sidebar.
        Passing an empty list will close the sidebar, while passing at least one element
        will open it.

        Args:
            elements (List[ElementBased]): A list of ElementBased objects to display in the sidebar.
            key (Optional[str], optional): If the sidebar is already opened with the same key, elements will not be replaced.

        Returns:
            None: This method does not return anything.

        Note:
            This method first sends each element separately using their send() method,
            then emits an event with all element dictionaries and the optional key.
        """
        coros = [
            element.send(for_id=element.for_id or "", persist=False)
            for element in elements
        ]
        await asyncio.gather(*coros)
        await context.emitter.emit(
            "set_sidebar_elements",
            {"elements": [el.to_dict() for el in elements], "key": key},
        )


class InfoPanelSidebar:
    """Helper class to display custom information in the left sidebar."""
    
    @staticmethod
    async def set_info_panel(info_data: Dict[str, str], title: str = "信息面板"):
        """
        Sets the information to display in the left sidebar info panel.
        
        Args:
            info_data (Dict[str, str]): Key-value pairs of information to display.
                For example: {"字段1": "值1", "字段2": "值2", "字段3": "值3"}
            title (str, optional): The title to display at the top of the info panel.
                Defaults to "信息面板".
                
        Returns:
            None: This method does not return anything.
        """
        await context.emitter.set_info_panel(info_data, title)
