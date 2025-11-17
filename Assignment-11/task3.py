"""
Singly Linked List Implementation

A comprehensive implementation of a Singly Linked List data structure with:
- insert_at_end(): Add node at the end of list
- insert_at_beginning(): Add node at the beginning of list
- display(): Show all nodes in the list
- insert_at_position(): Add node at specific position
- delete_at_beginning(): Remove first node
- delete_at_end(): Remove last node
- delete_at_position(): Remove node at specific position
- search(): Find node with specific value
- Interactive menu system

A linked list is a linear data structure where each node contains
data and a reference (link) to the next node.
"""

import logging
from typing import Any, Optional, List
from enum import Enum


# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ============================================================================
# CUSTOM EXCEPTIONS
# ============================================================================

class LinkedListError(Exception):
    """Base exception for linked list operations."""
    pass


class NodeNotFoundError(LinkedListError):
    """Raised when node is not found."""
    pass


class InvalidPositionError(LinkedListError):
    """Raised when position is invalid."""
    pass


class EmptyListError(LinkedListError):
    """Raised when operating on empty list."""
    pass


# ============================================================================
# NODE CLASS
# ============================================================================

class Node:
    """
    Node class for singly linked list.
    
    Attributes
    ----------
    data : Any
        Data stored in the node.
    next : Node or None
        Reference to the next node.
    """
    
    def __init__(self, data: Any):
        """
        Initialize a node.
        
        Parameters
        ----------
        data : Any
            Data to store in the node.
        """
        self.data = data
        self.next = None
        logger.debug(f"✓ Node created with data: {data}")
    
    def __str__(self) -> str:
        """String representation of node."""
        return str(self.data)
    
    def __repr__(self) -> str:
        """Detailed representation of node."""
        return f"Node({self.data})"


# ============================================================================
# SINGLY LINKED LIST IMPLEMENTATION V1: BASIC
# ============================================================================

