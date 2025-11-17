"""
Stack Data Structure Implementation

A comprehensive implementation of a Stack data structure with:
- push(): Add element to top of stack
- pop(): Remove and return top element
- peek(): View top element without removing
- is_empty(): Check if stack is empty

Also includes:
- size(): Get number of elements
- display(): Show all elements
- clear(): Remove all elements
- Interactive menu system
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

class StackError(Exception):
    """Base exception for stack operations."""
    pass


class StackUnderflowError(StackError):
    """Raised when trying to pop from empty stack."""
    pass


class StackOverflowError(StackError):
    """Raised when stack exceeds maximum capacity."""
    pass


# ============================================================================
# STACK IMPLEMENTATION V1: BASIC STACK
# ============================================================================

class Stack:
    """
    Basic Stack implementation using Python list.
    
    A stack is a Last-In-First-Out (LIFO) data structure where
    elements are added and removed from the same end (top).
    
    Attributes
    ----------
    items : list
        Internal list to store stack elements.
    
    Methods
    -------
    push(item)
        Add item to top of stack.
    pop()
        Remove and return top item.
    peek()
        View top item without removing.
    is_empty()
        Check if stack is empty.
    size()
        Get number of elements.
    display()
        Show all elements.
    clear()
        Remove all elements.
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items: List[Any] = []
        logger.info("✓ Stack created successfully")
    
    def push(self, item: Any) -> None:
        """
        Add item to top of stack.
        
        Parameters
        ----------
        item : Any
            Item to add to stack.
        
        Returns
        -------
        None
        
        Examples
        --------
        >>> stack = Stack()
        >>> stack.push(10)
        >>> stack.push(20)
        """
        self.items.append(item)
        logger.info(f"✓ Pushed: {item} (Stack size: {len(self.items)})")
    
    def pop(self) -> Any:
        """
        Remove and return top item from stack.
        
        Returns
        -------
        Any
            Item removed from top of stack.
        
        Raises
        ------
        StackUnderflowError
            If stack is empty.
        
        Examples
        --------
        >>> stack = Stack()
        >>> stack.push(10)
        >>> stack.pop()
        10
        """
        if self.is_empty():
            error_msg = "Cannot pop from empty stack"
            logger.error(f"✗ {error_msg}")
            raise StackUnderflowError(error_msg)
        
        item = self.items.pop()
        logger.info(f"✓ Popped: {item} (Stack size: {len(self.items)})")
        return item
    
    def peek(self) -> Any:
        """
        View top item without removing it.
        
        Returns
        -------
        Any
            Item at top of stack.
        
        Raises
        ------
        StackUnderflowError
            If stack is empty.
        
        Examples
        --------
        >>> stack = Stack()
        >>> stack.push(10)
        >>> stack.peek()
        10
        """
        if self.is_empty():
            error_msg = "Stack is empty, cannot peek"
            logger.error(f"✗ {error_msg}")
            raise StackUnderflowError(error_msg)
        
        logger.info(f"✓ Peeked: {self.items[-1]}")
        return self.items[-1]
    
    def is_empty(self) -> bool:
        """
        Check if stack is empty.
        
        Returns
        -------
        bool
            True if stack is empty, False otherwise.
        
        Examples
        --------
        >>> stack = Stack()
        >>> stack.is_empty()
        True
        >>> stack.push(10)
        >>> stack.is_empty()
        False
        """
        return len(self.items) == 0
    
    def size(self) -> int:
        """
        Get number of elements in stack.
        
        Returns
        -------
        int
            Number of elements.
        """
        return len(self.items)
    
    def display(self) -> None:
        """Display all elements in stack from top to bottom."""
        if self.is_empty():
            print("  Stack is empty")
            return
        
        print("  Stack (top to bottom):")
        for i in range(len(self.items) - 1, -1, -1):
            print(f"    [{i}] {self.items[i]}")
    
    def clear(self) -> None:
        """Remove all elements from stack."""
        self.items.clear()
        logger.info("✓ Stack cleared")
    
    def __str__(self) -> str:
        """String representation of stack."""
        if self.is_empty():
            return "Stack: []"
        return f"Stack: {self.items} (size: {len(self.items)})"
    
    def __repr__(self) -> str:
        """Detailed representation of stack."""
        return f"Stack({self.items})"