class SinglyLinkedList:
    """
    Singly Linked List implementation.
    
    A linear data structure where each node contains data and 
    a reference to the next node.
    
    Attributes
    ----------
    head : Node or None
        Reference to the first node in the list.
    
    Methods
    -------
    insert_at_beginning(data)
        Add node at the beginning of list.
    insert_at_end(data)
        Add node at the end of list.
    insert_at_position(data, position)
        Add node at specific position.
    delete_at_beginning()
        Remove first node.
    delete_at_end()
        Remove last node.
    delete_at_position(position)
        Remove node at specific position.
    search(data)
        Find and return node with specific data.
    display()
        Show all nodes in the list.
    __len__()
        Get number of nodes in list.
    is_empty()
        Check if list is empty.
    clear()
        Remove all nodes.
    reverse()
        Reverse the list.
    get_node_at(position)
        Get node at specific position.
    
    Examples
    --------
    >>> linked_list = SinglyLinkedList()
    >>> linked_list.insert_at_end(10)
    >>> linked_list.insert_at_end(20)
    >>> linked_list.insert_at_beginning(5)
    >>> linked_list.display()
    5 -> 10 -> 20 -> None
    """
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head: Optional[Node] = None
        logger.info("✓ Singly Linked List created")
    
    def insert_at_beginning(self, data: Any) -> None:
        """
        Insert node at the beginning of list.
        
        Parameters
        ----------
        data : Any
            Data to insert.
        
        Returns
        -------
        None
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Examples
        --------
        >>> ll = SinglyLinkedList()
        >>> ll.insert_at_beginning(10)
        >>> ll.insert_at_beginning(5)
        >>> ll.display()
        5 -> 10 -> None
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        logger.info(f"✓ Inserted at beginning: {data}")
    
    def insert_at_end(self, data: Any) -> None:
        """
        Insert node at the end of list.
        
        Parameters
        ----------
        data : Any
            Data to insert.
        
        Returns
        -------
        None
        
        Time Complexity: O(n) - must traverse to end
        Space Complexity: O(1)
        
        Examples
        --------
        >>> ll = SinglyLinkedList()
        >>> ll.insert_at_end(10)
        >>> ll.insert_at_end(20)
        >>> ll.display()
        10 -> 20 -> None
        """
        new_node = Node(data)
        
        # If list is empty
        if self.head is None:
            self.head = new_node
            logger.info(f"✓ Inserted at end (empty list): {data}")
            return
        
        # Traverse to the last node
        current = self.head
        while current.next is not None:
            current = current.next
        
        # Insert at end
        current.next = new_node
        logger.info(f"✓ Inserted at end: {data}")
    
    def insert_at_position(self, data: Any, position: int) -> None:
        """
        Insert node at specific position (0-indexed).
        
        Parameters
        ----------
        data : Any
            Data to insert.
        position : int
            Position to insert (0 = beginning, length = end).
        
        Returns
        -------
        None
        
        Raises
        ------
        InvalidPositionError
            If position is out of range.
        
        Time Complexity: O(n) - must traverse to position
        Space Complexity: O(1)
        
        Examples
        --------
        >>> ll = SinglyLinkedList()
        >>> ll.insert_at_end(10)
        >>> ll.insert_at_end(30)
        >>> ll.insert_at_position(20, 1)
        >>> ll.display()
        10 -> 20 -> 30 -> None
        """
        if position < 0:
            raise InvalidPositionError("Position cannot be negative")
        
        # Insert at beginning if position is 0
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        # Traverse to position-1
        current = self.head
        for i in range(position - 1):
            if current is None:
                raise InvalidPositionError(
                    f"Position {position} is out of range"
                )
            current = current.next
        
        if current is None:
            raise InvalidPositionError(
                f"Position {position} is out of range"
            )
        
        # Insert at position
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        logger.info(f"✓ Inserted at position {position}: {data}")
    
    def delete_at_beginning(self) -> Any:
        """
        Delete node at the beginning of list.
        
        Returns
        -------
        Any
            Data from deleted node.
        
        Raises
        ------
        EmptyListError
            If list is empty.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Examples
        --------
        >>> ll = SinglyLinkedList()
        >>> ll.insert_at_end(10)
        >>> ll.insert_at_end(20)
        >>> ll.delete_at_beginning()
        10
        >>> ll.display()
        20 -> None
        """
        if self.head is None:
            error_msg = "Cannot delete from empty list"
            logger.error(f"✗ {error_msg}")
            raise EmptyListError(error_msg)
        
        data = self.head.data
        self.head = self.head.next
        logger.info(f"✓ Deleted from beginning: {data}")
        return data
    
    def delete_at_end(self) -> Any:
        """
        Delete node at the end of list.
        
        Returns
        -------
        Any
            Data from deleted node.
        
        Raises
        ------
        EmptyListError
            If list is empty.
        
        Time Complexity: O(n) - must traverse to end
        Space Complexity: O(1)
        
        Examples
        --------
        >>> ll = SinglyLinkedList()
        >>> ll.insert_at_end(10)
        >>> ll.insert_at_end(20)
        >>> ll.delete_at_end()
        20
        >>> ll.display()
        10 -> None
        """
        if self.head is None:
            error_msg = "Cannot delete from empty list"
            logger.error(f"✗ {error_msg}")
            raise EmptyListError(error_msg)
        
        # If only one node
        if self.head.next is None:
            data = self.head.data
            self.head = None
            logger.info(f"✓ Deleted from end (last node): {data}")
            return data
        
        # Traverse to second-last node
        current = self.head
        while current.next.next is not None:
            current = current.next
        
        # Delete last node
        data = current.next.data
        current.next = None
        logger.info(f"✓ Deleted from end: {data}")
        return data
    
    def delete_at_position(self, position: int) -> Any:
        """
        Delete node at specific position (0-indexed).
        
        Parameters
        ----------
        position : int
            Position to delete.
        
        Returns
        -------
        Any
            Data from deleted node.
        
        Raises
        ------
        InvalidPositionError
            If position is out of range.
        EmptyListError
            If list is empty.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.head is None:
            raise EmptyListError("Cannot delete from empty list")
        
        if position < 0:
            raise InvalidPositionError("Position cannot be negative")
        
        # Delete from beginning if position is 0
        if position == 0:
            return self.delete_at_beginning()
        
        # Traverse to position-1
        current = self.head
        for i in range(position - 1):
            if current is None or current.next is None:
                raise InvalidPositionError(
                    f"Position {position} is out of range"
                )
            current = current.next
        
        if current.next is None:
            raise InvalidPositionError(
                f"Position {position} is out of range"
            )
        
        # Delete node at position
        data = current.next.data
        current.next = current.next.next
        logger.info(f"✓ Deleted at position {position}: {data}")
        return data
    
    def search(self, data: Any) -> Optional[Node]:
        """
        Search for node with specific data.
        
        Parameters
        ----------
        data : Any
            Data to search for.
        
        Returns
        -------
        Optional[Node]
            Node if found, None otherwise.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Examples
        --------
        >>> ll = SinglyLinkedList()
        >>> ll.insert_at_end(10)
        >>> ll.insert_at_end(20)
        >>> node = ll.search(10)
        >>> node is not None
        True
        """
        current = self.head
        while current is not None:
            if current.data == data:
                logger.info(f"✓ Found node with data: {data}")
                return current
            current = current.next
        
        logger.warning(f"⚠ Node with data {data} not found")
        return None
    
    def get_node_at(self, position: int) -> Optional[Node]:
        """
        Get node at specific position (0-indexed).
        
        Parameters
        ----------
        position : int
            Position of node.
        
        Returns
        -------
        Optional[Node]
            Node if found, None otherwise.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if position < 0:
            return None
        
        current = self.head
        for i in range(position):
            if current is None:
                return None
            current = current.next
        
        return current
    
    def display(self) -> None:
        """
        Display all nodes in the list.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Examples
        --------
        >>> ll = SinglyLinkedList()
        >>> ll.insert_at_end(10)
        >>> ll.insert_at_end(20)
        >>> ll.insert_at_end(30)
        >>> ll.display()
        10 -> 20 -> 30 -> None
        """
        if self.head is None:
            print("  List is empty: None")
            return
        
        print("  Linked List:")
        current = self.head
        index = 0
        nodes_str = []
        
        while current is not None:
            nodes_str.append(str(current.data))
            current = current.next
        
        result = " -> ".join(nodes_str) + " -> None"
        print(f"  {result}")
        
        # Print with positions
        print("\n  Detailed view:")
        current = self.head
        index = 0
        while current is not None:
            marker = " (HEAD)" if index == 0 else ""
            print(f"    [Position {index}] {current.data}{marker}")
            current = current.next
            index += 1
        print()
    
    def __len__(self) -> int:
        """
        Get number of nodes in list.
        
        Returns
        -------
        int
            Number of nodes.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def is_empty(self) -> bool:
        """
        Check if list is empty.
        
        Returns
        -------
        bool
            True if list is empty, False otherwise.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.head is None
    
    def clear(self) -> None:
        """
        Remove all nodes from list.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.head = None
        logger.info("✓ List cleared")
    
    def reverse(self) -> None:
        """
        Reverse the linked list.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Examples
        --------
        >>> ll = SinglyLinkedList()
        >>> ll.insert_at_end(10)
        >>> ll.insert_at_end(20)
        >>> ll.insert_at_end(30)
        >>> ll.reverse()
        >>> ll.display()
        30 -> 20 -> 10 -> None
        """
        if self.head is None or self.head.next is None:
            return
        
        prev = None
        current = self.head
        
        while current is not None:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        self.head = prev
        logger.info("✓ List reversed")
    
    def to_list(self) -> List[Any]:
        """
        Convert linked list to Python list.
        
        Returns
        -------
        List[Any]
            Python list containing all node data.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result
    
    def __str__(self) -> str:
        """String representation of linked list."""
        if self.head is None:
            return "None"
        
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next
        
        return " -> ".join(nodes) + " -> None"
    
    def __repr__(self) -> str:
        """Detailed representation of linked list."""
        return f"SinglyLinkedList({self.to_list()})"


# ============================================================================
# LINKED LIST IMPLEMENTATION V2: WITH TAIL POINTER
# ============================================================================

class OptimizedSinglyLinkedList(SinglyLinkedList):
    """
    Optimized Singly Linked List with tail pointer.
    
    Benefits:
    - insert_at_end() is O(1) instead of O(n)
    - Faster append operations
    """
    
    def __init__(self):
        """Initialize list with head and tail pointers."""
        super().__init__()
        self.tail: Optional[Node] = None
        logger.info("✓ Optimized Singly Linked List created")
    
    def insert_at_beginning(self, data: Any) -> None:
        """Insert at beginning - O(1)."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
        # Update tail if list was empty
        if self.tail is None:
            self.tail = new_node
        
        logger.info(f"✓ Inserted at beginning: {data}")
    
    def insert_at_end(self, data: Any) -> None:
        """
        Insert at end - O(1) due to tail pointer.
        
        Time Complexity: O(1) - Much better than basic version!
        Space Complexity: O(1)
        """
        new_node = Node(data)
        
        # If list is empty
        if self.head is None:
            self.head = self.tail = new_node
            logger.info(f"✓ Inserted at end (empty list): {data}")
            return
        
        # Add to end
        self.tail.next = new_node
        self.tail = new_node
        logger.info(f"✓ Inserted at end: {data}")
    
    def delete_at_beginning(self) -> Any:
        """Delete from beginning."""
        if self.head is None:
            raise EmptyListError("Cannot delete from empty list")
        
        data = self.head.data
        self.head = self.head.next
        
        # Update tail if list is now empty
        if self.head is None:
            self.tail = None
        
        logger.info(f"✓ Deleted from beginning: {data}")
        return data
    
    def clear(self) -> None:
        """Clear the list."""
        self.head = None
        self.tail = None
        logger.info("✓ List cleared")