# ============================================================================
# STACK IMPLEMENTATION V2: WITH MAX SIZE
# ============================================================================

class BoundedStack(Stack):
    """
    Stack with maximum capacity limit.
    
    Parameters
    ----------
    max_size : int
        Maximum number of elements allowed.
    """
    
    def __init__(self, max_size: int = 100):
        """Initialize bounded stack."""
        super().__init__()
        self.max_size = max_size
        logger.info(f"✓ Bounded Stack created (max_size: {max_size})")
    
    def push(self, item: Any) -> None:
        """
        Add item to stack with overflow check.
        
        Raises
        ------
        StackOverflowError
            If stack is full.
        """
        if len(self.items) >= self.max_size:
            error_msg = f"Stack overflow: Maximum size {self.max_size} reached"
            logger.error(f"✗ {error_msg}")
            raise StackOverflowError(error_msg)
        
        super().push(item)
    
    def is_full(self) -> bool:
        """Check if stack is at maximum capacity."""
        return len(self.items) == self.max_size


# ============================================================================
# STACK IMPLEMENTATION V3: WITH TYPE CHECKING
# ============================================================================

class TypedStack(Stack):
    """
    Stack that enforces a specific data type.
    
    Parameters
    ----------
    allowed_type : type
        Type of items allowed in stack.
    """
    
    def __init__(self, allowed_type: type = int):
        """Initialize typed stack."""
        super().__init__()
        self.allowed_type = allowed_type
        logger.info(f"✓ Typed Stack created (type: {allowed_type.__name__})")
    
    def push(self, item: Any) -> None:
        """
        Add item to stack with type check.
        
        Raises
        ------
        TypeError
            If item is not of allowed type.
        """
        if not isinstance(item, self.allowed_type):
            error_msg = (
                f"Type error: Expected {self.allowed_type.__name__}, "
                f"got {type(item).__name__}"
            )
            logger.error(f"✗ {error_msg}")
            raise TypeError(error_msg)
        
        super().push(item)


# ============================================================================
# STACK IMPLEMENTATION V4: WITH STATISTICS
# ============================================================================

class StatisticsStack(Stack):
    """
    Stack with statistics tracking.
    
    Tracks:
    - Total pushes performed
    - Total pops performed
    - Maximum size reached
    """
    
    def __init__(self):
        """Initialize statistics stack."""
        super().__init__()
        self.total_pushes = 0
        self.total_pops = 0
        self.max_size_reached = 0
        logger.info("✓ Statistics Stack created")
    
    def push(self, item: Any) -> None:
        """Add item and update statistics."""
        super().push(item)
        self.total_pushes += 1
        self.max_size_reached = max(self.max_size_reached, len(self.items))
    
    def pop(self) -> Any:
        """Remove item and update statistics."""
        item = super().pop()
        self.total_pops += 1
        return item
    
    def get_statistics(self) -> dict:
        """Get statistics dictionary."""
        return {
            "total_pushes": self.total_pushes,
            "total_pops": self.total_pops,
            "current_size": len(self.items),
            "max_size_reached": self.max_size_reached
        }


# ============================================================================
# STACK IMPLEMENTATION V5: LINKED LIST BASED
# ============================================================================

class Node:
    """Node for linked list implementation."""
    
    def __init__(self, data: Any):
        """Initialize node."""
        self.data = data
        self.next = None


class LinkedListStack:
    """
    Stack implementation using linked list.
    
    Benefits over array-based:
    - Dynamic size (no overflow)
    - Better for very large stacks
    """
    
    def __init__(self):
        """Initialize empty linked list stack."""
        self.top = None
        logger.info("✓ Linked List Stack created")
    
    def push(self, item: Any) -> None:
        """Add item to top of stack."""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        logger.info(f"✓ Pushed: {item}")
    
    def pop(self) -> Any:
        """Remove and return top item."""
        if self.is_empty():
            error_msg = "Cannot pop from empty stack"
            logger.error(f"✗ {error_msg}")
            raise StackUnderflowError(error_msg)
        
        item = self.top.data
        self.top = self.top.next
        logger.info(f"✓ Popped: {item}")
        return item
    
    def peek(self) -> Any:
        """View top item without removing."""
        if self.is_empty():
            error_msg = "Stack is empty, cannot peek"
            logger.error(f"✗ {error_msg}")
            raise StackUnderflowError(error_msg)
        
        logger.info(f"✓ Peeked: {self.top.data}")
        return self.top.data
    
    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return self.top is None
    
    def size(self) -> int:
        """Get number of elements."""
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count
    
    def display(self) -> None:
        """Display all elements."""
        if self.is_empty():
            print("  Stack is empty")
            return
        
        print("  Stack (top to bottom):")
        current = self.top
        index = 0
        while current:
            print(f"    [{index}] {current.data}")
            current = current.next
            index += 1
    
    def clear(self) -> None:
        """Remove all elements."""
        self.top = None
        logger.info("✓ Stack cleared")


# ============================================================================
# INTERACTIVE MENU SYSTEM
# ============================================================================

class StackMenu:
    """Interactive menu system for stack operations."""
    
    def __init__(self, stack_type: str = "basic"):
        """
        Initialize menu with specified stack type.
        
        Parameters
        ----------
        stack_type : str
            Type of stack: "basic", "bounded", "typed", "stats", "linkedlist"
        """
        self.stack_type = stack_type
        self.stack = self._create_stack(stack_type)
        logger.info(f"✓ Menu created with {stack_type} stack")
    
    def _create_stack(self, stack_type: str):
        """Create stack of specified type."""
        if stack_type == "basic":
            return Stack()
        elif stack_type == "bounded":
            return BoundedStack(max_size=10)
        elif stack_type == "typed":
            return TypedStack(allowed_type=int)
        elif stack_type == "stats":
            return StatisticsStack()
        elif stack_type == "linkedlist":
            return LinkedListStack()
        else:
            return Stack()
    
    def display_menu(self):
        """Display main menu options."""
        print("\n" + "="*60)
        print("STACK OPERATIONS MENU")
        print("="*60)
        print("1. Push - Add element to stack")
        print("2. Pop - Remove element from stack")
        print("3. Peek - View top element")
        print("4. Display - Show all elements")
        print("5. Size - Get number of elements")
        print("6. Is Empty - Check if stack is empty")
        print("7. Clear - Remove all elements")
        if isinstance(self.stack, BoundedStack):
            print("8. Is Full - Check if stack is full")
        if isinstance(self.stack, StatisticsStack):
            print("9. Statistics - Show stack statistics")
        print("0. Exit - Quit program")
        print("="*60)
    
    def run(self):
        """Run interactive menu system."""
        print("\n" + "="*60)
        print(f"STACK IMPLEMENTATION - {self.stack_type.upper()}")
        print("="*60)
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (0-9): ").strip()
            
            try:
                if choice == "1":
                    self._handle_push()
                elif choice == "2":
                    self._handle_pop()
                elif choice == "3":
                    self._handle_peek()
                elif choice == "4":
                    self._handle_display()
                elif choice == "5":
                    self._handle_size()
                elif choice == "6":
                    self._handle_is_empty()
                elif choice == "7":
                    self._handle_clear()
                elif choice == "8" and isinstance(self.stack, BoundedStack):
                    self._handle_is_full()
                elif choice == "9" and isinstance(self.stack, StatisticsStack):
                    self._handle_statistics()
                elif choice == "0":
                    print("\n✓ Thank you for using Stack Implementation!")
                    break
                else:
                    print("\n❌ Invalid choice. Please try again.")
            
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")
    
    def _handle_push(self):
        """Handle push operation."""
        try:
            if isinstance(self.stack, TypedStack):
                value = int(input("Enter integer value: "))
            else:
                value = input("Enter value: ")
            
            self.stack.push(value)
            print(f"✓ Successfully pushed: {value}")
        except ValueError:
            print("❌ Invalid input. Please enter a number for integer stack.")
        except StackOverflowError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_pop(self):
        """Handle pop operation."""
        try:
            item = self.stack.pop()
            print(f"✓ Successfully popped: {item}")
        except StackUnderflowError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_peek(self):
        """Handle peek operation."""
        try:
            item = self.stack.peek()
            print(f"✓ Top element: {item}")
        except StackUnderflowError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_display(self):
        """Handle display operation."""
        print("\n" + "-"*40)
        self.stack.display()
        print("-"*40)
    
    def _handle_size(self):
        """Handle size operation."""
        size = self.stack.size()
        print(f"✓ Stack size: {size} elements")
    
    def _handle_is_empty(self):
        """Handle is_empty operation."""
        is_empty = self.stack.is_empty()
        status = "empty" if is_empty else "not empty"
        print(f"✓ Stack is {status}")
    
    def _handle_clear(self):
        """Handle clear operation."""
        self.stack.clear()
        print("✓ Stack cleared successfully")
    
    def _handle_is_full(self):
        """Handle is_full operation."""
        if isinstance(self.stack, BoundedStack):
            is_full = self.stack.is_full()
            status = "full" if is_full else "not full"
            print(f"✓ Stack is {status} (capacity: {self.stack.max_size})")
    
    def _handle_statistics(self):
        """Handle statistics operation."""
        if isinstance(self.stack, StatisticsStack):
            stats = self.stack.get_statistics()
            print("\nStack Statistics:")
            print("-"*40)
            for key, value in stats.items():
                print(f"  {key}: {value}")
            print("-"*40)