# ============================================================================
# LINKED LIST IMPLEMENTATION V3: DOUBLY LINKED LIST (BONUS)
# ============================================================================

class DoublyNode:
    """Node for doubly linked list."""
    
    def __init__(self, data: Any):
        """Initialize node."""
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    Doubly Linked List implementation (bonus).
    
    Each node has references to both next and previous nodes,
    allowing traversal in both directions.
    """
    
    def __init__(self):
        """Initialize empty doubly linked list."""
        self.head: Optional[DoublyNode] = None
        self.tail: Optional[DoublyNode] = None
        logger.info("✓ Doubly Linked List created")
    
    def insert_at_beginning(self, data: Any) -> None:
        """Insert at beginning."""
        new_node = DoublyNode(data)
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        logger.info(f"✓ Inserted at beginning: {data}")
    
    def insert_at_end(self, data: Any) -> None:
        """Insert at end."""
        new_node = DoublyNode(data)
        
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        logger.info(f"✓ Inserted at end: {data}")
    
    def display_forward(self) -> None:
        """Display list forward."""
        if self.head is None:
            print("  List is empty")
            return
        
        print("  Doubly Linked List (Forward):")
        current = self.head
        while current is not None:
            print(f"    {current.data}", end=" <-> ")
            current = current.next
        print("None")
    
    def display_backward(self) -> None:
        """Display list backward."""
        if self.tail is None:
            print("  List is empty")
            return
        
        print("  Doubly Linked List (Backward):")
        current = self.tail
        while current is not None:
            print(f"    {current.data}", end=" <-> ")
            current = current.prev
        print("None")


# ============================================================================
# INTERACTIVE MENU SYSTEM
# ============================================================================

class LinkedListMenu:
    """Interactive menu system for linked list operations."""
    
    def __init__(self, list_type: str = "basic"):
        """
        Initialize menu with specified linked list type.
        
        Parameters
        ----------
        list_type : str
            Type of linked list: "basic", "optimized", "doubly"
        """
        self.list_type = list_type
        
        if list_type == "optimized":
            self.linked_list = OptimizedSinglyLinkedList()
        elif list_type == "doubly":
            self.linked_list = DoublyLinkedList()
        else:
            self.linked_list = SinglyLinkedList()
        
        logger.info(f"✓ Menu created with {list_type} linked list")
    
    def display_menu(self):
        """Display main menu options."""
        print("\n" + "="*70)
        print("LINKED LIST OPERATIONS MENU")
        print("="*70)
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Position")
        print("4. Delete at Beginning")
        print("5. Delete at End")
        print("6. Delete at Position")
        print("7. Search")
        print("8. Display")
        print("9. Get Length")
        print("10. Is Empty")
        print("11. Reverse")
        print("12. Clear")
        
        if self.list_type == "doubly":
            print("13. Display Forward")
            print("14. Display Backward")
        
        print("0. Exit")
        print("="*70)
    
    def run(self):
        """Run interactive menu system."""
        print("\n" + "="*70)
        print(f"LINKED LIST IMPLEMENTATION - {self.list_type.upper()}")
        print("="*70)
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (0-14): ").strip()
            
            try:
                if choice == "1":
                    self._handle_insert_at_beginning()
                elif choice == "2":
                    self._handle_insert_at_end()
                elif choice == "3":
                    self._handle_insert_at_position()
                elif choice == "4":
                    self._handle_delete_at_beginning()
                elif choice == "5":
                    self._handle_delete_at_end()
                elif choice == "6":
                    self._handle_delete_at_position()
                elif choice == "7":
                    self._handle_search()
                elif choice == "8":
                    self._handle_display()
                elif choice == "9":
                    self._handle_length()
                elif choice == "10":
                    self._handle_is_empty()
                elif choice == "11":
                    self._handle_reverse()
                elif choice == "12":
                    self._handle_clear()
                elif choice == "13" and self.list_type == "doubly":
                    self._handle_display_forward()
                elif choice == "14" and self.list_type == "doubly":
                    self._handle_display_backward()
                elif choice == "0":
                    print("\n✓ Thank you for using Linked List Implementation!")
                    break
                else:
                    print("\n❌ Invalid choice. Please try again.")
            
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")
    
    def _handle_insert_at_beginning(self):
        """Handle insert at beginning."""
        try:
            value = input("Enter value to insert: ")
            # Try to convert to number if possible
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass  # Keep as string
            
            self.linked_list.insert_at_beginning(value)
            print(f"✓ Successfully inserted {value} at beginning")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_insert_at_end(self):
        """Handle insert at end."""
        try:
            value = input("Enter value to insert: ")
            # Try to convert to number if possible
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass  # Keep as string
            
            self.linked_list.insert_at_end(value)
            print(f"✓ Successfully inserted {value} at end")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_insert_at_position(self):
        """Handle insert at position."""
        try:
            value = input("Enter value to insert: ")
            # Try to convert to number if possible
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass  # Keep as string
            
            position = int(input("Enter position (0-indexed): "))
            
            if isinstance(self.linked_list, DoublyLinkedList):
                print("❌ Position insertion not supported for doubly linked list")
            else:
                self.linked_list.insert_at_position(value, position)
                print(f"✓ Successfully inserted {value} at position {position}")
        except ValueError:
            print("❌ Invalid input. Position must be an integer.")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_delete_at_beginning(self):
        """Handle delete at beginning."""
        try:
            value = self.linked_list.delete_at_beginning()
            print(f"✓ Successfully deleted {value} from beginning")
        except EmptyListError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_delete_at_end(self):
        """Handle delete at end."""
        try:
            if isinstance(self.linked_list, DoublyLinkedList):
                # For doubly linked list
                if self.linked_list.tail is None:
                    raise EmptyListError("Cannot delete from empty list")
                value = self.linked_list.tail.data
                if self.linked_list.tail.prev is None:
                    self.linked_list.head = self.linked_list.tail = None
                else:
                    self.linked_list.tail = self.linked_list.tail.prev
                    self.linked_list.tail.next = None
            else:
                value = self.linked_list.delete_at_end()
            
            print(f"✓ Successfully deleted {value} from end")
        except EmptyListError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_delete_at_position(self):
        """Handle delete at position."""
        try:
            position = int(input("Enter position to delete (0-indexed): "))
            
            if isinstance(self.linked_list, DoublyLinkedList):
                print("❌ Position deletion not supported for doubly linked list")
            else:
                value = self.linked_list.delete_at_position(position)
                print(f"✓ Successfully deleted {value} from position {position}")
        except ValueError:
            print("❌ Invalid input. Position must be an integer.")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_search(self):
        """Handle search."""
        try:
            value = input("Enter value to search: ")
            # Try to convert to number if possible
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass  # Keep as string
            
            if isinstance(self.linked_list, DoublyLinkedList):
                print("❌ Search not implemented for doubly linked list")
            else:
                node = self.linked_list.search(value)
                if node:
                    print(f"✓ Found node with value: {value}")
                else:
                    print(f"❌ Value {value} not found in list")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_display(self):
        """Handle display."""
        print("\n" + "-"*70)
        if isinstance(self.linked_list, DoublyLinkedList):
            self.linked_list.display_forward()
        else:
            self.linked_list.display()
        print("-"*70)
    
    def _handle_display_forward(self):
        """Handle display forward."""
        print("\n" + "-"*70)
        if isinstance(self.linked_list, DoublyLinkedList):
            self.linked_list.display_forward()
        print("-"*70)
    
    def _handle_display_backward(self):
        """Handle display backward."""
        print("\n" + "-"*70)
        if isinstance(self.linked_list, DoublyLinkedList):
            self.linked_list.display_backward()
        print("-"*70)
    
    def _handle_length(self):
        """Handle get length."""
        if isinstance(self.linked_list, DoublyLinkedList):
            # Count manually for doubly linked list
            count = 0
            current = self.linked_list.head
            while current:
                count += 1
                current = current.next
            print(f"✓ List length: {count} nodes")
        else:
            length = len(self.linked_list)
            print(f"✓ List length: {length} nodes")
    
    def _handle_is_empty(self):
        """Handle is empty."""
        if isinstance(self.linked_list, DoublyLinkedList):
            is_empty = self.linked_list.head is None
        else:
            is_empty = self.linked_list.is_empty()
        
        status = "empty" if is_empty else "not empty"
        print(f"✓ List is {status}")
    
    def _handle_reverse(self):
        """Handle reverse."""
        if isinstance(self.linked_list, DoublyLinkedList):
            print("❌ Reverse not implemented for doubly linked list")
        else:
            self.linked_list.reverse()
            print("✓ List reversed successfully")
    
    def _handle_clear(self):
        """Handle clear."""
        self.linked_list.clear()
        print("✓ List cleared successfully")


# ============================================================================
# DEMONSTRATIONS AND TESTS
# ============================================================================

def demonstrate_basic_operations():
    """Demonstrate basic linked list operations."""
    print("="*80)
    print("DEMONSTRATION 1: Basic Singly Linked List Operations")
    print("="*80)
    
    ll = SinglyLinkedList()
    
    print("\n1. Checking if list is empty:")
    print(f"   is_empty(): {ll.is_empty()}")
    
    print("\n2. Inserting at end: 10, 20, 30, 40, 50")
    for value in [10, 20, 30, 40, 50]:
        ll.insert_at_end(value)
    
    print("\n3. Displaying list:")
    ll.display()
    
    print("4. List length:")
    print(f"   Length: {len(ll)} nodes")
    
    print("\n5. Inserting at beginning: 5, 0")
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(0)
    ll.display()
    
    print("6. Inserting at position 3: 25")
    ll.insert_at_position(25, 3)
    ll.display()
    
    print("7. Searching for values:")
    search_values = [20, 100, 50]
    for val in search_values:
        node = ll.search(val)
        result = "Found" if node else "Not found"
        print(f"   Search {val}: {result}")
    
    print("\n8. Deleting from beginning:")
    deleted = ll.delete_at_beginning()
    print(f"   Deleted: {deleted}")
    ll.display()
    
    print("9. Deleting from end:")
    deleted = ll.delete_at_end()
    print(f"   Deleted: {deleted}")
    ll.display()
    
    print("10. Deleting from position 2:")
    deleted = ll.delete_at_position(2)
    print(f"   Deleted: {deleted}")
    ll.display()
    
    print("11. Reversing list:")
    ll.reverse()
    ll.display()


def demonstrate_optimized_list():
    """Demonstrate optimized linked list with tail pointer."""
    print("\n" + "="*80)
    print("DEMONSTRATION 2: Optimized Singly Linked List (With Tail Pointer)")
    print("="*80)
    
    ll = OptimizedSinglyLinkedList()
    
    print("\n1. Inserting 1000 elements at end (O(1) each):")
    import time
    start = time.time()
    for i in range(1000):
        ll.insert_at_end(i)
    elapsed = time.time() - start
    print(f"   Time taken: {elapsed:.4f}s")
    print(f"   List length: {len(ll)} nodes")
    
    print("\n2. First 10 elements:")
    current = ll.head
    for i in range(10):
        print(f"   [{i}] {current.data}", end=" ")
        current = current.next
    print("\n   ...")
    
    print("\n3. Last 5 elements:")
    current = ll.tail
    elements = []
    for i in range(5):
        if current:
            elements.append(current.data)
            current = current.prev if hasattr(current, 'prev') else None
    print(f"   {elements}")


def demonstrate_doubly_linked_list():
    """Demonstrate doubly linked list."""
    print("\n" + "="*80)
    print("DEMONSTRATION 3: Doubly Linked List")
    print("="*80)
    
    dll = DoublyLinkedList()
    
    print("\n1. Inserting at beginning: 30, 20, 10")
    for value in [30, 20, 10]:
        dll.insert_at_beginning(value)
    
    print("\n2. Inserting at end: 40, 50")
    for value in [40, 50]:
        dll.insert_at_end(value)
    
    print("\n3. Displaying forward:")
    dll.display_forward()
    
    print("\n4. Displaying backward:")
    dll.display_backward()


def show_use_cases():
    """Show real-world use cases."""
    print("\n" + "="*80)
    print("REAL-WORLD USE CASES OF LINKED LISTS")
    print("="*80)
    
    use_cases = [
        {
            "name": "Undo/Redo Functionality",
            "description": "Store operations in a linked list for undo/redo",
            "example": "Each operation stored as node, traverse back for undo"
        },
        {
            "name": "Browser History",
            "description": "History of visited websites",
            "example": "Doubly linked list for forward/back navigation"
        },
        {
            "name": "Music Playlist",
            "description": "Songs in a playlist with play order",
            "example": "Circular linked list for repeat, doubly for skip"
        },
        {
            "name": "Image Viewer",
            "description": "Navigate between images",
            "example": "Doubly linked list for previous/next"
        },
        {
            "name": "Operating System",
            "description": "Process scheduling, memory management",
            "example": "Linked lists for process queue"
        },
        {
            "name": "Graph Adjacency List",
            "description": "Represent graph connections",
            "example": "Each vertex stores linked list of adjacent vertices"
        },
        {
            "name": "Hash Table Collision",
            "description": "Separate chaining for hash collisions",
            "example": "Each bucket stores linked list of colliding elements"
        },
        {
            "name": "Polynomial Representation",
            "description": "Store polynomial coefficients",
            "example": "Each term stored as node (coefficient, power)"
        }
    ]
    
    for i, case in enumerate(use_cases, 1):
        print(f"\n{i}. {case['name']}")
        print(f"   Description: {case['description']}")
        print(f"   Example: {case['example']}")


def show_complexity_analysis():
    """Show time complexity analysis."""
    print("\n" + "="*80)
    print("TIME COMPLEXITY ANALYSIS - SINGLY LINKED LIST")
    print("="*80)
    
    operations = [
        ("insert_at_beginning()", "O(1)", "Direct insertion at head"),
        ("insert_at_end()", "O(n)", "Must traverse to end"),
        ("insert_at_position()", "O(n)", "Must traverse to position"),
        ("delete_at_beginning()", "O(1)", "Direct deletion from head"),
        ("delete_at_end()", "O(n)", "Must traverse to end"),
        ("delete_at_position()", "O(n)", "Must traverse to position"),
        ("search()", "O(n)", "Linear search through list"),
        ("display()", "O(n)", "Traverse all nodes"),
        ("get_length()", "O(n)", "Traverse all nodes"),
    ]
    
    print("\n{:<30} {:<10} {:<40}".format("Operation", "Complexity", "Note"))
    print("-" * 80)
    
    for op, complexity, note in operations:
        print("{:<30} {:<10} {:<40}".format(op, complexity, note))
    
    print("\n" + "-" * 80)
    print("Optimized Version (with tail pointer):")
    print("-" * 80)
    print("{:<30} {:<10} {:<40}".format("insert_at_end()", "O(1)", "Direct insertion at tail ⭐"))


def benchmark_operations():
    """Benchmark different operations."""
    print("\n" + "="*80)
    print("PERFORMANCE BENCHMARK")
    print("="*80)
    
    import time
    
    # Basic list
    print("\n1. Basic Singly Linked List - Inserting 5000 elements at end:")
    ll = SinglyLinkedList()
    start = time.time()
    for i in range(5000):
        ll.insert_at_end(i)
    elapsed = time.time() - start
    print(f"   Time: {elapsed:.4f}s (O(n²) due to traversal)")
    
    # Optimized list
    print("\n2. Optimized Linked List - Inserting 5000 elements at end:")
    oll = OptimizedSinglyLinkedList()
    start = time.time()
    for i in range(5000):
        oll.insert_at_end(i)
    elapsed = time.time() - start
    print(f"   Time: {elapsed:.4f}s (O(n) with tail pointer) ⭐ MUCH FASTER!")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    print("="*80)
    print("SINGLY LINKED LIST - COMPREHENSIVE IMPLEMENTATION")
    print("="*80)
    
    print("\nSelect demonstration or interactive mode:")
    print("1. Demonstration 1: Basic Operations")
    print("2. Demonstration 2: Optimized List")
    print("3. Demonstration 3: Doubly Linked List")
    print("4. Show Use Cases")
    print("5. Show Complexity Analysis")
    print("6. Performance Benchmark")
    print("7. Interactive Mode - Basic Singly Linked List")
    print("8. Interactive Mode - Optimized Singly Linked List")
    print("9. Interactive Mode - Doubly Linked List")
    print("0. Exit")
    
    while True:
        choice = input("\nEnter your choice (0-9): ").strip()
        
        if choice == "1":
            demonstrate_basic_operations()
        elif choice == "2":
            demonstrate_optimized_list()
        elif choice == "3":
            demonstrate_doubly_linked_list()
        elif choice == "4":
            show_use_cases()
        elif choice == "5":
            show_complexity_analysis()
        elif choice == "6":
            benchmark_operations()
        elif choice == "7":
            menu = LinkedListMenu("basic")
            menu.run()
        elif choice == "8":
            menu = LinkedListMenu("optimized")
            menu.run()
        elif choice == "9":
            menu = LinkedListMenu("doubly")
            menu.run()
        elif choice == "0":
            print("\n✓ Thank you for using Linked List Implementation!")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()