# ============================================================================
# DEMONSTRATIONS AND TESTS
# ============================================================================

def demonstrate_basic_stack():
    """Demonstrate basic stack operations."""
    print("="*80)
    print("DEMONSTRATION 1: Basic Stack Operations")
    print("="*80)
    
    stack = Stack()
    
    print("\n1. Checking if stack is empty:")
    print(f"   is_empty(): {stack.is_empty()}")
    
    print("\n2. Pushing elements: 10, 20, 30, 40, 50")
    for value in [10, 20, 30, 40, 50]:
        stack.push(value)
    
    print("\n3. Stack status:")
    print(f"   Size: {stack.size()}")
    print(f"   Is empty: {stack.is_empty()}")
    
    print("\n4. Displaying stack:")
    stack.display()
    
    print("\n5. Peeking at top:")
    top = stack.peek()
    print(f"   Top element: {top}")
    
    print("\n6. Popping elements:")
    for i in range(3):
        item = stack.pop()
        print(f"   Popped: {item}")
    
    print("\n7. Stack after 3 pops:")
    stack.display()
    
    print("\n8. Popping remaining elements:")
    while not stack.is_empty():
        item = stack.pop()
        print(f"   Popped: {item}")
    
    print("\n9. Final state:")
    print(f"   Size: {stack.size()}")
    print(f"   Is empty: {stack.is_empty()}")


def demonstrate_bounded_stack():
    """Demonstrate bounded stack."""
    print("\n" + "="*80)
    print("DEMONSTRATION 2: Bounded Stack (max size: 5)")
    print("="*80)
    
    stack = BoundedStack(max_size=5)
    
    print("\n1. Pushing 5 elements:")
    for i in range(1, 6):
        stack.push(i * 10)
        print(f"   Pushed: {i*10}, Is full: {stack.is_full()}")
    
    print("\n2. Attempting to push when full:")
    try:
        stack.push(60)
    except StackOverflowError as e:
        print(f"   ✓ Caught: {e}")
    
    print("\n3. Stack display:")
    stack.display()


def demonstrate_typed_stack():
    """Demonstrate typed stack."""
    print("\n" + "="*80)
    print("DEMONSTRATION 3: Typed Stack (integers only)")
    print("="*80)
    
    stack = TypedStack(allowed_type=int)
    
    print("\n1. Pushing valid integers:")
    for value in [100, 200, 300]:
        stack.push(value)
        print(f"   Pushed: {value}")
    
    print("\n2. Attempting to push string:")
    try:
        stack.push("invalid")
    except TypeError as e:
        print(f"   ✓ Caught: {e}")
    
    print("\n3. Stack display:")
    stack.display()


def demonstrate_statistics_stack():
    """Demonstrate statistics stack."""
    print("\n" + "="*80)
    print("DEMONSTRATION 4: Statistics Stack")
    print("="*80)
    
    stack = StatisticsStack()
    
    print("\n1. Performing operations:")
    for i in range(1, 8):
        stack.push(i * 100)
    
    for _ in range(3):
        stack.pop()
    
    print("\n2. Stack statistics:")
    stats = stack.get_statistics()
    for key, value in stats.items():
        print(f"   {key}: {value}")


def demonstrate_linked_list_stack():
    """Demonstrate linked list stack."""
    print("\n" + "="*80)
    print("DEMONSTRATION 5: Linked List Stack")
    print("="*80)
    
    stack = LinkedListStack()
    
    print("\n1. Pushing elements: A, B, C, D, E")
    for value in ['A', 'B', 'C', 'D', 'E']:
        stack.push(value)
    
    print("\n2. Stack display:")
    stack.display()
    
    print("\n3. Peeking and popping:")
    print(f"   Peek: {stack.peek()}")
    print(f"   Pop: {stack.pop()}")
    print(f"   Pop: {stack.pop()}")
    
    print("\n4. Stack after operations:")
    stack.display()


def show_use_cases():
    """Show real-world use cases."""
    print("\n" + "="*80)
    print("REAL-WORLD USE CASES OF STACKS")
    print("="*80)
    
    use_cases = [
        {
            "name": "Browser History",
            "description": "Back button - LIFO of visited pages",
            "example": "Push page when visited, pop when back button clicked"
        },
        {
            "name": "Undo/Redo",
            "description": "Undo stack stores operations",
            "example": "Each action pushed to stack, undo pops and reverses"
        },
        {
            "name": "Function Call Stack",
            "description": "Execution context in programs",
            "example": "Function calls pushed, returns pop the stack"
        },
        {
            "name": "Expression Evaluation",
            "description": "Convert infix to postfix notation",
            "example": "Operators stored in stack, operands processed"
        },
        {
            "name": "Parenthesis Matching",
            "description": "Check balanced brackets in code",
            "example": "Push opening brackets, pop when closing found"
        },
        {
            "name": "Backtracking",
            "description": "Maze solving, puzzle solving",
            "example": "Push path, pop to backtrack when dead end"
        },
        {
            "name": "Compiler Design",
            "description": "Parse programming languages",
            "example": "Stack-based parsing of syntax"
        }
    ]
    
    for i, case in enumerate(use_cases, 1):
        print(f"\n{i}. {case['name']}")
        print(f"   Description: {case['description']}")
        print(f"   Example: {case['example']}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    print("="*80)
    print("STACK DATA STRUCTURE - COMPREHENSIVE IMPLEMENTATION")
    print("="*80)
    
    print("\nSelect demonstration or interactive mode:")
    print("1. Demonstration 1: Basic Stack")
    print("2. Demonstration 2: Bounded Stack")
    print("3. Demonstration 3: Typed Stack")
    print("4. Demonstration 4: Statistics Stack")
    print("5. Demonstration 5: Linked List Stack")
    print("6. Show Use Cases")
    print("7. Interactive Mode - Basic Stack")
    print("8. Interactive Mode - Bounded Stack")
    print("9. Interactive Mode - Typed Stack")
    print("10. Interactive Mode - Statistics Stack")
    print("11. Interactive Mode - Linked List Stack")
    print("0. Exit")
    
    while True:
        choice = input("\nEnter your choice (0-11): ").strip()
        
        if choice == "1":
            demonstrate_basic_stack()
        elif choice == "2":
            demonstrate_bounded_stack()
        elif choice == "3":
            demonstrate_typed_stack()
        elif choice == "4":
            demonstrate_statistics_stack()
        elif choice == "5":
            demonstrate_linked_list_stack()
        elif choice == "6":
            show_use_cases()
        elif choice == "7":
            menu = StackMenu("basic")
            menu.run()
        elif choice == "8":
            menu = StackMenu("bounded")
            menu.run()
        elif choice == "9":
            menu = StackMenu("typed")
            menu.run()
        elif choice == "10":
            menu = StackMenu("stats")
            menu.run()
        elif choice == "11":
            menu = StackMenu("linkedlist")
            menu.run()
        elif choice == "0":
            print("\n✓ Thank you for using Stack Implementation!")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()